import codecs
from bs4 import BeautifulSoup as bs
import os

IN_DIR = "../1_GET_TMAP/RESULT/"
OUT_DIR = "./RESULT/"
XML_list = os.listdir(IN_DIR)

for area_index in XML_list:
    each = IN_DIR + area_index
    print(each)
    fp= codecs.open(each, 'r', encoding='utf-8', errors= 'ignore')
    out_file = open(OUT_DIR+area_index[:-4]+".txt", 'w')
    print(OUT_DIR+area_index[:-4]+".txt")
    mapData = bs(fp,"html.parser")
    for pm in mapData.findAll("placemark"):
        idx = pm.findAll("tmap:congestion")[0].text
        val= pm.findAll("coordinates")[0].text
        out_file.write(idx+';'+val+'\n')
        print(idx+';'+val)
    out_file.close()
    #print(f)

  # cont = in_file.read()
    
    # TODO: fill in this block
