import random

print(random.randint(5, 20))  # line 1
# smallest:5
# largest:20
print(random.randrange(3, 10, 2))  # line 2
# smallest:3
# largest:9
# It won't get to 4
print(random.uniform(2.5, 5.5))  # line 3
# smallest:2.5
# largest: any number <5.5
print(random.randint(1, 100))
