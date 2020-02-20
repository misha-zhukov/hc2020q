import heapq
class PQData:
    def __init__(self, id, inner_obj):
        self.id = id
        self.inner_obj = inner_obj
        self.deleted = False

    def __gt__(self, value):
        return True 

class MaxPQ:

    def __init__(self):
        self.heap = []
        self.obj_dict = {}
        self.del_count = 0

    def push(self, key, inner_obj):
        data_obj = PQData(inner_obj, inner_obj)
        if data_obj.id in self.obj_dict.keys():
            self.del_count += 1
            self.obj_dict[data_obj.id].deleted = True

        self.obj_dict[data_obj.id] = data_obj
        heapq.heappush(self.heap, (-key, data_obj))

    # pop from empty raises an error
    def pop(self):
        while True:
            key, data_obj = heapq.heappop(self.heap)
            if not data_obj.deleted:
                break
            else:
                self.del_count -= 1
        
        del self.obj_dict[data_obj.id]

        return data_obj.inner_obj

    def __len__(self):
        return len(self.heap) - self.del_count

if __name__ == '__main__':
    pq = MaxPQ()
    pq.push(5, 5)
    pq.push(3, 3)
    pq.push(4, 4)
    pq.push(1, 1)
    pq.push(2, 2)
    pq.push(200, 1)

    while len(pq):
        print(pq.pop())



