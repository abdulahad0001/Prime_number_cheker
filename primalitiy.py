num1 = int(input("Enter your number:"))

if num1 > 1:
    for integer in range(2,num1):
        if(num1%integer)==0:
            print(num1, "is not a prime number")
            break

    else:
      print("Congrats!", num1,"is a prime number")

print("\n When you're checking for 0 and 1, Note that 0 and 1 are not prime numbers")


#You're not allowed to remove this line, if you share it
print("\n", "Created by Md. Abdul Ahad Khan")
