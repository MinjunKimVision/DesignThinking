#!/usr/bin/env python

import sys

SelectedOper = 4;

def plus(first,second) :
    print(first+"+"+second+"="+str(float(first)+float(second)))
def minus(first,second) :
    print(first+"-"+second+"="+str(float(first)-float(second)))
def times(first,second) :
    print(first+"x"+second+"="+str(float(first)*float(second)))
def divide(first,second) :
    if(first == "0" or second == "0"):
        print("Devided By Zero")
    elif(1) :    
        print(first+"/"+second+"="+str(float(first)/float(second)))

def OperationSelector(oper) :
    if(oper == "+") :
        SelectedOper = 0
        plus(sys.argv[1],sys.argv[2])
    elif(oper == "-") :
        SelectedOper = 1
        minus(sys.argv[1],sys.argv[2])
    elif(oper == "x" and oper == "X") :
        SelectedOper = 2
        times(sys.argv[1],sys.argv[2])
    elif(oper == "/") :
        SelectedOper = 3
        divide(sys.argv[1],sys.argv[2])

def main():
    OperationSelector(sys.argv[3])


main()
