# Rotate list l, k times

def rotatelist(l, k):
    new_list = l[:]

    # check
    if k < 1:
        return new_list

    for __ in range(k):
        # place the first element at the end of the list
        new_list.append(new_list[0])
        # delete it from the start of the list
        new_list.pop(0)
    return new_list

l = [1, 2, 3, 4, 5]
print(rotatelist(l, 1))
print(rotatelist(l, 3))
print(rotatelist(l, 12))
