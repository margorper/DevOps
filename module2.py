import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))

random = input("New Password? Type Y for new password...")
if random == "y":
    print(password)
elif random != "y":
    print('No Password for You!')


weight = input("How many pounds do you weight?")
kilos = float(weight) / 2.2
print("You weigh " + str(kilos) + " kilos!")
