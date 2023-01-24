from Menu_Plotter import Menu_Plotter

Menu = Menu_Plotter()

Menu.AddMenuNode("start", ["Log in", "Sign in", "Exit"], ["log in", "sign in", "exit"])
Menu.AddMenuNode("log in", ["Back"], ["start"])
Menu.AddMenuNode("sign in", ["Back"], ["start"])

Menu.SetStartNode("start")
Menu.ActivateCurrentNode()