# Local scope vs Global Scope


def test_scope():
    s = "Local String"
    print(s)


def test_scope2():
    global s
    s = "Changing to in local"
    print(s)

s = "Global string"
print(s)
test_scope()
print(s)
test_scope2()

# Global string
# Local String
# Global string
# Changing to in local


# Recursion
# Def: repetition calling themself

def recursive_list_reverse(ls: list)->list:
    """
    This function takes in a list of any type and reverse it
    :param ls: list to be reverseWd
    :return: a reversed list of ls
    """
    if ls:
        return recursive_list_reverse(ls[1:]) + [ls[0]]
    else:
        return []


print(recursive_list_reverse([1, 2, 3, 4]))

def pascal_triangle(n: int, r: int):
    """
    function returns n combination r from pascals triangle

    :param n:
    :param r:
    :return:
    """
    if n==0
        return 1
    elif r ==0:
        return 1
    elif n==r:
        return 1
    else
        return pascal_triangle(n-1,r) + pascal_triangle(n-1, r-1)

