#!/usr/bin/env python2

import os,re,sys,urllib

for arg in sys.argv[1:]:
    file = os.path.abspath(arg)
    print 'file://%s'%(urllib.quote(file))
    
