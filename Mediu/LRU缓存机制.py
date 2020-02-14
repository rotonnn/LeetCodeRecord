class LRUCache:
    
    def __init__(self, capacity: int):
        self.keys=[]
        self.values=[]
        self.cap=capacity

    def get(self, key: int) -> int:
        if key in self.keys:
            ind=self.keys.index(key)
            res=self.values[ind]
            self.keys.pop(ind)
            self.values.pop(ind)
            self.keys.append(key)
            self.values.append(res)
            return res
        else:return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            ind=self.keys.index(key)
            self.keys.pop(ind)
            self.values.pop(ind)
        if len(self.keys)<self.cap:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.keys.pop(0)
            self.values.pop(0)
            self.keys.append(key)
            self.values.append(value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)