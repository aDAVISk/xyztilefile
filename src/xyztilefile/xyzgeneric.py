
class XYZGeneric:
    def __init__(self, base=None, loadfunc=None, savefunc=None):
        self.base = base
        self.loadfunc = loadfunc
        self.savefunc = savefunc

    def __repr__(self):
        # ref: https://ja.pymotw.com/2/pprint/
        return f"<{repr(self.__class__)}: base={repr(self.base)}>"

class XYZHttpGeneric(XYZGeneric):
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        #print(self.data)
