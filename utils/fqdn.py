#!/usr/bin/python3
# coding=utf-8

import re
import sys

def splitNormalWord(str):
    return re.sub(r'([A-Z][a-z]+)', r'-\1', str)

def splitProperWork(str):
    return re.sub(r'([A-Z][A-Z]+)', r'-\1', str)

def deleteFirstMinus(str):
    return re.sub(r'^-', '', str)

def returnFQDN(str):
    str = splitNormalWord(str)
    str = splitProperWork(str)
    str = deleteFirstMinus(str)
    str = str.lower()
    return str