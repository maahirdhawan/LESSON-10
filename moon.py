while True:
    number = int(input("Enter your number: "))
    digits = len(str(number))
    temp = number
    sum = 0
    while temp>0:
        digit = temp % 10
        sum = sum + digit**digits
        temp =  temp // 10
    if number == sum:
        print("IT IS NEIL ARMSTRONG")
    else:
        print("IT IS NOT NEIL ARMSTRONG")