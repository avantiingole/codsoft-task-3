import string
import random

print("Welcome to my Password Generator")

if __name__ == "__main__":
    
    a = string.ascii_lowercase    
    b = string.ascii_uppercase   
    c = string.digits    
    d = string.punctuation
    
    while True:
        try:
            length=int(input("Please enter your password length:"))
            break
        except ValueError:
            print("Please enter valid length!")
        
        
    l=[]
    l.extend(list(a))
    l.extend(list(b))
    l.extend(list(c))
    l.extend(list(d))

    random.shuffle(l)
    print("Your generated password is: ")
    print("".join(l[0:length]))
    print("Thank you!!\n")