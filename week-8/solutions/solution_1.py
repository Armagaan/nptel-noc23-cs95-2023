def binary_kp(N, W, Weights, Values, print_table=False):
    # * Populate the DP table.
    # Initialize the dp table with 0.
    rows = N
    cols = W + 1
    dp_table = []
    for row in range(rows):
        dp_table.append([0 for __ in range(cols)])

    # Fill up 0th row.
    for col in range(cols):
        dp_table[0][col] = Values[0] if Weights[0] <= col else 0

    # Iterate over rows. Skip 0th row.
    for row in range(1, rows):
        # Iterate over col.
        for col in range(1, cols):
            item = row
            weight = col
            # Check if item's weight > current_max_weight
            if Weights[item] > weight:
                # If no:
                # take value above
                dp_table[row][col] = dp_table[row - 1][col]
            # Else
            else:
                # compute value excluding the item
                # value_without_item = dp[row-1][col]
                value_without_item = dp_table[row - 1][col]

                # compute value including the item
                # value_with_item = val[row] + dp[row-1][col - weight[row]]
                value_with_item = Values[item] + dp_table[row - 1][col - Weights[item]]

                # Take maximum between them.
                dp_table[row][col] = max(value_without_item, value_with_item)
    
    # The last item hold the max profit.
    max_profit = dp_table[-1][-1]

    # * Print the DP table.
    if print_table:
        print("----- DP table -----")
        for row in dp_table:
            print(row)
        print()

    # * Find the items in the knapsack
    itemset = []
    current_profit = max_profit
    for row in range(rows - 1, 0, -1):
        if current_profit == 0:
            break
        item = row
        col = cols + 1
        if current_profit in dp_table[row]:
            # Find the first occurance of current profit in the row.
            # That much space will have been utilized if this item was chosen.
            col = dp_table[row].index(current_profit)
        else:
            continue
        # Check previous row upto available space.
        if current_profit not in dp_table[row - 1][:col+1]:
            itemset.append(item)
            current_profit = current_profit - Values[item]
    if current_profit > 0 and current_profit in dp_table[0]:
        itemset.append(0)
    # reverse itemset for convenience
    itemset = itemset[::-1]

    # return last item.
    return max_profit, itemset

if __name__ == "__main__":
    N = 4
    W = 8
    Weights = (2, 3, 4, 5)
    Values = (1, 2, 5, 6)
    print_table = True

    max_profit, itemset = binary_kp(N, W, Weights, Values, print_table)

    print("N:", N)
    print("W:", W)
    print("Weights:", Weights)
    print("Values: ", Values)
    print("Max profit:", max_profit)
    print("Itemset:")
    for i in itemset:
        print(f"Item:{i}, W:{Weights[i]}, V:{Values[i]}")
