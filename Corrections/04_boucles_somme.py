s = 0
for num in range(1, 11):
    if num % 2 == 1:
        s += num
print(s)

sum(list(filter(lambda num : num % 2 == 1, range(1,11))))

# avec l'opérateur :=
s = 0
[s := s + num for num in range(0, 11) if num % 2 == 1]
