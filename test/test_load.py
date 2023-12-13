from xyztilefile import *
import pprint

pp = pprint.PrettyPrinter(indent=3)

test = XYZTileFile(base="./test/{z}/{x}/{y}.png")
pp.pprint(test)

test_http = XYZTileFile(base="http://www.mockup.net/tile/{z}/{x}/{y}.png")
pp.pprint(test_http)

test_sample = XYZTileFile(base="./tile/{z}/{x}/{y}.xyzsample")
pp.pprint(test_sample)

try:
    test_error = XYZTileFile()
except TypeError as e:
    print(f"TypeError is detected as expected: {e}")

try:
    test_error = XYZTileFile(base="http://google.com")
except ValueError as e:
    print(f"ValueError is detected as expected: {e}")

pp.pprint(calc_xyz_from_lonlat(135.0,35.0,15))
#print(globals())
