from .xyzgeneric import *

_loadfunc = lambda x : x

_savefunc = lambda x : x

class XYZSample2(XYZGeneric):
    def __init__(self, base=None, loadfunc=_loadfunc, savefunc=_savefunc):
        super().__init__(base=base, loadfunc=loadfunc, savefunc=savefunc)

class XYZHttpSample2(XYZHttpGeneric):
    def __init__(self, base=None, loadfunc=_loadfunc, savefunc=_savefunc):
        super().__init__(base=base, loadfunc=loadfunc, savefunc=savefunc)



xyztiletype = {"sample2":XYZSample2}
xyzhttptype = {"sample2":XYZHttpSample2}
