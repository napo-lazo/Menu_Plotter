from abc import ABC, abstractmethod

class _Node(ABC):
    '''Base abstract class for the Nodes that will be used in the Menu_Plotter class.'''
    _neighborNodesIds: list

    def __init__(self, neighborNodesIds: list):
        if (len(neighborNodesIds) == 0):
            raise ValueError("neighborNodesIds must not be an empty list")

        self._neighborNodesIds = neighborNodesIds

    @abstractmethod
    def ActivateNode(self) -> str:
        '''Abstract method that triggers the behavior of the node.'''
        ...

class _MenuNode(_Node):
    '''
    Concrete class for the nodes that display a menu with a list of options that the user most pick from.
    The Menu_Plotter class will then set the current node to the chosen option from the menu.
    An optional header and footer string can be passed to the node to add addtional information to the menu.
    '''
    _menuOptions: list
    _header: str
    _footer: str

    def __init__(self, neighborNodesIds: list, menuOptions: list, header: str = None, footer: str = None):
        super().__init__(neighborNodesIds)
        
        self._menuOptions = menuOptions
        self._header = header
        self._footer = footer

    def ActivateNode(self) -> str:
        '''
        Takes input from the user, verfies it's valid, and then returns the id of the 
        corresponding node to have Menu_Plotter set it as the new current node.
        '''
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
    '''
    Concrete class for the nodes that performs an action. If the node has multiple possible
    nodes it can travel to, a function that translates the result of the action function into
    a valid index value is needed, otherwise it will default to always picking the first node 
    in the list.
    '''
    _action: callable
    _resultInterpreter: callable

    def __init__(self, neighborNodesIds: list, action: callable, resultInterpreter: callable = None):
        super().__init__(neighborNodesIds)

        self._action = action
        self._resultInterpreter = resultInterpreter

    def ActivateNode(self) -> str:
        '''
        Triggers the action function of the node, translating its result
        to a valid index value if a resultInterpreter function was provided and
        lastly returns the id of the corresponding node to have Menu_Plotter set it 
        as the new current node.
        '''
        idIndex = 0
        
        self._action()

        if (self._resultInterpreter is not None):
            idIndex = self._resultInterpreter()

        return self._neighborNodesIds[idIndex]

class Menu_Plotter:
    ''''''
    _Nodes: dict = {}
    _currentNode: _Node

    def AddMenuNode(self, id: str, neighborNodesIds: list, menuOptions: list,  header: str = None, footer: str = None) -> None:
        '''
        Adds a menu node to the pool of nodes.
        A list with the ids of its neighbor nodes must be provided, as well as a list with the menu options
        that will be displayed on screen.
        Optionally, a header and/or footer string can be passed to displayed extra information on screen.
        '''
        if (id not in self._Nodes):
            self._Nodes[id] = _MenuNode(neighborNodesIds, menuOptions, header, footer)
        else:
            raise ValueError(f"Id '{id}' is already in use")
    
    def AddActionNode(self, id: str, neighborNodesIds: list, action: callable, resultInterpreter: callable = None) -> None:
        '''
        Adds an action node to the pool of nodes.
        A list with the ids of its neighbor nodes must be provided, as well as a function that will be
        triggered when activating the node.
        Optionally, if there are more than one neighbor nodes, a resultInterpreter function must be passed
        to translate the result of the action function, otherwise the node will default to go through the 
        first option in the neighborNodesIds.
        '''
        if (id not in self._Nodes):
            self._Nodes[id] = _ActionNode(neighborNodesIds, action, resultInterpreter)
        else:
            raise ValueError(f"Id '{id}' is already in use")

    def SetStartNode(self, id: str) -> None:
        '''Mark the node with the passed id as the starting point.'''
        self._currentNode = self._Nodes[id]

    def Start(self) -> None:
        '''Starts the traversal through the Menu_Plotter.'''
        while (True):
            nextNodeId = self._currentNode.ActivateNode()

            if (nextNodeId.lower() == "exit"):
                break

            self._currentNode = self._Nodes[nextNodeId]
