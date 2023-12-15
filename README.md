# xyztilefile

### cautions
- HTTP support has been implemented but not tested yet.
- XYZTileManager has been implemented, but it is a prototype.

### Sample
Basic usage sample.
```Python
from xyztilefile import *
xyz = calc_xyz_from_lonlat

x, y, z = calc_xyz_from_lonlat(135.0,35.0,15)

test_txt = XYZTileFile("./tile_sample/{z}/{x}/{y}.txt")
txt = test_txt.get(*xyz(135.0,35.0,15))
test_txt.set(x,y,z,txt+"\nNew line is added")
test_txt.save(x,y,z)
```
please check ./test/test_load.py for more sample codes

### currently supported file format 
- generic : this format is basic but your customization is needed.
- txt : encoding must be UTF-8 
- json : encoding must be UTF-8
- png : with skit-image (not tested yet)
- npy : with numpy (not tested yet)
