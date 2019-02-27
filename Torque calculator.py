import math


print("please use: T, F, d, or angle")
s = str(input("what would you like to solve for: "))

if s == "T":
  F = float(input("Force: "))
  d = float(input("distance: "))
  angle = int(input("angle in degrees: "))
  #T = int(input("Torque in units of force*distance units"))
  #angle = (angle * 180)/math.pi
  angle = (angle * math.pi)/180
  angle = math.sin(angle)
  T = F*d* angle
  print(T)
  
if s == "F":
  d = float(input("distance: "))
  angle = float(input("angle in degrees: "))
  T = float(input("Torque in units of force*distance units"))
  angle = (angle * math.pi)/180
  angle = math.sin(angle)
  F = T/(d*angle)
  print(F)
  
if s == "d":
    F = float(input("Force: "))
    angle = int(input("angle in degrees: "))
    T = float(input("Torque in units of force*distance units: "))
    angle = (angle * math.pi)/180
    angle = math.sin(angle)
    d = T/(F*angle)
    print(d)
  
if s == "angle":
    T = float(input("Torque in units of force*distance units: "))
    F = float(input("Force: "))
    d = float(input("distance: "))
    angle =T/(F*d)
    angle = math.asin(angle)
    angle = (angle * 180)/math.pi
    print(angle)
  
  
  
