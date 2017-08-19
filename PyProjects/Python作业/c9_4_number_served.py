class Restaurant:
    """"一个有关餐馆的类定义"""
    def __init__(self, restaurant_name, cuisine_type):
        """"构造函数，给属性赋值"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 5

    def describe_restaurant(self):
        """方法：餐馆的描述"""
        print("餐馆名字是：" + self.restaurant_name)
        print("菜肴风格是" + self.cuisine_type)

    @staticmethod
    def open_restaurant():
        """方法：餐馆正在营业"""
        print("餐馆正在营业")

    def read_number_served(self):
        """显示所有就餐的人数"""
        print("就餐人数：" + str(self.number_served))

    def set_number_served(self, number):
        """更改就餐人数"""
        self.number_served = number

    def increment_number_served(self, increment):
        """就餐人数递增"""
        self.number_served += increment


def main():
    """主要的调用函数"""
    restaurant = Restaurant("四川餐厅", "川菜")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    restaurant.read_number_served()
    print("将就餐人数改为12人")
    restaurant.set_number_served(12)
    restaurant.read_number_served()
    print("就餐人数递增5人")
    restaurant.increment_number_served(5)
    restaurant.read_number_served()


if __name__ == "__main__":
    main()
