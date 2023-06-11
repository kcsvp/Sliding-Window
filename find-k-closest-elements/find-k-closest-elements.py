class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x<arr[0]:
            return arr[:k]
        elif x>=arr[-1]:
            return arr[-k:]
        
        for i in range(len(arr)-1):
            if abs(x-arr[i]) < abs(arr[i+1]-x):
                break
        while i>=1 and abs(x-arr[i]) == abs(arr[i-1]-x):
            i -= 1
        res = [arr[i]]

        l,r,k = i-1,i+1,k-1
        while k>0:
            if l>=0 and r<len(arr):
                if abs(arr[l]-x) <= abs(arr[r]-x):
                    res.insert(0,arr[l])
                    l -=1
                else:
                    res.append(arr[r])
                    r += 1
            elif l>=0:
                res.insert(0,arr[l])
                l -=1
            else:
                res.append(arr[r])
                r += 1
            k -= 1
        return res