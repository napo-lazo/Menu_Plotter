from Menu_Plotter import Menu_Plotter

Menu = Menu_Plotter()
Menu.AddMenuNode("start", ["Log in", "Sign in", "Exit"])
Menu.SetStartNode("start")
Menu.ActivateCurrentNode()