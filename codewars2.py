# 7kyu
#String ends with?

#Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false


def solution(text, ending):
    return text.endswith (ending)

# solution() only has one operation and is to call the endswith() method on the text variable. The endswith() method has a time complexity of O(1), 
# which means that the time it takes to run the function is constant