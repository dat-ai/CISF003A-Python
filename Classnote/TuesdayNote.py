import re

# Tuple

first_tuple = (1, 2, 3, 4)
print(first_tuple[1])
print(first_tuple[-1])

# Mutability - what is it?

list1 = [1, 2, 3, 4, 5]


def modified_list(the_list):
    the_list.append(23)                                    # call function in the ref would change actual list
    print("The current value of the list is: ", the_list)
    the_list = [8, 9, 10, 11]                              # call the ref itself would NOT change the actual list
    print("the new value of the list is: ", the_list)


modified_list(list1)
print("Outside the function", list1)


# Is String mutability

first_string = "this is our first string"


def modify_string(a_string):
    a_string = a_string + " plus a new old string"
    print(a_string)
    a_string = "this is a new string"
    print(a_string)

modify_string(first_string)
print(first_string)


# Tuple is immutable
def modify_tuple(a_tuple):
    print(a_tuple)
    a_tuple = (9, 8, 7, 12)
    print(a_tuple)

modify_tuple(first_tuple)
print(first_tuple)


# Dictionary is mutable - like list

first_dictionary = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}


def modify_dictionary(a_dict):
    a_dict["seven"] = 7
    a_dict["eight"] = 8
    print(a_dict)

    a_dict = {"ten": 10, "eleven": 11}
    print(a_dict)

modify_dictionary(first_dictionary)
print(first_dictionary)

# ================ Regular Expression ==========================
# *  : 0 or more characters
# +  : 1 or more characters
#

# import library: import re


pattern = re.compile("ab*")
pattern2 = re.compile("ab+")

test_string = "what is ab going on aa bb abb"
val = pattern.search(test_string)
span_tuple = val.span()

print(span_tuple)
print(span_tuple[0], span_tuple[1])

# print(pattern.search(test_string))
# print(pattern.findall(test_string))
# print(pattern2.search(test_string))
# print(pattern2.findall(test_string))

# phone pattern
phone_pattern = re.compile("\d\d\d-\d\d\d-\d\d\d\d")
print(phone_pattern.match("3445-3532523"))
print(phone_pattern.match("650-475-3543-343"))
print(phone_pattern.match("sde-650-241-2314-131"))


# word separation
word_pattern = re.compile("\w+")
non_alphanumeric = re.compile("\W+")
sentence = "the quick brown fox jumps over the lazy dog"
print(word_pattern.findall(sentence))
print(non_alphanumeric.findall(sentence))


character_class_pattern = re.compile("[b-t]+")
second_character_class_pattern = re.compile("[b-t]{2,3}")

print(character_class_pattern.findall(sentence))
print(second_character_class_pattern.findall(sentence))

big_list = ["343-515-121", "2313-3133-41251", "495-451-412x", "week", "616-412-4241", "408-646-9337"]


def check_string(a_string):
    pat = re.compile("\d\d\d\-\d\d\d\-\d\d\d\d")
    vl = pat.search(a_string)
    if vl is None:
        return False
    elif ((vl.span())[1] - (vl.span())[0]) == len(a_string):
        return True
    else:
        return False
    return False


def check_string2(a_string):
    pat = re.compile("\d\d\d\-\d\d\d\-\d\d\d\d")
    vl = pat.search(a_string)
    if vl is None:
        return False
    elif ((vl.span())[1] - (vl.span())[0]) == 12:
        return True
    else:
        return False
    return False


new_list = [i for i in big_list if check_string(i)]
new_list2 = [i for i in big_list if check_string2(i)]

print(new_list)
print(new_list2)

