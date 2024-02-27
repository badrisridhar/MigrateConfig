# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:16:04 2024

@author: bathi
"""

from utility import Transform as tr

class ProcessInput:
    def processinp(self,jsonObject,objectname):
        output=[]
        jsonlist=jsonObject["member"]
        for jsonobj in jsonlist:
            transform=tr.Transform(objectname,jsonobj,None)
            output.append(transform.transform())
        return output

    def processinpchild(self,jsonObject,objectname):
        output=[]
        for jsonobj in jsonObject:
            transform=tr.Transform(objectname,jsonobj,None)
            output.append(transform.transform())
        return output