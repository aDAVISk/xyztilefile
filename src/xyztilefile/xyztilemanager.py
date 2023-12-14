import os
from .xyztilefile import *

class XYZTileManager:
    """Utilize locally saved cache files with the source

    The source can be local or online.
    Firstly, this class try to load from local cache file.
    If there is no cache file, this class retrieves data from the source.

    """
    def __init__(self, srcbase:str, cachebase:str):
        self.__cache = {}
        self.__src = XYZTileFile(srcbase, cache=self.__cache)
        self.__lcl = XYZHttpTileFile(cachebase, cache=self.__cache)

    def get(self, x:int, y:int, z:int):
        try:
            return self.__lcl.get(x,y,z)
        except OSERROR:
            pass
        res = self.__src.get(x,y,z)
        self.__save(x,y,z)
        return res
