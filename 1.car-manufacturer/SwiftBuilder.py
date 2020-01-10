from Builder import Builder


class SwiftBuilder(Builder):

    car  = None

    def startBuild(self,car):
        self.car = car
        return self

   

    def setModel(self,model):
        self.car.model = model
        return self
        

    def buildBody(self):
        self.car.setBody("Hatback")
        return self

    def buildEngine(self):
        self.car.setEngine("1700 CC")
        return self

    def buildWheels(self):
        self.car.setWheels('21"')
        return self

    def buildFeatures(self):
        return self

    def buildOptionalFeatures(self):
        self.car.setFeatures("TV")
        self.car.setFeatures("Swift Car")
        return self

    def getCar(self):
        return self.car
