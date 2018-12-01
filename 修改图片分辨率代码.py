import os
import time
from PIL import Image

def alter(path,object):
    s = os.listdir(path)
    count = 1
    for i in s:
        document = os.path.join(path,i)
        img = Image.open(document)
        out = img.resize((1125,2435))
        listStr = [str(int(time.time())), str(count)]
        fileName = ''.join(listStr)
        out.save(object+os.sep+'%s.jpg' % fileName)
        count = count + 1

alter('D:\\picture','D:\\picture')