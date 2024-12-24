

def mix(secret:int, new:int) -> int:
    # converting to binary
    secret = format(secret, 'b')
    new = format(new, 'b')
    # ensuring 2 numbers have the same num of chars
    diff = abs(len(secret) - len(new))
    diff = ''.join(["0" for x in range(diff)])
    if len(secret) < len(new):
        secret = diff + secret
    elif len(secret) > len(new):
        new = diff + new
    # actual xor operation
    xor = ''
    for a, b in zip(secret, new):
        nums = (int(a),int(b))
        if any(nums) and not all(nums):
            xor += '1'
        else:
            xor += '0'
    # converting back to base 10
    return int(xor, base=2)

def prune(secret:int) -> int:
    pruned = secret % 16777216
    return pruned
    
    
mix(42, 15)

print(prune(100000000))

# start = 15887950
# # mutiply by 64
# new = start * 64
# # mix
# secret = mix(start, new)
# # divide by 32 round down to nearest interger
# new = secret // 32
# # mix
# secret = mix(secret, new)
# # prune
# secret = prune(secret)
# # multiply by 2048
# new = secret * 2048
# # mix
# secret = mix(secret, new)
# # prune
# secret = prune(secret)
# print(secret)
    
def next_secret(start):
    # mutiply by 64
    new = start * 64
    # mix
    secret = mix(start, new)
    # divide by 32 round down to nearest interger
    new = secret // 32
    # mix
    secret = mix(secret, new)
    # prune
    secret = prune(secret)
    # multiply by 2048
    new = secret * 2048
    # mix
    secret = mix(secret, new)
    # prune
    secret = prune(secret)
    return secret

def go_deeper(num, depth):
    current = num
    for i in range(depth):
        print(current)

        current = next_secret(current)
        
    return current

# # go_deeper(123, 10)
# print(next_secret(123))
# print(next_secret(15887950))