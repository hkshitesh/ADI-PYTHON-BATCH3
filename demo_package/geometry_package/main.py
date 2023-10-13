from demo_package.geometry_package.two_d import area, perimeter
from demo_package.geometry_package.three_d import volume, surface_area

l=5
b=4
h=2

ar=area.calculate_area(l,b)
per =perimeter.calculate_perimeter(l,b)
print("Area is :",ar)
print("Perimeter is : ",per)

vol = volume.calculate_volume(l,b,h)
sur = surface_area.calculate_surface_area(l,b,h)
print("Volume is :",vol)
print("Surface Area is :",sur)
