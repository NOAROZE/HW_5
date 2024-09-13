# START
height: float = float(input("enter your height:"))
# אני עשיתי תווך כולל
while not 0.4 <= height <= 2.5:
    print("wrong input")
    height: float = float(input("enter your height:"))

# END

# START
num_1: int = int(input("enter a number:"))
num_2: int = int(input("enter a number:"))
if num_1 > num_2:
    for i in range(num_1, num_2 - 1, -1):
        print(i)
else:
    for j in range(num_1, num_2 + 1):
        print(j)
# END

# START
pie: float = float(input("Enter the value of pie:"))
account: int = 1
while account < 3:
    if pie == 3.14:
        print("you are correct")
        break
    else:
        pie: float = float(input("Enter the value of pie:"))
        account += 1
if not pie == 3.14:
    print("pie is 3.14")

# END

# START
while True:
    # input
    num_1: float = float(input("enter  the firs number:"))
    num_2: float = float(input("enter  the second number:"))
    num_3: float = float(input("enter  the third number:"))
    # Average calculation
    avg_num: float = (num_1 + num_2 + num_3) / 3
    # Check whether to exit
    if 0 < num_1 < 10 < num_2 < 60 < num_3 < 100 and num_2 == avg_num:
        break

# END
