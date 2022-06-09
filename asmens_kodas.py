uzduoti perdaryti su klasemis, dat eteme
      personal_code=input("iveskite koda")
true_or_false=(personal_code.isdigit())
list_of_personal_code=list(personal_code)
o=len(personal_code)
if o == 11 and personal_code.isdigit():
    a=int(list_of_personal_code[0])
    b=int(list_of_personal_code[1])
    c=int(list_of_personal_code[2])
    d=int(list_of_personal_code[3])
    e=int(list_of_personal_code[4])
    f=int(list_of_personal_code[5])
    g=int(list_of_personal_code[6])
    h=int(list_of_personal_code[7])
    j=int(list_of_personal_code[8])
    k=int(list_of_personal_code[9])
    l=int(list_of_personal_code[10])
    controlm1 = ((a * 1) + ( b * 2) + ( c * 3 )+ ( d * 4 )+ ( e * 5 ) + ( f * 6 ) + ( g * 7 )+ ( h * 8 ) + ( j * 9 ) + ( k * 1 )) % 11
    controlm2 = (( a * 3 ) + ( b * 4)  + ( c * 5) + ( d * 6) + (e * 7) + (f * 8) + (g * 9) + (h * 1) + (j * 2) + (k * 3)) % 11
    def methods():
        if controlm1 ==10:
            if controlm2 == 10:
                return 0
            else:
                return controlm2
        else:
            return controlm1
    z=(methods())
    if (a >= 3 and a <= 6 ) and (d == 0 or d == 1) and (f == 0 or f == 1) and (o == 11) and (z == l):
        print("Personal code is valid")
    else:
        print("Personal code is not valid")
else:
    print(f"This: {​personal_code}​  identification number is in wrong format")
