from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = defaultdict(int)
        
        for x in s:
            count[x] += 1
            
        for x in t:
            count[x] -= 1
            
        for val in count.values():
            if val != 0:
                return False
        
        return True        

# solution = Solution()
# print(solution.isAnagram("racecar", "carrace"))  # Should return True
# print(solution.isAnagram("hello", "world"))      # Should return False

        # sum = sum1 = sum2 = 0
        # ascii1 = [ord(char) for char in s]
        # ascii2 = [ord(char) for char in t]

        # for i in ascii1:
        #     sum1 += i
        # for i in ascii2:
        #     sum2 += i

        # if sum1 == sum2:
        #     return True
        # else:
        #     return False
        # s = "racecar"
        # t = "carrace"
        # t_list = list(t)
        # s_list = list(s)
        
        # if len(t_list) != len(s_list):
        #     return False
        
        # for i in s_list:
        #     for j in t_list:
        #         print(i, j)
        #         if i == j:
        #             t_list.remove(j)
        #             break
                            
        # # print(len(t_list))
            
        # if len(t_list) == 0:
        #     return True
        # else:
        #     return False