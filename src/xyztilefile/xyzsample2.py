from .xyzgeneric import *

# Default functions for loading and saving
_loadfunc = lambda x : x

_savefunc = lambda x : x

class XYZSample2(XYZGeneric):
    def __init__(self, base, loadfunc=_loadfunc, savefunc=_savefunc):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc)

class XYZHttpSample2(XYZHttpGeneric):
    def __init__(self, base, loadfunc=_loadfunc, savefunc=_savefunc):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc)


# {"type string from the extension" : Class}
xyztiletype = {"xyzsample2":XYZSample2}
xyzhttptype = {"xyzsample2":XYZHttpSample2}
