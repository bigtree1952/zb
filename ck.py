#!/usr/bin/env python
# coding=utf-8
import sys
import os

#读取文件
f=open(r"D:\\22.txt",'r',encoding="UTF-8")
contents=f.read()

#存入文件
f= open("D:\\512.txt", 'w',encoding="UTF-8") 
f.write(contents)
f.close()