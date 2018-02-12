# -*- coding: utf-8 -*-
"""
调取配置文件和屏幕分辨率的代码
 """
import os
import sys
import json


def open_setting_config():
    """
    调用配置文件
    """
    # print(os.getcwd())
    with open('config\\setting.json', 'r') as f:
    # with open('{}/config/setting.json'.format(""), 'r') as f:
        print("Load setting config")
        return json.load(f)


def open_relative_config():
    """
    调用配置文件
    """
    screen_size = _get_screen_size()
    config_file = "config\\{screen_size}\\config.json".format(
        screen_size=screen_size
    )
    # config_file = "{path}/config/{screen_size}/config.json".format(
    #     path=sys.path[0],
    #     screen_size=screen_size
    # )
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            print("Load config file from {}".format(config_file))
            return json.load(f)
    else:
        with open('config\\default.json', 'r') as f:
        # with open('{}/config/default.json'.format(sys.path[0]), 'r') as f:
            print("Load default config")
            return json.load(f)
            

def write_relative_config(data):
    screen_size = _get_screen_size()
    config_file = "config\\{screen_size}\\config.json".format(
        screen_size=screen_size
    )
    if os.path.exists(config_file):
        with open(config_file, 'w') as f:
            print("Write config file from {}".format(config_file))
            json.dump(data, f, indent=4)
    else:
        with open('config\\default.json', 'w') as f:
        # with open('{}/config/default.json'.format(sys.path[0]), 'w') as f:
            print("Write default config")
            json.dump(data, f, indent=4)


def write_setting_config(data):
    with open('config\\setting.json', 'w') as f:
    # with open('{}/config/setting.json'.format(sys.path[0]), 'w') as f:
        print("Write setting config")
        json.dump(data, f, indent=4)
    

def _get_screen_size():
    return "1920x1200"

