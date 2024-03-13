r_type={"add":"000","sub":"000","sll":"001","slt":"010","sltu":"011","xor":"100","srl":"101","or":"110","and":"111"}
i_type=["lw","addi","sltiu","jalr"]
s_type=["sw"]
b_type={"beq":"000","bne":"001","blt":"100","bge":"101","bltu":"110","bgeu":"111"}
j_type=["jal"]
u_type=["lui","auipc"]

registers= dictionary={"zero":"00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100","t0":"00101","t1":"00110","t2":"00111","fp":"01000","s0":"01000","s1":"01001","a0":"01010","a1":"01011","a2":"01100","a3":"01101","a4":"01110","a5":"01111","a6":"10000","a7":"10001","s2":"10010","s3":"10011","s4":"10100","s5":"10101","s6":"10110","s7":"10111","s8":"11000","s9":"11001","s10":"11010","s11":"11011","t3":"11100","t4":"11101","t5":"11110","t6":"11111"}

import sys

input_=sys.argv[1]
output_=sys.argv[2]
f=open(input_, "r")
a=f.readlines()
f1=open(output_, "w")
l_labels={}
halt=False

def isnum(string1):
    try:
        n=int(string1)
        return True
    except:
        return False

for i in range(len(a)):
    if a[i].split()[0][-1]==":":
        l_labels[a[i].split()[0][:-1]]=i
try:
    for i in range(len(a)):
        x=a[i].split()
        string=""
        if len(x)==0:
            continue
        elif len(x)>3:
            print("Invalid Instruction-",i)
            break
        
        if x[0][-1]==":":
            x_=x
            del x[0]

        if x[0] in r_type:
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
                        print("Invalid Register Type-",i)
                else:
                    print("Invalid Register Type-",i)
            else:
                print("Invalid Register Type-",i)
        
        elif x[0] in u_type:
            string=''

            if x[0]=='lui':
                string+='0110111'
                operands=x[1].split(',')
                if operands[0] in registers:
                    string=registers[operands[0]]+string
                    if int(operands[1])>0:
                        two=bin(int(operands[1]))[2:]
                        if len(two)<32:
                            stringtest='0'*(32-len(two))+str(two)
                            stringtesta=stringtest[:20]
                            string=stringtesta+string
                        else:
                            string=str(two)[:20]+string
                    else:
                        two=bin(int(operands[1]))[3:]
                        if len(two)<32:
                            stringtest='1'*(32-len(two))+str(two)
                            stringtesta=stringtest[:20]
                            string=stringtesta+string
                        else:
                            string=str(two)[:20]+string
                else:
                    print('Invalid Register Type-',i)
                    break

            elif x[0]=='auipc':           
                string+='0010111'
                operands=x[1].split(',')
                if operands[0] in registers:
                    string=registers[operands[0]]+string
                    if int(operands[1])>0:
                        two=bin(int(operands[1]))[2:]
                        if len(two)<32:
                            stringtest='0'*(32-len(two))+str(two)
                            stringtesta=stringtest[:20]
                            string=stringtesta+string
                        else:
                            string=str(two)[:20]+string
                    else:
                        two=bin(int(operands[1]))[3:]
                        if len(two)<32:
                            stringtest='1'*(32-len(two))+str(two)
                            stringtesta=stringtest[:20]
                            string=stringtesta+string
                        else:
                            string=str(two)[:20]+string
                else:
                    print('Invalid Register Type-',i)
                    break

        elif  x[0] in i_type:

            if x[0] == "lw":
                string+="0000011"
                operands=x[1].split(",")
                if operands[0] in registers and operands[1].split("(")[1][:-1] in registers:
                    string = "010" + registers[operands[0]] + string
                    operands=operands[1].split("(")
                    imme=str(bin(int(operands[0])))
                    imme_=""
                    if imme[0]=="-":
                        imme="0"+imme[3:]
                        
                        for j in imme:
                            if j=="0":
                                imme_+="1"
                            else:
                                imme_+="0"
                        imme=imme_;imme_='';c=1
                        for k in range(len(imme)-1,-1,-1):
                            if (int(imme[k])+c) ==2:
                                imme_='0'+imme_
                                c=1
                            elif (int(imme[k])+c) ==1:
                                imme_ ='1'+imme_
                                c=0
                            else:
                                imme_ = '0' +imme_
                                c=0
                        
                        imme=imme_
                        ext="1"
                    elif imme[0]=="0":
                        ext="0"
                        imme=imme[2:]
                    imme = (ext*12) + imme
                    imme = imme[-12:]

                    string = imme + registers[operands[1][:-1]] + string
                else:
                    print("Invalid Register Type-",i)

            elif x[0] == "addi":
                string += "0010011"

                operands=x[1].split(",")

                if operands[0] in registers:
                    string = "000" + registers[operands[0]] +string
                    if operands[1] in registers:
                        #string = registers[operands[1]] +  string

                        imme=str(bin(int(operands[2])))
                        if imme[0]=="-":
                            imme="0"+imme[3:]
                            imme_=''
                            for j in imme:
                                if j=="0":
                                    imme_+="1"
                                else:
                                    imme_+="0"
                            imme=imme_;imme_='';c=1
                            for k in range(len(imme)-1,-1,-1):
                                if (int(imme[k])+c) ==2:
                                    imme_='0'+imme_
                                    c=1
                                elif (int(imme[k])+c) ==1:
                                    imme_ ='1'+imme_
                                    c=0
                                else:
                                    imme_ = '0' +imme_
                                    c=0
                        
                            imme=imme_
                            ext="1"
                        elif imme[0]=="0":
                            ext="0"
                            imme=imme[2:]
                        imme = (ext*12) + imme
                        imme = imme[-12:]

                        string = imme + registers[operands[1]] + string
                    else:
                        print("Invalid Register Type-",i)
                else:
                    print("Invalid Register Type-",i)
            
            elif x[0] == "sltiu":
                string += "0010011"

                operands=x[1].split(",")

                if operands[0] in registers:
                    string = "011" + registers[operands[0]] + string
                    if operands[1] in registers:
                        #string = registers[operands[1]] + string

                        imme=str(bin(int(operands[2])))
                        if imme[0]=="-":
                            imme="0"+imme[3:]
                            imme_=''
                            for j in imme:
                                if j=="0":
                                    imme_+="1"
                                else:
                                    imme_+="0"
                            imme=imme_;imme_='';c=1
                            for k in range(len(imme)-1,-1,-1):
                                if (int(imme[k])+c) ==2:
                                    imme_='0'+imme_
                                    c=1
                                elif (int(imme[k])+c) ==1:
                                    imme_ ='1'+imme_
                                    c=0
                                else:
                                    imme_ = '0' +imme_
                                    c=0
                            
                            imme=imme_
                            ext="1"
                        elif imme[0]=="0":
                            ext="0"
                            imme=imme[2:]
                        imme = (ext*12) + imme
                        imme = imme[-12:]
                        

                        string = imme + registers[operands[1]] + string
                    else:
                        print("Invalid Register Type-",i)
                else:
                    print("Invalid Register Type-",i)
            
            elif x[0] == "jalr":
                string += "1100111"

                operands=x[1].split(",")

                if operands[0] in registers:
                    string = "000" + registers[operands[0]] + string
                    if operands[1] in registers:
                        #string = registers[operands[1]] + string

                        imme=str(bin(int(operands[2])))
                        if imme[0]=="-":
                            imme="0"+imme[3:]
                            imme_=''
                            for j in imme:
                                if j=="0":
                                    imme_+="1"
                                else:
                                    imme_+="0"
                            imme=imme_;imme_='';c=1
                            for k in range(len(imme)-1,-1,-1):
                                if (int(imme[k])+c) ==2:
                                    imme_='0'+imme_
                                    c=1
                                elif (int(imme[k])+c) ==1:
                                    imme_ ='1'+imme_
                                    c=0
                                else:
                                    imme_ = '0' +imme_
                                    c=0
                        
                            imme=imme_
                            ext="1"
                        elif imme[0]=="0":
                            ext="0"
                            imme=imme[2:]
                        imme = (ext*12) + imme
                        imme = imme[-12:]

                        string = imme + registers[operands[1]] + string
                    else:
                        print("Invalid Register Type-",i)
                else:
                    print("Invalid Register Type-",i)
                    
                    
        elif x[0] in s_type:
            string='0100011'
            operands=x[1].split(',')
            if operands[0] in registers:
                if operands[1].split("(")[1][:-1] in registers:
                    imme=str(bin(int(operands[1].split("(")[0])))
                    
                    if imme[0]=="-":
                        imme="0"+imme[3:]
                        imme_=''
                        for j in imme:
                            if j=="0":
                                imme_+="1"
                            else:
                                imme_+="0"
                        imme=imme_;imme_='';c=1
                        for k in range(len(imme)-1,-1,-1):
                            if (int(imme[k])+c) ==2:
                                imme_='0'+imme_
                                c=1
                            elif (int(imme[k])+c) ==1:
                                imme_ ='1'+imme_
                                c=0
                            else:
                                imme_ = '0' +imme_
                                c=0
                    
                        imme=imme_
                        ext="1"
                    elif imme[0]=="0":
                        ext="0"
                        imme=imme[2:]
                    imme = (ext*12) + imme +"0"
                    imme = imme[-13:-1]
                    
                    string= imme[:-5] + registers[operands[0]] + registers[operands[1].split("(")[1][:-1]] + "010" + imme[-5:]+ string
                    
                else:
                    print("Invalid Register Type-",i)
            else:
                print("Invlaid Register Type-",i)
                
        
        
        elif x[0] in j_type and isnum(x[1].split(",")[1]):
            string='1101111'
            operands=x[1].split(',')
            if operands[0] in registers:
                string=registers[operands[0]]+string
            else:
                print("Invalid Register Type-",i)
                break

            diff= int(operands[1])
            imme=str(bin(diff))
            
            if imme[0]=="-":
                imme="0"+imme[3:]
                imme_=''
                for j in imme:
                    if j=="0":
                        imme_+="1"
                    else:
                        imme_+="0"
                imme=imme_;imme_='';c=1
                for k in range(len(imme)-1,-1,-1):
                    if (int(imme[k])+c) ==2:
                        imme_='0'+imme_
                        c=1
                    elif (int(imme[k])+c) ==1:
                        imme_ ='1'+imme_
                        c=0
                    else:
                        imme_ = '0' +imme_
                        c=0
            
                imme=imme_
                ext="1"
            elif imme[0]=="0":
                ext="0"
                imme=imme[2:]
            imme = (ext*20) + imme +"0"
            imme = imme[-21:-1]
            
            
            string=imme[0]+imme[10:]+imme[9]+imme[1:9]+string
            
        
        elif x[0] in j_type:
            string='1101111'
            operands=x[1].split(',')
            if operands[0] in registers:
                string=registers[operands[0]]+string
            else:
                print("Invalid Register Type-",i)
                break
            label=operands[1]

            if label in l_labels:
                diff= l_labels[label] -i
                imme=str(bin(diff))
                
                if imme[0]=="-":
                    imme="0"+imme[3:]
                    imme_=''
                    for j in imme:
                        if j=="0":
                            imme_+="1"
                        else:
                            imme_+="0"
                    imme=imme_;imme_='';c=1
                    for k in range(len(imme)-1,-1,-1):
                        if (int(imme[k])+c) ==2:
                            imme_='0'+imme_
                            c=1
                        elif (int(imme[k])+c) ==1:
                            imme_ ='1'+imme_
                            c=0
                        else:
                            imme_ = '0' +imme_
                            c=0
                
                    imme=imme_
                    ext="1"
                elif imme[0]=="0":
                    ext="0"
                    imme=imme[2:]
                imme = (ext*20) + imme +"0"
                imme = imme[-20:]
                
                
                string=imme[0]+imme[10:]+imme[9]+imme[1:9]+string
                
            else:
                print("Invalid Label Name-",i)
                break
            
        
        #Virtual Halt
        elif x == ["beq","zero,zero,0"]:
            string="00000000000000000000000001100011"
            f1.write(string)
            halt=1
            break
        
        
        #B_type instructions with immediate values
        elif (x[0] in b_type) and isnum(x[1].split(",")[2]):
            string+="1100011"
            operands=x[1].split(",")
            imme=str(bin(int(operands[2])))
            if imme[0]=="-":
                imme="0"+imme[3:]
                imme_=''
                for j in imme:
                    if j=="0":
                        imme_+="1"
                    else:
                        imme_+="0"
                imme=imme_;imme_='';c=1
                for k in range(len(imme)-1,-1,-1):
                    if (int(imme[k])+c) ==2:
                        imme_='0'+imme_
                        c=1
                    elif (int(imme[k])+c) ==1:
                        imme_ ='1'+imme_
                        c=0
                    else:
                        imme_ = '0' +imme_
                        c=0
            
                imme=imme_
                ext="1"
            elif imme[0]=="0":
                ext="0"
                imme=imme[2:]
            imme = (ext*12) + imme
            imme = imme[-13:-1]
            
            string= b_type[x[0]]+ imme[8:] + imme[1]+ string
            if operands[0] in registers:
                string = registers[operands[0]] + string
                if operands[1] in registers:
                    string = imme[0]+ imme[2:8]+ registers[operands[1]] + string
                else:
                    print('Invalid Register Type-',i)
                    break
            else:
                print('Invalid Register Type-',i)
                break
            
            
        #B_type instructions with labels
        elif x[0] in b_type:
            string+='1100011'
            operands=x[1].split(",")
            label= x[1].split(",")[2]
            if label in l_labels:
                
                diff= l_labels[label] -i
                imme=str(bin(diff))
                
                if imme[0]=="-":
                    imme="0"+imme[3:]
                    imme_=''
                    for j in imme:
                        if j=="0":
                            imme_+="1"
                        else:
                            imme_+="0"
                    imme=imme_;imme_='';c=1
                    for k in range(len(imme)-1,-1,-1):
                        if (int(imme[k])+c) ==2:
                            imme_='0'+imme_
                            c=1
                        elif (int(imme[k])+c) ==1:
                            imme_ ='1'+imme_
                            c=0
                        else:
                            imme_ = '0' +imme_
                            c=0
                
                    imme=imme_
                    ext="1"
                elif imme[0]=="0":
                    ext="0"
                    imme=imme[2:]
                imme = (ext*12) + imme +"0"
                imme = imme[-12:]
                
                string= b_type[x[0]]+ imme[8:]+ imme[1] + string
                if operands[0] in registers:
                    string = registers[operands[0]] + string
                    if operands[1] in registers:
                        string = imme[0]+ imme[2:8]+ registers[operands[1]] + string
                    else:
                        print('Invalid Register Type-',i)
                        break
                else:
                    print('Invalid Register Type-',i)
                    break
            else:
                print("Invalid Label Name-",i)
                break
        
        
        
        #commiting to output file
        if a[i]!=a[-1]:
            f1.write(string+"\n")
        else:
            print("No Virtual Halt Included")
            f1.write(string)
except:
    print("Error")
#if halt!=1:
#    print("No Virtual Halt Included")
f1.close()
