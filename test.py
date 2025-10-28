

def count_up_to(n=10):
    count = 1
    for count <= n:
        yield count  # Pauses the function and sends the value
        print(count)
        count += 1
