class Solution:
    
    def minimumTotal(self,triangle):
        if len(triangle) == 1:
            return triangle[0][0]
        l = [0] * len(triangle)
        l[0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(i,-1,-1):
                if j == i:
                    l[j] = l[j - 1] + triangle[i][j]
                elif j == 0:
                    l[j] = l[0] + triangle[i][0]
                else:
                    l[j] = min(l[j],l[j - 1]) + triangle[i][j]
            print(l)
        return min(l)
