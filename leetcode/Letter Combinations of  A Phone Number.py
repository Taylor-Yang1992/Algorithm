class Solution:
    
    def letterCombinations(self,digits):
        if not digits:
            return []
        d = {"2":["a","b","c"],
             "3":["d","e","f"],
             "4":["g","h","i"],
             "5":["j","k","l"],
             "6":["m","n","o"],
             "7":["p","q","r","s"],
             "8":["t","u","v"],
             "9":["w","x","y","z"]}
        pre = [""]
        for i in digits:
            cur = []
            for c in d[i]:
                for e in pre:
                    cur.append(e + c)
            pre = cur
        return pre
