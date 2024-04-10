import xml.etree.ElementTree as ET
import pandas as pd
import os
import sys
from packages.row import row
from packages.uncompressor import unzip, zip_len

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)   

def to_dataframe(filename: str):
    list = []

    for i in range(0, zip_len(filename)):
        tree = ET.ElementTree(ET.fromstring(unzip(filename, i)))
        root = tree.getroot()
        r = row(root)
        list.append(r.to_dict())

    return pd.DataFrame(list)