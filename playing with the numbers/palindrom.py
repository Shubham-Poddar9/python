number=int(input("enter your number"))
on=number
reverse=0
while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
if on==reverse:
    print("It is palindrome")
else:
    print("it is not palindrome")