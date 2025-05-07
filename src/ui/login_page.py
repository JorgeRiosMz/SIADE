import flet as ft 

class LoginPage():
    def __init__(self, page: ft.Page):
        page.title = "Login"
        page.window.title = "Login"
        page.window.maximized = True
        page.add(
            ft.Text("funciona"),
        )
        page.update()
        