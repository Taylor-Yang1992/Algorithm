class Solution:
    
    def calculate(self,s):
        if not s:
            return 0
        ll = []
        l = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                ll.append(int(s[j:i]))
            elif s[i] == " ":
                i += 1
            else:
                if not l:
                    l.append(s[i])
                else:
                    if l[-1] in ("*","/"):
                        op = l.pop(-1)
                        e1 = ll.pop(-1)
                        e2 = ll.pop(-1)
                        ll.append(e2 * e1 if op == "*" else int(e2 / e1))
                    l.append(s[i])
                i += 1
        if l and l[-1] in ("*","/"):
            op = l.pop(-1)
            e1 = ll.pop(-1)
            e2 = ll.pop(-1)
            ll.append(e2 * e1 if op == "*" else int(e2 / e1))
        for op in l:
            e1 = ll.pop(0)
            e2 = ll.pop(0)
            ll.insert(0,e1 + e2 if op == "+" else e1 - e2)
        return ll[0]
"""
Notes:
  It's not a good solution because there are too many pop operations at the beiginning of the list.
  It wastes a lot
"""
