import os
from .xyztilefile import *

_convfunc = lambda x : x

class XYZTileManager:
    """Utilize locally saved cache files with the source

    The source can be local or online.
    Firstly, this class try to load from local cache file.
    If there is no cache file, this class retrieves data from the source.
    The retrieve data is automatically saved to local cache file.

    """
    def __init__(self, srcbase:str, cachebase:str, convfunc=_convfunc):
        self._cache = {}
        self._src = XYZTileFile(srcbase, cache=self._cache)
        self._lcl = XYZHttpTileFile(cachebase, cache=self._cache)
        self._convfunc = convfunc

    def get(self, x:int, y:int, z:int):
        try:
            return self._lcl.get(x,y,z)
        except OSError:
            pass
        res = self._convfunc(self._src.get(x,y,z))
        self._lcl.set_save(x,y,z, res)
        return res
