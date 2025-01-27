def isAnagram(s, t):
    alpha_count = [0] * 26
    if len(s) != len(t):
        return False
    else:
        for c1, c2 in zip(s, t):
            alpha_count[ord(c1) - ord('a')] += 1 # ord('a') = 98
            alpha_count[ord(c2) - ord('a')] -= 1 
        return all(ele == 0 for ele in alpha_count)
    
isAnagram('asif', 'fisa')