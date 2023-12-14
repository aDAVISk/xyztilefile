from .xyzgeneric import *

# Default functions for loading and saving files
_loadfunc = lambda filename : "".join([ff for ff in open(filename, "r")]).rstrip()

_savefunc = lambda filename, val : print(val, file=open(filename,"w"))

_parsefunc = lambda response : response.text

class XYZTxt(XYZGeneric):
    def __init__(self, base, loadfunc=_loadfunc, savefunc=_savefunc, **kwargs):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc, **kwargs)

class XYZHttpTxt(XYZHttpGeneric):
    def __init__(self, base, parsefunc=_parsefunc, **kwargs):
        super().__init__(base, parsefunc=_parsefunc, **kwargs)


# {"type string from the extension" : Class}
xyztiletype = {"txt":XYZTxt}
xyzhttptype = {"txt":XYZHttpTxt}
