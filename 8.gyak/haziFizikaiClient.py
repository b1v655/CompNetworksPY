import sys


def DiffManchester(code):
    output=""
    last={}
    last[1]="(10),"
    for bit in code:
        if bit=='1':
            if last[1]=="(01),":
                last[1]="(10),"
            elif last[1]=="(10),":
                last[1]="(01),"
            output+=last[1]
        if bit=='0':
            output+=last[1]         
    print "Output: ",output

def Manchester(code):
    output=""
    for bit in code:
        if bit=='1':
            output+="(10),"
        if bit=='0':
            output+="(01),"
    print "Output: ",output
    
def NRZL(code):
    output=[]
    for bit in code:
        if bit=='1':
            output+="(11),"
        if bit=='0':
            output+="(00),"
    print "Output: ",output

def RZ(code):
    output="" 
    for bit in code:
        if bit=='1':
            output+="(10),"
        if bit=='0':
            output+="(00),"
    print "Output: ",output
    
print "Coding: "+sys.argv[1]
print "Input: "+sys.argv[2]

if sys.argv[1] == "DiffManchester":
    DiffManchester(sys.argv[2])

if sys.argv[1] == "Manchester":
    Manchester(sys.argv[2])
    
if sys.argv[1] == "NRZ-L":
    NRZL(sys.argv[2])
    
if sys.argv[1] == "RZ":
    RZ(sys.argv[2])
