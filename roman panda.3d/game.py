from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText

from map import Mapmanager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        
        self.land = Mapmanager()
        x,y,z = self.land.loadland("land.txt")
        self.hero = Hero((x//2,y//1,5),self.land)
        self.skybox()
    def skybox(self):
        self.sky = loader.loadModel('skybox/skybox.egg')
        self.sky.setScale(500)
        self.sky.setBin('background', 1)
        self.sky.setLightOff()
        self.sky.reparentTo(render)




game = Game()
game.run()
        