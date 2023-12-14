from xyztilefile import *
import pprint


pp = pprint.PrettyPrinter(indent=3)

pp.pprint(calc_xyz_from_lonlat(135.0,35.0,15))
x, y, z = calc_xyz_from_lonlat(135.0,35.0,15)

test= XYZTileFile("./test/{z}/{x}/{y}.png")
pp.pprint(test)

test_http = XYZTileFile("http://www.mockup.net/tile/{z}/{x}/{y}.png")
pp.pprint(test_http)
try:
    pp.pprint(test_http.save())
except NotImplementedError as e:
    print(f"NotImplementedError is detected as expected: {e}")
test_http.get(x,y,z)


test_sample = XYZTileFile("./tile/{z}/{x}/{y}.xyzsample")
pp.pprint(test_sample)

try:
    test_error = XYZTileFile(None)
except TypeError as e:
    print(f"TypeError is detected as expected: {e}")

try:
    test_error = XYZTileFile("http://google.com")
except ValueError as e:
    print(f"ValueError is detected as expected: {e}")


xyz = calc_xyz_from_lonlat

test_main = XYZTileFile("./tile_sample/{z}/{x}/{y}.txt")
txt = test_main.get(*xyz(135.0,35.0,15))
pp.pprint(txt)
pp.pprint(test_main.set(x,y,z,txt))#+"\nNew line is added"))
pp.pprint(test_main.save(x,y,z))
