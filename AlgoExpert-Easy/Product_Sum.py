
#   Write a function that takes in a "special" array and returns its product sum.
#   A "special" array is a non-empty array that contains either integers or other
#   "special" arrays. The product sum of a "special" array is the sum of its
#   elements, where "special" arrays inside it are summed themselves and then
#   multiplied by their level of depth.
#   The depth of a "special" array is how far nested it is. For instance, the
#   depth of[] is 1; the depth of the inner array in
#   [[]] is2; the depth of the innermost array in
#   [[[]]] is3.
#   Therefore, the product sum of[x, y] isx + y; the
#   product sum of[x, [y, z]] isx + 2 * (y + z); the
#   product sum of[x, [y, [z]]] isx + 2 * (y + 3z).


# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier=1):
    sum = 0
    for item in array:
        if type(item) is list:
            sum += productSum(item, multiplier + 1)
        else:
            sum += item
    return sum * multiplier
