# -*- coding: utf-8 -*-

VERSION = "1.0.0"

import time
import threading
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import capture
import ocr
import win32api
import os
from common import tool
import const
import autopaipaiUI
import pricesettingUI

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import setting

try:
    from common import config
except Exception as ex:
    print(ex)
    print('请将脚本放在项目根目录中运行')
    print('请检查项目根目录中的 common 文件夹是否存在')
    exit(-1)

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()

# 设置，设置保存在 config 文件夹中
setconfig = config.open_setting_config()
raisePricePos = setconfig["raisePricePos"]
raisePriceBtnPos = setconfig["raisePriceBtnPos"]
bidBtnPos = setconfig["bidBtnPos"]
reloadBtnPos = setconfig["reloadBtnPos"]
attackBtnPos = setconfig["attackBtnPos"]
# raisePriceBtnPos = (raisePricePos[0]+150, raisePricePos[1])
# bidBtnPos = (raisePricePos[0]+150, raisePricePos[1]+132)

currTimePosSize = setconfig["currTimePosSize"]
minPricePosSize = setconfig["minPricePosSize"]
myPricePosSize = setconfig["myPricePosSize"]

raisePrice = setconfig["raisePrice"]
bidTime = setconfig["bidTime"]
attackLastTime = setconfig["attackLastTime"]

minPriceFileName = "minPrice.bmp"
currTimeFileName = "currTime.bmp"
myPriceFileName = "myPrice.bmp"

bidRunning = threading.Event()
bidRunning.set()
# bidRunning = None

def reloadPriceSetting():
    global setconfig, raisePrice, bidTime, attackLastTime
    setconfig = config.open_setting_config()
    raisePrice = setconfig["raisePrice"]
    bidTime = setconfig["bidTime"]
    attackLastTime = setconfig["attackLastTime"]


def start():
    # setting.cal_setting_config()
    timeSync()

    m.click(raisePricePos[0], raisePricePos[1])
    # k.press_key(k.control_key)
    # k.tap_key('A')
    # K.release_key(k.control_key)
    k.press_keys([k.control_key, 'A'])
    k.tap_key(k.delete_key)
    k.type_string(raisePrice)
    # m.click(x_dim/2, y_dim/2, 1)
    # k.type_string('Hello, World!')700


def bid(signal=None):
    while bidRunning.isSet():
        time.sleep(0.01)
        minute = time.strftime("%H:%M")

        if minute >= '11:30':
            print('出价失败！')
            if signal is not None:
                signal.emit('{}'.format('出价失败！'))
            break

        if minute != '11:29':
            continue

        second = time.strftime("%S")

        now = time.strftime("%H:%M:%S")
        sys.stdout.write('thread({}) {}!\n'.format(threading.currentThread().name, now))
        if signal is not None:
            signal.emit('{}'.format('等待出价..'))

        if second == bidTime:
            m.click(raisePriceBtnPos[0], raisePriceBtnPos[1])
            print('加价按钮已点击！')
            time.sleep(0.01)
            m.click(bidBtnPos[0], bidBtnPos[1])
            print('出价按钮已点击！')

            if signal is not None:
                signal.emit('{}'.format('出价按钮已点击！'))

            break

    attack(signal)


def getMyPrice():
    capture.customCapture(myPriceFileName, myPricePosSize["pos"], myPricePosSize["size"])
    try:
        myPrice = int(ocr.image_to_string(myPriceFileName, font='fontpp'))
    except Exception:
        myPrice = 0
    return myPrice


def attack(signal=None):
    if bidRunning.isSet():
        time.sleep(1)
    else:
        return
    myPrice = 0
    while bidRunning:
        if myPrice == 0:
            myPrice = getMyPrice()
            if signal is not None:
                signal.emit('你的出价为{}'.format(myPrice))
            if myPrice == 0:
                time.sleep(0.1)
                continue

        minute = time.strftime("%H:%M")
        now = time.strftime("%H:%M:%S")
        if minute >= '11:30':
            print('确认出价失败！')
            if signal is not None:
                signal.emit('{}'.format('确认出价失败！'))
            break

        second = time.strftime("%S")
        sys.stdout.write('thread({}) {}!\n'.format(threading.currentThread().name, now))

        if second == attackLastTime:
            m.click(attackBtnPos[0], attackBtnPos[1])
            print('确认出价按钮已点击')
            if signal is not None:
                signal.emit('{}'.format('最后出击，确认出价按钮已点击！'))
            break

        capture.customCapture(minPriceFileName, minPricePosSize["pos"], minPricePosSize["size"])
        try:
            minPrice = int(ocr.image_to_string(minPriceFileName))
            print('最低出价为：', minPrice)

            if signal is not None:
                signal.emit('最低出价为：{}'.format(minPrice))
            os.remove(minPriceFileName)
        except Exception:
            if signal is not None:
                signal.emit('最低出价获取失败，重试！')
            print('最低出价获取失败，重试！')
            continue

        if myPrice <= minPrice + 300:
            m.click(attackBtnPos[0], attackBtnPos[1])
            print('确认出价按钮已点击')

            if signal is not None:
                signal.emit('{}'.format('确认出价按钮已点击！'))
            break


def timeSync():
    import datetime
    print("正在校准系统时间")

    # capture.customCapture(currTimeFileName, currTimePosSize["pos"], currTimePosSize["size"])
    # currTime = ocr.image_to_string(currTimeFileName)
    # lastTime = currTime
    # while lastTime == currTime or lastTime == '':
    #     lastTime = currTime
    #     t = time.time()
    #     capture.customCapture(currTimeFileName, currTimePosSize["pos"], currTimePosSize["size"])
    #     currTime = ocr.image_to_string(currTimeFileName)
    #     os.remove(currTimeFileName)
    #     print('拍牌系统时间为：', currTime, '获取拍牌系统时间耗时：', time.time()-t)
    #     if currTime == "":
    #         continue

    # retrycount = 0
    # while retrycount < 1:
    #     retrycount += 1
    t = time.time()
    tool.writelog('log\\test.log', ['start capture'])
    capture.customCapture(currTimeFileName, currTimePosSize["pos"], currTimePosSize["size"])
    tool.writelog('log\\test.log', [os.getcwd()])
    currTime = ocr.image_to_string(currTimeFileName)
    tool.writelog('log\\test.log', [currTime])
    os.remove(currTimeFileName)
    tool.writelog('log\\test.log', ['remove ok!'])
    print('拍牌系统时间为：', currTime, '获取拍牌系统时间耗时：', time.time()-t)

    if currTime == "":
        raise Exception('拍牌系统时间为空，时间校准失败！')

    day = datetime.datetime.now()
    now = datetime.datetime.strptime(currTime, '%H:%M:%S')
    # print(day.weekday())
    # print(now.hour)
    # millisecond = int((time.time()-t) * 1000)
    # print(millisecond)
    win32api.SetSystemTime(day.year, day.month, day.weekday(), day.day, now.hour-8, now.minute, now.second, 0)
    print("系统时间校准完毕")


def reload():
    m.click(reloadBtnPos[0], reloadBtnPos[1])


class autopaipai(QWidget, autopaipaiUI.Ui_MainWindow):

    signal_ShowStatus = pyqtSignal(str)
    signal_ShowError = pyqtSignal(Exception, str)
    bidThread = None
    timeThread = None
    MainWindow = None

    # @tool.log()
    # @tool.catchException()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.btnStart.clicked.connect(self.Start)
        self.btnTimeSync.clicked.connect(self.TimeSync)
        self.btnSetting.clicked.connect(self.Setting)

        self.signal_ShowStatus.connect(self.ShowStatus)
        self.signal_ShowError.connect(self.ShowError)

        self.timeThread = ShowSysTimeThread()
        self.timeThread.signal_ShowSysTime.connect(self.ShowSysTime)
        self.timeThread.signal_timesync.connect(self.TimeSync)
        self.timeThread.start()
        
        screen = QDesktopWidget().availableGeometry()  
        size = MainWindow.geometry()  
        MainWindow.move(screen.width() - size.width(), screen.height() - size.height())
        MainWindow.setWindowFlag(Qt.WindowStaysOnTopHint)
        MainWindow.closeEvent = self.closeEvent
        self.MainWindow = MainWindow

    @tool.log()
    @tool.catchException()
    def Start(self, e):
        start()
        if self.bidThread is not None:
            self.bidThread.stop()

        self.bidThread = BidThread()
        self.bidThread.signal_ShowStatus.connect(self.ShowStatus)
        self.bidThread.signal_ShowError.connect(self.ShowError)
        self.bidThread.start()

    @tool.log()
    @tool.catchException()
    def TimeSync(self, e):
        timeSync()

    @tool.log()
    @tool.catchException()
    def Setting(self, e):
        setting.cal_setting_config()
        setting.test_pos()
        os.startfile(setting.filePath)
        button = QMessageBox.warning(self.MainWindow, '需要重启', '位置校准后需要重启软件！请重启', buttons=QMessageBox.Ok|QMessageBox.Cancel)
        if button == QMessageBox.Ok:
            self.MainWindow.close()

    # @tool.log()
    @tool.catchException()
    def ShowSysTime(self, time):
        self.lblTime.setText(time)

    @tool.log()
    @tool.catchException()
    def ShowStatus(self, text):
        # common.writelog(file='log\\{}.log'.format(time.strftime('%Y%m%d')), logContent=['info', text])
        status = '{}: {}'.format(time.strftime('%H:%M:%S'),str(text))
        self.statusbar.showMessage(status)

    def ShowError(self, e, funcName=''):
        ErrorInfo = '{}失败！: {}'.format(const.FunctionName.get(funcName, funcName), repr(e))

        # button = QMessageBox.critical(self, '发生错误', ErrorInfo, QMessageBox.Ok|QMessageBox.Cancel)
        # if button == QMessageBox.Ok:
        # self.close()
        self.ShowStatus(ErrorInfo)

    @tool.log()
    @tool.catchException()
    def closeEvent(self, event):
        if self.timeThread is not None:
            self.timeThread.stop()
        global bidRunning
        if self.bidThread is not None and bidRunning.isSet():
            self.bidThread.stop()

        # time.sleep(0.1)

        tool.writelog(file='log\\{}{}.log'.format(self.__class__.__name__, time.strftime('%Y%m%d')), logContent=['info', 'closed'])
        print('closed')
        event.accept()


class ShowSysTimeThread(QThread):
    
    signal_ShowSysTime = pyqtSignal(str)
    signal_timesync = pyqtSignal()
    
    def __init__(self, parent = None):
        super(ShowSysTimeThread, self).__init__(parent)
        self._flag = threading.Event()  # 用于暂停线程的标识
        self._running = threading.Event()  # 用于停止线程的标识

    def run(self):
        self._running.set()
        timesynccount = 0
        while self._running.isSet():
            time.sleep(0.1)
            self.signal_ShowSysTime.emit(time.strftime("%H:%M:%S"))

            timesynccount += 1
            if timesynccount >= 50:
                timesynccount = 0
                # self.signal_timesync.emit()

    def stop(self):
        self._running.clear()


class BidThread(QThread):

    signal_ShowStatus = pyqtSignal(str)
    signal_ShowError = pyqtSignal(Exception, str)

    def __init__(self, parent = None):
        super(BidThread, self).__init__(parent)
        self._flag = threading.Event() #用于暂停线程的标识
        global bidRunning
        bidRunning = threading.Event() #用于停止线程的标识

    def run(self):
        self.signal_ShowStatus.emit('自动拍牌已启动！')
        global bidRunning
        bidRunning.set()
        try:
            bid(self.signal_ShowStatus)
        except Exception as e:
            self.signal_ShowError.emit(e, '出价线程')  
            self.signal_ShowStatus.emit('出价线程出错，已停止！原因：{}'.format(str(e)))

    def stop(self):
        global bidRunning
        bidRunning.clear()


if __name__ == '__main__':
    # start()
    # bidTread = threading.Thread(target=bid)
    
    # bidTread.start()
    # bidTread.join()
    
    # input('输入[Enter]后退出。。。')

    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = autopaipai()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())