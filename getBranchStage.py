#!/usr/bin/python3
# coding=utf-8

import sys
import validate
from branch import flow


match_branch_model = [
    {"model": "git", "flow": flow.standard_git_flow},
    {"model": "github", "flow": flow.standard_github_flow},
]

def getBranchFlow(branch_model):
    for i in match_branch_model:
        if branch_model == i["model"]:
            return i["flow"]


def getBranchStage(branch_model, ref_name):
    branch_flow = getBranchFlow(branch_model)
    branch_stage = flow.getFlowStage(branch_flow, ref_name)
    print(branch_stage)

if __name__ == '__main__':
    validate.equalParamsNumer(2)
    getBranchStage(sys.argv[1], sys.argv[2])
