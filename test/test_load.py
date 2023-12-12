from xyztilefile import XYZTileFile
import pprint

test = XYZTileFile()
pp = pprint.PrettyPrinter(indent=3)
pp.pprint(test)
test.data = 100
pp.pprint(test)
