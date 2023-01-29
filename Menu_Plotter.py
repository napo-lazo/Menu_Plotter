from abc import ABC, abstractmethod

class _Node(ABC):
    _neighborNodesIds: list

    def __init__(self, neighborNodesIds: list):
        if (len(neighborNodesIds) == 0):
            raise ValueError("neighborNodesIds must not be an empty list")

        self._neighborNodesIds = neighborNodesIds

    @abstractmethod
    def ActivateNode(self) -> str:
        ...

class _MenuNode(_Node):
    _menuOptions: list
    _header: str
    _footer: str

    def __init__(self, neighborNodesIds: list, menuOptions: list, header: str = None, footer: str = None):
        super().__init__(neighborNodesIds)
        
        self._menuOptions = menuOptions
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
    
class _ActionNode(_Node):
    _action: callable
    _resultInterpreter: callable

    def __init__(self, neighborNodesIds: list, action: callable, resultInterpreter: callable = None):
        super().__init__(neighborNodesIds)

        self._action = action
        self._resultInterpreter = resultInterpreter

    def ActivateNode(self) -> str:
        idIndex = 0
        
        self._action()

        if (self._resultInterpreter is not None):
            idIndex = self._resultInterpreter()

        return self._neighborNodesIds[idIndex]

class Menu_Plotter:
    _Nodes: dict = {}
    _currentNode: _Node

    def AddMenuNode(self, id: str, neighborNodesIds: list, menuOptions: list,  header: str = None, footer: str = None) -> None:
        if (id not in self._Nodes):
            self._Nodes[id] = _MenuNode(neighborNodesIds, menuOptions, header, footer)
        else:
            raise ValueError(f"Id '{id}' is already in use")
    
    def AddActionNode(self, id: str, neighborNodesIds: list, action: callable, resultInterpreter: callable = None) -> None:
        if (id not in self._Nodes):
            self._Nodes[id] = _ActionNode(neighborNodesIds, action, resultInterpreter)
        else:
            raise ValueError(f"Id '{id}' is already in use")

    def SetStartNode(self, id: str) -> None:
        self._currentNode = self._Nodes[id]

    def ActivateCurrentNode(self) -> None:
        while (True):
            nextNodeId = self._currentNode.ActivateNode()

            if (nextNodeId.lower() == "exit"):
                break

            self._currentNode = self._Nodes[nextNodeId]
