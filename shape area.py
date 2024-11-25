def shape_area(shape,dimension):
    if shape=='circle':
        return 3.14*(dimension**2)
    elif shape=='square':
        return dimension**2
    elif shape=='triangle':
        return 0.5*dimension[0]*dimension[1]
    else:
        return "Invalid Shape"
print(f"Circle: {shape_area('circle',2)}")
print(f"Square: {shape_area('square',5)}")
print(f"Triangle: {shape_area('triangle',(10,5))}")
print(f"Rectangle: {shape_area('rectangle',(10,8))}")