
from random import choice
from random import sample
from name import f_name, l_name
from email import email_domain, email_words, email_number
from creditcard import year, day, number
from address import country, postal_codes_address, street

print("""
         ____________________________________________________________________________________________________________
        |                                                                                                            |
        |   #           #       # # # #       #######            ###         ##      #      # # #    #       #       |      
        |   #           #       #       #     #      #          #   #        # #     #    #      #   #     #         |  
        |   #           #       #       #     #       #        #     #       #  #    #    #          #   #           |
        |   #           #       # # # #       #       #       # # # # #      #   #   #      #        # #             |
        |   #           #       #  #          #       #      #         #     #    #  #        #      #   #           |
        |   #           #       #   #         #      #      #           #    #     # #    #      #   #     #         |
        |    # # # # # #        #     #       #######      #             #   #      ##      # # #    #       #       |
        |____________________________________________________________________________________________________________|





            






""")

#code for main.py after the upper lists have been imported

def welcome_message():              #welcome message is in this function
    return "This is a generator used to generate fake e-mails, names, adresses, credit card numbers etc. You name it! Enjoy!"

print(welcome_message())

#_______________________________________________________________

def credit_card():
    #  expiration date
    date1 = choice(day)
    year1 = choice(year)
    expiration_date = str(date1) + "/" + str(year1)

    #CSV code
    CSV = sample(email_number,3)
    CSV2 = "".join([str(i) for i in CSV])

    #name 
    name1 = choice(f_name)
    name2 = choice(l_name)
    name3 = name1 + " " + name2
    
    # 16 digit number with spaces in between
    number1 = sample(number,2)
    number2 = sample(number,2)
    number3 = sample(number,2)
    number4 = sample(number,2)
    number5 = ''.join([str(i) for i in number1])
    number6 = "".join([str(i) for i in number2])
    number7 = "".join([str(i) for i in number3])
    number8 = "".join([str(i) for i in number4])

    number9 = number5 + " " + number6  + " " + number7 + " " + number8

    output  =  "\n\n\nName : "+ name3 +"\n"  +"Account Nummber : " + number9+"\n" + "CSV : "+ CSV2 +"\n" + "Expiration Date :  "+ expiration_date+ "\n"
    return output

    #___________________________________________________________________-


def email():
    # special char``
    # punc = input("do you want a special character in your email address?(y/n) :")
    # number98 = eval(input("do you want a number in your email address?(y/n) :"))
    name24 = choice(f_name)
    name00 = choice(l_name)
    flag = True 
    while flag:
        for c in email_domain:
            print(c, end ="\n")
        input3 = input("\n\n\nFrom the list of the domains shown above, which do you you want? :")
        if input3 not in email_domain:
            print("\n\n\n you have printed an incorrect option, please try again")
        else:
            print("Okay, let's go forward with our procedure")
            flag = False
            
    e_mail = "\n\n\nHere is your fake e-mail : "+ name24 + name00  +"@"+ input3
    return e_mail
    

    #_____________________________________________________

def name():
    name4123 = choice(f_name)
    name532 = choice(l_name)
    name6123 ="\n\n\nyour fake name is : "+ name4123+" "+name532
    return name6123

#________________________________________________________

def address():
    #name
    name13 = choice(f_name)
    name23 = choice(l_name)
    name33 = name13 + " " + name23
    #A NUMBER AND A SREET NAME
    number123 = choice(email_number)
    street1 = choice(street)
    finale = str(number123) +" "+ street1.strip()

    #COUNTRY
    country1 =  choice(country).strip()
    final_address = "\n\n\nyour final fake address is as shown: \n\n"+ name33 + "\n\n" + finale + "\n\n" + country1
    
    return final_address

    #___________________________________________________________________________________
    
input1_list  = ["creditcard","email","name","address"]
 
#input for what kind of fake information does the user want to input
def run_again():
    input1 = input('\n\n\nwhat kind of information do you want to generate ?(creditcard/email/name/address) :')
    if input1.lower()=="creditcard":
        print(credit_card())

    elif input1.lower()=="email":
        print(email())

    elif input1.lower()=="name":
        print(name())

    elif input1.lower()=="address":
        print(address())
    elif input.lower() not in input1_list:
        print("you have entered an incorrect option")
    
    pass
print(run_again())
flag1 = True
while flag1:
    again = input("\n\n\nif you want to run this program again please type (Y/N) : ")
    if again.upper()=="Y":
        print(run_again())
    if again.upper()=="N":   
        print("\n\n\nGoodbye!")
        flag1 = False
    #else:
    #     print("\n\n\nyou have entered an incorrect option  ")
        
    
            

        