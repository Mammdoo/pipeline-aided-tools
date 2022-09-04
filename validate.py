#!/usr/bin/python3
# coding=utf-8

import sys

def equalParamsNumer(needNum):
    if len(sys.argv) != (needNum + 1):
        print("工具包参数异常，期望" + str(needNum) + "个")
        sys.exit(1)