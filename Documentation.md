###Documentation - STDict a TREAP dictionary
A dictionary is a data-structure that uses keys to associate values, as an example, in this dictionary we can associated the integer 1 with "Hello world". Because this dictionary is built on a TREAP, it's sorted, and the built-in methods has a high probability to perform in the average case.

##More information on TREAP and binary search tree (BST)
Insertion in the dictionary follows the following rules: if the key is greater than the root key, then it will be inserted to the right else insertion will be to the left. If the slot to the right or the left is occupied, and insertion should have been in either, then instead we compare the keys to that of the right or left key and follow the same rules. Because insertion follows these rules the dictionary will be sorted.

A balanced BST is a tree where the min a max depth of the tree is close to equal. This is achieved by given each node a randomized priority value and rotating the tree when the priority is wrong. This is where the TREAP is different from an ordinary BST, there is a high probability that the TREAP is balanced and therefore the methods have a high probability to run in the average case.




***
```
The sorted dictionary STDict and it's functionality
  1. Time-complexity
  2. Create a new sorted dictonary
      2.1  New:     STDict()
      2.2  Method: .get_type()
      2.3  Method: .type_change()
  3. Functionality
      3.1  Method: .insert()
      3.2  Method: .delete(key)
      3.4  Method: .get(key)
      3.4  Method: .set(key)
      3.5  Method: .max_key()
      3.6  Method: .min_key()
      3.7  Method:  len()
      3.8  Method: .sorted_string()
      3.9  Method: .clear()
 
```  
***

### 1. Time-complexity

| Algorithm     | Average       | Worst case |
| ------------- |:-------------:| ----------:|
| Space         |   O(n)        |   O(n)     |
| Search        | 	O(log n)    |   O(n)     |
| Insert        | 	O(log n)    |   O(n)     |
| Delete        |  	O(log n)    |   O(n)     |
| sort          | 	O(nlog n)   |   O(n^2)   |


***
### 2. Create a new sorted dictonary

2.1 New: STDict_object=STDict()

    Creates a new sorted dictionary data-structure. The data structures handel keys as integer or strings.
    By deafault, when a new dictonarry is created, the keys type is set as integers.

2.2 Method: STDict_object.get_type()

    Returns the type of keys allowed in the STDict-object. "S" = strings and "I"= integers.
    
2.3 Method: STDict_object.type_change(type)

    Change the types of which type of keys are allowed to be stored in the STDict-object.
    Type can be either "S" = strings or "I"= integer. Raise an error if wrong type is given
    or if the STDict-object already contains keys in a specific type and the type is changed.
    By default, when a new dictionary is created, the keys are set as integers.
    

***
### 3. Functionality

Down below you will find a discription of all the methods included in this package.

3.1 Metod: STDict_object.insert(key, value)

    Insert a key and a associated value in a STDict-object, key can be either integer or string depending
    which type is set. Values can be strings or integers. Raises a error if the key is already in the STDict-object
    or key with wrong type is inserted.
    
    
3.2 Metod: STDict_object.delete(key)

    Deletes key and associated value from a STDict-object if the key is present. Key can be either integer or string.
    If key is not present rasises an error.
    
3.3 Metod: STDict_object.get(n) or STDict_object[key]

    Search the STDict for key and returns associated-value if key is present else returns False.
    
3.4 Metod: STDict_object.set(key, val) or STDict_object[key] = value

    Search the STDict for key and sets the keys associated-value to value if key is present.
    Rasise a error if key is not present in STDict object.
 
3.5 Metod: STDict_object.max_key()

    Returns the maximum key of a STDdict-object.
 
3.6 Metod: STDict_object.min_key()

    Returns the minimum key of a STDdict-object.
    
3.7 function len(STDict_object)

    Returns the number of keys in a STDict-object.
    
    
3.8 Metod: STDict_object.sorted_string()

    Returns all keys and associated values of a STDict() object sorted by keys.
    The keys and associated values are returned as a string in ascending order.

3.9 Metod: STDict_object.clear()

    Clears the a STDict-object of all keys and associated values.
