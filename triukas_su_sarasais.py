# class Workers:
#     def __init__(self, name, surname, wage):
#         self.name = name
#         self.surname = surname
#         self.__wage = wage

# antanas = Worker ("Antanas", "Antaniukas", 650)
# print(antanas._wage)

# antanas.__wage = -150

# print(antanas.__wage)

# neleidziam keisti ish isores

class Workers:
    def __init__(self, name, surname, wage):
        self.name = name
        self.surname = surname
        self.__wage = wage

    def calc_avegare(self):
        return self.__wage // 10


    @property
    def wage_after(self) -> int:
        return self.__wage

    def set_wage(self, new_wage: int) -> int:
        self.__wage = new

    @property
    def wage_before(self) -> int:
        return self.__wage

    @wage_after.setter
    def wage_after(self, new : int) -> int:
        self.__wage = new
        



antanas = Workers ('Antanas', 'Antaniukas', 650)
# print(antanas.wage_after)

# antanas.wage_after = -150

# print(antanas.wage_after)

class Company:
    def __init__(self):
        self.worker = Workers('Antanas', 'Antaniukas', 650)

def get_company_financials(self):
    return self.worker.wage_after
