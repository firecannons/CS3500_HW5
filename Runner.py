import sys
import os
import subprocess

ExecutableName = sys . argv [ 1 ]
InputFolder = sys . argv [ 2 ]
OutputFolder = sys . argv [ 3 ]

print ( sys . argv )

mystr = ''

for filename in os.listdir(InputFolder):
  filename2, file_extension = os.path.splitext(filename)
  subproc_array = [ './' + ExecutableName , InputFolder + '/' + filename , '>' , OutputFolder + '/' + filename2 + '-my' + file_extension ]
  proc_string = ''
  for Item in subproc_array :
    proc_string = proc_string + Item + ' '
  #subprocess.call( subproc_array )
  print(proc_string)
  os.system(proc_string)
  
  
  subproc_array = [ 'colordiff' , OutputFolder + '/' + filename2 + file_extension + '.out' , OutputFolder + '/' + filename2 + '-my' + file_extension, '--ignore-space-change', '--ignore-case', '--ignore-blank-lines' ]
  proc_string = ''
  for Item in subproc_array :
    proc_string = proc_string + Item + ' '
  print ( proc_string )
  mystr = os.system(proc_string)
  print ( '\n\n\n\n' )
