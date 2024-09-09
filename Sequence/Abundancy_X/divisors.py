# Program to enumerate the divisors of numbers in standard sequences. The
# sequence must be formatted the same way as .txt files from the OEIS are.
# With an option to include only prime divisors.

def is_prime(num):
    # Prime number checker
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def divisor_counts(input, max=33):
    # Function that returns a list of the first n terms of the sequence of
    # the number of divisors of each n in a given sequence.

    with open(input, "r") as file:
        divisor_counts = []
        stop = 0

        for line in file:
            list_line = line.split()

            try:
                number = int(list_line[1])
                count = 0

                if stop == max:
                    break

                for divisor in range(1, int(number / 2) + 1):
                    if number % divisor == 0:
                        count += 1
                divisor_counts += [count + 1]
                stop += 1

            except IndexError:
                pass
        return divisor_counts


div_seq = divisor_counts("Sequence/Abundancy_X/Abundant_numbers(A005101).txt")
print(div_seq)
