import urllib.request as ur

TMAP_APP_KEY = "0fcab96b-4ce9-38fb-9125-28ea08ca942c" #change my key(ygh1kr@kookmin.ac.kr) from default key
MIN_LAT = 37.56
MIN_LON = 126.88
MAX_LAT = 37.57
MAX_LON = 126.89
ZOOM_LEVEL = 19

dxy = MAX_LAT - MIN_LAT


OUT_DIR = "./RESULT/"

# TODO: use for loops to get the traffic info for 4 * 4 areas

for i in range (4) :
    for j in range(4):
        AREA_INDEX= 4*i+j
        rq = ur.Request("https://apis.skplanetx.com/tmap/traffic?version=1"+"&minLat="+str(MIN_LAT+dxy*j)+"&minLon="+str(MIN_LON+dxy*i)+"&maxLat="+str(MAX_LAT+dxy*j)+"&maxLon="+str(MAX_LON+dxy*i)+"&zoomLevel="+str(ZOOM_LEVEL)+"&reqCoordType=WGS84GEO&resCoordType=WGS84GEO&appKey="+TMAP_APP_KEY
)
        rq.add_header("Accept", "application/xml")
        in_file = ur.urlopen(rq)
        out_file = open(OUT_DIR+'traffic_%02d.xml' % (AREA_INDEX), 'wb')
        out_file.write(in_file.read())
        out_file.close()







