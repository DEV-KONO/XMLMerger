from zipfile import ZipFile

def unzip(route, index):
    zf = ZipFile(route, 'r')
    File_list = zf.namelist()
    f = zf.open(File_list[index])
    #returns an xml file in a string format
    zf.close()
    return str(f.read().decode("utf-8-sig"))

def zip_len(route):
    zf = ZipFile(route, 'r')
    return int(len(zf.namelist()))