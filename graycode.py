def generateGrayCode(length):
    if length == 1:
        return ['0', '1']
    else:
        prev = generateGrayCode(length - 1)
        return ['0' + x for x in prev] + ['1' + x for x in reversed(prev)]


print(generateGrayCode(4))
