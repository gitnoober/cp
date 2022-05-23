class Robot:

    def __init__(self, w: int, h: int):
        self.i = 0
        self.pos = [[0,0,'South'] + [[i,0,'East'] for i in range(1,w)] + [[w-1,i,'North'] for i in range(1,h)] + [i,h-1,'West'] for i in range(w-2,-1,-1)] + [[0,i,'South'] for i in range(h-2,0,-1)]

    def step(self, num: int) -> None:
        self.i+=num

    def getPos(self) -> list[int]:
        return self.pos[self.i % len(self.pos)][:2]

    def getDir(self) -> str:
        return self.pos[self.i % len(self.pos)][2] if self.i else 'East'

# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()