class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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
        t_list = list(t)
        s_list = list(s)
        
        if len(t_list) != len(s_list):
            return False
        
        for i in s_list:
            for j in t_list:
                print(i, j)
                if i == j:
                    t_list.remove(j)
                    break
                            
        # print(len(t_list))
            
        if len(t_list) == 0:
            return True
        else:
            return False