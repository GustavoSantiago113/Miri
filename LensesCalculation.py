def calculate_focal_length_distance(magnification, f2):
    magnification = abs(magnification)  # Ensure magnification is positive
    f1 = abs(f2) / magnification
    d = 1 / ((1 / f1) + (1 / f2))
    return f1, d

# Example usage
magnification = float(input("Enter the desired magnification: "))
f2 = float(input("Enter the focal length of the second lens: "))

f1, d = calculate_focal_length_distance(magnification, f2)
print("The focal length of the first lens should be:", f1)
print("The distance between the lenses should be:", d)