def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        # If the list has an even number of elements, take the average of the middle two.
        middle_left = sorted_numbers[n // 2 - 1]
        middle_right = sorted_numbers[n // 2]
        return (middle_left + middle_right) / 2
    else:
        # If the list has an odd number of elements, return the middle value.
        return sorted_numbers[n // 2]
 
def mode(numbers):
    # Create a dictionary to store the frequency of each number.
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
 
    # Find the number(s) with the highest frequency.
    max_frequency = max(frequency.values())
    mode_values = [num for num, freq in frequency.items() if freq == max_frequency]
 
    # If there are multiple modes, return the first one.
    return mode_values[0]
 
def mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
