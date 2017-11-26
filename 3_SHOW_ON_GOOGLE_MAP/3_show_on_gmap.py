import webbrowser
import os

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
    #path example : path=color:0x0000ff|weight:5|40.737102,-73.990318|40.749825,-73.987963|40.752946,-73.987384|40.755823,-73.986397

#https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyAEDoAkrq_KdFyPSho9YOnYLstgubov210&center=37.60,126.90&zoom=15&size=600x600&maptype=roadmap&path=color:green|126.913952,37.592662|126.91383,37.592144|126.913698,37.59161|126.913396,37.590471|126.913098,37.589212|126.912991,37.588712

#https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key=AIzaSyAEDoAkrq_KdFyPSho9YOnYLstgubov210
    

    for line in in_file:
        congestion, linestring = line.split(';')
        #print(line)
        paths +="&path=color:"+con_color[congestion]+"|"+linestring.replace(" ","|")
        #print(paths)

        #TOOD: Fill in this block to make color string.
        # congestion 1 --> blue
        # congestion 2 --> green
        # congestion 3 --> yellow
        # congestion 4 --> orange
        # congestion 5 --> red









        #TOOD: Fill in this block to make (lat, lon) string.  Use the first and the last (lat, lon) only




    #+test url https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyAEDoAkrq_KdFyPSho9YOnYLstgubov210&center=37.60,126.90&zoom=12&size=600x600&maptype=roadmap&path=yellow126.916806,37.588333|126.916156,37.588433|126.915932,37.588489|126.915827,37.588525|126.915668,37.588611|126.915468,37.58872|126.915157,37.588951|126.915133,37.588974



    urlstr = "https://maps.googleapis.com/maps/api/staticmap?key="+ GOOGLE_APP_KEY + "&center=" + CENTER + "&zoom=12&size=600x600&maptype=roadmap" + paths
    print(urlstr)

    #webbrowser.open(urlstr)

    out_file.write(urlstr)
    out_file.close()

