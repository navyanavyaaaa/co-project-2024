r_type={"add":"000","sub":"000","sll":"001","slt":"010","sltu":"011","xor":"100","srl":"101","or":"110","and":"111"}
i_type=["lw","addi","sltiu","jalr"]
s_type=["sw"]
b_type=["beq","bne","blt","bge","bltu","bgeu"]
j_type=["jal"]
u_type=["lui","auipc"]

registers= {"zero":"00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100","t0":"00101","t1":"00110","t2":"00111","fp":"01000","s0":"01000","s1":"01001","a0":"01010","a1":"01011","a2":"01100","a3":"01101","a4":"01110","a5":"01111","a6":"10000","a7":"10001","s2":"10010","s3":"10011","s4":"10100","s5":"10101","s6":"10110","s7":"10111","s8":"11000","s9":"11001","s10":"11010","s11":"11011","t3":"11100","t4":"11101","t5":"11110","t6":"11111"}

f=open("test.txt", "r")
a=f.readlines()
f1=open("bin.txt", "w")

for i in a:
    x=i.split()
    string=""
    if len(x)==0:
        pass
    elif x[0] in r_type:
        string+="0110011"
        operands=x[1].split(",")
        if operands[0] in registers:
            string = r_type[x[0]] + registers[operands[0]] + string
            if operands[1] in registers:
                string = registers[operands[1]] + string
                if operands[2] in registers:
                    string = registers[operands[2]] + string
                    if x[0] == "sub":
                        string = "0100000" + string
                    else:
                        string = "0000000" + string


                else:
                    print("Invalid Register Type.")
            else:
                print("Invalid Register Type.")
        else:
            print("Invalid Register Type.")
    
    elif x[0] in u_type:
        string=''
        if x[0]=='lui':
            string+='0110111'
            operands=x[1].split(',')
            if operands[0] in registers:
                string=registers[operands[0]]+string
                if int(operands[0])>0:
                    two=bin(int(operands[1]))[2:]
                    if len(two)<20:
                        string='0'*(20-len(two))+str(two)+string
                    else:
                        string=str(two)+string
                else:
                    two=bin(int(operands[1]))[3:]
                    if len(two)<20:
                        string='1'*(20-len(two))+str(two)+string
                    else:
                        string=str(two)+string
            else:
                print('Invalid Register Type')

        elif x[0]=='auipc':
            
            string+='0010111'
            operands=x[1].split(',')
            if operands[0] in registers:
                string=registers[operands[0]]+string
                if int(operands[0])>0:
                    two=bin(int(operands[1]))[2:]
                    if len(two)<20:
                        string='0'*(20-len(two))+str(two)+string
                    else:
                        string=str(two)+string
                else:
                    two=bin(int(operands[1]))[3:]
                    if len(two)<20:
                        string='1'*(20-len(two))+str(two)+string
                    else:
                        string=str(two)+string
            else:
                print('Invalid Register Type')
        else:
            print('Invalid Register Type')

    elif  x[0] in i_type:

        if x[0] == "lw":
            string+="0000011"
            operands=x[1].split(",")
            if operands[0] in registers and operands[1].split("(")[1][:-1] in registers:
                string = "010" + registers[operands[0]] + string
                operands=operands[1].split("(")
                imme=str(bin(operands[0]))
                if imme[0]=="-":
                    ext="1"
                    imme=imme[3:]
                elif imme[0]=="0":
                    ext="0"
                    imme=imme[2:]
                imme = (ext*12) + imme
                imme = imme[-12:]

                string = imme + registers[operands[1][:-1]] + string
            else:
                print("Invalid Register Type")

        elif x[0] == "addi":
            string += "0010011"

            operands=x[1].split(",")

            if operands[0] in registers:
                string = "000" + registers[operands[0]] +string
                if operands[1] in registers:
                    string = registers[operands[1]] +  string

                    imme=str(bin(operands[2]))
                    if imme[0]=="-":
                        ext="1"
                        imme=imme[3:]
                    elif imme[0]=="0":
                        ext="0"
                        imme=imme[2:]
                    imme = (ext*12) + imme
                    imme = imme[-12:]

                    string = imme + registers[operands[1][:-1]] + string
                else:
                    print("Invalid Register Type")
            else:
                print("Invalid Register Type")
        
        elif x[0] == "sltiu":
            string += "0010011"

            operands=x[1].split(",")

            if operands[0] in registers:
                string = "011" + registers[operands[0]] + string
                if operands[1] in registers:
                    string = registers[operands[1]] + string

                    imme=str(bin(operands[2]))
                    if imme[0]=="-":
                        ext="1"
                        imme=imme[3:]
                    elif imme[0]=="0":
                        ext="0"
                        imme=imme[2:]
                    imme = (ext*12) + imme
                    imme = imme[-12:]

                    string = imme + registers[operands[1][:-1]] + string
                else:
                    print("Invalid Register Type")
            else:
                print("Invalid Register Type")
        
        elif x[0] == "jalr":
            string += "1100111"

            operands=x[1].split(",")

            if operands[0] in registers:
                string = "000" + registers[operands[0]] + string
                if operands[1] in registers:
                    string = registers[operands[1]] + string

                    imme=str(bin(operands[2]))
                    if imme[0]=="-":
                        ext="1"
                        imme=imme[3:]
                    elif imme[0]=="0":
                        ext="0"
                        imme=imme[2:]
                    imme = (ext*12) + imme
                    imme = imme[-12:]

                    string = imme + registers[operands[1][:-1]] + string
                else:
                    print("Invalid Register Type")
            else:
                print("Invalid Register Type")
    elif x[0] in s_type:
        string='0100011'
        operands=x[1].split(',')
        operandsother=operands.split('(')
        if int(operandsother[0])>0:
            one=bin(int(operandsother[0]))[2:]
            if len(one)<12:
                one=str(one)
                one='0'* (12-len(one))+str(one)
            two=one[0:5]
            three=one[5:12]
        else:
            one=bin(int(operandsother[0]))[3:]
            if len(one)<12:
                one=str(one)
                one='1'* (12-len(one))+str(one)
            two=one[0:5]
            three=one[5:12]

        string='010'+two+string
        operandsother[1]=operandsother[1][:2]
        if operandsother[1] in registers:
            string=registers[operandsother[1]]+string
        else:
            print("Invalid Register Type")
        if operands[0] in registers:
            string=three+registers[operands[0]]+string
        else:
            print("Invalid Register Type")

    f1.write(string+"\n")
f1.close()

            

                


        
