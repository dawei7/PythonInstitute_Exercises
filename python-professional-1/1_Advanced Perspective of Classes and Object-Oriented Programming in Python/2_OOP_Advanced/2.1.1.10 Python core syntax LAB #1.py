"""
Estimated time
30-60 minutes

Level of difficulty
Medium

Objectives
improving the student's skills in operating with special methods
Scenario
Create a class representing a time interval;
the class should implement its own method for addition, subtraction on time interval class objects;
the class should implement its own method for multiplication of time interval class objects by an integer-type value;
the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
check the argument type, and in case of a mismatch, raise a TypeError exception.
"""

class TimeInterval:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def check_type(self, other):
        if type(other) != TimeInterval:
            raise TypeError("The second argument is not an instance of TimeInterval")

    def __add__(self, other):
        self.check_type(other)
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
        self.check_type(other)
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
# print(interval1+hello) TypeError: The second argument is not an instance of TimeInterval

print(interval1-interval2) # 20:20:30 Same as before

# print(interval1-interval2) # When trying again it fails because Exception: The time interval cannot be below zero

print(interval1*7) # 154:41:30


