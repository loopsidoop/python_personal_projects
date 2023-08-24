import random


def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

def rand_upper_let():
    return chr(random.randint(65,90))
def rand_lower_let():
    return chr(random.randint(97,122))
def rand_dig():
    return chr(random.randint(48,57))
def rand_punc():
    return chr(random.randint(32,47))

def password_gen(length):
    password = ""
    while len(password) < length:
        options = (rand_upper_let(), rand_lower_let(), rand_dig(), rand_punc())
        password += random.choice(options)
    return password

while True:
    try:
        userPass = int(input("How long is the password? "))
    except ValueError:
        print("\t---Please type a number---")
    else:
        break
print(f"Your password is: \n\t{password_gen(userPass)}")