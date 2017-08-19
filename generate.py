# Date: 08/19/2017
# Author: Ethical-H4CK3R
# Description: Wifi possible password
#
#

import argparse

class Wifi(object):
 def __init__(self,fname,lname=None):
  self.keys = [] # all possible keys
  self.num = 10000 # 0-10000
  self.fname = fname  # firstname of wifi
  self.lname = lname  # lastname of wifi

 def populate(self,name):
  for num in xrange(self.num):
   k1 = '{}{}\n'.format(name.lower(),num)
   k2 = '{}{}\n'.format(name.title(),num)
   k3 = '{}{}\n'.format(name.upper(),num)

   if len(k1.strip()) < 8:continue
   self.keys.append(k1)
   self.keys.append(k2)
   self.keys.append(k3)

 def generate(self):
  self.populate(self.fname)

  if self.lname:
   if self.fname.lower() != self.lname.lower():
    self.populate(self.lname)
    self.populate('{}{}'.format(self.fname,self.lname))

  if not len(self.keys):return
  with open('pass.lst','w') as fwrite:
   for key in self.keys:
    fwrite.write('{}'.format(key))

if __name__ == '__main__':
 arg = argparse.ArgumentParser()
 arg.add_argument('essid',help='the firstname of the wifi')
 arg.add_argument('-l', help='lastname of wifi',dest='lastname')
 arg = arg.parse_args()
 Wifi(arg.essid).generate() if not arg.lastname else\
 Wifi(arg.essid,arg.lastname).generate()
