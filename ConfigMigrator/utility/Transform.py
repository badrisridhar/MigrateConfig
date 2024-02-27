# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:16:53 2024

@author: bathi
"""

from utility import readXml as rx
from rules import getrules as gr

class Transform:
    def __init__(self, objectname, jsonobject, parent):
        self.objectname = objectname
        self.jsonobject = jsonobject
        self.parent = parent
        
    def transform(self):
        readXml = rx.ReadXml(self.objectname)
        resp = readXml.getRule()
        attrrule = resp[2]
        for key in attrrule.keys():
            if key in self.jsonobject.keys():
                getrule = gr.GetRules()
                rules = getrule.getObject(rlname=attrrule[key])
                self.jsonobject=rules.execute(jsonObj=self.jsonobject, attr=key, parent=self.parent)
                
        return self.jsonobject
    
    