"""
Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Unfortunately, not all numbers are lucky. Petya calls a number nearly lucky if the number of lucky digits in it is a lucky number. He wonders whether number n is a nearly lucky number.

Input
The only line contains an integer n (1 ≤ n ≤ 1018).

Please do not use the %lld specificator to read or write 64-bit numbers in С++. It is preferred to use the cin, cout streams or the %I64d specificator.

Output
Print on the single line "YES" if n is a nearly lucky number. Otherwise, print "NO" (without the quotes).
"""

def main():
    input_number = input()
    freq = {"4":0, "7":0}
    for i in input_number:
        if i in freq:
            freq[i] += 1
    lucky_digit = freq["4"] + freq["7"]

    for i in str(lucky_digit):
        if i not in freq:
            print("NO")
            return
    print("YES")
if __name__ == "__main__":
    main()