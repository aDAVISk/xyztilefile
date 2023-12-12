from .xyzgeneric import *

class XYZSample(XYZgeneric):
    pass

class XYZHttpSample(XYZHttpGeneric):
    pass

tiletype = {"sample":XYZSample}
httptype = {"sample":XYZHttpSample}

#print(globals())
#globals()["XYZTileFile"].types["sample"] = XYZSample
