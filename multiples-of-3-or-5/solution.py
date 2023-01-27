limit = 1000
i = 0
y = []

while i < limit:

    if i % 3 == 0 or i % 5 == 0:
        y.append(i)
    i += 1
    print()
    
result = sum(y)
print(result)
