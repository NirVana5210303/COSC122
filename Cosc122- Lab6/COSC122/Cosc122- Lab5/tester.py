from spelling import *

dictionary = load_dict_words("words.txt")
document = load_doc_words("sherlock.txt")

#spellcheck_with_list(document, dictionary)

# see http://www.bigprimes.net/archive/prime/
# for a big list of prime numbers
# prime sized hashtables help modulo hashing spread hash values evenly
# prime sizing is also important for quadratic probing to work effectively,
# especially with high load factors

#spellcheck_with_hashtable(document, dictionary, 'Chaining', 1000)
#spellcheck_with_hashtable(document, dictionary, 'Chaining', 1000003)
#spellcheck_with_hashtable(document, dictionary, 'Linear', 700001)
#spellcheck_with_hashtable(document, dictionary, 'Quadratic', 700001)


#You can use print statements between store commands
#to see how the hashtable fills up.
#For example:
#hash_table = ChainingHashTable(5)
#hash_table.store('Paul')
#print hash_table
#hash_table.store('Peter')
#print hash_table
#hash_table.store('Paula')
#print hash_table
#hash_table.store('David')
#print hash_table
#hash_table.store('Bobby')
#print hash_table
#hash_table.store('Dianne')
#print hash_table


#hash_table = ChainingHashTable(5)
#hash_table.store('Paul')
#hash_table.store('Peter')
#hash_table.store('Paula')
#hash_table.store('David')
#hash_table.store('Bob')
#hash_table.store('Di')
#print hash_table

#hash_table = LinearHashTable(7)
#hash_table.store('Aby')
#print hash_table
#hash_table.store('Ken')
#print hash_table
#hash_table.store('Nat')
#print hash_table
#hash_table.store('Jim')
#print hash_table



hash_table = QuadraticHashTable(7)
hash_table.store('Aby')
hash_table.store('Ken')
hash_table.store('Nat')
hash_table.store('Jim')
hash_table.store('Bob')
print hash_table



#hash_table.store('Paul')
#print hash_table
#hash_table.store('Peter')
#print hash_table
#hash_table.store('Paula')
#print hash_table
#hash_table.store('David')
#print hash_table
#hash_table.store('Bobby')
#print hash_table
#hash_table.store('Dianna')
#print hash_table