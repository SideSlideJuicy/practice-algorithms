limit = 4000000
termA = 1
termB = 2
nextTerm = 2
sum = 0

while nextTerm < limit:
    
    if nextTerm < limit and nextTerm % 2 == 0:
        sum += nextTerm

    nextTerm = termA + termB
    termA = termB
    termB = nextTerm

print(sum)