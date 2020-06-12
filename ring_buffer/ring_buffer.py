class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity  # place to store the data concat int
        self.current = 0  # len is a tracker

        # ds cannot be larger than capacity

    def append(self, item):
        # update len
        if len(self.storage) < self.capacity:  # storage has to be < capacity
            self.storage.append(item)  # add item to storage
        else:
            self.storage[self.current] = item  # will move to next index
        # if storage is > than capacity - start at 0(current)
        if self.current < len(self.storage) - 1:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        new_items = []  # create a new list
        for i in self.storage:  # loop through the storage
            if i is not None:
                new_items.append(i)
        return new_items
