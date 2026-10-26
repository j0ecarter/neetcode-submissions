from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        letter1 = Counter(s1)
        letter2 = Counter(s2[:len(s1)]) # takes all chars from 0 to len(s1) and their count

        if letter1 == letter2:
            return True

        for i in range(len(s1), len(s2)): # left and right pointers for the window
            letter2[s2[i]] += 1 # adding the count of the remaining chars in the window

            left_placement = s2[i - len(s1)] # getting the left placement after s1
            letter2[left_placement] -= 1

            if letter2[left_placement] == 0:
                del letter2[left_placement]

            if letter1 == letter2:
                return True

        return False

        