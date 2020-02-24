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
    trip_list = []
    
    for i in tickets:
        if i.source == "NONE":
            start = i
        if i.destination =='NONE':
            end = i
    current_destination = start.destination
    # for i in tickets:
    while current_destination != 'NONE':
        for i in tickets:
            if i.source == current_destination:
                hash_table_insert(hashtable, i.source, i.destination)
                trip_list.append(i.source)
                current_destination = i.destination
            hash_table_insert(hashtable, end.source, end.destination)

    # print(trip_list)
    return trip_list

# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#                    ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# reconstruct_trip(tickets, 10)