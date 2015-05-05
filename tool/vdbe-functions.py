#!/usr/bin/env python

import collections
import re
import sys

def main():
  functions = collections.OrderedDict()
  fn_name, fn_code = None, None
  
  lines = list(sys.stdin.readlines())
  
  while lines:
    line = lines.pop(0)
    print line,
    match = re.search(r'case OP_(\w+)', line)
    if not match:
      continue
    
    fn_name = match.group(1)
    fn_code = []
    while 1:
      line = lines.pop(0)
      if '/* Opcode:' in line:
	print line
        break
      
      print line,
      fn_code.append(line)
    
    functions[fn_name] = fn_code
   
  for fn_name, fn_code in functions.items():
    print 'void bytcode_fn_%s(ExecState* state) {' % fn_name
    print ''.join(fn_code)
    print '}'
    print '\n\n\n' 
      
      
main()
