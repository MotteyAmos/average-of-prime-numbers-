# this code was writing by me from scratch 

def prime_numbers_upto():
    # find prime numbers up to a specied value by the user
    prime_numbers = []
    while True:
        try:
            number = int(input("Enter a number to print numbers up to: "))
            if number <0:
                print("negetive numbers are not prime!!!")
                continue
            else:
                break
        except:
            print("numbers only!!!!")
            continue
    for i in range(1, number +1):
        if i % 2 == 0:
            if i == 2:
                prime_numbers.append(i)
        elif i % 3 == 0:
            if i == 3:
                prime_numbers.append(i)
        elif i % 5 != 0 or i == 5:
            prime_numbers.append(i)
    
    return prime_numbers
    

def average_of_prime_numbers():
    # find the average of prime numbers upto a given number specified by user
    prime_numbers = prime_numbers_upto()
    sum_of_prime_numbers = 0
    for i in prime_numbers:
        sum_of_prime_numbers += i
    average_of_prime_numbers = sum_of_prime_numbers / len(prime_numbers)
    print("List of prime numbers are ", prime_numbers)
    print("The average of the prime nubers is", average_of_prime_numbers)

average_of_prime_numbers()
