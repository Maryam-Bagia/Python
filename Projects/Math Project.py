# This is a program to find volume, area, perimiter etc.

import math
pi = (22/7)

print("Welcome to my project.")

print("1.2D Shape")
print("2.3D Shape")

choice = input("Enter your choice number:")

# 2D Shapes
if(choice == "1"):
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")
    shape = input("Enter your shape in lowercase :")
   # Square
    if(shape == "square"):
        print("Perimeter")
        print("Area")
        mes = input("What do you want to find? ")
        # Perimeter
        if(mes == "perimeter"):
           length = int(input("Enter length of square :"))
           perimeter = 4*length
           print("Perimeter of given square = " , perimeter)
        # Area  
        elif(mes == "area"):
           length = int(input("Enter length of square :"))
           area = length*length  
           print("Area of given square = " , area)
        else:
           print("Invalid choice.")
   # Rectangle     
    elif(shape == "rectangle"):
        print("Perimeter")
        print("Area")
        mes = input("What do you want to find? ")
        # Perimiter
        if(mes == "perimeter"):
           length = int(input("Enter length of rectangle :"))
           breadth = int(input("Enter breadth of rectangle :"))
           perimeter = 2*(length+breadth)
           print("Perimiter of given rectangle = " , perimeter)
         # Area  
        elif(mes == "area"):
           length = int(input("Enter length of rectangle :"))
           breadth = int(input("Enter breadth of rectangle :"))
           area = length*breadth  
           print("Area of given rectangle = " , area)
        else:
           print("Invalid choice.")
   # Triangle
    elif(shape == "triangle"):
        print("Perimiter")
        print("Area")
        mes = input("What do you want to find? ")
        # Perimiter
        if(mes == "perimiter"):
           a = int(input("Enter first side of triangle :"))
           b = int(input("Enter second side of triangle :"))
           c = int(input("Enter third side of triangle :"))
           perimeter = a+b+c
           print("Perimiter of given triangle = " , perimeter)
        # Area  
        elif(mes == "area"):
           a = int(input("Enter first side of triangle :"))
           b = int(input("Enter second side of triangle :"))
           c = int(input("Enter third side of triangle :"))
           s = (a+b+c)/2
           area = math.sqrt(s*(s-a)*(s-b)*(s-c))
           print("Area of given triangle = " , area)
        else:
           print("Invalid choice.")
   # Circle
    elif(shape == "circle"):
        print("Circumference")
        print("Area")
        mes = input("What do you want to find? ")
        # Circumference
        if(mes == "circumference"):
           r = int(input("Enter radius of circle :"))
           circumference = 2*pi*r
           print("Circumference of given circle = ",circumference)
        # Area  
        elif(mes == "area"):
           r = int(input("Enter radius of circle :"))
           area = pi*r*r
           print("Area of given circle = ",area)
    else:
       print("Invalid choice.")  
# 3D Shapes                          
elif(choice == "2"):
    print("1.Cube")
    print("2.Cuboid")
    print("3.Cone")
    print("4.Sphere")
    print("5.Cylinder")
    shape = input("Enter your shape in lowercase :")
   # Cube
    if(shape == "cube"):
        print("Surface area")
        print("Volume")
        mes = input("What do you want to find? ")
        # Surface area
        if(mes == "surface area"):
           length = int(input("Enter length of Cube :"))
           SurfaceArea = 6*length*length
           print("Surface area of given Cube is = " , SurfaceArea)
        # Volume 
        elif(mes == "volume"):
           length = int(input("Enter length of Cube :"))
           volume = length*length*length  
           print("Volume of given Cube is = " , volume)
        else:
           print("Invalid choice.")
   # Cuboid
    elif(shape == "cuboid"):
        print("Surface area")
        print("Volume")
        mes = input("What do you want to find? ")
        # Surface area
        if(mes == "surface area"):
           length = int(input("Enter length of cuboid :"))
           breadth = int(input("Enter breadth of cuboid :"))
           height = int(input("Enter height of cuboid :"))
           SurfaceArea = 2*((length*breadth)+(breadth*height)+(height*length))
           print("Surface area of given cuboid = " , SurfaceArea)  
         # Volume 
        elif(mes == "volume"):
           length = int(input("Enter length of cuboid :"))
           breadth = int(input("Enter breadth of cuboid :"))
           height = int(input("Enter height of cuboid :"))
           volume = length*breadth*height 
           print("Volume of given cuboid = " , volume)
        else:
           print("Invalid choice.")
   # Cone
    elif(shape == "cone"):
        print("Curved surface area")
        print("Total surface area") 
        print("Volume") 
        mes = input("What do you want to find? ") 
        # Curved surface area
        if(mes == "curved surface area"):
           r = int(input("Enter radius of base of cone :"))
           l = int(input("Enter slant of cone :"))
           csa = pi*r*l 
           print("Curved surface area of given cone = " , csa)
        # Total surface area   
        elif(mes == "total surface area"):
             r = int(input("Enter radius of base of cone :"))
             l = int(input("Enter slant of cone :"))
             tsa = pi*r*(l+r)
             print("Total surface area of given cone = ", tsa) 
        # Volume    
        elif(mes == "volume"):
             r = int(input("Enter radius of base of cone :")) 
             h = int(input("Enter height of cone :"))    
             volume = (1/3)*pi*r*r*h   
             print("Volume of given cone = ", volume)
        else:
           print("Invalid choice.")     
   # Sphere
    elif(shape == "sphere"):  
        print("Curved surface area")
        print("Volume")
        mes = input("What do you want to find? ")
        # Curved surface area
        if(mes == "curved surface area"):
           r = int(input("Enter radius of sphere :"))
           csa = 4*pi*r*r
           print("Curved surface area of given sphere = ", csa)
        # Volume
        elif(mes == "volume"):
            r = int(input("Enter radius of sphere :"))
            volume = (4/3)*pi*r*r*r
            print("Volume of given sphere = ", volume)
        else:
           print("Invalid choice.")
   # Cylinder        
    elif(shape == "cylinder"):
        print("Curved surface area")      
        print("Total surface area")
        print("Volume")
        mes = input("What do you want to find? ")
        # Curved surface area
        if(mes == "curved surface area"):
           r = int(input("Enter radius of cylinder :"))
           h = int(input("Enter height of cylinder :")) 
           csa = 2*pi*r*h
           print("Curved surface area of given cylinder = ", csa)    
        # Total surface area
        elif(mes == "total surface area"):
           r = int(input("Enter radius of cylinder :"))
           h = int(input("Enter height of cylinder :"))
           tsa = 2*pi*r*(h+r)  
           print("Total surface area of cylinder = ", tsa)
        # Volume
        elif(mes == "volume"):  
           r = int(input("Enter radius of cylinder :"))
           h = int(input("Enter height of cylinder :"))
           volume = pi*r*r*h
           print("Volume of given cylinder = ", volume)
        else:
           print("Invalid choice.")        
else:
    print("Invalid choice.")

print("Thank you for using it.")
print("                                                             Presented by - Maryam Bagia")