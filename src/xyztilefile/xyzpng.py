import json
import skimage
from .xyzgeneric import *

# Default functions for loading and saving files
_loadfunc = lambda byteio : skimage.io.imread(byteio)

_savefunc = lambda filename, val : skimage.io.imsave(filename, val)

class XYZJson(XYZGeneric):
    def __init__(self, base, loadfunc=_loadfunc, savefunc=_savefunc, **kwargs):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc, **kwargs)

class XYZHttpJson(XYZHttpGeneric):
    def __init__(self, base, loadfunc=_loadfunc, **kwargs):
        super().__init__(base, loadfunc=_loadfunc, **kwargs)


# {"type string from the extension" : Class}
xyztiletype = {"json":XYZJson}
xyzhttptype = {"json":XYZHttpJson}
