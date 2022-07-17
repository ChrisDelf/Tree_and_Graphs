def isAnagram(self, s: str, t: str) --> bool:
    # first we can check for len
    if len(s) != len(t):
        return False
    isAnagram = True
    # going to use a hashmap to store the data
    ana_hash = {}
    
    # going to iterate through the first string and place it into the hash

    for i in range(len(s)):
        if s[i] not in ana_hash:
            ana_hash[s[i]] = 1
        else:
            ana_hash[s[i]] += 1

    # now we have to iterate through the t string

    for i in range(len(t)):
        if t[i] in ana_hash:
            ana_hash[t[i]] -= 1
            if ana_hash[t[i]] < 0:
                return False
        else:
            return False

    return True
