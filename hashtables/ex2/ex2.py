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
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    # loop over the tickets 
    for ticket in tickets:
        # and hash each ticket so that the startin position is the key and the destination is the value inserting the key-value pair in the hash table
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    # start from the first location
    counter = 0 
    # set a ticket to be "None"
    ticket = "NONE"
    while True:
        current_ticket = hash_table_retrieve(hashtable, ticket)
        # as long as the current ticket is not NONE set the route at the counter to be the current ticket and then update the ticket to be the current ticket. Then increment the counter to continue to the next location. 
        if current_ticket is not "NONE":
            route[counter] = current_ticket
            ticket = current_ticket
            counter += 1
        # once the current ticket is none we're at the last destination and we'll stop the loop and return the route
        else:
            break

    return route
    


