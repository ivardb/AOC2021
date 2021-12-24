def function(z, digit, zDivider, xAdd, yAdd):
    m = (z % 26) + xAdd
    z = z / zDivider
    if m != digit:
        z = 26 * z + digit + yAdd
    return z

if __name__ == "__main__":
    params = [(1, 25, 6), (1, 11, 12), (1, 15, 8), (26, -11, 7), (1, 15, 7), (1, 15, 12), (1, 14, 2), (26, -7, 15), (1, 12, 4), (26, -6, 5), (26, -10, 12), (26, -15, 11), (26, -9, 13), (26, 0, 7)]
    possible = []
    for i, (zP, xP, yP) in enumerate(params):
        print(f"Round {i}")
        res = []
        for z in range(26):
            for w in range(1, 10):
                if (z % 26) + xP == w:
                    res.append((z, w))
        if not res:
            if zP == 1:
                print(f"{i}: z = z * 26 + digit + {yP}")
            else:
                print(f"{i}: z = z / {zP} * 26 + digit + {yP}")
        else:
            print(f"{i}: z = z / {zP}")
        print(res)
        possible.append(res)
    rounds = []
    accepted = []
    for w in range(1, 10):
        for w2 in range(1, 10):
            for w3 in range(1, 10):
                z3 = 676 * w + 26 * w2 + 4368 + 8 + w3
                rem = z3 % 26
                for pRem, w4 in possible[3]:
                    if rem == pRem:
                        z4 = z3 // 26
                        for w5 in range(1, 10):
                            z5 = z4 * 26 + w5 + 7
                            for w6 in range(1, 10):
                                z6 = z5 * 26 + w6 + 12
                                for w7 in range(1, 10):
                                    z7 = z6 * 26 + w7 + 2
                                    rem = z7 % 26
                                    for pRem, w8 in possible[7]:
                                        if rem == pRem:
                                            z8 = z7 // 26
                                            for w9 in range(1, 10):
                                                z9 = z8 * 26 + w9 + 4
                                                rem = z9 % 26
                                                for pRem, w10 in possible[9]:
                                                    if rem == pRem:
                                                        z10 = z9 // 26
                                                        rem = z10 % 26
                                                        for pRem, w11 in possible[10]:
                                                            if rem == pRem:
                                                                z11 = z10 // 26
                                                                rem = z11 % 26
                                                                for pRem, w12 in possible[11]:
                                                                    if rem == pRem:
                                                                        z12 = z11 // 26
                                                                        rem = z12 % 26
                                                                        for pRem, w13 in possible[12]:
                                                                            if rem == pRem:
                                                                                z13 = z12 // 26
                                                                                rem = z13 % 26
                                                                                for pRem, w14 in possible[13]:
                                                                                    if rem == pRem:
                                                                                        z14 = z13 // 26
                                                                                        if z14 == 0:
                                                                                            accepted.append(f"{w}{w2}{w3}{w4}{w5}{w6}{w7}{w8}{w9}{w10}{w11}{w12}{w13}{w14}")
    print(f"Part 1: {accepted[-1]}")
    print(f"Part 2: {accepted[0]}")
