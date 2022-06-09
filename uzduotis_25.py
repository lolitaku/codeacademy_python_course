# Pirma uzduotis:

# Sukurti programą, kuri:

# •Prie kiekvieno sakinio su jūsų pasirinktu tekstu, pridėtų
# šauktuką ir atspausdintų naują sakinį.
# Patarimai:
# •Naudoti map (su lambda) arba comprehension, " ".join()

my_string = "Labas vakaras. Kaip tu. Viso gero"
ab = my_string.split(". ")
print(ab)

new = map(lambda x: x + "!" , ab)
print(new)
print(list(new))


# arba be lambdos

new_string = [sentence + "!" for sentence in my_string]
print(new_string)





new_list = list(range(50))
my_list = [x * 10 for x in my_list]
print(new_list)


new_list2 = list(range(50))
my_list = [x for x in my_list if x % 7 == 0]
print(new_list2)

new_list3 = [x ** 2 for x in my_list]
print(new_list3)
print(sum(new_list3))
print(min(new_list3))
print(max(new_list3))
print(median(new_list3))
new_list3.sort(reverse=True))

print(new_list3)