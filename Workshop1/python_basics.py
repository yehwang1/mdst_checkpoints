"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
from random import randint
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    num = input("Enter a number: ")
    if int(num)%2 == 0:
        print ("even")
    else:
        print ("odd")



def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    x = randint(1, 9)
    guess = int(input("Guess the number: "))
    while x ==1 or x ==2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7 or x == 8 or x ==9:
        if int(guess) > x:
            print("too high")
            guess = input("Guess the number: ")
        elif int(guess) < x:
            print("too low")
            guess = input("Guess the number: ")
        else:
            print ("correct")
            again = input("play again? ")
            if again == "yes":
                part2()
            elif again == "no":
                break
            else:
                print("invalid")

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    string = input ("Enter a string: ")
    reverse = string[len(string)-1::-1]
    if string == reverse:
        print("Your string is a palindrome")
    else:
        print("Not a palindrome")


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

    user1 = base64.b64encode(username.encode('utf-8'))
    pass1 = base64.b64encode(password.encode('utf-8'))
    output = open(filename,"w+")
    output.write(str(user1,"utf-8") + "\n")
    output.write(str(pass1,"utf-8"))
    output.close()
    




def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    input = open(filename,'r')
    username = input.readline()
    password1 = input.readline()


    username = base64.b64decode(username.encode('ascii')).decode('ascii')
    print("Username = ", username)


    password1 = base64.b64decode(password1.encode('ascii')).decode('ascii')
    print("Password = ", password1)
    
    encodeU = base64.b64encode(username.encode('utf-8'))
    if (password != None):
        p1E = base64.b64encode(password.encode('utf-8'))
    else:
        p1E = base64.b64encode(password1.encode('utf-8'))
        
    output = open(filename,"w+")
    output.write(str(encodeU,"utf-8"))
    output.write('\n')
    output.write(str(p1E,"utf-8"))



if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
