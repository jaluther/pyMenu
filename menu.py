#!/usr/bin/env python2.7
import os,time
import yaml,json

# Build menu data from YAML file
with open('devices.yml', 'r') as stream:
  menuDict = yaml.load(stream)

menuList = sorted(menuDict.keys())
for i in menuList:
  print "for item: %s, ssh to: %s" % (i, menuDict[i]['conn'])

def main():
  while True:
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
    print '999\tExit'
    # get chosen input 
    choice = raw_input(">> ")
    try:
      # prepare vars (decrement by 1 to match dict keys)
      choice = int(choice)
      choice -=1
      # Check boundary
      if choice == 998:
        return
      # SSH to chosen device
      chosenDevice = menuList[choice]
      print "for item: %s, ssh to: %s" % (chosenDevice, menuDict[chosenDevice]['conn'])
      time.sleep(1)
    except (ValueError, IndexError):
      print 'Exception caught: %s' % IndexError
      time.sleep(1)
      pass

if __name__ == "__main__":
  main()

