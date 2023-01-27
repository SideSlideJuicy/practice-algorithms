import time



# User input
user_input = int(input("Enter the value: ")) + 1



from datetime import timedelta
start_time = time.monotonic()


# Create variables & lists

list_of_palindromes = []

i=True

result = 0
x = 1
y = 1



# Loop
while i:
        result = x * y
        #print(f"{x} * {y} = {result}")
        converted = str(result)
        x += 1

        if result > 9 and converted == converted[::-1]:
            list_of_palindromes.append(result)

        if x == user_input:
            y += 1
            x = 1

        if y == user_input:
            i = False



# Return the max value of the list
max_value = max(list_of_palindromes)


# Output
print(f"The largest palindrome is: {max_value}")


end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))