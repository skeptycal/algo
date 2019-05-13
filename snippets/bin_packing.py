# https://www.youtube.com/watch?v=kiMFyTWqLhc
# ? start with the largest ... add the smallest, next smallest, etc.
# ? start with the largest ... add the next largest that fits ... etc.

# * first fit decreasing
#   * order largest to smallest - fit in order
#   * 'optimal - same as lower bound'

# * full bin packing
#   * group by desired size first, maximizing each group, starting with largest
#   * put into spaces

example = [100, 80, 60, 65, 110, 25, 50, 60, 90, 140, 75, 120, 75, 100, 70, 200, 120, 40]
print(example)
container_size: int = 400
lower_bound = sum(example) // container_size
print(lower_bound)

test_fit = [400 for i in range(10)]
print(test_fit)
for i in example:
    for j in range(len(test_fit)):
        k = test_fit[j] - i
        print(k)
        if k >= 0:
            test_fit[j] = k

print(test_fit)
