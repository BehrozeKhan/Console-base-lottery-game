import random as r
lottery_num = []
for i in range(0,3):
    num = r.randint(1,50)
    while num in lottery_num:
        num = r.randint(1,50)
    lottery_num.append(num)
lottery_num.sort()
user_num = []
for i in range(0,3):
    num = int(input("Please enter a number between 1 and 50:"))
    while(num in user_num or num<1 or num>50):
        print("Invalid number, please try again")
        num = int(input("Please enter a number between 1 and 50:"))
    user_num.append(num)

print("Today's lottery numbers")
print(lottery_num)

print("Your selection")
print(user_num)

counter = 0
for num in user_num:
    if num in lottery_num:
        counter+=1
print("you guessed " + str(counter)+ " numbers correctly")        