from .xyzgeneric import *

# Default functions for loading and saving
_loadfunc = lambda filename : filename

_savefunc = lambda filename, val : print(filename, val)

class XYZSample(XYZGeneric):
    def __init__(self, base, loadfunc=_loadfunc, savefunc=_savefunc):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc)

class XYZHttpSample(XYZHttpGeneric):
    def __init__(self, base, loadfunc=_loadfunc, savefunc=_savefunc):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc)


# {"type string from the extension" : Class}
xyztiletype = {"xyzsample":XYZSample}
xyzhttptype = {"xyzsample":XYZHttpSample}
