from .xyzgeneric import *

class XYZSample2(XYZgeneric):
    pass

class XYZHttpSample2(XYZHttpGeneric):
    pass

tiletype = {"sample2":XYZSample2}
httptype = {"sample2":XYZHttpSample2}

#print(globals())
#globals()["XYZTileFile"].types["sample"] = XYZSample
