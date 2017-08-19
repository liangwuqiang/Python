from c9_3_user import User

class Admin(User):
    def __init__(self, first_name, last_name, email, phone_code):
        super().__init__(first_name, last_name, email, phone_code)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)


def main():
    admin = Admin("阿", "强", "l_wuqiang@126.com", "13589958545")
    admin.show_privileges()

if __name__ == "__main__":
    main()
