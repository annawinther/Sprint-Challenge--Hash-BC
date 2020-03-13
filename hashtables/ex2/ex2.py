#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # loop over the tickets 
        # and hash each ticket so that the startin position is the key and the destination is the value inserting the key-value pair in the hash table
  
    # find the n-th location in the route by checking the hastabel for n-1
    # set a first_ticket to be where the destination is "None"
    # then use the first ticket to set it to current ticket and loop over incrementing the counter so that we are moving to the next location each time in the loop 
        # Retrieve value by using current ticket as key in hash_table_retrieve
    


    pass
