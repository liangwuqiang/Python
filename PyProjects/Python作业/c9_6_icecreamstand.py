from c9_4_number_served import Restaurant


class IceCreamStand(Restaurant):
    """冰淇淋店继承于餐厅"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["甜的", "咸的", "辣的", "酸的"]

    def show_flavors(self):
        """显示各种口味"""
        print("口味的种类有：" + str(self.flavors))


def main():
    print("ok")
    my_icecreamstand = IceCreamStand("我的冰淇淋店", "油炸")
    my_icecreamstand.describe_restaurant()
    my_icecreamstand.open_restaurant()
    my_icecreamstand.show_flavors()

if __name__ == "__main__":
    main()
