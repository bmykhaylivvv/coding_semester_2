import auth
from notebook import Note, Notebook, Menu

# Set up a main user(admin) and permissions.
auth.authenticator.add_user('admin', 'adminadmin')
auth.authorizor.add_permission('notebook')
auth.authorizor.add_permission('adding_users')
auth.authorizor.add_permission("adding_permission")

# Give permissions to main user(admin)
auth.authorizor.permit_user("notebook", "admin")
auth.authorizor.permit_user("adding_users", "admin")
auth.authorizor.permit_user("adding_permission", "admin")


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "adduser": self.add_user,
            "add_user_permission": self.add_user_permission,
            "notebook": self.notebook,
            "test": self.test,
            "change": self.change,
            "logout": self.logout,
            "quit": self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(
                    username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def logout(self):
        self.username = None

    def add_user(self):
        if self.is_permitted("adding_users"):
            self.username = input('NEW USER username: ')
            self.password = input('NEW USER password: ')
            auth.authenticator.add_user(self.username, self.password)

    def add_user_permission(self):
        if self.is_permitted('adding_permission'):
            self.username_to_permit = input(
                'Enter the USERNAME of user you want to give permission: ')
            print(
                'AVAILABLE PERMISSIONS:\n- notebook\n- adding_users\n- adding_permission')
            self.permission_name = input(
                'Enter the PERMISSION name (sensitive to input correctness, choose from the list): ')
            auth.authorizor.permit_user(
                self.permission_name, self.username_to_permit)

    def notebook(self):
        if self.is_permitted("notebook"):
            Menu().run()

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(
                permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(
                e.username, permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")

    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
Please enter a command:
\tlogin\tLogin
\tadduser\tAdd new user
\tadd_user_permission Add smb permission
\tnotebook  Notebook
\tlogout\tLogOut
\tquit\tQuit
""")
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(
                        answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")


class AuthenticatorMenu:
    def __init__(self, main_user):
        pass


Editor().menu()
# if __name__ == "__main__":
#     Menu().run()
