import random

def count_greater_than_50():
  L = [random.randint(1, 100) for _ in range(50)]
  count = sum(1 for num in L if num > 50)
  print("List:", L)
  print("Number of items greater than 50:", count)

count_greater_than_50()