# 0/1 KNAPSACK USING DYNAMIC PROGRAMMING
# Bottom-Up and Top-Down Approaches


def knapsack_bottom_up(weights, profits, capacity):

    count = len(weights)

    # Create DP table without using built-in max()
    dp = [[0 for c in range(capacity + 1)]
          for r in range(count + 1)]

    # Construct the table
    for item in range(1, count + 1):

        current_weight = weights[item - 1]
        current_profit = profits[item - 1]

        for limit in range(capacity + 1):

            if current_weight <= limit:

                take = current_profit + dp[item - 1][limit - current_weight]
                skip = dp[item - 1][limit]

                if take > skip:
                    dp[item][limit] = take
                else:
                    dp[item][limit] = skip

            else:
                dp[item][limit] = dp[item - 1][limit]

    # Trace selected items
    chosen = []
    remaining = capacity

    for item in range(count, 0, -1):

        if dp[item][remaining] != dp[item - 1][remaining]:

            chosen.append(item)
            remaining -= weights[item - 1]

    chosen.reverse()

    return dp[count][capacity], chosen, dp


def knapsack_top_down(weights, profits, capacity):

    total_items = len(weights)

    # Memoization table
    memo = [[None for c in range(capacity + 1)]
            for r in range(total_items + 1)]

    def solve(index, remaining):

        if index == 0 or remaining == 0:
            return 0

        if memo[index][remaining] is not None:
            return memo[index][remaining]

        position = index - 1

        if weights[position] > remaining:
            result = solve(index - 1, remaining)

        else:
            included = profits[position] + solve(
                index - 1,
                remaining - weights[position]
            )

            excluded = solve(index - 1, remaining)

            if included > excluded:
                result = included
            else:
                result = excluded

        memo[index][remaining] = result
        return result

    best_value = solve(total_items, capacity)

    # Identify selected items
    selected = []
    remaining = capacity

    for index in range(total_items, 0, -1):

        if solve(index, remaining) != solve(index - 1, remaining):

            selected.append(index)
            remaining -= weights[index - 1]

    selected.reverse()

    return best_value, selected


# -------------------------------
# MAIN PROGRAM
# -------------------------------

weights = [2, 3, 4, 5]
profits = [12, 10, 20, 15]
capacity = 7

print("================================")
print("       0/1 KNAPSACK PROBLEM")
print("================================")

print("\nAvailable Items:")

for i in range(len(weights)):
    print(
        "Item", i + 1,
        " | Weight =", weights[i],
        " | Profit =", profits[i]
    )

print("\nKnapsack Capacity:", capacity)


# Bottom-Up Method
bottom_value, bottom_items, table = knapsack_bottom_up(
    weights,
    profits,
    capacity
)

print("\n----- BOTTOM-UP APPROACH -----")
print("Maximum Profit:", bottom_value)
print("Selected Items:", bottom_items)


# Top-Down Method
top_value, top_items = knapsack_top_down(
    weights,
    profits,
    capacity
)

print("\n----- TOP-DOWN APPROACH -----")
print("Maximum Profit:", top_value)
print("Selected Items:", top_items)

print("\n================================")
print("Program Completed Successfully")
print("================================")


OUTPUT

================================
       0/1 KNAPSACK PROBLEM
================================

Available Items:
Item 1  | Weight = 2  | Profit = 12
Item 2  | Weight = 3  | Profit = 10
Item 3  | Weight = 4  | Profit = 20
Item 4  | Weight = 5  | Profit = 15

Knapsack Capacity: 7

----- BOTTOM-UP APPROACH -----
Maximum Profit: 32
Selected Items: [1, 3]

----- TOP-DOWN APPROACH -----
Maximum Profit: 32
Selected Items: [1, 3]

================================
Program Completed Successfully
================================
