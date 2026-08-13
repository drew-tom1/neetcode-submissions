class MyHashMap:

    def __init__(self):
        self.table = {}
        

    def put(self, key: int, value: int) -> None:
        self.table[key] = value
        

    def get(self, key: int) -> int:
        if key in self.table.keys():
            return self.table[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.table.keys():
            del self.table[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)