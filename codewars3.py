# 6 kyu
# Stop gninnipS My sdroW!

# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    words = sentence. split(" ")
    return " ".join([word[::-1] if len(word) >=5 else word for word in words])


#  spin_words is  O(n) 
# there is a for loop and an if statement and that makes it an O(1) because it iterates over the words. 
# The join() function has a time complexity of O(n) because of the number of words in the sentence
# overall is O(n) + O(1) + O(1) + O(n) = O(n)