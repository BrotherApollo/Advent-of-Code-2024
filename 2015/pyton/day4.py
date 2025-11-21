from hashlib import md5

def getHash(data):
    hash_obj = md5(data.encode("utf-8"))
    return hash_obj.hexdigest()

def findsolution(key, num_zeros):
    solution = 0
    match = "0" * num_zeros
    limit = int(1e7)

    while True:
        data = f"{key}{solution}"
        if match == getHash(data)[:num_zeros]:
            print(f"Found the solution: {solution}")
            break
        
        solution += 1
        if solution > limit:
            print(f"exceeded our limit of {limit}")
            break


if __name__ == "__main__":
    secret_key = input("what is your key?")

    #Part one
    print("Part one, 5 leading 0s")
    findsolution(secret_key, 5)

    #Part two
    print("Part tow, 6 leading 0s")
    findsolution(secret_key, 6)
