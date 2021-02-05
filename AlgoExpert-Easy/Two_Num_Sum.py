# Write a function that takes in a non-empty array of distinct integers and an
# integer representing a target sum. If any two numbers in the input array sum
# up to the target sum, the function should return them in an array, in any
# order. If no two numbers sum up to the target sum, the function should return
# an empty array.

# Note that the target sum has to be obtained by summing two different integers
# in the array; you can't add a single integer to itself in order to obtain the
# target sum.

def twoNumberSum(array, targetSum):
    hash = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in array:
            return [targetSum - num, num]
        else:
            hash[num] = True
    return []
