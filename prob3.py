def find_maximum(numbers, comparator):
    max_value = numbers[0]
    for num in numbers[1:]:
        max_value = comparator(max_value, num)
    return max_value

comparator = lambda a, b: a if a > b else b

# Example usage
numbers = [15, 8, 34, 79, 26]
max_number = find_maximum(numbers, comparator)
print(f"The maximum number is: {max_number}")
