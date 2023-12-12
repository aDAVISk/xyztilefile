
class XYZTileFile:
    def __init__(self):
        self.data = None

    def __repr__(self):
        # ref: https://ja.pymotw.com/2/pprint/
        return f"<XYZTileFile: {repr(self.data)}>"
