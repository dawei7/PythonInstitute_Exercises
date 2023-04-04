"""
Estimated time
20 minutes

Level of difficulty
Easy

Objectives
improving the student's skills in operating with static and class methods
Scenario
Create a class representing a luxury watch;
The class should allow you to hold a number of watches created in the watches_created class variable.
The number could be fetched using a class method named get_number_of_watches_created;
the class may allow you to create a watch with a dedicated engraving (text).
As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method),
as a regular __init__ method should not allow ordering engravings;
the regular __init__ method should only increase the value of the appropriate class variable;
The text intended to be engraved should follow some restrictions:

it should not be longer than 40 characters;
it should consist of alphanumerical characters, so no space characters are allowed;
if the text does not comply with restrictions, an exception should be raised;
before engraving the desired text, the text should be validated against restrictions using a dedicated static method.

Create a watch with no engraving
Create a watch with correct text for engraving
Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
After each watch is created, call class method to see if the counter variable was increased
"""

class LuxuryWatch:
    # Internal Class variable
    __watches_created = 0

    def __init__(self):
        LuxuryWatch.__watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created
    
    #Alternative Constructor
    @classmethod
    def create_with_engraving(cls,engraving):
        # Call static class to validate engraving
        cls.validate_engraving(engraving)
        # Calling standard constructor and creating an object
        _watch = cls()
        # As an addition to the standard constructor add a new object variable engraving  
        _watch.engraving = engraving
        #return created object
        return _watch
    
    @staticmethod
    def validate_engraving(engraving:str):
        try:
            if len(engraving) > 40 or not engraving.isalnum():
                raise Exception("Only alphanmetic characters are allowed; Moreover only a maximum length of 40 characters is possible.")
        except Exception as e:
            print(e)


# Create a watch with no engraving
watch_1 = LuxuryWatch()
print(LuxuryWatch.get_number_of_watches_created()) # 1
# Create a watch with correct text for engraving
watch_2 = LuxuryWatch.create_with_engraving("HelloLuxuryWatch") # 2
print(LuxuryWatch.get_number_of_watches_created())
# Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
watch_3 = LuxuryWatch.create_with_engraving("foo@baz.com") # Only alphanmetic characters are allowed; Moreover only a maximum length of 40 characters is possible.
print(LuxuryWatch.get_number_of_watches_created()) # 3