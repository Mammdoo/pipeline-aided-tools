#!/usr/bin/python3
# coding=utf-8

import sys
from utils import fqdn, validate

if __name__ == '__main__':
    validate.equalParamsNumer(1)
    print(fqdn.returnFQDN(sys.argv[1]))
