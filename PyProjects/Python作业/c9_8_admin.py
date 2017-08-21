from c9_3_user import User
from c9_8_privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, email, phone_code):
        super().__init__(first_name, last_name, email, phone_code)
        self.privileges = Privileges()


def main():
    admin = Admin("阿", "强", "l_wuqiang@126.com", "13589958545")
    admin.privileges.show_privileges()

if __name__ == "__main__":
    main()
