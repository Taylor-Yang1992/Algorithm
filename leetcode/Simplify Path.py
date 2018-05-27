class Solution:
    
    def handle(self,s,w):
        if not w in [".",".."]:
            s.append(w)
        elif w == "..":
            if s:
                s.pop(-1)
        
    def simplifyPath(self,path):
        if path == "/":
            return "/"
        s = []
        i = 0
        j = 0
        while j < len(path):
            if path[j] != "/":
                j += 1
            else:
                if i != j:
                    w = path[i:j]
                    self.handle(s,w)
                j += 1
                i = j
        if i < len(path):
            w = path[i:len(path)]
            self.handle(s, w)
        if not s:
            return "/"
        else:
            result = ""
            for item in s:
                result += "/" + item
            return result  
