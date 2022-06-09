# class Car:
#     def __init__(self, year: int, model: str, fuel_type: str):
#         self.year = year
#         self.model = model
#         self.fuel_type = fuel_type

#     def driving(self):
#         print('Driving!')

#     def standing_still(self):
#         print('Standing still!')

#     def refueling(self):
#         print("Refueling!")

#     def give_info(self):
#         return f'Made year is: {self.year}, the model is: {self.model}, fuel type is: {self.fuel_type}'

# class Electric(Car):
#     def fuel_type(self):
#         print('Battery is full')

#     def refueling(self):
#         print('Battery charged')

#     def drive_autonomous(self):
#         print ('Driving autonomous')

# bmw1 = Car(2008, 'e60', 'Disiel')

# bmw2 = Electric(2000, 'Tesla', 'Electric')

# bmw1.driving()
# bmw1.standing_still()
# bmw1.refueling()
# bmw1.give_info()

# bmw2.refueling()
# bmw2.drive_autonomous()




import datetime


class Workers:
    def __init__(self, name : str, hours_salary: int, work_from: int):
        self.name = name
        self.hours_salary = hours_salary
        self.work_from = work_from


def days_worked(self):

    now = datetime.datetime.now()
    print(now)

first_day = input("Enter date: ")
date = datetime.datetime.strptime(first_day, "%Y-%m-%d")
days_worked = (datetime.datetime.now() - date)
print(days_worked)

def salary_days(self) ->int:
    date = self.worked_days()
    salary = int(data.days) * self.hourly_salary * 8
    return salary



worker1 = Workers('Jogis', 10, {days_worked})  
worker2 = Workers('')


