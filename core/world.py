class World:
    #dentro de textures debe tener la representacion visual del bloque
    textures=[]
    #secciones de bloques (chunks)
    bloques=[]
    x=0
    y=0
    loadSize=16
    def __init__(self,textures,x,y,loadsize=16):
        self.textures.extend(textures)
        self.x=x
        self.y=y
    def load():
        print("")
    def updateLoaded():
        load()