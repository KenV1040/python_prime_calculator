import time




def main():
    # I control all my tests here
    print("Prime calculator!")
    #test_numbers = [500,1000,1500,2000,2500,5000,10000]
    #test_numbers = [20000,30000,40000,50000]
    test_numbers = [100000]
    # The array of numbers is the maximum number I'll calculate prime numbers up to.
    # Also, I repeat this 3 times to get an average time. This is to ensure reliable results
    for number in test_numbers:
        for i in range(1):
            time_took = primeSieve(2, number)
            print("{} run".format(i))
            print("Number: {num} Time took: {time}".format(num=number, time= time_took))
            print("-------------------")


def primeSieve(begin, end):
    i = begin
    n = end
    prime = []
    start_time = time.time()
    while (i < n):
        isContinue = False
        for primeNumber in prime:
            if i % primeNumber == 0:
                i = i + 1
                isContinue = True
                break
        if isContinue: continue
        prime.append(i)
        i = i + 1

    time_took = time.time() - start_time
    #print(prime)
    print("Length of prime numbers: {}".format(len(prime)))
    print("Largest prime: {}".format(prime[-1]))
    return time_took

if __name__ == "__main__":
    main()




"""     notInPrime = False
            for nonPrimeNumber in nonPrime:
                if i == nonPrimeNumber:
                    notInPrime = True
                    break
            if notInPrime:
                i = i + 1
                continue """