class Menu_Plotter:
    _Nodes = {}
    _currentNode = None

    def AddMenuNode(self, id: str, menuOptions: list):
        if (id not in self._Nodes):
            self._Nodes[id] = _MenuNode(menuOptions)

    def SetStartNode(self, id: str):
        self._currentNode = self._Nodes[id]

    def ActivateCurrentNode(self):
        self._currentNode.ActivateNode()

class _MenuNode:
    _menuOptions = []
    neighborNodes = []

    def __init__(self, menuOptions: list):
        self._menuOptions = menuOptions

    def ActivateNode(self):
        optionNumber = 1

        for option in self._menuOptions:
            print(f"{optionNumber} - {option}")
            optionNumber += 1