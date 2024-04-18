def bin_to_decimal(bin_str):
    is_negative = bin_str[0] == "1"
    decimal_value = int(bin_str, 2)
    if is_negative:
        decimal_value = decimal_value - 2 ** 32
    return decimal_value
    
def dec_to_twos_comp(decimal, bits):
    if decimal >= 0:
        return format(decimal, f'0{bits}b')
    else:
        return format(2**bits + decimal, f'0{bits}b')    
        
def unsigned_binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal



        

def sext(i,n):
    
    dec=i
    if dec[0]=='0':
        val= "0"*n +i
        return val[-n:]
    else:
        val="1"*n +i
        return val[-n:]
    
def hext(i):
    dec=hex(i)
    b="0"*8 + dec[2:]
    return "0x"+b[-8::]

def bin2int(b):
    if int(b)==0:
        return 0
    int1=0
    for i in range(-1,-len(b),-1):
        if b[i]=="1":
            int1+= 2**(((-1)*i)-1)
    if b[0]=='1':
        int1-= 2**(len(b)-1)
    return int1

def bin_to_decimal(bin_str):
    is_negative = bin_str[0] == '1'
    decimal_value = int(bin_str, 2)
    if is_negative:
        decimal_value = decimal_value - 2 ** 12
    return decimal_value

def shift(i,n,d):
    leng=len(i)
    if d=="r":
        a="0"*n + i
        a=a[:leng]
    elif d=="l":
        a=i + "0"*n
        a=a[(-1)*leng::]
    return a

registers= {"00000":"0","00001":"0","00010":"100000000","00011":"0","00100":"0","00101":"0","00110":"0","00111":"0",
            "01000":"0","01001":"0","01010":"0","01011":"0","01100":"0","01101":"0","01110":"0","01111":"0",
            "10000":"0","10001":"0","10010":"0","10011":"0","10100":"0","10101":"0","10110":"0","10111":"0",
            "11000":"0","11001":"0","11010":"0","11011":"0","11100":"0","11101":"0","11110":"0","11111":"0"}

data_mem={"0x00010000":"0b00000000000000000000000000000000",
          "0x00010004":"0b00000000000000000000000000000000",
          "0x00010008":"0b00000000000000000000000000000000",
          "0x0001000c":"0b00000000000000000000000000000000",
"0x00010010":"0b00000000000000000000000000000000",
"0x00010014":"0b00000000000000000000000000000000",
"0x00010018":"0b00000000000000000000000000000000",
"0x0001001c":"0b00000000000000000000000000000000",
"0x00010020":"0b00000000000000000000000000000000",
"0x00010024":"0b00000000000000000000000000000000",
"0x00010028":"0b00000000000000000000000000000000",
"0x0001002c":"0b00000000000000000000000000000000",
"0x00010030":"0b00000000000000000000000000000000",
"0x00010034":"0b00000000000000000000000000000000",
"0x00010038":"0b00000000000000000000000000000000",
"0x0001003c":"0b00000000000000000000000000000000",
"0x00010040":"0b00000000000000000000000000000000",
"0x00010044":"0b00000000000000000000000000000000",
"0x00010048":"0b00000000000000000000000000000000",
"0x0001004c":"0b00000000000000000000000000000000",
"0x00010050":"0b00000000000000000000000000000000",
"0x00010054":"0b00000000000000000000000000000000",
"0x00010058":"0b00000000000000000000000000000000",
"0x0001005c":"0b00000000000000000000000000000000",
"0x00010060":"0b00000000000000000000000000000000",
"0x00010064":"0b00000000000000000000000000000000",
"0x00010068":"0b00000000000000000000000000000000",
"0x0001006c":"0b00000000000000000000000000000000",
"0x00010070":"0b00000000000000000000000000000000",
"0x00010074":"0b00000000000000000000000000000000",
"0x00010078":"0b00000000000000000000000000000000",
"0x0001007c":"0b00000000000000000000000000000000"}


f=open("s_test1.txt", "r")
a=f.readlines()
a1=open("bin.txt", "w")

PC=0
jump=False
while PC < len(a):
    
    a[PC]=a[PC].split()[0]
    opcode= a[PC][-7:]
    
    
    ##btype
    if opcode=="1100011":
        func3= a[PC][-15:-12]
        rs1=registers[a[PC][-20:-15]]
        rs2=registers[a[PC][-25:-20]]
        imm1=a[PC][-12:-7]
        imm2=a[PC][-32:-25]
        imm=imm2[0]+imm1[-1]+imm2[1:]+imm1[:-1]
        n=len(rs1)
        if len(rs1)<len(rs2):
            n=len(rs2)
        
        if int(rs1,2)==int(rs2,2)==int(imm,2)==0:
            jump=True
            break
        ###
        if func3=="000":
            if bin2int(sext(rs1,n))==bin2int(sext(rs2,n)):
                PC+=bin2int(imm+"0")
            
        if func3=="001":
            if bin2int(sext(rs1,n))!=bin2int(sext(rs2,n)):
                PC+=bin2int(imm+"0")
        
        if func3=="101":
            if bin2int(sext(rs1,n))>=bin2int(sext(rs2,n)):
                PC+=bin2int(imm+"0")
        
        if func3=="111":
            if int(rs1,2)>int(rs2,2):
                PC+=int(imm+"0",2)
                
        if func3=="100":
            if bin2int(sext(rs1,n))<=bin2int(sext(rs2,n)):
                PC+=bin2int(imm+"0")
        
        if func3=="110":
            if int(rs1,2)<int(rs2,2):
                PC+=int(imm+"0",2)
                
    ##jtype
    if opcode=="1101111":
        
        rd = a[PC][-12:-7]
        imm= a[PC][0]+a[PC][10:20]+a[PC][9]+a[PC][1:9]
        
        registers[rd]= sext("0"+bin(PC+4)[2:],32)
        PC+=bin2int(sext(imm+"0"))
    
    
    ##stype
    if opcode=="0100011":
        
        inst=a[PC]
        imm=inst[0:7]+inst[-12:-7]
        rs2=inst[7:12]
        rs1=registers[inst[-20:-15]]
        address = bin2int(rs1)+bin2int(imm)
        
        hex_address = hext(address)
        data_mem[hex_address] = "0b"+sext(rs2,32)
        
    ##rtype
    if opcode=="0110011":
        
        funct3= a[PC][-15:-12]
        funct7=a[PC][:7]
        rs1=registers[a[PC][7:12]]
        rs2=registers[a[PC][12:17]]
        dest=a[PC][-12:-7]
        result=False
        
        if funct3 == "000" and funct7 == "0000000":# ADD
            result = bin(bin2int(rs1) + bin2int(rs2))[2:]
        elif funct3 == "000" and funct7 == "0100000":  # SUB
            result = bin(bin2int(rs1) - bin2int(rs2))
        elif funct3 == "001": # SLL
            no=int(rs2[-5::],2)
            result=shift(rs1,no,"l")
        elif funct3 == "010":  # SLT
            if bin2int(rs1)<bin2int(rs2):
                result= "1"
        elif funct3 == "011":  # SLTU
            if int(rs1)<int(rs2):
                result= "1"
                
        elif funct3 == "100":  # XOR
            l=len(rs1)
            result=""
            if len(rs2)>l:
                l=len(rs2)
            rs1=sext(rs1,l)
            rs2=sext(rs2,l)
            for i in range(l):
                if rs1[i]==rs2[i]:
                    result+="0"
                else:
                    result+="1"
            
        elif funct3 == "101":  # SRL
            no=int(rs2[-5::],2)
            result=shift(rs1,no,"r")
            
        elif funct3 == "110": # OR
            l=len(rs1)
            result=""
            if len(rs2)>l:
                l=len(rs2)
            rs1=sext(rs1,l)
            rs2=sext(rs2,l)
            for i in range(l):
                if rs1[i]==rs2[i]=="0":
                    result+="0"
                else:
                    result+="1"
                    
        elif funct3 == "111":  # AND
            l=len(rs1)
            result=""
            if len(rs2)>l:
                l=len(rs2)
            rs1=sext(rs1,l)
            rs2=sext(rs2,l)
            for i in range(l):
                if rs1[i]==rs2[i]=="1":
                    result+="1"
                else:
                    result+="0"
                    
        if result!=False:
            registers[dest]=result
        else:
            print("Invalid Input")
    ##utype
    if opcode=="0110111":
        
        r=a[PC][:20]+"0"*12
        des=a[PC][30:-7]
        registers[des]=bin(PC+ bin2int(r))[2:]
        
    if opcode=="0010111":
        
        binary_inst=a[PC]
        
        r=a[PC][:20]+"0"*12
        des=a[PC][30:-7]
        registers[des]=r
        
    
    ##itype
    
    if opcode=="0010011":
        
        rd=a[PC][-12:-7]
        func3=a[PC][-15:-12]
        rs1=a[PC][-20:-15]
        imm=a[PC][:-20]
        
        
        if func3=="000":
            
            dec=bin2int(registers[rs1])+bin2int(imm)
            registers[rd]=dec_to_twos_comp(dec,32)
            
        elif func3=="011":
            if int(imm,2)>int(registers[rs1],2):
                registers[rd]="1"
                
    if opcode=="0000011":
        if func3 == "010":
            offset = bin2int(imm)
            dec_rs = bin2int(rs1)
            address = dec_rs + offset
            hex_address = hext(address)
            registers[rd]=data_mem[hex_address]
    
    if opcode=="1100111":
        registers[rd]= sext("0"+bin(PC+4)[2:],32)
        PC=int(registers[rs1],2)+bin2int(sext(imm+"0"))
        
        
    ##writing registers:
    if jump==True:
        break
    
    a1.write("0b"+sext("0"+bin(PC+1)[2:]+'00',32))
    for i in registers:
        print(i,":",registers[i],",",end='')
        a1.write(" "+"0b"+sext("0"+registers[i],32))
    print()
    a1.write("\n")
    PC+=1
if jump==True:
    a1.write("0b"+sext("0"+bin(PC+1)[2:]+"00",32))
    for i in registers:
        a1.write(" "+"0b"+sext("0"+registers[i],32))
    a1.write("\n")
for i in data_mem:
    a1.write(i+":"+data_mem[i]+"\n")
a1.close()
