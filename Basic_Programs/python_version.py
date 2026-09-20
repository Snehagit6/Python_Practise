import sys
print("Python %s in %s"%(sys.version, sys.platform))
s = "Python is %s in %s" #'%s'->placeholder for string datatype
print(s%(sys.version, sys.platform))