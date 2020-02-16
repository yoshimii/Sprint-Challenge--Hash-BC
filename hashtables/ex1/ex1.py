#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
       
    for i in weights:
        hash_table_insert(ht, i, (i, weights.index(i)) )
        value = hash_table_retrieve(ht, i)
        for j in weights:
            
            if value[0] + j == limit:
                if weights.index(value[0]) > weights.index(j):
                    answer = (weights.index(value[0]), weights.index(j))
                    print('IF indexes: ', answer)               
                else:
                    answer = (weights.index(j), weights.index(value[0]))
                    print('ELSE indexes: ', answer)
                print(answer)
                return answer
            else: print('Not found')
            
weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2)

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_4)

weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(answer_3)