from fileinput import filename
import xml.etree.ElementTree as ET
from uncompressor import unzip, zip_len

for i in range(0,zip_len(r"C:\Users\samue\Downloads\facturas 31 dic.zip")):
    root = ET.ElementTree(ET.fromstring(unzip(r"C:\Users\samue\Downloads\facturas 31 dic.zip", i))).getroot()

    for elem in root:
        try:
            if elem.tag == r"{http://www.sat.gob.mx/cfd/4}Impuestos":
                print(elem.attrib["TotalImpuestosTrasladados"])
        except KeyError:

            print("Probablemente no tiene IVA")

            # print(i)
            # print(unzip(r"C:\Users\samue\Downloads\facturas 31 dic.zip", i))
            # raise
    