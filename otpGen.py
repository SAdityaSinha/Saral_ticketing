import random

def codeGen():
    otp = 0
    for i in range(4):
        a = random.randint(1,9)
        otp *= 10
        otp += a
        
    return otp 

# print(codeGen())
