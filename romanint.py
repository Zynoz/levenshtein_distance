def int_to_roman(input):
    if not isinstance(input, type(1)):
        print('error')
    elif not 0 < input < 4000:
        print('error')
    else:
        ints = (1000, 900, 500, 400, 100, 90, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []
        for i in range(len(ints)):
            count = int(input / ints[i])
            result.append(nums[i] * count)
            input -= ints[i] * count
        return ''.join(result)
