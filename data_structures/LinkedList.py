class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"<Node object: data={self.data}>"


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self._length: int = 0

    def __repr__(self) -> str:
        return f"<LinkedList object: head = {self.head}>"

    def __len__(self) -> int:
        return self._length

    def __get_item(self, idx):
        if not isinstance(idx, int):
            raise TypeError("Not valid index")
        if idx >= self._length or idx < -self._length:
            raise IndexError("Index out of range")

        if idx < 0:
            idx += self._length

        mid = self._length // 2
        if idx < mid:
            current = self.head
            for _ in range(idx):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._length - idx - 1):
                current = current.previous
        return current

    def __getitem__(self, idx):
        current = self.__get_item(idx)
        return current.data

    def __setitem__(self, idx, data):
        current = self.__get_item(idx)
        current.data = data

    def insert_first(self, data):
        new = Node(data)
        if self.head is None:
            self.tail = new
        else:
            new.next = self.head
            self.head.previous = new
        self.head = new
        self._length += 1

    def insert_last(self, data):
        new = Node(data)
        if self.tail is None:
            self.head = new
        else:
            new.previous = self.tail
            self.tail.next = new
        self.tail = new
        self._length += 1

    def insert_at(self, idx, data):
        new = Node(data)
        if idx == 0:
            self.insert_first(data)
        elif idx == self._length:
            self.insert_last(data)

        else:
            previous = self.__get_item(idx-1)
            next = previous.next
            new.next == next
            new.previous = previous
            previous.next = new
            next.previous = new
        self._length += 1

    def delete_first(self):
        self.head = self.head.next
        if self.head:
            self.head.previous = None
        self._length -= 1

    def delete_last(self):
        self.tail = self.tail.previous
        if self.tail:
            self.tail.next = None
        self._length -= 1

    def delete_at(self, idx):
        if idx == 0:
            self.delete_first()
        elif idx == (self._length - 1):
            self.delete_last()
        else:
            current = self.__get_item(idx)
            previous = current.previous
            next = current.next
            previous.next = next
            next.previous = previous
            self._length -= 1
