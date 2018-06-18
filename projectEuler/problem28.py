# https://projecteuler.net/problem=28

def spiral_diag_sum(n):
    if n < 1: return None
    elif n == 1: return 1
    elif n % 2 == 0: return None
    else:
        numbers = [1]
        numbers_needed = 2 * n - 1
        increment = 2
        while len(numbers) < numbers_needed:
            for p in range(4):
                numbers.append(numbers[-1] + increment)
            increment += 2
    print(numbers)
    return sum(numbers)
print(spiral_diag_sum(1001))
