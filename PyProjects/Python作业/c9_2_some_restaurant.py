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
    si_chuan = Restaurant("四川餐厅", "川菜")
    si_chuan.describe_restaurant()

    guang_zhou = Restaurant("广东餐厅", "粤菜")
    guang_zhou.describe_restaurant()

    shan_dong = Restaurant("山东餐厅", "鲁菜")
    shan_dong.describe_restaurant()


if __name__ == "__main__":
    """判断"""
    main()
