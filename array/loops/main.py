# array of 1 - 10000
# from _codecs import encode
# array = list(range(1, 101))

# def square(arr):
#     arr2 = []
#     for number in array:
#         arr2.append(number * number)
#     return arr2

# print(square(array))


# def findPairs(arr):
#     for number in arr:
#         for number2 in arr:
#             print(number, number2)

# findPairs(array)


# def findPairs(arr):
#     results = []

#     number_of_array = len(arr)

#     for first_value in range(number_of_array):
#         for anchor in range(first_value + 1, number_of_array):

#             results.append((arr[first_value], arr[anchor]))
    
#     return results

# print(findPairs(array))


# Exercise 1: The E-Commerce "Two-Sum" (Amazon Style)
# The Scenario: A customer has a gift card for exactly $50. You have an array of item prices. You need to find two items whose prices add up exactly to the gift card amount.

# Goal: Write a function that returns the indices of the two numbers that sum to a target.

# Array: prices = [10, 25, 30, 15, 40]

# Target: 50

# Why this helps: This teaches you to use the Values inside the boxes to make a decision (an if statement) while looping.



# item_prices = [90, 29, 89, 8656, 989757, 989, 10, 25, 30, 15, 40]
# targett = 50


# def find_indices(arr, target):
#     number_of_array = len(arr)

#     for fv in range(number_of_array):
#         for fx in range(fv + 1, number_of_array):
#             if (arr[fv] + arr[fx]) == target:
#                 return [fv, fx]
                
#     return None


# print(find_indices(item_prices, targett))


# Exercise 2: The Social Media "Mutual Friends" (Meta Style)
# The Scenario: You have two lists of friend IDs for two different users. You need to find out which IDs appear in both lists to show "Mutual Friends."

# Goal: Compare List_A and List_B and create a new array called mutual containing only the names found in both.

# Array A: ["Alice", "Bob", "Charlie", "David"]

# Array B: ["Eric", "Bob", "Dan", "Alice"]

# Why this helps: This teaches you how to use nested loops to compare two different arrays instead of comparing an array to itself.





# Generating 500 friend IDs for each list
# eric_alfred has IDs 0 to 499
# david_uche has IDs 400 to 899
# Mutual friends will be 400 to 499 (100 mutual friends)
# eric_alfred = [f"Friend_ID_{i}" for i in range(100)]
# david_uche = [f"Friend_ID_{i}" for i in range(100, 900)]




# def find_mutual_friends(arr1, arr2):
#     mutual = []

#     for first_set in arr1:
#         for second_set in arr2:
#             if first_set == second_set:
#                 mutual.append(first_set)
#     return mutual
            


# print(find_mutual_friends(eric_alfred, david_uche))



# Exercise 3: The Stock Market "Max Profit" (FinTech Style)
# The Scenario: You have an array where each index is a day, and the value is the price of a stock on that day. You want to know the maximum profit you could have made by buying on one day and selling on a future day.

# Goal: Find the largest difference between arr[j] (sell price) and arr[i] (buy price) where j > i.

# Array: stock_prices = [7, 1, 5, 3, 6, 4]

# Why this helps: This forces you to understand the Time Flow of an array (you can't sell a stock before you buy it), which perfectly reinforces why we use range(i + 1, n).

stock_prices = [7, 1, 5, 3, 6, 4]


def max_profit(arr):
    length_of_array = len(arr)

    best_profit = 0

    for i in range(length_of_array):
        for j in range (i + 1, length_of_array):
            if arr[j] - arr[i] > 0:
                current_check = arr[j] - arr[i]
                if current_check > best_profit:
                    best_profit = current_check
    return best_profit


print(max_profit(stock_prices))



