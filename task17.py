class Session:
    def __init__(self):
        """_summary_
        """
        self.username = None

    def login(self, username: str):
        """_summary_

        Args:
            username (str): _description_
        """
        self.username = username
        print(f"{self.username} logged in")

    def logout(self):
        """_summary_
        """
        if self.username:
            print(f"{self.username} logged out")
        else:
            print("No user logged in")


s = Session()
s.login("Ali")
s.logout()
