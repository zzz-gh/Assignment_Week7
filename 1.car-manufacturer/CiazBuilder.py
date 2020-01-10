from Builder import Builder


class CiazBuilder(Builder):

    car  = None

    def startBuild(self,car):
        self.car = car
        return self

    print("CiazGLX") 

    def setModel(self,model):
        self.car.model = model
        return self
        

    def buildBody(self):
        self.car.setBody("Salon")
        return self

    def buildEngine(self):
        self.car.setEngine("1400 CC")
        return self

    def buildWheels(self):
        self.car.setWheels('17"')
        return self

    def buildFeatures(self):
        return self

    def buildOptionalFeatures(self):
        self.car.setFeatures("TV")
        self.car.setFeatures("Cruiz Car")
        return self

    def getCar(self):
        return self.car
