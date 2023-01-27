class Menu_Plotter:
    _Nodes = {}
    _currentNode = None

    def AddMenuNode(self, id: str, menuOptions: list, neighborNodesIds: list, header: str = None, footer: str = None):
        if (id not in self._Nodes):
            self._Nodes[id] = _MenuNode(menuOptions, neighborNodesIds, header, footer)
    
    def AddActionNode(self, id: str, action: callable, neighborNodesIds: list, resultInterpreter: callable = None):
        if (id not in self._Nodes):
            self._Nodes[id] = _ActionNode(action, neighborNodesIds, resultInterpreter)

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
    _header = None
    _footer = None

    def __init__(self, menuOptions: list, neighborNodesIds: list, header: str = None, footer: str = None):
        self._menuOptions = menuOptions
        self._neighborNodesIds = neighborNodesIds
        self._header = header
        self._footer = footer
        

    def ActivateNode(self) -> str:
        invalidInput = True

        while (invalidInput):
            optionNumber = 1

            if (self._header is not None):
                print(self._header)

            for option in self._menuOptions:
                print(f"{optionNumber} - {option}")
                optionNumber += 1
            
            if (self._footer is not None):
                print(self._footer)

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
    
class _ActionNode:
    _action = None
    _neighborNodesIds = []
    _resultInterpreter = None

    def __init__(self, action: callable, neighborNodesIds: list, resultInterpreter: callable = None):
        self._neighborNodesIds = neighborNodesIds
        self._action = action
        self._resultInterpreter = resultInterpreter

    def ActivateNode(self):
        idIndex = 0
        
        self._action()

        if (self._resultInterpreter is not None):
            idIndex = self._resultInterpreter()

        return self._neighborNodesIds[idIndex]
