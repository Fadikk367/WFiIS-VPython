def elements_that_is_in_both_lists(L1, L2):
    S1 = set(L1)
    S2 = set(L2)
    L = list(S1 & S2)
    #for i in (S1 & S2):
    #    L.append(i)
    return L

L1 = [3, 1, 6, 10, 10, 10]
L2 = [2, 8, 4, 3, 1, 6, 10]

print(elements_that_is_in_both_lists(L1, L2))