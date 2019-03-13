#!/usr/bin/python
import os,time
import yaml,json

debug=False

# Build menu data from YAML file
with open('devices.yml', 'r') as stream:
  menuDict = yaml.load(stream)

menuList = sorted(menuDict.keys())
for i in menuList:
  print "for item: %s, ssh to: %s" % (i, menuDict[i]['conn'])

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
      chosenDevice = menuList[choice]
      print "CONNECT: 'ssh %s'" % (menuDict[chosenDevice]['conn'])
      os.system('ssh ' + menuDict[chosenDevice]['conn'])
    except Exception, e:
      if debug:
        print 'Exception caught: %s' % e
      pass
    if debug:
      time.sleep(1)

if __name__ == "__main__":
  main()

