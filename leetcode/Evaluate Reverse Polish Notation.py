class Solution:
    
    def evalRPN(self,tokens):
        l = []
        for item in tokens:
            if not item in ["+","-","*","/"]:
                l.append(int(item))
            else:
                e2 = l.pop(-1)
                e1 = l.pop(-1)
                if item == "+":
                    e = e1 + e2
                elif item == "-":
                    e = e1 - e2
                elif item == "*":
                    e = e1 * e2
                else:
                    e = int(e1 / e2)
                l.append(e)
        return l[0]
