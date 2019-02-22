def long_repeat(line):
    reigning_champion = 0
    contender = 0
    for x in range(len(line) - 1):
        if line[x] == line[x+1]:
            contender += 1
            if contender > reigning_champion:
                reigning_champion = contender
        else:
            contender = 0
    if len(line) > 0:
        return reigning_champion + 1
    return reigning_champion

print(long_repeat('sdsffffse'))  # == 4
print(long_repeat('ddvvrwwwrggg'))  # == 3
print(long_repeat('abababaab'))  # == 2
print(long_repeat(''))  # == 0
print(long_repeat("abababa"))  # == 1
