
class Human:
    def __init__(self,age: float, hourly_wage: float):
         self.age : float = age
         self.hourly_wave: float = hourly_wage

    def return_age(self) -> float:
        return self.age 

    def  get_monthly_salary(self) -> float:
        return self.hourly_wave * 160

my_cool_human = Human(age = 30, hourly_wage = 8.5)
print(my_cool_human.return_age())
print(my_cool_human.get_monthly_salary())


