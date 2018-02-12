# -*- coding: utf-8 -*-


try:
    from common import config
except Exception as ex:
    print(ex)
    print('请将脚本放在项目根目录中运行')
    print('请检查项目根目录中的 common 文件夹是否存在')
    exit(-1)

import re
import capture
import os

setconf = config.open_setting_config()
relconf = config.open_relative_config()
filePath = "config\\posImage"


def test_pos():
    # posList = [x for x in config.keys() if re.match(r'^(.*)Pos$', x ,re.I) != None]
    
    for x in setconf.keys():
        if re.match(r'^(.*)Pos$', x, re.I) is not None:
            value = setconf[x]
            size = [40, 20]
            pos = [value[0] - size[0] // 2, value[1] - size[1] // 2]
        elif re.match(r'^(.*)PosSize$', x, re.I) is not None:
            pos = setconf[x]["pos"]
            size = setconf[x]["size"]
        else:
            continue

        capture.customCapture(os.path.join(filePath, x + '.bmp'), pos, size)
        print(x, " ok")


def cal_setting_config():
    global setconf
    orginPoint = relconf['orgin']
    for x in relconf.keys():
        if re.match(r'^(.*)Pos$', x, re.I) is not None:
            pos = relconf[x]
            setconf[x] = [pos[0]+orginPoint[0], pos[1]+orginPoint[1]]
        elif re.match(r'^(.*)PosSize$', x, re.I) is not None:
            pos = relconf[x]["pos"]
            setconf[x]["pos"] = [pos[0]+orginPoint[0], pos[1]+orginPoint[1]]
            setconf[x]["size"] = relconf[x]["size"]
        else:
            continue
        print(x, " ok")
    config.write_setting_config(setconf)
    setconf = config.open_setting_config()
    print('位置校准完毕！')


if __name__ == "__main__":
    cal_setting_config()
    test_pos()
    input('输入[Enter]后退出。。。')

