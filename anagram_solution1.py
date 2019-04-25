def anagram(s1, s2):
    """
    Takes two strings and returns True if they are anagrams
    Returns False if not.
    """
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    pos = 0
    matches= True

    while pos < len(s1) and matches:
        if list1[pos] == list2[pos]:
            pos += 1
        else:
            matches = False

    return matches

print(anagram('hello', 'olleh'))
print(anagram('mallam', 'llamaem'))
