class Solution():
    Tab = list[int]
    def permute(self,tab: Tab) -> Tab:  #permutacje n-elementowa zbioru n-elementowego
        n = len(tab)
        result = []
        self.permuteHelper(tab, n, [], result)
        return (result, len(result))

    def permuteHelper(self, tab: Tab, n: int, cur: Tab,result: Tab):    #pomocnicza funkcja rekurencyjna
        if(n == 0): result.append(cur); return
        for i in range(len(tab)):
            self.permuteHelper(tab[:i] + tab[i+1:],n-1,cur + [tab[i]],result)
        return
    
    def variationNoRep(self, tab:Tab, m:int):   #m elementowa wariacja bez powtórzeń zbioru n elementowego
        result = []
        self.variationNoRepHelper(tab,m,[],result)
        return (result, len(result))

    def variationNoRepHelper(self, tab:Tab, m:int, cur:Tab, result:Tab):    #pomocnicza funkcja rekurencyjna
        if(len(cur) == m): result.append(cur); return
        for i in range(len(tab)):
            self.variationNoRepHelper(tab[:i] + tab[i+1:], m, cur + [tab[i]], result)
        return

    def variation(self, tab:Tab, m:int):    #m elemenetowa wariacja z powtórzeniami zbioru m elementowego
        result = []
        self.variationHelper(tab, m, [], result)
        return (result, len(result))
    
    def variationHelper(self, tab:Tab, m:int, cur:Tab, result:Tab): #pomocnicza funkcja rekurencyjna
        if(len(cur) == m): result.append(cur); return
        for i in range(len(tab)):
            self.variationHelper(tab, m, cur + [tab[i]], result)
        return

    def combine(self, tab:Tab, m:int):  #m elementowa kombinacja zbioru n elementowego
        result = []
        self.combineHelper(tab, m, [], result)
        return (result, len(result))

    def combineHelper(self, tab:Tab, m:int, cur:Tab, result:Tab):   #pomocnicza funkcja rekurencyjna
        if(len(cur) == m): result.append(cur); return
        if(len(tab) == 0): return
        for i in range(len(tab)):
            self.combineHelper(tab[i+1:], m, cur + [tab[i]], result)
        return


a = Solution()
tab = [1,2,3,4,5,6,7,8]
#print(a.permute(tab))
#print(a.variationNoRep(tab,2))
#print(a.variation(tab, 3))
#print(a.combine(tab, 3))