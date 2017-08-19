class User:
    """一个有关用户的类"""

    def __init__(self, first_name, last_name, email, phone_code):
        """构造函数，用于初始化实例属性"""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_code = phone_code
        self.login_attempts = 0

    def describe_user(self):
        """有关用户的详细信息"""
        print("用户的名字：" + self.first_name.title() + self.last_name.title())
        print("电子邮箱：" + self.email)
        print("手机号码：" + self.phone_code)

    def greeet_user(self):
        """向用户问候"""
        print("欢迎光临，" + self.first_name.title() + self.last_name.title())

    def increment_login_attempts(self):
        """试图登录的累计"""
        self.login_attempts +=1

    def reset_login_attempts(self):
        """恢复试图登录的次数为0"""
        self.login_attempts = 0


def main():
    """程序入口"""
    lwq = User("梁", "武强", "l_wuqiang@126.com", "13589958545")
    chy = User("曹", "海鹰", "l_wuqiang@126.com", "13561093685")

    lwq.describe_user()
    chy.describe_user()
    lwq.greeet_user()
    chy.greeet_user()
    for i in range(5):
        lwq.increment_login_attempts()
    print("登录次数" + str(lwq.login_attempts))
    lwq.reset_login_attempts()
    print("复位后，登录次数：" + str(lwq.login_attempts))


if __name__ == "__main__":
    """是否直接调用该文件"""
    main()

