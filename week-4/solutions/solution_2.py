def flatten(list_):
    '''Flatten a nested list.'''
    flattened_list = []
    # iterate over the items
    for item in list_:
        # if the item is not a list
        if not isinstance(item, list):
            # append to flattened list
            flattened_list.append(item)
        else:
            # flattened_list.extend(flatten(item))
            flattened_list += flatten(item)
    return flattened_list

if __name__ == "__main__":
    # * Tip: Use vscode's debuggind mode for better understanding of recursive calls.
    print(flatten([1, 2, [3], [4, [5, 6]]]))
