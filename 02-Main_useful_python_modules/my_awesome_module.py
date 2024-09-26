def talk():
    '''
    Description: Print a message at the screen 
    '''
    print('Hello, What do you want me to do?')

    return

def deg_to_rad_2output(angle):
    '''
    Description: Function that converts an angle from deg to radian
    
    Parameters: 
    angle (float): input value in degree
    
    Output: 
    angle, angle_rad (tuple). 
        angle (float) input value 
        angle_rad (float) angle in radians
    '''
    pi = 3.14159 
    angle_rad = pi * angle / 180 
    return angle, angle_rad

def print_pi():
    '''
    Description: print value of pi with 5 digits
    '''
    print('pi=', 3.14159)
