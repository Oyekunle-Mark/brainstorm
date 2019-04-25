def anagram(s1, s2):
    """
    Takes two strings and returns true if they are anagrams and false otherwise
    Takes O(n) time
    """
    arr1 = [0] * 26
    arr2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        arr1[pos] = arr1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        arr2[pos] = arr2[pos] + 1

    j = 0
    matches = True

    while j < 26 and matches:
        if arr1[j] == arr2[j]:
            j += 1
        else:
            matches = False

    return matches

print(anagram('listen', 'silent'))

