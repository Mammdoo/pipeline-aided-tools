#!/usr/bin/python3
# coding=utf-8

import re

standard_git_flow = [
    {"regex": "feature/", "stage": "develop"},
    {"regex": "develop", "stage": "develop"},
    {"regex": "bugfix/", "stage": "develop"},
    {"regex": "release/", "stage": "testing"},
    {"regex": "hotfix/", "stage": "testing"},
    {"regex": "main", "stage": "testing"},
    {"regex": "master", "stage": "testing"},
    {"regex": "^[v]{0,1}([0-9]|[1-9][0-9]+)(\\.([0-9]|[1-9][0-9]+)){2,}$", "stage": "release"}
]

standard_github_flow = [
    {"regex": "feature/", "stage": "develop"},
    {"regex": "master", "stage": "testing"},
    {"regex": "main", "stage": "testing"},
    {"regex": "^[v]{0,1}([0-9]|[1-9][0-9]+)(\\.([0-9]|[1-9][0-9]+)){2,}$", "stage": "release"}
] 


def getFlowStage(branch_flow, ref_name):
    for i in branch_flow:
        result = re.compile(i["regex"]).match(ref_name)
        if result:
            return i["stage"]
    return None
