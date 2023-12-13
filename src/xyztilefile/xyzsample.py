from .xyzgeneric import *

_loadfunc = lambda x : x

_savefunc = lambda x : x

class XYZSample(XYZGeneric):
    def __init__(self, base=None, loadfunc=_loadfunc, savefunc=_savefunc):
        super().__init__(base=base, loadfunc=loadfunc, savefunc=savefunc)

class XYZHttpSample(XYZHttpGeneric):
    def __init__(self, base=None, loadfunc=_loadfunc, savefunc=_savefunc):
        super().__init__(base=base, loadfunc=loadfunc, savefunc=savefunc)


xyztiletype = {"sample":XYZSample}
xyzhttptype = {"sample":XYZHttpSample}
