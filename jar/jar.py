
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity can't be negative")
        self._capacity=capacity
        self._size=0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("Exceed Capacity")
        if self._size+n > self._capacity:
            raise ValueError("Exceed Capacity")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Can't withdraw that much cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(5)
jar.withdraw(1)
print(jar)
