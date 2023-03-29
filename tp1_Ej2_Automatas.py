def solve(string):

    items = string.split()
    nums = [int(item) for item in items if item.isdigit()]

    i = 0
    while i < len(items):
        if items[i] == '*':
            nums[i // 2] *= nums[i // 2 + 1]
            del items[i:i + 2]
            del nums[i // 2 + 1]
        else:
            i += 1

    result = nums[0]
    i = 1
    while i < len(items):
        if items[i] == '+':
            result += nums[i // 2 + 1]
        i += 2

    return result


print(solve('2 + 7 * 2 + 1'))
print(solve('2 * 2 * 2 + 32 * 2'))
