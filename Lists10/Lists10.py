list=["hello2022Year","goodbye2021Year"]
C=["y","n"]
print(list)
while 1:
    try:
        A=str(input("1#Xотите узнать cостоит ли строка из цифр: Y или N:").lower())#1
        B=C.index(A)
        if B==0:
            print("1#ответ на isdigit:",list[0].isdigit())#1
        elif B==1 :
            A=str(input("2#Xотите узнать cостоитли ли строка из букв: Y или N:").lower())#2
            B=C.index(A)
            if B==0:
                print("2#ответ на isalpha:",list[0].isalpha())#2
            elif B==1 :
                A=str(input("3#Xотите узнать cостоитли ли строка из цифр или букв: Y или N:").lower())#3
                B=C.index(A)
                if B==0:
                    print("3#ответ на isalnum:",list[0].isalnum())#3
                elif B==1 :
                    A=str(input("4#Xотите узнать начинается ли строка с заглавной буквы: Y или N:").lower())#4
                    B=C.index(A)
                    if B==0:
                        print("4#ответ на istitle:",list[0].istitle())#4
                    elif B==1 :
                        A=str(input("5#Xотите преобразование строки к верхнему регистру: Y или N:").lower())#5
                        B=C.index(A)
                        if B==0:
                            print("5#ответ на istitle:",list[0].upper())#5
                        elif B==1 :
                            A=str(input("6#Xотите преобразование строки к нижнему регистру: Y или N:").lower())#6
                            B=C.index(A)
                            if B==0:
                                print("6#ответ на lower:",list[0].lower())#6
                            elif B==1 :
                                A=str(input("7#Xотите преобразование первый символ строки в верхний регистр, а все остальные в нижний: Y или N:").lower())#7
                                B=C.index(A)
                                if B==0:
                                    print("7#ответ на capitalize:",list[0].capitalize())#7
                                elif B==1 :
                                    A=str(input("8#Xотите узнать длину строки: Y или N:").lower())#8
                                    B=C.index(A)
                                    if B==0:
                                        print("8#ответ на len:",len(list))#8
                                    elif B==1 :
                                        A=str(input("9#Xотите узнать состоит ли строка из неотображаемых символов: Y или N:").lower())#9
                                        B=C.index(A)
                                        if B==0:
                                            print("9#ответ на isspace:",list[0].isspace())#9
                                        elif B==1 :
                                            A=str(input("10#Xотите развернуть список: Y или N:").lower())#10
                                            B=C.index(A)
                                            if B==0:
                                                list.reverse()
                                                print("10#ответ на reverse:",list)#10
    except: ValueError




