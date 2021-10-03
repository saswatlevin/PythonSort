#################################################### BASIC PYTHON FACTS ##########################################################
# This is a comment. Comments begin with #.
# Comments aren't code and aren't executed by Python.

# Variable assignment takes place from right to left.
# Eg:- For the expression X = Y where X and Y are variables, the value in Y is assigned to X.

# A List is a Python data structure that allows a collection of elements of different data types.
# Each list element is assigned an index. The first index is 0.
# The way we access a list element is by using the list's index at which the element is located: 
# listName[listIndex] where listName is a Python list.

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# range() is a built-in function in Python.
# The range function's syntax is: range(START, STOP, STEP) with START and STEP being optional.
# If we don't specify START, Python assigns it a default value of 0.
# If we don't specify STEP, Python assigns it a default value of 1.
# range() returns a sequence of numbers from START to STOP - 1.

# def is the keyword used to declare a function in Python.
# A function in Python is a block of code that executes code in its body when it is called. 
# A function can take have 0 or more parameters. 
#################################################### BASIC PYTHON FACTS ##########################################################

#################################################### ABOUT bubbleSortAscending() FUNCTION ########################################
# It takes the list of numbers to be sorted as its parameter. 
# We use a sorting method called Bubble Sort to Sort the list.
# The process is divided into passes. 
# In each pass, we compare adjacent pairs of numbers in the list.
# In a pair of adjacent numbers if the numbers in that pair are not in ascending order, 
# then we swap the positions of those numbers,
# If this isn't the case, then we do nothing & move to the next adjacent pair of numbers,
# Eg:- The adjacent number pair (6, 2) would become become (2, 6) but the adjacent number pair (4, 10) would remain (4, 10),
# The number of passes is one less than the length in the list.
# At the end of each pass, all the numbers in the list are traversed & the Nth largest number in the list is sorted.
# In all subsequent passes, only the (listLength - N - 1) numbers are traversed where N is the number of sorted numbers.
# This process is continued till the entire list is sorted in ascending order.
#################################################### ABOUT bubbleSortAscending() FUNCTION ########################################


 

def bubbleSortAscending(numberList):
  # This function's body starts here
  
  # Getting the length of the list
  listLength = len(numberList)
  
  # This outer for loop decides the number of passes on the list
  for numberOfSortedElements in range(0, listLength):
    # This inner for loop conducts each pass on the list
    for listIndex in range (0, (listLength - numberOfSortedElements - 1)):
      
      # During each pass,
      # in a pair of adjacent numbers if the numbers in that pair are not in ascending order, 
      if numberList[listIndex] > numberList[listIndex + 1]:
        
        # then we swap the positions of those numbers (swapping happens below)
        temporaryVariable = numberList[listIndex]
        numberList[listIndex] = numberList[listIndex + 1]
        numberList[listIndex + 1] = temporaryVariable
   
        

# Declaring listOne and listTwo
listOne = [30, 58, 19, -10, 31, -6, 84]
listTwo = [7, -4, 8.1, 2.9, -15.2, 10.04, 9.65]


print("Unsorted listOne: ")
print(listOne)

print("Unsorted listTwo: ")
print(listTwo)

# Calling the bubbleSortAscendingFunction to sort listOne
bubbleSortAscending(listOne)

# Calling the bubbleSortAscendingFunction to sort listTwo
bubbleSortAscending(listTwo)

print("Sorted listOne: ")
print(listOne)
          
print("Sorted listTwo: ")
print(listTwo)
          



