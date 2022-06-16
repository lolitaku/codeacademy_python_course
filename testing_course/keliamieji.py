def ar_keliamieji(metai):
    if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
        return("Keliamieji")
    else:
        return("Nekeliamieji")

if __name__ == "__main__":
    print(ar_keliamieji1(2000))
    print(ar_keliamieji2(2020))
    print(ar_keliamieji3(2100))

# Keliamieji
# Keliamieji
# Nekeliamieji
