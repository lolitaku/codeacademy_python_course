# Parašyti klasę "Namas", kuri turėtų savybę 
# "plotas" ir "verte". Padaryti taip, kad savybė
#  "verte" koreguojama tik įvedus skaičių. 
#  Programoje naudoti dekoratorių @property.

class Home:
    def __init__(self, area: str, value: int):
        self.area = area
        self.__value = value
    
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, new: int) -> int:
        if new < 0:
            print("Value could not be lower than 1")
        else:
            self.__value = new

new_home = Home('Big', 180000)

print(new_home.value)

new_home.value = 200000

print(new_home.value)
