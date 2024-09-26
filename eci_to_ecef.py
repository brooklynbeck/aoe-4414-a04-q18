# eci_to_ecef.py
#
# Usage: python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km
# Takes ecef coordinates and transforms them into sez coordinates
# Parameters:
# year
# month
# day
# hour
# minute
# second
# eci_x_km
# eci_y_km
# eci_z_km
# Output:
# Prints ecef x, y, and z coordinates
#
# Written by Brooklyn Beck
# Other contributors: None
#
# import Python modules
import math # math module
import sys # argv
# "constants"
W_E = 7.292115*10**(-5) #rad/sec

# initialize script arguments
year = float('nan')
month = float('nan')
day = float('nan')
hour = float('nan')
minute = float('nan')
second = float('nan')
eci_x_km = float('nan')
eci_y_km = float('nan')
eci_z_km = float('nan')

# parse script arguments
if len(sys.argv)==10:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
  eci_x_km = float(sys.argv[7])
  eci_y_km = float(sys.argv[8])
  eci_z_km = float(sys.argv[9])
else:
  print(\
  'Usage: '\
  'python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'\
  )
  exit()

# main script

jd = day - 32075 + 1461*(year+4800-(14-month)//12)//4 + 367*(month-2+(14-month)//12*12)//12 - 3*((year+4900-(14-month)//12)//100)//4
d_frac = (second + 60*(minute+60*hour))/86400
jd_frac = jd-0.5 + d_frac

t_ut1 = (jd_frac - 2451545.0)/36525.0
gmst_sec = 67310.54841 + (876600*60*60+8640184.812866)*t_ut1 + 0.093104*t_ut1**2 - 6.2*10**(-6)*t_ut1**3
gmst_rad = (gmst_sec%86400)*W_E

ecef_x_km = eci_x_km*math.cos(-1*gmst_rad) - eci_y_km*math.sin(-1*gmst_rad)
ecef_y_km = eci_x_km*math.sin(-1*gmst_rad) + eci_y_km*math.cos(-1*gmst_rad)
ecef_z_km = eci_z_km

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)