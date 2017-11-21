# --- Directions
# Write a program that console logs the numbers
# from 1 to n. But for multiples of three print
# 'fizz' instead of the number and for the multiples
# of five print 'buzz'. For numbers which are multiples
# of both three and five print 'fizzbuzz'.
# --- Example
#   fizzBuzz(5);
#   1
#   2
#   fizz
#   4
#   buzz


def fizzbuzz (n):			# n ---> whole number
	a = int(n)
	i = 1
	while i <= a:
	# for i in range(a):
		if i % 3 == 0 and i % 5 == 0:
			print 'fizzbuzz'
		elif i % 5 == 0:
			print 'buzz'
		elif i % 3 == 0:
			print 'fizz'
		else:
			print i

		i += 1


x = raw_input('Enter whole number: ')
result = fizzbuzz(x)