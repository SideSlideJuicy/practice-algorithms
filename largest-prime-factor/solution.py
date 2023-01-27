# User input for variable called 'user_input'
user_input = input("Enter the value: ")
user_input = int(user_input)

factor_calc = user_input
message = user_input

# Creates a new empty lists for factors & prime factors
list_factors = []
list_prime_factors = []


x = 0

while x < user_input:
    x += 1
    #print(x)

    if x > 1 and x <= user_input and user_input % x == 0:
        user_input = user_input / x
        #print(f"user_input is: {user_input}")
        
        list_prime_factors.append(x)
        #print(f"prime is: {x}")

        x = 0

"""
x = 0

while x < factor_calc:
    x += 1
    #print(f"x is: {x}")

    if factor_calc % x == 0:
        factor = factor_calc / x
        #print(f"factor is: {factor}")
        list_factors.append(x)
"""

#print(f"All factors of {message} are: {list_factors}")
print(f"The prime factorization of {message} is: {list_prime_factors}")


