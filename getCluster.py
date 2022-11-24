#!/usr/bin/python3
# coding=utf-8

import sys
from utils import validate
from branch import flow

if __name__ == '__main__':
    validate.equalParamsNumer(2)
    print(flow.getFlowCluster(sys.argv[1], sys.argv[2]))
