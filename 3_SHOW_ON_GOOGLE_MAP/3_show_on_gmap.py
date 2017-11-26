import webbrowser
import os
import codecs

GOOGLE_APP_KEY = 'AIzaSyAEDoAkrq_KdFyPSho9YOnYLstgubov210'
CENTER = '37.60,126.90'

IN_DIR = '../2_PARSE_TMAP/RESULT/'
OUT_DIR = './RESULT/'
con_color ={"0":"white","1":"blue","2":"green","3":"yellow", "4":"orange", "5":"red"}


for area_index in os.listdir(IN_DIR):
    in_file = open(IN_DIR + area_index, 'r')
    out_file = open(OUT_DIR + area_index, 'w')
    #print(area_index)
    paths = ''
    for line in in_file:
        congestion, linestring = line.split(';')
        #print(line)
        paths +="&path=color:"+con_color[congestion]+"|"+linestring.replace(" ","|")
        paths=paths.strip()
        #print(paths)
    urlstr = "https://maps.googleapis.com/maps/api/staticmap?key="+ GOOGLE_APP_KEY + "&center=" + CENTER + "&zoom=12&size=600x600&maptype=roadmap" + paths
    print(urlstr)

    webbrowser.open(urlstr)

    out_file.write(urlstr)
    out_file.close()

