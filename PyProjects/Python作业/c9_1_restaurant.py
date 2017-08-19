class Restaurant:
    """"一个有关餐馆的类定义"""
    def __init__(self, restaurant_name, cuisine_type):
        """"构造函数，给属性赋值"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """方法：餐馆的描述"""
        print("餐馆名字是：" + self.restaurant_name)
        print("菜肴风格是" + self.cuisine_type)

    @staticmethod
    def open_restaurant():
        """方法：餐馆正在营业"""
        print("餐馆正在营业")


def main():
    """主要的调用函数"""
    restaurant = Restaurant("四川餐厅", "川菜")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

if __name__ == "__main__":
    main()
