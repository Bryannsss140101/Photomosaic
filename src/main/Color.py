class Color:
    r: float = 0.0
    g: float = 0.0
    b: float = 0.0

    def get_r(self) -> float:
        return self.r

    def get_g(self) -> float:
        return self.g

    def get_b(self) -> float:
        return self.b

    def __init__(self, vector: list):
        self.r = vector[2]
        self.g = vector[1]
        self.b = vector[0]

    def __str__(self) -> str:
        return ("[" +
                str(self.r) + ", " +
                str(self.g) + ", " +
                str(self.b) + "]")

    def predominant_chanel(self) -> int:
        channel: int = 0

        if self.r > self.b and self.r > self.g:
            channel = 0
        elif self.g > self.r and self.g > self.b:
            channel = 1
        elif self.b > self.r and self.b > self.g:
            channel = 2
        else:
            channel = 0

        return channel

    def predominant_value(self) -> float:
        channel: float = 0.0

        return channel

    def predominant_chanel(self) -> int:
        channel: int = 0

        if self.r > self.b and self.r > self.g:
            channel = 0
        elif self.g > self.r and self.g > self.b:
            channel = 1
        elif self.b > self.r and self.b > self.g:
            channel = 2
        else:
            channel = 0

        return channel
