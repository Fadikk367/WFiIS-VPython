def list_product(list):
    product = 1
    for el in list:
        product *= el
    return product

L = [2, 3, 4, 5]

print(list_product(L))