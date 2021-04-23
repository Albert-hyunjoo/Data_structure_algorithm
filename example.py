def dp_longest_inc_subseq(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1+L[pre])
    print(L)
    return max(L)

print(dp_longest_inc_subseq([94, 8, 78, 22, 38, 79, 93, 8, 84, 39]))