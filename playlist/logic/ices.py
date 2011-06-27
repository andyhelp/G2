# -*- coding: utf-8 -*-
import urllib
import os
import sys
ICES_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(ICES_PATH, "../..")))
import settings

NEXT_URL="http://localhost/next/"+settings.NEXT_PASSWORD


def ices_init():
  f = open("pid", "w")
  f.write(str(os.getpid()))
  f.close()
  

def ices_get_next():

  l = urllib.urlopen(NEXT_URL).readlines()
  global l
  return l[0][:-1]

def ices_get_metadata():
  global l
  return l[1]
