test_dict = {'Codingal': 1, 'is': 2, 'best': 3, 'for': 4, 'coding': 5}

print(f"The original dictionaty: {str(test_dict)}")

K = 2

res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print(f"Frequency of K is: {str(res)}")
