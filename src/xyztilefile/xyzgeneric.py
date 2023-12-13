import warnings

# Default functions for loading and saving
_loadfunc = lambda x : x

_savefunc = lambda x : x

class XYZGeneric:
    def __init__(self, base=None, loadfunc=_loadfunc, savefunc=_savefunc):
        if not isinstance(base, str):
            raise TypeError("base must be string.")
        if not ("{x}" in base and "{y}" in base and "{z}" in base):
            raise ValueError('base must contain "{x}", "{y}", and "{z}".')
        self.base = base
        self.loadfunc = loadfunc
        if loadfunc is _loadfunc:
            warnings.warn("XYZGeneric: default loading function is set.")
        self.savefunc = savefunc
        if savefunc is _savefunc:
            warnings.warn("XYZGeneric: default saving function is set.")

    def __repr__(self):
        # ref: https://ja.pymotw.com/2/pprint/
        return f"<{repr(self.__class__)}: base={repr(self.base)}, {repr(self.loadfunc == _loadfunc)}>"

class XYZHttpGeneric(XYZGeneric):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #print(self.data)

# {"type string from the extension" : Class}
xyztiletype = {"xyzgeneric":XYZGeneric}
xyzhttptype = {"xyzgeneric":XYZHttpGeneric}
