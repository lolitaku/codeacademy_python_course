# Leistų įvesti darbuotojus: vardą, pavardę, gimimo datą, pareigas, atlyginimą, nuo kada dirba (data būtų nustatoma automatiškai, pagal dabartinę datą).
# Duomenys būtų saugomi duomenų bazėję, panaudojant SQLAlchemy ORM (be SQL užklausų)
# # Vartotojas galėtų įrašyti, peržiūrėti, ištrinti ir atnaujinti darbuotojus.

class Paskisti:

    @staticmethod
    def do_smth() -> None:
        name = input("Please, enter your name: ")
        surname = input("Please, enter your surname: ")
        birthday = input("Please, enter your birthday: ")
        occupation = input("Please, enter your ocuupation: ")
        salary = input("Please, enter your salary: ")
        start_date = input("Please, enter start_date: ")
        print(
        f'My personal info is: {name} - {surname} - {birthday} - {occupation} - {salary} - {start_date}',
        )

if __name__== '__main__':
    Paskisti.do_smth()
