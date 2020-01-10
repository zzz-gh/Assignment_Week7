

class Car:
    model = ''
    wheels = []
    body = None
    engine = None
    features = []

    

    def showSpecification(self):
        print(
            f"Model  is {self.model} \n"
            f"Body  is {self.body} \n"
            f"Engine  is {self.engine} \n"
        )

        print("Features :\n")
        # print(self.features)
        for feature in self.features:
            print(feature)
   
    def setBody(self,body):
        self.body = body

    def setEngine(self,engine):
        self.engine = engine

    def setWheels(self,wheel):
        i = 0
        while i<4:
            self.wheels.append(wheel)
            i +=1

    def setFeatures(self,feature):
        self.features.append(feature)



    