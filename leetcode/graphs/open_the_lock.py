
class Solution:
    def openLock(self, deadends, target: str) -> int:
        
        q = [('0000',0)]
        vis = {'0000'}
        deaddics = {j:1 for j in deadends}
        ok = False
        dist = None


        for state, dis in q :
            if state in deaddics:
                continue
            for j in range(4):

                p = (int(state[j])+1)%10
                st = list(state[:])
                st[j] = str(p)
                st = ''.join(st)

                def op(st):
                    nonlocal vis,deaddics,ok,dist
                    if st in vis or st in deaddics:
                        return

                    q.append((st, dis+1))
                    vis.add(st)
                    if st == target:
                        dist = dis + 1
                        ok = True
                        

                op(st)
                p = (int(state[j])-1)%10
                st = list(state[:])
                st[j] = str(p)
                st = ''.join(st)

                op(st)


            if ok :
                break

        
        if target == '0000' and target not in deaddics:
            dist = 0
            ok = True
        if ok :
            return dist
        else:
            return -1




deadends = ["0201","0101","0102","1212","2002"]
target = "0000"
obj = Solution().openLock(deadends, target)
print(obj)

