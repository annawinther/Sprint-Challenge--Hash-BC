#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

weights = [1, 4, 5, 6, 7]

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # if weight len less than 2 
    if length < 2:
        # return None
        answer = None
    
    # hash_table_insert(ht, weights[0], 0)
    answer = ['test', 'working']
        
    print_answer(answer)

    # loop through one and insert the weight at index and the index to the hashtable

    # loop through again this time retrieving the weight and index using the difference between the limit and and the wieght at index
    
    # retrieve from the hastable.
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

get_indices_of_item_weights(weights, 2, 1)