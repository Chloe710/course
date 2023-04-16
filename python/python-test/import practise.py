from car import ElectircCar
my_tesla=ElectircCar('tesla','models',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

class Res:
    def __init__(self, res_name, cuisine_type):
        self.res_name = res_name
        self.cuisine_type = cuisine_type
        # 添加number_serve属性
        # self.number_served=0

    def desc_res(self):
        print(f'The cuisine type here is {self.cuisine_type}')

    def open_res(self):
        print(f'{self.res_name} is now opening.')

    # def set_number_served(self):
    #     self.set_number_served=set_number_served=20
    #     print(f'This restaurant can serve {set_number_served} customers each day .')


class IceCreamStand:
    def __init__(self, res_name, cuisine_type, flavors):
        super().__init__(res_name, cuisine_type)
        self.flavors = flavors = []
    # def __init__ (self,flavors):
    #     self.flavors=flavors
    #     print(f'There are several flavors here,such as {self.flavors}')


icecreamstand = IceCreamStand('Tims', 'chinese', ['peach', 'chocolate', 'vanilla', 'curry', 'durian'])
print(f'There is a new icecream stand named {icecreamstand.res_name}')
print(f'The  cuisine type here  is {icecreamstand.cuisine_type}')
# icecreamstand.desc_res()
# icecreamstand.open_res()
# icecreamstand=IceCreamStand([peach,chocolate,vanilla,curry,durian])
# icecreamstand.self.flavors