# Interfejs Mediatora
class Mediator:
    def notify(self, sender, event):
        pass

# Komponent, który będzie używał mediatora
class Component:
    def __init__(self, dialog):
        self.dialog = dialog

    def click(self):
        self.dialog.notify(self, "click")

    def keypress(self):
        self.dialog.notify(self, "keypress")

# Konkretna klasa dla przycisku (Button)
class Button(Component):
    def __init__(self, dialog, label):
        super().__init__(dialog)
        self.label = label  # Label for button (e.g., 'OK', 'Cancel')

    def click(self):
        print(f"Button '{self.label}' clicked.")
        super().click()

# Konkretna klasa dla pola tekstowego (Textbox)
class Textbox(Component):
    def __init__(self, dialog, placeholder):
        super().__init__(dialog)
        self.placeholder = placeholder  # Placeholder for the input field

    def keypress(self):
        print(f"Textbox with placeholder '{self.placeholder}' received a keypress.")
        super().keypress()

# Konkretna klasa dla pola wyboru (Checkbox)
class Checkbox(Component):
    def __init__(self, dialog, label):
        super().__init__(dialog)
        self.label = label
        self.checked = False

    def check(self):
        self.checked = not self.checked
        print(f"Checkbox '{self.label}' is now {'checked' if self.checked else 'unchecked'}.")
        self.dialog.notify(self, "check")

# Mediator dla formularza logowania/rejestracji
class AuthenticationDialog(Mediator):
    def __init__(self):
        self.title = ""
        self.loginOrRegisterChkBx = Checkbox(self, "Log in/Register")
        self.loginUsername = Textbox(self, "Username")
        self.loginPassword = Textbox(self, "Password")
        self.registrationUsername = Textbox(self, "Registration Username")
        self.registrationPassword = Textbox(self, "Registration Password")
        self.registrationEmail = Textbox(self, "Email")
        self.okBtn = Button(self, "OK")
        self.cancelBtn = Button(self, "Cancel")

    def show_login_form(self):
        print("Showing login form.")
        print(f"Hide registration fields. Show {self.loginUsername.placeholder}, {self.loginPassword.placeholder}")

    def show_registration_form(self):
        print("Showing registration form.")
        print(f"Hide login fields. Show {self.registrationUsername.placeholder}, {self.registrationPassword.placeholder}, {self.registrationEmail.placeholder}")

    # Powiadomienie o zdarzeniu z komponentu
    def notify(self, sender, event):
        if sender == self.loginOrRegisterChkBx and event == "check":
            if self.loginOrRegisterChkBx.checked:
                self.title = "Log in"
                self.show_login_form()
            else:
                self.title = "Register"
                self.show_registration_form()

        elif sender == self.okBtn and event == "click":
            self.handle_ok_button_click()

        elif sender == self.cancelBtn and event == "click":
            print("Authentication process cancelled.")

    def handle_ok_button_click(self):
        if self.loginOrRegisterChkBx.checked:
            # Handling login (this should include validation)
            print("Attempting to log in with username and password.")
            # Example check: assuming the username is "user" and password is "password"
            if self.loginUsername.placeholder == "user" and self.loginPassword.placeholder == "password":
                print("Login successful!")
            else:
                print("Login failed! Invalid username or password.")
        else:
            # Handling registration
            print("Registering new user with details:")
            print(f"Username: {self.registrationUsername.placeholder}")
            print(f"Password: {self.registrationPassword.placeholder}")
            print(f"Email: {self.registrationEmail.placeholder}")
            print("Registration successful and logging in.")

# Testowanie procesu logowania i rejestracji
if __name__ == "__main__":
    # Tworzymy dialog
    dialog = AuthenticationDialog()

    # Przykład: użytkownik wybiera logowanie
    dialog.loginOrRegisterChkBx.check()  # Zaznaczenie logowania
    dialog.okBtn.click()  # Kliknięcie przycisku OK

    # Przykład: użytkownik wybiera rejestrację
    dialog.loginOrRegisterChkBx.check()  # Zaznaczenie rejestracji
    dialog.okBtn.click()  # Kliknięcie przycisku OK
    dialog.cancelBtn.click()  # Kliknięcie przycisku Anuluj
