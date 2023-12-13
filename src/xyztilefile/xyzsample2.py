from .xyzgeneric import *

# Default functions for loading and saving files
_loadfunc = lambda filename : filename

_savefunc = lambda filename, val : print(filename, val)

_parsefunc = lambda response : print(response)

class XYZSample2(XYZGeneric):
    def __init__(self, base, loadfunc=_loadfunc, savefunc=_savefunc, **kwargs):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc, **kwargs)

class XYZHttpSample2(XYZHttpGeneric):
    def __init__(self, base, parsefunc=_parsefunc, **kwargs):
        super().__init__(base, parsefunc=_parsefunc, **kwargs)


# {"type string from the extension" : Class}
xyztiletype = {"xyzsample2":XYZSample2}
xyzhttptype = {"xyzsample2":XYZHttpSample2}
