"""
Estimated time
20 minutes

Level of difficulty
Easy

Objectives
improving the student's skills in operating with multiple inheritance;
pointing out the nature of multiple inheritance problems.
Scenario
Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and sending via fax.
The methods are delivered by the following classes:
scan(), delivered by the Scanner class;
print(), delivered by the Printer class;
send() and print(), delivered by the Fax class.
Each method should print a message indicating its purpose and origin, like:
'print() method from Printer class'
'send() method from Fax class'
create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
on each object call the methods: scan(), print(), send();
observe the output differences. Was the Printer class utilized each time?
"""

class Scanner():
    def __init__(self):
        pass
    def scan(self):
        print("scan(), delivered by the Scanner class")

class Printer():
    def __init__(self):
        pass
    def print(self):
        print("print(), delivered by the Printer class")

class Fax():
    def __init__(self):
        pass

    def send(self):
        print("send(), delivered by the Fax class")

    def print(self):
        print("print(), delivered by the Fax class")


# create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
class MDF_SPF(Scanner,Printer,Fax):
    pass

# create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
class MDF_SFP(Scanner,Fax,Printer):
    pass

# on each object call the methods: scan(), print(), send();
MDF_SPF_1 = MDF_SPF()
MDF_SPF_1.scan() # scan(), delivered by the Scanner class
MDF_SPF_1.print() # print(), delivered by the Printer class
MDF_SPF_1.send() # send(), delivered by the Fax class

MDF_SFP_1 = MDF_SFP()
MDF_SFP_1.scan() #scan(), delivered by the Scanner class
MDF_SFP_1.print() #print(), delivered by the Fax class
MDF_SFP_1.send() #send(), delivered by the Fax class

# observe the output differences. Was the Printer class utilized each time?
"""
Instance MDF_SFP_1 did not call method from Printer class, because accoding to MRO — Method Resolution Order, methods are inherited from classes bottom to top and left to right.
The class Fax has already a print() method and is more left than the class Printer in class MDF_SFP().
"""
