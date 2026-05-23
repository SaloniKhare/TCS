class MedianFinder:

    def __init__(self):
        self.mih=[]
        self.mah=[]

    def addNum(self, num: int) -> None:
        heappush(self.mah,-num)
        heappush(self.mih,-heappop(self.mah))
        if len(self.mih)>len(self.mah):
            heappush(self.mah,-heappop(self.mih))

    def findMedian(self) -> float:
        if len(self.mah)>len(self.mih):
            return -self.mah[0]
        return (-self.mah[0]+self.mih[0])/2        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
