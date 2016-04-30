'''
  Author Alumet 2015
  https://github.com/Alumet/Codingame
'''

import math


#set an anreal value for landing site
land_x2=land_y2=-1

for i in range(int(input())):

    land_x, land_y = [int(j) for j in input().split()]
    
    #test if two consecutive points have the same y coodinate
    if land_y==land_y2:
        target_x1=land_x2
        target_x2=land_x
        target_y=land_y
    
    land_x2,land_y2=land_x, land_y


#class to autopilot lander
class autopilot():
    
    #update all parameters
    def update_parameters(self, x, y, h_speed, v_speed, fuel):
        self.x=x
        self.y=y
        self.h_speed=h_speed
        self.v_speed=v_speed
        self.fuel=fuel
        self.rotate=0
        self.power=0
    
    #return the rotation and power values
    def update(self):
        
        if self.is_over_target()==False:
            if self.goes_opposit() or self.is_to_fast_H():
                self.rotate=self.angle_to_slow()
                self.power=4
            elif self.is_to_slow_H():
                self.rotate=self.angle_to_conter_grav()
                self.power=4
            else:
                self.rotate=0
                self.power=self.power_to_hover()
        else:
            if self.is_landing():
                self.rotate=0
                self.power=3
            elif self.has_safe_speed():
                self.rotate=0
                self.power=2
            else:
                self.rotate=self.angle_to_slow()
                self.power=4
        
        print(self.rotate,self.power)
    
    #is the lander to fast horizontaly?
    def is_to_fast_H(self):
        if abs(self.h_speed)>20*4:
            return True 
        else:
            return False
            
    #is the lander to slow horizontaly?      
    def is_to_slow_H(self):
        if abs(self.h_speed)<20*2:
            return True 
        else:
            return False
    
    #is the lander going the good way?
    def goes_opposit(self):
        if self.x<target_x1 and self.h_speed<0:
            return True
        elif self.x>target_x2 and self.h_speed>0:
            return True
        else:
            return False
    
    #return the good angle to slow down if to fast
    def angle_to_slow(self):
        speed=math.sqrt(self.h_speed**2+self.v_speed**2)+0.000001
        angle=math.degrees(math.asin(self.h_speed/speed))
        return int(angle)
    
    #return the angle to conteract gravity while aiming toward target
    def angle_to_conter_grav(self):
        angle = math.degrees(math.acos(3.711/4.0));
        if self.x < target_x2:
            return int(-angle)
        elif (target_x1 < self.x):
            return int(angle)
        else:
            return 0
    
    #is the lander over the landing zone?
    def is_over_target(self):
        if self.x > target_x1 and self.x < target_x2:
            return True
        else:
            return False
    
    #does the lander has a safe V and H speed?
    def has_safe_speed(self):
        if abs(self.h_speed)<=0 and abs(self.v_speed)<=35:
            return True
        else:
            return False
    
    #is the lander close to the ground?
    def is_landing(self):
        if self.y < target_y+30:
            return True
        else:
            return False
            
    #return the good power to hover
    def power_to_hover(self):
        if abs(self.v_speed)>0:
            return 4
        else:
            return 3
    

lander=autopilot()

# game loop
while 1:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    
     
    lander.update_parameters(x, y, h_speed, v_speed, fuel)
    lander.update()
    
