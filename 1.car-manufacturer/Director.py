from Builder import Builder
from Car import Car
class Director:
    builder = None

    def setBuilder(self,builder):
        self.builder = builder

    def buildGLModel(self):
        return self.builder.startBuild(Car()).setModel("GL").buildBody().buildEngine().buildWheels().buildFeatures().getCar()

    def buildGLXModel(self):
        return self.builder.startBuild(Car()).setModel("GLX").buildBody().buildEngine().buildWheels().buildFeatures().buildOptionalFeatures().getCar()