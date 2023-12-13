import os
from .xyzgeneric import *

__LATLIMIT = 85.0511
__YZERO = math.atanh(math.sin(math.radians(__LATLIMIT)))
__TD = 256

def calc_xyz_from_lonlat(lon: float, lat: float, z: int):
    """Calculates XYZ tile indices of the given zoom level at the given longitude and latitude.

    Args:
        lon (float): longitude (degree).
        lat (float): latitude (degree).
        z (int): zoom level (0 or greater).

    Returns:
        (x, y, z) (tupple): tile indices x and y of the zoom level z.

    """
    if z < 0:
        raise ValueError("Zoom level must be 0 or greater.")
    #print(lon, lat, z)
    n = 2.0 ** z
    x = int((lon + 180.0) / 360.0 * n)
    y = int( (__YZERO-math.atanh(math.sin(math.radians(lat))))
        /(2.0*__YZERO) * n )
    return (x, y, z)

class XYZTileFile:
    """Factory class of XYZFiletype instances.

    An instance of the appropriate XYZFiletype class will be returned by judging the extension of the given base string. This class will call XYZHttpTileFile constructor if the base start with "http://".

    Keyword arguments:
        base (string): base url or file path of xyz file system. This must contain keywords "{x}", "{y}", and "{z}".
        loadfunc (method): (optional) user-defined loading function.
        savefunc (method): (optional) user-defined saving function.

    """
    typeclass = {}
    def __new__(cls, base: str, **kwargs):
        if isinstance(base, str):
            if base[0:7] == "http://":
                return XYZHttpTileFile(base=base, **kwargs)
            type = os.path.splitext(base)[-1][1:]
            if type in cls.typeclass:
                return cls.typeclass[type](base=base, **kwargs)
        return XYZGeneric(base=base, **kwargs)

class XYZHttpTileFile(XYZTileFile):
    typeclass = {}
    def __new__(cls, base=None, **kwargs):
        if isinstance(base, str):
            if base[0:7] != "http://":
                return XYZTileFile(base=base, **kwargs)
            type = os.path.splitext(base)[-1][1:]
            if type in cls.typeclass:
                return cls.typeclass[type](base=base, **kwargs)
        return XYZHttpGeneric(base=base, **kwargs)


for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module == "xyztilefile.py" \
        or module == "xyzgeneric.py" or module[-3:] != '.py':
        continue
    #print(f"Importing {module}")
    exec(f"from .{module[:-3]} import *" )
    XYZTileFile.typeclass.update(xyztiletype)
    XYZHttpTileFile.typeclass.update(xyzhttptype)
del module
del xyztiletype
del xyzhttptype

#print(XYZTileFile.typeclass)
