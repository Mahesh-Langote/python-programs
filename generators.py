def generate_numbers(n):
    for i in range(n):
        yield i

numbers = generate_numbers(5)
for num in numbers:
    print(num)
