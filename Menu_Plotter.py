class Menu_Plotter:
    _Nodes = {}
    _currentNode = None

    def AddMenuNode(self, id: str, menuOptions: list, neighborNodesIds: list):
        if (id not in self._Nodes):
            self._Nodes[id] = _MenuNode(menuOptions, neighborNodesIds)

    def SetStartNode(self, id: str):
        self._currentNode = self._Nodes[id]

    def ActivateCurrentNode(self):
        while (True):
            nextNodeId = self._currentNode.ActivateNode()

            if (nextNodeId.lower() == "exit"):
                break

            self._currentNode = self._Nodes[nextNodeId]


class _MenuNode:
    _menuOptions = []
    _neighborNodesIds = []

    def __init__(self, menuOptions: list, neighborNodesIds: list):
        self._menuOptions = menuOptions
        self._neighborNodesIds = neighborNodesIds

    def ActivateNode(self) -> str:
        invalidInput = True

        while (invalidInput):
            optionNumber = 1

            for option in self._menuOptions:
                print(f"{optionNumber} - {option}")
                optionNumber += 1
            
            userInput = input()

            try:
                userInput = int(userInput)
            except ValueError:
                print("ERROR: Type a valid number from the options' list to proceed")
                continue

            if (userInput > 0 and userInput <= optionNumber - 1):
                invalidInput = False
            else:
                print("ERROR: Type a valid number from the options' list to proceed")
                continue
        
        return self._neighborNodesIds[userInput - 1]
