#!/usr/bin/python

class JND_judger :

    def __init__(self,arr):
        self.arr = arr
    def nonincreseadsquence(self):
        arrLensize = len(self.arr)
        pre = [-1] * arrLensize
        self.arrLen = [1] * arrLensize

        for i in range(0,arrLensize):
            for j in range(0,i):
                if self.arr[i] >= self.arr[j] and self.arrLen[i] < self.arrLen[j]+1:
                    self.arrLen[i] = self.arrLen[j]+1
                    pre[i] = j

        maxLen = 0
        maxIndex = -1
        for i,item in enumerate(self.arrLen):
            if maxLen < item:
                maxLen = item
                maxIndex = i
        print pre
        print self.arrLen
        while pre[maxIndex] is not -1:
            print maxIndex,'->',pre[maxIndex]
            maxIndex = pre[maxIndex]


if __name__ == '__main__':
    arr = [ 2,3,1,2,5,7,4,9,5,10,8 ]
    sl = JND_judger(arr)
    sl.nonincreseadsquence()
