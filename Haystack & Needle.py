# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    window = len(needle)
    subs = []

    if haystack == needle:
        return 0

    for i in range(len(haystack) - window + 1):
        subs.append(haystack[i:i + window])
    
    for i in range(len(subs)):
        if subs[i] == needle:
            return i

    return -1
