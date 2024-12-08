class Alg():
    def __init__(self,a:'python list',ans:'python list',maxv:'list of size 1',work:'list of size 1',show:'bool'):
        ## Nothing can be changed below
        self._a = a
        self._ans = ans
        self._maxv = maxv
        self._work = work
        self._show = show
        self._exam() #Everything happens in _exam
        
    ############################################################
    #          Nothing can be changed in _exam
    ########################################################### 
    def _exam(self):
        alg1_ans = []
        alg1_max = [0]
        if (len(self._a) < 25):
          self._alg1()
          assert(self._work[0])
          #your answer is checked here after exam
          check_result(self._a,self._ans,self._maxv[0],alg1_ans,alg1_max[0]) 
          
          for e in self._ans:
            alg1_ans.append(e)
          alg1_max[0] = self._maxv[0]
          self._ans.clear()
          
          self._maxv[0] = 0 
          self._work[0] = 0

        #always run alg2
        self._alg2()
        assert(self._work[0])
        #your answer is checked here after exam
        check_result(self._a,self._ans,self._maxv[0],alg1_ans,alg1_max[0]) 

    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg1(self):
        a = self._a
        n = len(a)
        self._work[0] = 0
        
        # We'll store all valid combinations (indices, sum) for printing
        all_combos = []

        # Recursive function to find all valid subsets
        def recurse(i, current_indices, current_sum):
            self._work[0] += 1
            if i >= n:
                # End of array
                all_combos.append((current_indices[:], current_sum))
                return

            # Option 1: Skip this course
            recurse(i+1, current_indices, current_sum)

            # Option 2: Take this course if possible
            # After taking course i, skip i+1 by going to i+2
            if i+2 <= n:
                recurse(i+2, current_indices + [i], current_sum + a[i])
            else:
                # If i+2 is out of range, just take i and store
                new_sum = current_sum + a[i]
                new_indices = current_indices + [i]
                self._work[0] += 1
                all_combos.append((new_indices, new_sum))

        # Call recursion from index 0
        recurse(0, [], 0)

        # Find the combination with the maximum sum
        max_val = 0
        best_combo = []
        for combo, s in all_combos:
            if s > max_val:
                max_val = s
                best_combo = combo

        self._maxv[0] = max_val
        self._ans.extend(best_combo)

        if self._show:
            print("-------- Alg 1 ----------")
            # Print all combos with indexing
            count = 1
            for combo, s in all_combos:
                print(f"{count}: {combo} = {s}")
                count += 1

        # Print final results (always show final answer)
        print("maxv =", self._maxv[0])
        print("ans =", self._ans)
        print("work =", self._work[0])
        print("The complexity of alg1 is TIME: O(2^N) AND SPACE: O(N) ")
         
        
    ############################################################
    #          WRITE CODE BELOW
    ########################################################### 
    def _alg2(self):
        a = self._a
        n = len(a)
    
        self._work[0] = 0
        self._ans.clear()
    
        if n == 0:
            self._maxv[0] = 0
            self._work[0] += 1
            if self._show:
                print("-------- Alg 2 ----------")
            print("maxv =", self._maxv[0])
            print("ans =", self._ans)
            print("work =", self._work[0])
            return
    
        # DP solution
        dp = [0]*n
        dp[0] = a[0]
        self._work[0] += 1
        if self._show:
            print("-------- Alg 2 ----------")
            print(f"DP[0] = a[0] = {dp[0]}")

        if n > 1:
            dp[1] = max(a[0], a[1])
            self._work[0] += 1
            if self._show:
                print(f"DP[1] = max(a[0], a[1]) = max({a[0]}, {a[1]}) = {dp[1]}")
    
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + a[i])
            self._work[0] += 1
            if self._show:
                print(f"DP[{i}] = max(DP[{i-1}], DP[{i-2}] + a[{i}]) = max({dp[i-1]}, {dp[i-2]} + {a[i]}) = {dp[i]}")
    
        self._maxv[0] = dp[n-1]
    
        # Backtrack to find chosen indices
        indices = []
        i = n - 1
        while i >= 0:
            if i == 0:
                if dp[0] > 0:
                    indices.append(0)
                break
            if dp[i] == dp[i-1]:
                i -= 1
            else:
                indices.append(i)
                i -= 2
    
        indices.reverse()
        self._ans.extend(indices)
    
        # Print final results (always show final answer)
        print("maxv =", self._maxv[0])
        print("ans =", self._ans)
        print("work =", self._work[0])
        print("The complexity of alg2 is TIME: O(N) AND SPACE: O(N) ")

############################################################
#  AFTER EXAM DELETE CODE BELOW AND ADD GIVEN CODE
###########################################################  

############################################################
#  class  Solution
# Nothing can be changed in Solution
###########################################################    
class Solution():
    def rob(self, nums:'Python list') -> 'int':
        #Nothing can be changed here
        ans = []
        maxv = [0]
        work = [0]
        t = Alg(nums,ans,maxv,work,False)
        return maxv[0]

############################################################
# Nothing can be changed in check_result
# Note check_result is a global hanging function
###########################################################  
def check_result(a:'Python list',ans:'Python List',amax:'int',alg1_ans:'Python list',alg1_max:'int'):
    if (alg1_max):
        #alg1 did not run
        if (alg1_max != amax):
          print("alg1 max=", alg1_max)
          print("alg2 max=", amax)
          assert(False)

        x = sorted(alg1_ans)
        y = sorted(ans)
    x = sorted(ans)
    t = 0
    for e in x:
        t = t + a[e]
    assert(t == amax)
    # assert you did not break the rule
    lx = len(x)
    for i in range(0,lx-1,2):
        pos1 = x[i]
        pos2 = x[i +1]
        assert(pos2 >= (pos1+1))

