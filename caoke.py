#!/usr/bin/env python
# coding=utf-8
import sys
import os

#运行方式安装好python
#D:\>python caoke.py a1.txt 即可以生成如下
#转换成功！文件为: coverted_a1.txt


def convert(source_file):
   dest_file = 'coverted_' + os.path.basename(source_file)
   ret = {}
   with open(source_file,'r',encoding='UTF-8') as f:
     for line_no, line in enumerate(f):
         line = str(line).strip()
         try:
            name, url = line.split(',') 
            if name in ret:
              ret[name] = ret[name] + '#' + url
            else:
              ret[name] = url
         except ValueError:
            pass
   with open(dest_file, 'w', encoding='UTF-8') as d:
      for name, urls in ret.items():
         line = name + ',' + urls + '\n'
         d.write(line)
   print("转换成功！文件为: %s" % dest_file)
   
   

        
if __name__ == '__main__':
   if len(sys.argv) == 1:
       print("请在脚本后面指定输入源文件!")
   elif len(sys.argv) >= 2:
       file_name = sys.argv[1]
       source_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name) 
       if os.path.isfile(file_name):
          convert(file_name)
       elif os.path.isfile(source_file):
          convert(source_file)
       else:
          print ("不存在源文件：%s" % file_name)
