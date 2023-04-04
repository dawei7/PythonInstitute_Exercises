"""
Estimated time
10-20 minutes

Level of difficulty
Medium

Objectives
improving the student's skills in operating with special methods
Scenario
Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
to add an integer to a time interval object means to add seconds;
to subtract an integer from a time interval object means to remove seconds.
"""

class TimeInterval:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def check_type_time_interval(self, other):
        if type(other) != TimeInterval:
            raise TypeError("The second argument is neither an int nor an instance of TimeInterval")
    
    def check_type_int(self, other):
        return  type(other) == int

    def __add__(self, other):
                
        if self.check_type_int(other):
            other = TimeInterval(0,0,other)
        else:
            self.check_type_time_interval(other)
    
        remainder_minutes = 0
        remainder_hours = 0

        if self.seconds + other.seconds <= 60:
            self.seconds += other.seconds
        else:
            remainder_minutes = (self.seconds + other.seconds) // 60
            self.seconds = (self.seconds + other.seconds) % 60

        if self.minutes + remainder_minutes + other.minutes <= 60:
            self.minutes += remainder_minutes + other.minutes 
        else:
            remainder_hours = (self.minutes + remainder_minutes + other.minutes) // 60
            self.minutes = (self.minutes + remainder_minutes + other.minutes) % 60
        
        self.hours += remainder_hours + other.hours 

        return self
    
    def __sub__(self, other):

        if self.check_type_int(other):
            other = TimeInterval(0,0,other)
        else:
            self.check_type_time_interval(other)

        remainder_minutes = 0
        remainder_hours = 0

        if self.seconds - other.seconds >= 0:
            self.seconds -= other.seconds
        else:
            remainder_minutes = (self.seconds - other.seconds) // 60
            self.seconds = (self.seconds - other.seconds) % 60

        if self.minutes + remainder_minutes - other.minutes >= 0:
            self.minutes -= -remainder_minutes + other.minutes 
        else:
            remainder_hours = (self.minutes + remainder_minutes - other.minutes) // 60
            self.minutes = (self.minutes + remainder_minutes - other.minutes) % 60
        
        self.hours -= -remainder_hours + other.hours

        if self.hours <0:
            raise Exception("The time interval cannot be below zero")

        return self
    
    def __mul__(self,other):

        remainder_minutes = 0
        remainder_hours = 0

        if self.seconds * other <= 60:
            self.seconds *= other
        else:
            remainder_minutes = self.seconds * other // 60
            self.seconds = self.seconds * other % 60
        
        if (self.minutes + remainder_minutes) * other <= 60:
            self.minutes = (self.minutes + remainder_minutes) * other
        else:
            remainder_hours = (self.minutes + remainder_minutes) * other // 60
            self.minutes = (self.minutes + remainder_minutes) * other % 60
        
        self.hours = (self.hours + remainder_hours) * other

        return self

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"


interval1 = TimeInterval(20,20,30)
interval2 = TimeInterval(50,50,50)
print(interval1+interval2) # 71:11:20
# hello = "hello"
# print(interval1+hello) TypeError: The second argument is neither an int nor an instance of TimeInterval

print(interval1-interval2) # 20:20:30 Same as before

# print(interval1-interval2) # When trying again it fails because Exception: The time interval cannot be below zero

print(interval1*7) # 154:41:30

# Added methods
print(interval1+80) # 154:42:50
print(interval1-51) # 154:41:59

