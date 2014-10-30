import math
import sys

x = 10

print("\n" + "Guess the secret number!" + "\n")

number = sys.stdin.readline()

while int(number) != x:

	if int(number) < x:
		print ("\n" + "Too low")
	elif int(number) > x:
		print ("\n" + "Too high")

	print("\n" + "Guess the secret number again" + "\n")

	number = sys.stdin.readline()

print("\n" + "Well done, you guessed correctly")


