"""
Estimated time
15-30 minutes

Level of difficulty
Medium

Objectives
Improving the student's skills in creating decorators and operating with them.
Scenario
Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
Apply your decorator to those functions to ensure that the time of the function executions can be monitored.
"""

from datetime import datetime

def track_timestamp():
    def wrapper(function):
        def internal_wrapper(*args):
            print("*"*30)
            print(f"Current timestamp: {datetime.now().strftime('%Y-%m-%d, %H:%M:%S')}")
            print("*"*30)
            print(function(*args))
        return internal_wrapper
    return wrapper

@track_timestamp()
def add_nums(*args):
    result = 0
    for num in args:
        result+=num
    return result
    
@track_timestamp()
def subtract_nums(*args):
    result = 0
    for num in args:
        result-=num
    return result

add_nums(5,6,7)

subtract_nums(5,6,7)