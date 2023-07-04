index = 0

while True:
    palidrome = input("Enter a string of your choice!: ")
   #If you do not enter any input and just press enter, the program will quit.
    if index == len(palindrome):
        break
    elif palindrome == palindrome[::-1]:
        print("Palindrome string!")
    else:
        print("Not a palindrome string!")
