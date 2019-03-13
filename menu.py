#!/usr/bin/python
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
    # clear screen at start of every loop
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
    # get chosen input 
    choice = raw_input(">> ")
    try:
      # If 'q' exit while loop (return)
      if choice.lower() == 'q':
        return
      # prepare vars (decrement by 1 to match dict keys)
      choice = int(choice)
      choice -=1
      # if input below 0 skip loop (pass) - list behavour undesirable
      if choice < 0:
        raise Exception('number out of range')
      # SSH to chosen device
      chosenDevice = menuList[choice]
      print "for item: %s, Run: 'ssh %s'" % (chosenDevice, menuDict[chosenDevice]['conn'])
      os.system('ssh ' + menuDict[chosenDevice]['conn'])
    except Exception, e:
      # for DEBUG, uncomment
      #print 'Exception caught: %s' % e
      pass
    # for DEBUG, uncomment
    #time.sleep(1)

if __name__ == "__main__":
  main()

