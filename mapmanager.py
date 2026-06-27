class Mapmanager():
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.colors = [(0.2, 0.2, 0.35, 1),(0.2, 0.5, 0.2, 1),(0.7, 0.2, 0.2, 1),(0.5, 0.3, 0.0, 1)]
        self.startNew()
    def startNew(self):
        self.land = render.attachNewNode("Land")
    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        return self.colors[len(self.colors) - 1]
    def addBlock(self, position):
        block = loader.loadModel(self.model)
        block.setTexture(loader.loadTexture(self.texture))
        block.setPos(position)
        block.setColor(self.getColor(int(position[2])))
        block.reparentTo(self.land)
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split()
                for z in line:
                    for z0 in range(int(z) + 1):
                        self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x, y
