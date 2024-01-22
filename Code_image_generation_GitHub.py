#*************+
#Image-based vulnerability detection under backdoor attack
#
#This code is used in this paper to generate images from code samples
#
#Lorena González-Manzano and Joaquin Garcia-Alfaro 
#*********************************************+

ByteArray = bytearray(str(CODESAMPLE),'utf-8')
        
flatNumpyArray = numpy.array(ByteArray)
size=int(sqrt(len(flatNumpyArray)))

reducedflatNumpyArray=flatNumpyArray[:size*size]

grayImage = reducedflatNumpyArray.reshape(size, size)