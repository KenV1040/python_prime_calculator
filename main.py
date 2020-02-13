import time




def main():
    # I control all my tests here
    print("Prime calculator!")
    test_numbers = [1000,15000]
    # The array of numbers is the maximum number I'll calculate prime numbers up to.
    # Also, I repeat this 3 times to get an average time. This is to ensure reliable results
    for number in test_numbers:
        for i in range(3):
            time_took = primeSieve(2, number)
            print("{} run".format(i))
            print("Number: {num} Time took: {time}".format(num=number, time= time_took))
            print("-------------------")


def primeSieve(begin, end):
    i = begin
    n = end
    nonPrime = []
    prime = []
    start_time = time.time()
    while (i < n):
        if i % 2 == 0 and i != 2:    
            i = i + 1
            continue
        else:
            for nonPrimeNumber in nonPrime:
                if i == nonPrimeNumber:
                    break
            i = i + 1
            continue
        """ if (i in nonPrime):
            i = i + 1
            continue """
        temp_i = i
        while (temp_i < n):
            nonPrimeNumber = temp_i * i
            nonPrime.append(nonPrimeNumber)
            temp_i = temp_i + 1
        prime.append(i)
        i = i + 1

    time_took = time.time() - start_time
    for primeNumber in prime:
        if primeNumber % 2 == 0:
            print("This prime number is divisible by 2: {}".format(primeNumber))
    print("Length of prime numbers: {}".format(len(prime)))
    return time_took

if __name__ == "__main__":
    main()