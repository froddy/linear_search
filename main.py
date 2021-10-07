# demo linear search function
# froddy
# 07-10-2021

# initialise and populate an array e.g. mylist = [1,2,3,4,5,6]
# populate an array e.g. mylist = [1,2,3,4,5,6]
# to search it: call function passing a list and the target value to find
# linear_search(mylist, 4)
# should return 4

#target is the thing we are looking for.

#hard coded for test
mylist = [1,2,3,4,5,6]

def binary_search(items, target):

    #initialise variables
    current_cell = 0  #starting position
    found = False  # if we find it we can quit loop early

    #repeat while current cell number less than list length and
    #while target has not been found (still False)
    while current_cell < len(items) and found == False:
        if items[current_cell] == target:
            found = True  # we found it! we can exit loop early :)
        # otherwise proceed to next item (next cell)
        # we need to increment the counter first though!
        #current_cell = current_cell + 1
        current_cell = current_cell + 1 
        print(len(items))

    #remember an array starts at 0, but it make more sense to people if we think of the first cell as 1, good job we have already added one then.
    return current_cell

    

