import random

class ValueNoise():
    def __init__(self, seed=0, amplify=1):
        self.seed = 0
        self.amplify = amplify

    def noise1D(self, x):
        random.seed(f"{x}{self.seed}")
        v1 = random.random()*self.amplify
        random.seed(f"{x-1}{self.seed}")
        v2 = random.random()*self.amplify
        random.seed(f"{x+1}{self.seed}")
        v3 = random.random()*self.amplify
        return (v1+v2+v3)/3

    def noise2D(self, x, y):
        random.seed(f"{x}{y}{self.seed}")
        v1 = random.random()*self.amplify
        random.seed(f"{x+1}{y}{self.seed}")
        v2 = random.random()*self.amplify
        random.seed(f"{x}{y+1}{self.seed}")
        v3 = random.random()*self.amplify
        random.seed(f"{x+1}{y+1}{self.seed}")
        v4 = random.random()*self.amplify
        random.seed(f"{x-1}{y}{self.seed}")
        v5 = random.random()*self.amplify
        random.seed(f"{x}{y-1}{self.seed}")
        v6 = random.random()*self.amplify
        random.seed(f"{x-1}{y-1}{self.seed}")
        v7 = random.random()*self.amplify
        random.seed(f"{x+1}{y-1}{self.seed}")
        v8 = random.random()*self.amplify
        random.seed(f"{x-1}{y+1}{self.seed}")
        v9 = random.random()*self.amplify
        return (v1+v2+v3+v4+v5+v6+v7+v8+v9)/9

    def noise3D(self, x, y, z):
        pass
