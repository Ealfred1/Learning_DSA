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