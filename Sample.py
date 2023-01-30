from Menu_Plotter import Menu_Plotter

Menu = Menu_Plotter()

def printBalance():
    print("You have $10,000")

def withdrawMoney():
    print("You have withdrawn $500")

Menu.AddMenuNode("start", ["print", "withdraw", "exit"], ["Show Balance", "Withdraw", "Exit"], "Welcome", "Thanks for choosing us")
Menu.AddActionNode("print", ["printMenu"], printBalance)
Menu.AddMenuNode("printMenu", ["start"], ["Back"])
Menu.AddActionNode("withdraw", ["withdrawMenu"], withdrawMoney)
Menu.AddMenuNode("withdrawMenu", ["start"], ["Back"])

Menu.SetStartNode("start")
Menu.Start()