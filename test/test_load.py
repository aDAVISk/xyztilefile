from xyztilefile import *
import pprint

test = XYZTileFile()
pp = pprint.PrettyPrinter(indent=3)
pp.pprint(test)
test.data = 100
pp.pprint(test)

test_http = XYZTileFile(type="http")
pp.pprint(test_http)

test_sample = XYZTileFile(type="sample2")
pp.pprint(test_sample)
