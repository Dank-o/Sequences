# Program to enumerate the abundance of numbers in standard sequences. The
# abundance of a number is the difference between the sum of the number's
# proper divisors and the number.

def is_in_seq_file(input, n):

    # Function that checks if a given number is in an abundant number.

    with open(input, "r") as file:
        for line in file:
            list_line = line.split()

            try:
                if int(list_line[1]) == n:
                    return True
                elif int(list_line[1]) > n:
                    return False
            except IndexError:
                pass
    # Ensure a False is returned if query exceeds maximum file value.
        return False


def abundances(input, max=30):
    # A function that returns the sequence of abundances (difference betweeen
    # n and aliquot sum) of a given sequence numbers. NEW SEQUENCE!
    # Reads file with aliquot sums (from https://oeis.org/A001065)
    with open("Sequence/Abundancy_X/aliquot_sums(A001065).txt", "r") as file2:
        difference = ()
        differences = ""
        stop = 0

        for line in file2:
            list_line = line.split()

            try:

                if stop == max:
                    break

                n = int(list_line[0])

                if is_in_seq_file(input, n):
                    aliquot_sum = int(list_line[1])
                    difference = aliquot_sum - n
                    differences += f"{n} {difference} \n"
                    stop += 1

            except IndexError:
                pass

        print([int(i) for i in differences.split()[1::2]])
        # return differences

        # with open("Sequence/Abundancy_X/simple_abundances.txt", "w") as file:
        #     file.write(differences)


abundances("Sequence/Abundancy_X/primitive_abundant(A071395).txt", 100)
