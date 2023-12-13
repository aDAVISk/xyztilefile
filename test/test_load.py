from xyztilefile import *
import pprint

pp = pprint.PrettyPrinter(indent=3)

test = XYZTileFile(base="./test/{z}/{x}/{y}.png")
pp.pprint(test)

test_http = XYZTileFile(base="http://www.mockup.net/tile/{z}/{x}/{y}.png")
pp.pprint(test_http)

test_sample = XYZTileFile(base="./tile/{z}/{x}/{y}.xyzsample")
pp.pprint(test_sample)

#print(globals())
