
class XYZgeneric:
    def __init__(self):
        self.data = None

    def __repr__(self):
        # ref: https://ja.pymotw.com/2/pprint/
        return f"<{repr(self.__class__)}: {repr(self.data)}>"

class XYZHttpGeneric(XYZgeneric):
    def __init__(self):
        super().__init__()
        #print(self.data)
