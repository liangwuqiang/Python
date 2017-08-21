class Car:
    
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("该车有 " + str(self.odometer_reading) + " 里程数.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    
    def __init__(self, battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print("该车有 " + str(self.battery_size) + "-kWh 电量.")

    def get_range(self):
        if self.battery_size == 60:
            _range = 140
        elif self.battery_size == 85:
            _range = 185

        message = "该车大约能跑 " + str(_range)  # 调用局部变量的问题
        message += " 公里，在满电的情况下."
        print(message)

    def update_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


my_car = Car('大众', '帕萨特', 2015)
print(my_car.get_descriptive_name())

his_car = ElectricCar('本田', '雅阁', 2015)

print(his_car.get_descriptive_name())
his_car.battery.get_range()
his_car.battery.update_battery()
print("进行了电池升级")
his_car.battery.get_range()
