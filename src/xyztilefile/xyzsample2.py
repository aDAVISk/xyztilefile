from .xyzgeneric import *

class XYZSample2(XYZGeneric):
    pass

class XYZHttpSample2(XYZHttpGeneric):
    pass

xyztiletype = {"sample2":XYZSample2}
xyzhttptype = {"sample2":XYZHttpSample2}

#print(globals())
#globals()["XYZTileFile"].types["sample"] = XYZSample
