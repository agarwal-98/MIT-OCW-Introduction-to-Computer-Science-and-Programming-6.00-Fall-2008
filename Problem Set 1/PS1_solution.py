from math import *

# Problem 1

integer = 3 

# prime_count starts with 1 to account for prime no. 2 as the first prime number
prime_count = 1 
while(prime_count<=999):
  not_a_prime = []
  for divisor in range(3,int(integer/2)):
      if integer%divisor == 0:
      # if integer is divisible by a divisor it is added to not_a_prime list
        not_a_prime.append(integer)
        break

  if len(not_a_prime) == 0:
    # if the list is empty, it means the integer is a prime number
    prime_count = prime_count + 1
      
  integer+=2 

print (integer-2)


# Problem 2

integer = 3 
prime_count = 1 

# initiating sum of log of prime numbers with log of 2
sum_logprimes = log(2)
while(prime_count<=999):
  not_a_prime = []
  for divisor in range(3,int(integer/2)):
    if integer%divisor == 0:
      not_a_prime.append(integer)
      break

  if len(not_a_prime) == 0:
    # if the list is empty, it means the integer is a prime number
     prime_count = prime_count + 1
     sum_logprimes = sum_logprimes + log(integer)
      
  integer+=2
	 

print (integer-2)
print (sum_logprimes) 
print ((sum_logprimes)/(integer-2))






# print(inte[10000-1])


# for y in range(3,x/2): 
# ...             if x%y == 0:
# ...                break
# ...             else:
# ...                 inte.append(x) 