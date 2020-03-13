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
    for ticket in tickets:
        # and hash each ticket so that the startin position is the key and the destination is the value inserting the key-value pair in the hash table
        hash_table_insert(hashtable, ticket.source, ticket.destination)
  
    # start from the first location
    counter = 0 
    # set a first_ticket to be where the key (source) is "None"
    first_ticket = hash_table_retrieve(hashtable, "NONE")
    # print('first', first_ticket)
    route[counter] = first_ticket
    current_ticket = first_ticket
    # then use the first ticket to set it to current ticket and loop over incrementing the counter so that we are moving to the next location each time in the loop 
    while current_ticket is not "NONE":
        # increment counter each time we go over 
        counter += 1
        # Retrieve value by using current ticket as key in hash_table_retrieve
        current_ticket = hash_table_retrieve(hashtable, current_ticket)
        route[counter] = current_ticket

    return route
    


