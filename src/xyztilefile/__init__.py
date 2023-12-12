import os
from .xyztilefile import XYZTileFile
__all__ = ['XYZTileFile']

#for module in os.listdir(os.path.dirname(__file__)):
#    if module == '__init__.py' or module == "xyztilefile.py" \
#        or module[-3:] != '.py':
#        #or module == "xyzgeneric.py" or module[-3:] != '.py':
#        #or module[-3:] != '.py':
#        #print("Pass")
#        continue
#    print(f"Importing {module}")
#    exec("from .%s import *" % module[:-3])
#del module
