# from posixpath import supports_unicode_filenames
# from unicodedata import name


# # my_list = [4, 3, 2, 1]
# # my_list2 = []

# # for number in my_list:
# #     my_list2.append(number**2)

# # print(my_list2)

# # def square(x):
# #     return x**2

# # my_list3 = map(lambda x: x**2, my_list)

# # print(my_list3)
# # print(list(my_list3))

# # date = "2000-03-25"
# # print(date.split)("-")
# # y = date.split("-")[0]
# # m = date.split("-")[1]
# # d = date.split("-")[2]
# # y, m, d  = date.split("-")[0], date.split("-")[1], date.split("-")[2]
# # # standartinis budas


# # y, m, d = map(int, date.split("-")) 
# # # trumpesni budas su map
# # print(y, m, d)



# # my_string = "labasirvakaras123ir852"

# # my_list = []

# # for char in my_string.split("ir"):
# #     my_list.append(char)
# # print(my_list)


# # number = "4, 3, 2, 1"
# # p, a, t, k = map(float, numbers.split(","))
# # print(p, a, t, k)




# # # class Person():
# #     def__init__(self, name, surname):
# #     self.name = name
# #     self.surname = supports_unicode_filenames

# # def__repr__(self):
# #     return f"{self.name}, {self.surname}"

# # p1 = Person("asdf". "asdr")



# def more_than_two(some_list: list) -> list:
#     second_list = []
#     for number in some_list:
#         if number > 2 :
#             second_list.append(number)
#     return second_list

# print(more_than_two(my_list))

# def more_than_teo (x):
#     return x > 2

# new_list = filter(more_than_two, my_list)
# print(list(new_list))

# my_list = []

from functools import reduce

my_list = [2, 1, 3, 4]
new_list = reduce(lambda x, y: x * y, my_list)
sudaugina nuo pradziu 2*1*3*4

print(new_list)