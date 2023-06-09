symadd = {}
litadd = {}

with open("symtab.txt", "r") as sym:
    for s in sym:
        word = s.split("  ")
        symadd[int(word[0])] = word[2]
    print(symadd)

with open("littab.txt", "r") as lit:
    for s in lit:
        word = s.split("  ")
        litadd[int(word[0])] = word[2]
    print(litadd)

with open("intermediate.txt", "r") as intm, open("Pass2.txt", "w") as pass2:
    for string in intm:
        word = string.split(" ")
        if(len(word)==2):
            address = word[0]
            s = str(word[1])
            
            for_s = 0
            #(IS,01)(RG,01)(L,01)
            if s[1:6].lower() == "is,00":
                pass2.write(address+ " ")
                pass2.write("+ 00 00 000\n")


            elif s[1:3].lower() == "is":
                pass2.write(address+ " ")
                pass2.write("+ " + s[4:6] + " ")
                if s[8:10].lower() == "rg":
                    pass2.write(s[11:13] + " ")
                    for_s = 7
                    if s[8+for_s].lower() == "s":
                        pass2.write(symadd[int(s[17:19])])
                    if s[8+for_s].lower() == "l":
                        pass2.write(litadd[int(s[17:19])])
                        for_s = 0
                if s[8].lower() == "s":
                        pass2.write("00"+" ")
                        pass2.write(symadd[int(s[10:12])])
            elif s[1:6].lower() == "dl,01":
                pass2.write(address + "+ 00 00 " + s[-4:-2] + "\n")
            else:
                pass2.write(address+ " + " + " "+"\n")

"""
intermediate : 
(AD,01)(C,500)
500 (IS,09)(S,01)
501 (IS,01)(RG,01)(S,01)
502 (IS,02)(RG,02)(L,01)
503 (DS,02)(C,3)
504 (IS,01)(RG,02)(S,01)
505 (IS,04)(RG,02)(S,01)
506 (IS,02)(RG,01)(L,02)
507 (IS,01)(RG,01)(L,03)
508 (DL,02)(C,02)
509 (DL,02)(C,05)
510 (IS,01)(RG,01)(L,04)
511 (IS,10)(S,01)
512 (IS,00)
513 (DL,02)(C,02)
515 (DL,01)(C,10)
516 (DL,02)(C,06)

littab : 
1  3  503
2  2  508
3  5  509
4  6  516

symtab : 
1  A  513
2  B  515


"""
