class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)
        if self.b == [] or self.b[-1]>=x:
            self.b.append(x)


    def pop(self) -> None:
        if self.a[-1] == self.b[-1]:
            self.b.pop()
        self.a.pop()

    def top(self) -> int:
        return self.a[-1]


    def min(self) -> int:
        if self.b == []:
            return None
        return self.b[-1]