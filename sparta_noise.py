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
        v = []
        random.seed(f"{x}{y}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y+1}{self.seed}")
        v.append(random.random()*self.amplify)
        total = 0
        for i in v:
            total += v
        return total/len(v)

    def noise3D(self, x, y, z):
        v = []
        random.seed(f"{x}{y}{z}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y}{z}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y+1}{z}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y}{z+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y}{z}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y-1}{z}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y}{z-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y+1}{z+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y-1}{z-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y-1}{z-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y+1}{z-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y-1}{z+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y+1}{z+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y-1}{z+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y+1}{z-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y+1}{z+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y+1}{z-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y-1}{z+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x}{y-1}{z-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y+1}{z}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y-1}{z}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y+1}{z}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y-1}{z}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y}{z+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y}{z+1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x+1}{y}{z-1}{self.seed}")
        v.append(random.random()*self.amplify)
        random.seed(f"{x-1}{y}{z-1}{self.seed}")
        v.append(random.random()*self.amplify)
        total = 0
        for i in v:
            total += v
        return total/len(v)
"""
Coming up next...
class PerlinNoise():
"""
