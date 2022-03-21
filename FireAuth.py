import hashgen
import otpGen
import mail_demo
# print(hashgen.hash_gen("hello")) # just for the test of successful import


def authnt(auth):
    while True:
        c=int(input("1:Sign-IN \n2:Sign-UP\nChoose your option\n"))
        if c == 1:
            mil = input("Enter your mail id::")
            pas = input("Enter you passwor::")
            hsh = hashgen.hash_gen(pas) 
            # hsh = pas

            try:
                auth.sign_in_with_email_and_password(mil,hsh) #pyrebase code
                print("login success ! ")
                break
            except:
                print("\nEmail-ID or password not correct")


        elif c == 2:
            #sign-UP
            nm=input("Enter your name :: ")
            newmil = input("Enter your mail ID :: ")
            newpas = input("Enter your new password :: ")
            cnfnewpas = input("Confirm your Password :: ")

            if newpas == cnfnewpas:
                print("verifying your mail !")
                otp = otpGen.codeGen()
                mail_demo.mailingOTP(newmil,otp)
                # print("otp::  ",otp)
                while True:
                    while True:
                        try:
                            votp=int(input("Enter the recived OTP :: "))
                            break
                        except:
                            print("Please enter the OTP in integer format")
                        
                    if otp == votp:
                        print("OTP verified! \nCreating your account")
                        newhsh = hashgen.hash_gen(newpas)
                        try:
                            auth.create_user_with_email_and_password(newmil,newhsh) #pyrebase code
                            print("Account Created and is active to use")
                            mail_demo.mailingVerified(newmil,nm)
                        except:
                            print("Mail ID already exist")

                        break
                    else:
                        print("Please Enter the correct OTP")
            else:
                print("Confirmed password dosenot matched ! ")
                
                    
        
        else:
            print("\n\nchoose between 1 or 2")
