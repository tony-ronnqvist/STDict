import random


class STDict:
    """Creates a new sorted dictionary data-structure. The data structures handel keys as integer or strings.
    By default, when a new dictionary is created, the keys are set as strings.
    
    A dictionary is a data-structure that associate keys with values, as an example, in this dictionary we
    can associate the integer 1 with the string "Hello world". Because this dictionary is built on a TREAP, it
    is sorted, and the built-in methods has a high probability to perform in the average case. Insertion in the
    dictionary follows the following rules:
    
    If the inserted key is greater than the key of the root, then it will be added as the right leaf, given that
    the root key has no leaf to the right. If the root already has a right leaf, then they key is compared against
    the key of the right leaf, and the same rules are applied. If the inserted key is less than the root, then it is
    instead added as the left leaf. Because insertion follows these rules the dictionary will be sorted.
    
    A balanced BST is a tree where the minimum and maximum depth of the tree are close to equal. This is achieved by
    given each node a randomized priority value and rotating the tree when the priority is wrong. This is where the
    TREAP is different from an ordinary BST; there is a high probability that the TREAP is balanced and therefore
    the methods have a high probability to run in the average case."""

  

    def __init__(self, root=None):
        self._root = root
        self._size = 0
        self._string = str("[ ]")
        self._type = "I"

    def __len__(self):
        """Returns the number of keys in a STDict() object, O(1). Called as len(STDict)"""
        return self._size

    def __getitem__(self, key):
        """Search the STDict for key and returns associated value if key is present, else returns False.
        Called as STDict[key], O(n)"""
        found = self._help_set_get(self._root, key, "get")
        if found is None:
            return False
        return found._val

    def get(self, key):
        """Search the STDict for key and returns associated value if key is present, else returns False.
         Called as STDict.get(key)"""
        found = self._help_set_get(self._root, key, "get")
        if found is None:
            return False
        return found._val

    def __setitem__(self, key, val):
        """Search the STDict for key and sets they keys associated value to value if key is present.
        Raises an error if key is not present in STDict object. Called as STDict[key]=value"""
        self._type_check(key)
        self._help_set_get(self._root, key, "set", val)
        return

    def set(self, key, val):
        """Search the STDict for key and sets they keys associated value to value if key is present.
        Raises an error if key is not present in STDict object. Called as STDict.set(key)=value"""
        self._type_check(key)
        self._help_set_get(self._root, key, "set", val)
        return

    def clear(self):
        """Clears the a STDict-object of all keys and associated values, O(1)"""
        self._root = None
        self._size = 0
        self._string = str("[ ]")
        return

    def insert(self, key, val):
        """ Insert a key and a associated value in a STDict-object, key can be either integer or string depending
        which type is set. Values can be strings or integers. Raises a error if the key is already in the
        STDict-object or key with wrong type is inserted."""
        self._type_check(key)
        new_node = node(val, key)
        self._root = self._add(new_node, self._root)
        self._size += 1

    def sorted_string(self):
        """ Returns all keys and associated values of a STDict() object sorted by keys.
        The keys and associated values are returned as a string in ascending order."""
        if self._root is None:
            return str("[ ]")
        self._string = str("[")
        string = self._traversal_string(self._root)
        return string[:-2] + str("]")

    def max_key(self):
        """Returns the maximum key of a STDict object. O(n)"""
        minimum=self._help_max(self._root)._key
        return minimum

    def min_key(self):
        """Returns the minimum key of a STDict object. O(n)"""
        maximum = self._help_min(self._root)._key
        return maximum

    def delete(self, key):
        """Deletes key and associated value from a STDict() object if the key is present,
         else raises an error. Key can be either integer or string. O(n)"""
        self._root = self._delete(self._root, key)
        self._size -= 1
        return

    def change_type(self, type_):
        """Change the types of which type of keys are allowed to be stored in the STDict-object.
        Type can be either "S" = strings or "I"= integer. Raise an error if wrong type is given
        or if the STDict-object already contains keys in a specific type and the type is changed.
        By default, when a new dictionary is created, the keys are set as integers."""
        if type_ != "S" and type_ != "I":
            raise TypeError("Error: Type: str("+str(type_)+") not valid, str(S)=string and str(I)=integes.")
        elif self._size == 0 or self._type == type_:
            self._type = type_
        else:
            raise TypeError("Can't change type to str("+str(type_)+") when keys already in STDict has type str("+str(self._type)+")")

    def get_type(self):
        """Returns the type of keys allowed in the STDict-object. "S" = strings and "I"= integers."""
        return self._type

    def _type_check(self, key):
        """Help-function to control error for the STDict-methods. Key = key to check if correct type"""
        if self._type == "I" and isinstance(key,str):
            raise TypeError("STDict keys is set as type int()")

        elif self._type == "S" and isinstance(key,int):
            raise TypeError("STDict keys is set as type str()")
        else:
            return

    def _delete(self, tree_root, key):
        """help-function to the delete method. tree_root = root of tree (node) , key = key to delete"""
        if tree_root is None:
            raise ValueError("key: " + str(key) + " not in STDict")
        if key < tree_root._key:
            tree_root._left = self._delete(tree_root._left, key)
        elif key > tree_root._key:
            tree_root._right = self._delete(tree_root._right, key)
        elif tree_root._right and tree_root._left:
            if tree_root._left._prio_val < tree_root._left._prio_val:
                tree_root = tree_root._rotate(1)
                tree_root._left = self._delete(tree_root._left, key)
            else:
                tree_root = tree_root._rotate(0)
                tree_root._right = self._delete(tree_root._right, key)
        elif tree_root._right is not None:
            tree_root = tree_root._right
        elif tree_root._left is not None:
            tree_root = tree_root._left
        else:
            tree_root = None
        return tree_root

    def _help_max(self, tree_to_search):
        """help-function to the max_key method. tree_to_search is root of tree to find max in"""
        if tree_to_search._right is not None:
            return self._help_max(tree_to_search._right)
        else:
            return tree_to_search

    def _help_min(self, tree_to_search):
        """help-function to the min_key method. tree_to_search is root of tree to find min in"""
        if tree_to_search._left is not None:
            return self._help_min(tree_to_search._left)
        else:
            return tree_to_search

    def _traversal_string(self, tree_sort):
        """"help-function sorted_string method. Tree_sort is root of tree to sort"""
        if tree_sort is None:
            return None
        else:
            self._traversal_string(tree_sort._left)
            self._string += str(tree_sort._key) + ": " + str(tree_sort._val) + ", "
            self._traversal_string(tree_sort._right)
            return self._string

    def _add(self, node_, tree_root):
        """Help function to insert method. node_= Node to insert in the tree see,
        insert. tree_root = root of the tree to insert node in O(n)"""
        if tree_root is None:
            return node_
        if node_._key == tree_root._key:
            raise ValueError("Key: " + str(node_._key) + " already in STDict")
        if node_._key < tree_root._key:
            tree_root._left = self._add(node_,tree_root._left)
            if tree_root._prio_val > tree_root._left._prio_val:
                tree_root = tree_root._rotate(0)
        else:
            tree_root._right = self._add(node_,tree_root._right)
            if tree_root._prio_val > tree_root._right._prio_val:
                tree_root = tree_root._rotate(1)
        return tree_root

    def _help_set_get(self, tree_find, lookup_key, set_or_get, set_value=None):
        """Help function to set and get methods. tree_find = root of tree to search in. Lookup_key = key to search for.
        set_or_get decides if the method its used in is set or get. set_value = value to set,
        only used if set_or_get is not get"""
        if tree_find is None:
            if set_or_get == "get":
                return tree_find
            else:
                raise ValueError("key: " + str(lookup_key) + " not in STDict")
        if lookup_key == tree_find._key:
            if set_or_get == "get":
                return tree_find
            else:
                tree_find._val = set_value
                return
        if tree_find._key > lookup_key:
            return self._help_set_get(tree_find._left, lookup_key, set_or_get, set_value)
        else:
            return self._help_set_get(tree_find._right, lookup_key, set_or_get, set_value)

class node:
    """A help class for nodes that build up STDict data-structure. Functionality includes creating nodes and
    rotating nodes"""
    def __init__(self, val, key):
        self._val = val
        self._right = None
        self._left = None
        self._key = key
        self._prio_val = random.random()

    def _rotate(self, rotate_index):
        """Rotates a node, help function for the STDict O(1). 1 = left rotate"""
        if rotate_index == 1:
            new_node = self._right
            new_child = self
            new_child._right = new_node._left
            new_node._left = new_child
        else:
            new_node = self._left
            new_child = self
            new_child._left = new_node._right
            new_node._right = new_child
        return new_node
