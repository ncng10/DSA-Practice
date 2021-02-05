# Given two non-empty arrays of integers, write a function that determines
# whether the second array is a subsequence of the first one.
# A subsequence of an array is a set of numbers that aren't necessarily adjacent
# in the array but that are in the same order as they appear in the array. For
# instance, the numbers

def isValidSubsequence(array, sequence):
    currSequence = 0
    for num in array:
        if currSequence == len(sequence):
            break
        if sequence[currSequence] == num:
            currSequence += 1
    return currSequence == len(sequence)
