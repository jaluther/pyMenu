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
  fullDeviceDict = yaml.load(stream)
fullDeviceList = sorted(fullDeviceDict.keys())

try:
  # get a list of device types
  devTypeList = []
  for k,v in fullDeviceDict.items():
    devTypeList.append(v['devType'])
  # remove duplicates
  devTypeList = list(set(devTypeList))

  # get a list of environment types
  envList = []
  for k,v in fullDeviceDict.items():
    envList.append(v['env'])
  # remove duplicates
  envList = list(set(envList))
  if debug:
    print devTypeList
    print envList
except Exception, e:
  print 'devices.yml formatting error: %s key missing' % e
  quit()

def printMenu(mList):
  # clear screen
  os.system('clear')
  # Print header
  print '#'*30
  print '# SSH Menu'
  print '#'*30
  # created numbered list (increment to start at 1)
  for i in mList:
    print '%s\t%s' % (mList.index(i)+1, i)
  # print trailer
  print ''
  print 'q\tBack'

def parseChoice(choice):
  # prepare vars (decrement by 1 to match dict keys)
  choice = int(choice)
  choice -=1
  # if input below 0 skip loop (raise) - list behavour undesirable
  if choice < 0:
    raise Exception('number out of range')
  return choice

def buildConn(deviceList,choice):
  # build out connection string i.e. username@ip/hostname
  chosenDevice = deviceList[choice]
  if fullDeviceDict[chosenDevice].has_key('id'):
    id = fullDeviceDict[chosenDevice]['id']
  elif defaultid:
    id = defaultid
  else:
    id = raw_input("Username: >> ")
    print '!!!!!! TIP: set default user id in python script !!!!!!'
  conn = '%s@%s' % (id, fullDeviceDict[chosenDevice]['host'])
  return conn

def topMenu():
  while True:
    topMenuList = [
            'All devices menu',
            'Device Type menu',
            'Environment menu']
    printMenu(topMenuList)
    # get chosen input
    choice = raw_input(">> ")
    try:
      # If 'q' exit while loop (return)
      if choice.lower() == 'q':
        return
      choice = parseChoice(choice)

      # Static menu list (based on topMenuList)
      if choice == 0:
        deviceListMenu(fullDeviceList)
      if choice == 1:
        devTypeMenu()
      if choice == 2:
        envMenu()

    except Exception, e:
      if debug:
        print 'Exception caught: %s' % e
      pass
    if debug:
      time.sleep(1)

def devTypeMenu():
  while True:
    printMenu(devTypeList)
    # get chosen input
    choice = raw_input(">> ")
    try:
      # If 'q' exit while loop (return)
      if choice.lower() == 'q':
        return
      choice = parseChoice(choice)

      # Create a filtered list a call device list menu
      filteredDevList = []
      for k,v in fullDeviceDict.items():
        if v['devType'] == devTypeList[choice]:
          filteredDevList.append(k)
      filteredDevList.sort()
      deviceListMenu(filteredDevList)

    except Exception, e:
      if debug:
        print 'Exception caught: %s' % e
      pass
    if debug:
      time.sleep(1)

def envMenu():
  while True:
    printMenu(envList)
    # get chosen input
    choice = raw_input(">> ")
    try:
      # If 'q' exit while loop (return)
      if choice.lower() == 'q':
        return
      choice = parseChoice(choice)

      # Create a filtered list and call device list menu
      filteredDevList = []
      for k,v in fullDeviceDict.items():
        if v['env'] == envList[choice]:
          filteredDevList.append(k)
      filteredDevList.sort()
      deviceListMenu(filteredDevList)

    except Exception, e:
      if debug:
        print 'Exception caught: %s' % e
      pass
    if debug:
      time.sleep(1)

def deviceListMenu(deviceList):
  while True:
    printMenu(deviceList)
    # get chosen input
    choice = raw_input(">> ")
    try:
      # If 'q' exit while loop (return)
      if choice.lower() == 'q':
        return
      choice = parseChoice(choice)

      # SSH to chosen device
      conn = buildConn(deviceList,choice)
      print "CONNECT: 'ssh %s'" % (conn)
      os.system('ssh ' + conn)
    except Exception, e:
      if debug:
        print 'Exception caught: %s' % e
      pass
    if debug:
      time.sleep(1)

if __name__ == "__main__":
  topMenu()

