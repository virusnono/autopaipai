# -*- coding: utf-8 -*-

import time
from PIL import ImageGrab


def customCapture(filename, pointLeft, bmpSize):
    coordinate = (pointLeft[0], pointLeft[1], pointLeft[0] + bmpSize[0], pointLeft[1] + bmpSize[1])  
    pic = ImageGrab.grab(coordinate)  
    pic.save(filename, 'bmp')


if __name__ == '__main__':
    import ocr
    import os
    import shutil
    import autopaipai
    dirName = 'img/trainingdata'
    filePath = os.path.join(dirName, 'custom.bmp')

    while True:
        try:
            # customCapture(filePath, (200, 652), (56, 19)) #当前价格
            customCapture(filePath, autopaipai.currTimePosSize['pos'], autopaipai.currTimePosSize['size']) #当前时间

            string = ocr.image_to_string(filePath)
            if string == '':
                print('reload')
                time.sleep(5)
                autopaipai.reload()
            newName = string + '.bmp'
            if newName not in os.listdir(dirName):
                shutil.copyfile(filePath, os.path.join(dirName, newName))
            os.remove(filePath)
        except Exception as e:
            continue