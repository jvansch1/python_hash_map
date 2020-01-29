def hash_function(input, size):

    if isinstance(input, int) or isinstance(input, float):
        return int(input % size)
    if isinstance(input, str):
        i = 1
        sum = 0

        while i <= len(input):
            sum += ord(input[i - 1]) * i
            i += 1

        return sum % size
