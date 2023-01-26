from Menu_Plotter import Menu_Plotter

Menu = Menu_Plotter()

def printBalance():
    print("You have $10,000")

def withdrawMoney():
    print("You have withdrawn $500")

Menu.AddMenuNode("start", ["Show Balance", "Withdraw", "Exit"], ["print", "withdraw", "exit"])
Menu.AddActionNode("print", printBalance, ["start"])
Menu.AddMenuNode("print", ["Back"], ["start"])
Menu.AddActionNode("withdraw", withdrawMoney, ["start"])
Menu.AddMenuNode("withdraw", ["Back"], ["start"])

Menu.SetStartNode("start")
Menu.ActivateCurrentNode()