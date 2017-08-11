#!/usr/bin/python
import sys
import os

def LIST(dir):
 filename = os.listdir(dir)
 for filename in filenames:
  path = os.path.join(dir, filename)
  print path
  print os.path.abspath(path)

def main():
 LIST(sys.argvs[1])

