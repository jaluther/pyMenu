#!/usr/bin/python
# 
# Written by: James Luther
# https://github.com/jaluther/pyMenu

import os,time
import yaml,json

debug=False
defaultid=False
#defaultid='james'

# Build menu data from YAML file
with open('devices.yml', 'r') as stream:
  menuDict = yaml.load(stream)

menuList = sorted(menuDict.keys())

def printMenu(menuList):
  # clear screen 
  os.system('clear')
  # Print header
  print '#'*30
  print '# SSH Menu'
  print '#'*30
  # created numbered list (increment to start at 1)
  for i in menuList:
    print '%s\t%s' % (menuList.index(i)+1, i)
  # print trailer
  print ''
  print 'q\tQuit'

def buildConn(choice):
  chosenDevice = menuList[choice]
  if menuDict[chosenDevice].has_key('id'):
    conn = '%s@%s' % (menuDict[chosenDevice]['id'], menuDict[chosenDevice]['host'])
  elif defaultid:
    conn = '%s@%s' % (defaultid, menuDict[chosenDevice]['host'])
  else:
    id = raw_input("Username: >> ")
    print '!!!!!! TIP: set default user id in python script !!!!!!'
    conn = '%s@%s' % (id, menuDict[chosenDevice]['host'])
  return conn

def main():
  while True:
    printMenu(menuList)
    # get chosen input 
    choice = raw_input(">> ")
    try:
      # If 'q' exit while loop (return)
      if choice.lower() == 'q':
        return
      # prepare vars (decrement by 1 to match dict keys)
      choice = int(choice)
      choice -=1
      # if input below 0 skip loop (raise) - list behavour undesirable
      if choice < 0:
        raise Exception('number out of range')

      # SSH to chosen device
      conn = buildConn(choice)
      print "CONNECT: 'ssh %s'" % (conn)
      os.system('ssh ' + conn)
    except Exception, e:
      if debug:
        print 'Exception caught: %s' % e
      pass
    if debug:
      time.sleep(1)

if __name__ == "__main__":
  main()

