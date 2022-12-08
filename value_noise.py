import random

def value_noise2D(x, y, seed):
    random.seed(str(x)+str(y)+str(seed))
    v1 = random.random()
    random.seed(str(x-1)+str(y-1)+str(seed))
    v2 = random.random()
    random.seed(str(x+1)+str(y+1)+str(seed))
    v3 = random.random()
    random.seed(str(x+1)+str(y-1)+str(seed))
    v4 = random.random()
    random.seed(str(x-1)+str(y+1)+str(seed))
    v5 = random.random()
    random.seed(str(x-1)+str(y)+str(seed))
    v6 = random.random()
    random.seed(str(x+1)+str(y)+str(seed))
    v7 = random.random()
    random.seed(str(x)+str(y-1)+str(seed))
    v8 = random.random()
    random.seed(str(x)+str(y+1)+str(seed))
    v9 = random.random()
    return (v1+v2+v3+v4+v5+v6+v7+v8+v9)/9 # Returns the average of all the values surrounding the given x, y coordinates
