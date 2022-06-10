import xml.etree.ElementTree as etree
import shutil
import os

first = 1
for fileName in os.listdir("."):
  if ".nessus" in fileName:
    print("[+] Processing", fileName)
    if first:
      mainTree = etree.parse(fileName)
      report = mainTree.find('Report')
      first = 0
    else:
      tree = etree.parse(fileName)
      for element in tree.findall('.//ReportHost'):
        report.append(element)

if "nss_report" in os.listdir("."):
  shutil.rmtree("nss_report")

os.mkdir("nss_report")
mainTree.write("nss_report/report.nessus", encoding="utf-8", xml_declaration=True)
print("\n[i] Done")