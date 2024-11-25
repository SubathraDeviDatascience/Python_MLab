def temperature_converter(scale,temperature):
    if scale=='C_to_F':
        return (temperature*5/9)+32
    elif scale=='F_to_C':
        return (temperature-32)*9/5
    else:
        return "Invalid Temperature"
print(f"C to F : {temperature_converter('C_to_F',10)}")
print(f"F to C : {temperature_converter('F_to_C',32)}")
print(f"E to C : {temperature_converter('E_to_C',10)}")