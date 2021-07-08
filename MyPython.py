import os
import sys
import clr

pathToDllFolder = os.path.abspath(r".\bin\Debug\netstandard2.0")
sys.path.append(pathToDllFolder)
clr.AddReference("MyMockTestEnvCreator")
import System
from MyMockTestEnvCreator import Class1

class MyPythonClass(Class1):
    def __setattr__(self, key, value):
        if key in self.__dir__():
            super().__setattr__(key,value)
        else:
            print("Error. Diese Property gibt es nicht in der C# Klasse, also darf nichts geschrieben werden..")
            #raise AttributeError(f"Could not set attribute. Object {self.__name__} has no property with name {key}.")
try:
    myPythonClass = MyPythonClass()
    myPythonClass.MyProp="Diese Property existiert in der C# Klasse"
    myPythonClass.PropDasEsNichtGibt = "Hier sollte ein Error kommen."
    returnFromPythonClass = myPythonClass.Run()
    print(returnFromPythonClass)
except:
    raise
