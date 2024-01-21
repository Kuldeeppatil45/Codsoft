import string
import random

if __name__=="__main__":
    try:
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        p = int(input("Enter your password length\n"))
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        random.shuffle(s)
        print("Your password is: ")
        print("".join(s[0:p]))
    except ValueError as v:
        print("invalid input, pls enter the no of  passwaord length\n ",v)
    except Exception as e:
        print(e)