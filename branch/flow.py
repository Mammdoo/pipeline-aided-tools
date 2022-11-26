#!/usr/bin/python3
# coding=utf-8

import re

standard_git_flow = [
    {"regex": "feature/", "cluster": "integration", "public_registry": "disabled"},
    {"regex": "develop", "cluster": "integration", "public_registry": "disabled"},
    {"regex": "bugfix/", "cluster": "integration", "public_registry": "disabled"},
    {"regex": "release/", "cluster": "staging", "public_registry": "disabled"},
    {"regex": "hotfix/", "cluster": "staging", "public_registry": "disabled"},
    {"regex": "main", "cluster": "staging", "public_registry": "disabled"},
    {"regex": "master", "cluster": "staging", "public_registry": "disabled"},
    {"regex": "^[v]{0,1}([0-9]|[1-9][0-9]+)(\\.([0-9]|[1-9][0-9]+)){2,}$", "cluster": "production", "public_registry": "enabled"}
]

standard_github_flow = [
    {"regex": "feature/", "cluster": "integration", "public_registry": "disabled"},
    {"regex": "master", "cluster": "staging", "public_registry": "disabled"},
    {"regex": "main", "cluster": "staging", "public_registry": "disabled"},
    {"regex": "^[v]{0,1}([0-9]|[1-9][0-9]+)(\\.([0-9]|[1-9][0-9]+)){2,}$", "cluster": "production", "public_registry": "enabled"}
] 

customize_to_business_product = [
    {"regex": "^feature/", "cluster": "integration", "public_registry": "disabled"},
    {"regex": "^t-", "cluster": "integration", "public_registry": "disabled"},
    {"regex": "master", "cluster": "staging", "public_registry": "disabled"},
    {"regex": "main", "cluster": "staging", "public_registry": "disabled"},
    {"regex": "^[v]{0,1}([0-9]|[1-9][0-9]+)(\\.([0-9]|[1-9][0-9]+)){2,}$", "cluster": "production", "public_registry": "enabled"},
    {"regex": "^baseline-([0-9]|[1-9][0-9]+)(\\.([0-9]|[1-9][0-9]+)){2,}$", "cluster": "baseline", "public_registry": "enabled"}
]

match_branch_model = [
    {"model": "git", "flow": standard_git_flow},
    {"model": "github", "flow": standard_github_flow},
    {"model": "tob", "flow": customize_to_business_product}
]

def getBranchFlow(branch_model):
    for i in match_branch_model:
        if branch_model == i["model"]:
            return i["flow"]
    return "undefined"

def getFlowCluster(branch_model, ref_name):
    branch_flow=getBranchFlow(branch_model)
    if branch_flow == "undefined":
        return "undefined"
    for i in branch_flow:
        result = re.compile(i["regex"]).match(ref_name)
        if result:
            return i["cluster"]
    return "undefined"

def getFlowPublicRegistryStatus(branch_model, ref_name):
    branch_flow=getBranchFlow(branch_model)
    if branch_flow == "undefined":
        return "undefined"
    for i in branch_flow:
        result = re.compile(i["regex"]).match(ref_name)
        if result:
            return i["public_registry"]
    return "undefined"
