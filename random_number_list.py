import random

randomList = []
for num in range(20):
    randomList.append(random.randrange(1, 100))
randomList.sort()
print(f"Sorted List: {randomList}")
print(f"Sum: {sum(randomList)}")