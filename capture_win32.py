# -*- coding: utf-8 -*-

import time
import win32gui, win32ui, win32con, win32api


def customCapture(filename, pointLeft, bmpSize):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, bmpSize[0], bmpSize[1])
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), bmpSize, mfcDC, pointLeft, win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

def windowCapture(filename):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


# if __name__ == '__main__':
#     import ocr
#     import os
#     import shutil
#     import autoPaipai
#     dirName = 'img/trainingdata'
#     filePath = os.path.join(dirName, 'custom.bmp')

#     while True:
#         try:
#             # customCapture(filePath, (200, 652), (56, 19)) #当前价格
#             customCapture(filePath, (166, 633), (80, 19)) #当前时间

#             string = ocr.image_to_string(filePath)
#             if string == '':
#                 print('reload')
#                 time.sleep(5)
#                 autoPaipai.reload()
#             newName = string + '.bmp'
#             if newName not in os.listdir(dirName):
#                 shutil.copyfile(filePath, os.path.join(dirName, newName))
#             os.remove(filePath)
#         except Exception as e:
#             continue