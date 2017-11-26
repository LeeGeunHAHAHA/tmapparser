import codecs

IN_DIR = "../1_GET_TMAP/RESULT/"
OUT_DIR = "./RESULT/"

for area_index in range(16):
    in_file = codecs.open(IN_DIR+'traffic_%02d.xml' % (area_index), 'r', 'utf-8')
    out_file = open(OUT_DIR+'congestion_coor_%02d.txt' % (area_index), 'w')

    cont = in_file.read()
    
    # TODO: fill in this block


















    out_file.close()
