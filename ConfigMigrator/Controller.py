# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:53:46 2024

@author: bathi
"""

from utility import ReadExcel as re
from utility import GetConfig as gc
from utility import PutConfig as pc
from utility import ProcessInput as pi
import warnings

readExcel = re.ReadExcel(filename = './input/Input.xlsx')
inputData = readExcel.getInputData()
#print(inputData)
rownum = 4
for input1 in inputData:
    success = 0
    error = 0
    errormsg = ""
    payload = ""
    getConfig = gc.GetConfig(input1, readExcel)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        data = getConfig.getJson()
    #print(data)
    processInp = pi.ProcessInput()
    out = processInp.processinp(data,input1[1])
    #print (json.dumps(out))
    print("Data fetched for "+input1[1]+" with where clause: "+input1[2])
    #input("Hit any key to continue with the load...")
    #print(json.dumps(out[0]))
    for ot in out:
          putConfig = pc.PutConfig(ot, readExcel,input1[1],input1[0])
          with warnings.catch_warnings():
              warnings.simplefilter("ignore")
              resp = putConfig.postJaon()
          #print (resp.status_code)
          if(str(resp.status_code).startswith("2")):
              success = success + 1
          else:
              
              error = error + 1
              errormsg = errormsg + str(resp.json())+"\n"
              payload = payload + str(ot)+"\n"
          #print(resp.json())
    readExcel.updateCell("D"+str(rownum), success)
    readExcel.updateCell("E"+str(rownum), error)
    if(error>0):
        readExcel.updateCell("F"+str(rownum), errormsg)
        readExcel.updateCell("G"+str(rownum), payload)
    print("Data load completed for "+input1[1]+" where clause: "+input1[2])
    rownum = rownum + 1
print("Check input excel to see the status")
          