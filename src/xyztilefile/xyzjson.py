import json
from .xyzgeneric import *

# Default functions for loading and saving files
_loadfunc = lambda filename : json.load(open(filename, "r"))

_savefunc = lambda filename, val : json.dump(val, open(filename,"w"))

_parsefunc = lambda response : response.text

class XYZJson(XYZGeneric):
    def __init__(self, base, loadfunc=_loadfunc, savefunc=_savefunc, **kwargs):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc, **kwargs)

class XYZHttpJson(XYZHttpGeneric):
    def __init__(self, base, parsefunc=_parsefunc, **kwargs):
        super().__init__(base, parsefunc=_parsefunc, **kwargs)


# {"type string from the extension" : Class}
xyztiletype = {"json":XYZJson}
xyzhttptype = {"json":XYZHttpJson}
