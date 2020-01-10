from Director import Director
from CiazBuilder import CiazBuilder
from SwiftBuilder import SwiftBuilder

if __name__ == '__main__':

    director = Director()
    ciazBuilder = CiazBuilder()
    swiftBuilder = SwiftBuilder()

    director.setBuilder(ciazBuilder)
    ciazGl = director.buildGLModel()
    print("Ciaz")
    ciazGl.showSpecification()

    director.setBuilder(swiftBuilder)
    swiftGl = director.buildGLXModel()
    print("Swift")
    swiftGl.showSpecification()
    