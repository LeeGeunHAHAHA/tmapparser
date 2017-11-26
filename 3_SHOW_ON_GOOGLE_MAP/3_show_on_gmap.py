import webbrowser

GOOGLE_APP_KEY = 'AIzaSyB-IM1lK9obC5m46g11iUd7s5SAGUmUFS0'
CENTER = '37.60,126.90'

IN_DIR = '../2_PARSE_TMAP/RESULT/'
OUT_DIR = './RESULT/'

for area_index in range(16):
    in_file = open(IN_DIR + "congestion_coor_%02d.txt" % (area_index), 'r')
    out_file = open(OUT_DIR + "gmap_urlstr_%02d.txt" % (area_index), 'w')

    paths = ''

    for line in in_file:
        congestion, linestring = line.split(';')

        #TOOD: Fill in this block to make color string.
        # congestion 1 --> blue
        # congestion 2 --> green
        # congestion 3 --> yellow
        # congestion 4 --> orange
        # congestion 5 --> red









        #TOOD: Fill in this block to make (lat, lon) string.  Use the first and the last (lat, lon) only








    urlstr = ("https://maps.googleapis.com/maps/api/staticmap?key="+ GOOGLE_APP_KEY + "&center=" + CENTER + "&zoom=12&size=600x600&maptype=roadmap" + paths)

    webbrowser.open(urlstr)

    out_file.write(urlstr)
    out_file.close()

