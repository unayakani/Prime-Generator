import math

n = 1

max = 10000000000

for _ in range(max):

    if n < 10:
        match n:
            case 1: pass
            case 2:
                with open("primes.txt", "a") as file:
                    file.write(str(2))
                    file.write('\n')
            case 3:
                with open("primes.txt", "a") as file:
                    file.write(str(3))
                    file.write('\n')
            case 4: pass
            case 5:
                with open("primes.txt", "a") as file:
                    file.write(str(5))
                    file.write('\n')
            case 6: pass
            case 7:
                with open("primes.txt", "a") as file:
                    file.write(str(7))
                    file.write('\n')
            case 8: pass
            case 9: pass

    elif n >= 10:

        is_prime = True

        for div in range(2, (int(math.sqrt(n)) + 1)):

            if n % div == 0:
                is_prime = False
                break

        if is_prime:
            with open("primes.txt", "a") as file:
                file.write(str(n))
                file.write('\n')

    n += 1
