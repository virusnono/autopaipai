# -*- coding: utf-8 -*-

import sys
import time
from common import tool

# reload(sys)
# sys.setdefaultencoding('utf-8')

import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
try:
    from pyocr import pyocr
    from PIL import Image
except ImportError:
    print('模块导入错误,请使用pip安装,pytesseract依赖以下库：')
    print('http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil')
    print('http://code.google.com/p/tesseract-ocr/')
    tool.writelog('log\\test.log', ['模块导入错误,请使用pip安装,pytesseract依赖以下库：',
                                    'http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil',
                                    'http://code.google.com/p/tesseract-ocr/'])
    raise SystemExit
tools = pyocr.get_available_tools()[:]
if len(tools) == 0:
    print("No OCR tool found")
    tool.writelog('log\\test.log', ['No OCR tool found'])
    sys.exit(1)

print("Using '%s'" % (tools[0].get_name()))
tool.writelog('log\\test.log', ["Using '%s'" % (tools[0].get_name())])


def image_to_string(fileName='img\\custom.bmp', font='eng'):
    t = time.time()
    # img = Image.open('img\\86600.tiff')
    img = Image.open(fileName)
    tool.writelog('log\\test.log', ['file open ok!'])

    img = img.convert('L')
    # img.save('img\\Lim.jpg')

    # #  setup a converting table with constant threshold
    # threshold  = 160
    # table  =  []
    # for  i  in  range( 256 ):
    #     if  i  <  threshold:
    #         table.append(0)
    #     else :
    #         table.append( 1 )
    #
    # #  convert to binary image by the table
    # img  =  img.point(table,  '1')
    # img.save('img\\thresh.jpg')

    tool.writelog('log\\test.log', ['start image to string'])
    val = tools[0].image_to_string(img, lang=font)
    tool.writelog('log\\test.log', ['image to string ok'])
    # val = tools[0].image_to_string(img, lang='fontpp')
    # print(time.time()-t)
    # print(val)
    # print(tools[0].image_to_string(Image.open('img\\11.jpg'), lang='chi_sim'))

    return val

if __name__ == "__main__":
    print(image_to_string('img/trainingdata/yanzhengma.bmp'))