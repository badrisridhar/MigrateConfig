# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:13:37 2024

@author: bathi
"""

from rules import rules as rm
from utility import ProcessInput as pi


class ChildObj(rm.Rules):
    
    def execute(self, jsonObj, attr, parent):
        childobj = jsonObj[attr]
        processInp = pi.ProcessInput()
        out = processInp.processinpchild(childobj,attr)
        jsonObj[attr] = out    
        return jsonObj
        