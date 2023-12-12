from .xyzgeneric import *

class XYZSample(XYZGeneric):
    pass

class XYZHttpSample(XYZHttpGeneric):
    pass

xyztiletype = {"sample":XYZSample}
xyzhttptype = {"sample":XYZHttpSample}

#print(globals())
#globals()["XYZTileFile"].types["sample"] = XYZSample
