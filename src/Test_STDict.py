##############################################################################
#                          TEST CODE FOR STDict                              #
##############################################################################


def test_prioVal_and_key(STDictonary_root):
    """Test function for the STDict that checks that the priority order of the tree is correct. That all left and right
    pointers is less then/greater then the root value. STDictonary_root = root of the STDict to test, O(n)"""
    if STDictonary_root is None:
        return
    else:
        if STDictonary_root._left and STDictonary_root._right is None:
            pass
        if STDictonary_root._left is not None:
            assert STDictonary_root._left._prio_val >= STDictonary_root._prio_val
            assert STDictonary_root._left._key < STDictonary_root._key
        if STDictonary_root._right is not None:
            assert STDictonary_root._right._prio_val >= STDictonary_root._prio_val
            assert STDictonary_root._right._key > STDictonary_root._key

        test_prioVal_and_key(STDictonary_root._left)
        test_prioVal_and_key(STDictonary_root._right)


def test_size(STDictonary_root, count=0):
    """Test function for the size counter of the STDict-class, STDictonary_root = root of STDict to test , O(n)"""
    if STDictonary_root is None:
        return count
    else:
        count += 1
        count = test_size(STDictonary_root._left, count)
        count = test_size(STDictonary_root._right, count)

    return count


import re


def test_string_sorted(STDictonary):
    """Test function of the tree class, checks that the order of the string is correctly sorted by key
     tree_test = tree you want to test, O(n)"""
    string_test = STDictonary.sorted_string()[:-1]
    string_test = string_test[1:]
    string_test = re.split(r"(?:: )|(?:, )", string_test)
    type_ = STDictonary.get_type()
    if type_ == "I":
        for i in range(0, len(string_test) - 2, 2):
            if i == int(len(string_test)):
                return
            assert int(string_test[i]) < int(string_test[i + 2])
    else:
        for i in range(0, len(string_test) - 2, 2):
            if i == int(len(string_test)):
                return

            assert str(string_test[i]) < str(string_test[i + 2])


def healthy(STDictonary):
    """Uses the test functions to check that the STDict is correct, tree_test = tree you want to test O(n)"""
    assert len(STDictonary) == test_size(STDictonary._root)

    if len(STDictonary) == 0:
        assert STDictonary._root == None

    test_prioVal_and_key(STDictonary._root)
    test_string_sorted(STDictonary)


def test_delete_set_get_insert(STDictonary, key, val):
    """Tests the methods set, get, insert and delete."""
    STDictonary.insert(key, val)
    size_ = len(STDictonary)

    STDictonary.delete(key)
    assert size_ - 1 == len(STDictonary)
    assert STDictonary[key] == False

    STDictonary.insert(key, val)
    assert STDictonary[key] == val
    assert size_ == len(STDictonary)

    STDictonary[key] = "new_value"
    assert STDictonary[key] == "new_value"
    assert size_ == len(STDictonary)


def test_type_error(STDictonary):
    type_ = STDictonary.get_type()
    if type_ == "I":
        try:
            STDictonary.insert("C", "A")
        except TypeError:
            return True
    else:
        try:
            STDictonary.insert(2, "A")
        except TypeError:
            return True
    return False


def test_min_max(STDictonary):
    string_test = STDictonary.sorted_string()[:-1]
    string_test = string_test[1:]
    string_test = re.split(r"(?:: )|(?:, )", string_test)
    string_test = string_test[::2]
    if STDictonary.get_type() == "S":
        assert max(string_test) == STDictonary.max_key()
    else:
        for i in range(0, len(string_test)):
            string_test[i] = int(string_test[i])
        assert min(string_test) == STDictonary.min_key()


def gen_rand_dict(n, m, c, type_):
    """Generates random STDict with n keys each with values from 0 to m or ASCII if type is "S"."""
    random.seed(c)
    dictonary = STDict()
    if type_ == "I":
        for i in range(0, n):
            dictonary.insert(random.randint(0, m), random.randint(0, m))
        return dictonary
    else:
        dictonary.change_type("S")
        for i in range(0, n):
            dictonary.insert(chr(random.randint(0, m)), random.randint(0, m))
        return dictonary


def test_main():
    """Main test, uses healthy and the test_delete_set_get_insert"""
    # int()
    int_dict_1 = gen_rand_dict(10, 100, 11, "I")
    int_dict_2 = gen_rand_dict(20, 150, 122, "I")
    int_dict_3 = gen_rand_dict(30, 250, 210, "I")

    # str()
    str_dict_1 = gen_rand_dict(10, 100, 11, "S")
    str_dict_2 = gen_rand_dict(20, 150, 122, "S")
    str_dict_3 = gen_rand_dict(30, 250, 210, "S")

    # Big test for STDict with int-type

    healthy(int_dict_1)
    test_delete_set_get_insert(int_dict_1, 10, "A")
    healthy(int_dict_2)
    test_delete_set_get_insert(int_dict_2, 64, "B")
    healthy(int_dict_3)
    test_delete_set_get_insert(int_dict_3, 42, "C")

    # Big test for STDict with str-type
    healthy(str_dict_1)
    test_delete_set_get_insert(str_dict_1, "B", 1)
    healthy(str_dict_2)
    test_delete_set_get_insert(str_dict_2, "C", 2)
    healthy(str_dict_3)
    test_delete_set_get_insert(str_dict_3, "D", 3)

    # Error-test for both int and str
    error_1 = test_type_error(int_dict_1)
    assert error_1 == True
    error_2 = test_type_error(str_dict_1)
    assert error_2 == True

    # Min and max-test for both int and str
    test_min_max(int_dict_3)
    test_min_max(str_dict_3)
    return