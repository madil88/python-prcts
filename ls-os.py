#!/usr/bin/python
import os
import commands

def LIST(dir):
 cmd = 'ls -la' + dir
 print 'about to do this:', cmd
 return
 (status, output) = commands.getstatusoutput(cmd)

def main():
 LIST(sys.argv[1])
 

