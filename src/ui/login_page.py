import flet as ft 

class LoginPage():
    def __init__(self, page: ft.Page):
        super().__init__()
        self.view_user = "login"

        self.user_name = ft.TextField(hint_text = "Nombre de usuario")
        self.mail_field = ft.TextField(hint_text = "Correo electrónico")
        self.password_field = ft.TextField(hint_text = "Contraseña")
        self.login_button = ft.ElevatedButton(text = "Iniciar sesión")

        self.set_properties(page)
        self.deploy_controls(page)

        page.update()
        

    def set_properties(self, page: ft.Page):
        #page properties
        page.title = "Login"
        page.window.title = "Login"
        page.window.maximized = True
        page.bgcolor = "#51576D"
        page.padding = 0
        page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Center content vertically

        #field properties
        fields = [self.user_name, self.mail_field, self.password_field]

        for field in fields:
            field.border_radius = 10
            field.bgcolor = "#626880"
            field.border_width = 0
            color = "#B5BFE2"

        self.login_button.bgcolor = "#45475A"
        self.login_button.color = ft.colors.WHITE
        self.login_button.width = 800
        self.login_button.style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius = 10),)
        self.login_button.height = 50  # Set a fixed width for the button
            


    def deploy_controls(self, page: ft.Page): 
        img_container = ft.Container(
            content = ft.Image(
                src = "/home/jorge/Documentos/SIBACO_proyecto/assets/photo_2025-05-06_19-15-50.jpg",
                fit = ft.ImageFit.COVER,  # This will make the image cover the container while maintaining aspect ratio
                expand = True,  # This will make the image expand to fill the container
            ),
            expand = True,
            border_radius = 20,
            padding = 0,
            height = page.height,  # Use full page height
        )

        title_login = ft.Text("SIADE", size = 34, weight = ft.FontWeight.BOLD)
        subtitle_login = ft.Text("Sistema Inteligente de Apoyo al Diagnóstico Enfermedades", size = 16)
        header_login = ft.Column(
            [title_login, subtitle_login],
            alignment = ft.MainAxisAlignment.CENTER,
            expand = True,
        )

        change_view = ft.Text(
            f"Crea tu cuenta" if self.view_user == "login" else "Inicia sesión", 
            color = ft.colors.BLUE,
            style = ft.TextStyle(
                decoration=ft.TextDecoration.UNDERLINE,
                decoration_color = ft.colors.BLUE))
            
        controls_login = [] if self.view_user == "login" else [self.user_name]
        controls_login.extend([self.mail_field, self.password_field, self.login_button, change_view])
        login_form = ft.Column(
            controls = controls_login,
            expand = True,
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,  # Center the button horizontally
        )


        login_container = ft.Container(
            content = ft.Column([header_login, login_form]),
            expand = True,
            border_radius = 20,
            padding = 20,
            height = page.height,  # Use full page height
        )

        controls_row = ft.Row(
            controls = [img_container, login_container],
            expand = True,
            spacing = 0,
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment = ft.CrossAxisAlignment.STRETCH,  # Stretch containers vertically
        )

        page.add(controls_row)
        