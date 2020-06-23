# #   FUNCTION STRUCTURE
# def function-name (parameter,parameters):
#     statement 1
#     statement 2
    
#     return value_to_return



def celsius_to_fahrenheit(celsius_float):
    return celsius_float *1.8 +32
print("convert Celsius to Fahrenheit.")
print()
celsius_float = float(input ("Enter a celsius temp."))
fahrenheit_float = celsius_to_fahrenheit(celsius_float)
print(celsius_float, "converts to ",fahrenheit_float," Fahrenheit")
    #clswrk in slide 
# def get_digit(number,position):
#     """return digit at position in number,counting from right"""
#     return number//(10**position)%10

def get_vertex():
    x = float(input("   please enter x: "))
    y = float(input("   please enter y: "))
    return x,y

def get_triangle():
    print("First vertex")
    x1,y1 = get_vertex()
    print("second vertex")
    x2,y2 = get_vertex()
    print("Third vertex")
    x3,y3 = get_vertex()
    return x1,y1,x2,y2,x3,y3
    
    def side_length(X1,y1,x2,y2):
        """ return lenght of a side(Euclidean distance)"""
        return math.sqrt((X1-X2)**2 + (y1 - y2)**2))
    def claculate_area (x1,y1,x2,y2,x3,y3):
        """ return area using Heron"s formula"""
        
    