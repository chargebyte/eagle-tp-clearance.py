from subprocess import call
import subprocess
import os

def run_with_error(parameters):
  try:
    shutup = open(os.devnull, 'w')
    process = subprocess.Popen(["python", "eagle-tp-clearance.py", parameters], stdout=shutup, stderr=shutup)
    stream_data = process.communicate()[0]
    assert process.returncode != 0
  except OSError as e:
    print "error executing: " + str(e)
    assert 0

def run_without_error(parameters):
  try:
    shutup = open(os.devnull, 'w')
    process = subprocess.Popen(["python", "eagle-tp-clearance.py", parameters], stdout=shutup, stderr=shutup)
    stream_data = process.communicate()[0]
    assert process.returncode == 0
  except OSError as e:
    print "error executing: " + str(e)
    assert 0

def test_commandline_interface():
  yield run_with_error, "" 		#run without any arguments
  yield run_without_error, "-h"		#run with argument to output the help screen
