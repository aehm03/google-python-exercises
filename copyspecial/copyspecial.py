#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dirs):
  
  file_names = [];
  file_paths= []
  
  # use each dir in the arguments as starting point
  for dir in dirs:
    
    # put initial dir on stack
    stack = [dir]
   
    while stack:
      
      # take first from stack
      current_dir = stack.pop(0)
      
      # get content 
      dir_content = os.listdir(current_dir)
      
      # process directory content 
      for content in dir_content:
        
        # get absolute paht
        content_path = os.path.abspath(os.path.join(current_dir, content))
        
        # if it's another directory, put it on the stack
        if os.path.isdir(content_path):
          stack.append(content_path)
        
        # if it's a file, check if it matches
        if os.path.isfile(content_path):
          match = re.search(r'__\w+?__', content) # important: non greedy
          if match:
            print content
            # check if name is already taken
            if not content in file_names:
              file_paths.append(content_path)
              file_names.append(content)
            else:
              print "duplicate of existing filename ", content 
      #print filenames
       
  return file_paths

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  
  # +++your code here+++
  # Call your functions
  file_paths = get_special_paths(args)
  
  if todir:
  
if __name__ == "__main__":
  main()
