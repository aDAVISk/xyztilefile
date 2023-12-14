import warnings

# Default functions for loading and saving files
_loadfunc = lambda filename : filename

_savefunc = lambda filename, val : print(filename, val)

_parsefunc = lambda response : response

class XYZGeneric:
    def __init__(self, base: str, loadfunc=_loadfunc, savefunc=_savefunc, cache = None):
        if not isinstance(base, str):
            raise TypeError("base must be string.")
        if not ("{x}" in base and "{y}" in base and "{z}" in base):
            raise ValueError('base must contain "{x}", "{y}", and "{z}".')
        self._base = base
        self._loadfunc = loadfunc
        if loadfunc is _loadfunc:
            warnings.warn("XYZGeneric: default loading function is set.")
        self._savefunc = savefunc
        if savefunc is _savefunc:
            warnings.warn("XYZGeneric: default saving function is set.")
        if cache is None:
            cache = {}
        if not isinstance(cache, dict):
            raise TypeError("chache must be dict.")
        if len(cache) > 0:
            warnings.warn("XYZGeneric: non-empty shared chache is set.")
        self._cache = cache

    def __repr__(self):
        # ref: https://ja.pymotw.com/2/pprint/
        return f"<{repr(self.__class__)}: base={repr(self._base)}, cache={repr(self._cache)}>"

    def has(self, x:int, y:int, z:int):
        key = self._base.format(x=x,y=y,z=z)
        return key in self._base

    def get(self, x:int, y:int, z:int):
        key = self._base.format(x=x,y=y,z=z)
        if key not in self._base:
            self._cache[key] = self._loadfunc(key)
        return self._cache[key]

    def set(self, x:int, y:int, z:int, val):
        key = self._base.format(x=x,y=y,z=z)
        self._cache[key] = val
        return self

    def save(self, x:int, y:int, z:int):
        key = self._base.format(x=x,y=y,z=z)
        print(key)
        if key not in self._cache:
            return False
        self._savefunc(key, self._cache[key])
        return True

    def save_all(self):
        for key in self._cache:
            self._savefunc(key, self._cache[key])
        return True

class XYZHttpGeneric(XYZGeneric):
    def __init__(self, base, parsefunc=_parsefunc, loadfunc=None, savefunc=None, **kwargs):
        super().__init__(base, loadfunc=loadfunc, savefunc=savefunc, **kwargs)
        self._parsefunc = parsefunc
        if parsefunc is _parsefunc:
            warnings.warn("XYZHttpGeneric: default parsing function is set.")
        #print(self.data)

    def get(self, x:int, y:int, z:int):
        key = self._base.format(x=x,y=y,z=z)
        if key not in self._base:
            # get response with key, then pass response to _parsefunc.
            # raise error if not successfully retrieve the data
            self._cache[key] = self._parsefunc(key)
        #copy.deepcopy した方がいい？
        return self._cache[key]


    def set(self, *args, **kwargs):
        raise NotImplementedError("set is nulled for http tile class.")

    def save(self, *args, **kwargs):
        raise NotImplementedError("save is nulled for http tile class.")

    def save_all(self, *args, **kwargs):
        raise NotImplementedError("save_all is nulled for http tile class.")


# {"type string from the extension" : Class}
# These variables are not used for Generic classes
#xyztiletype = {"xyzgeneric":XYZGeneric}
#xyzhttptype = {"xyzgeneric":XYZHttpGeneric}
