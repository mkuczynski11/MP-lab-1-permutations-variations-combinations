class Solution():
    Tab = list[int]
    def permute(self,n : int) -> Tab:  #permutacje n-elementowa zbioru n-elementowego
        result = []
        tab = [x+1 for x in range(n)]
        self.permuteHelper(tab,n, [], result)
        return (result, len(result))

    def permuteHelper(self, tab: Tab, n: int, cur: Tab,result: Tab):    #pomocnicza funkcja rekurencyjna
        if(n == 0): result.append(cur); return
        for i in range(len(tab)):
            self.permuteHelper(tab[:i] + tab[i+1:],n-1,cur + [tab[i]],result)
        return


a = Solution()
n = 15
permutations,l = a.permute(n)
for permutation in permutations:
    print(permutation)
print(f"n={n} liczba permutacji: {l}")