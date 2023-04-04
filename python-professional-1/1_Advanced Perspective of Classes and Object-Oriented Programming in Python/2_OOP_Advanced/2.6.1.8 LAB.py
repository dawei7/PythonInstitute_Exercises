"""
Estimated time
40 minutes

Level of difficulty
Medium

Objectives
Creation of abstract classes and abstract methods;
multiple inheritance of abstract classes;
overriding abstract methods;
delivering multiple child classes.
Scenario
You are about to create a multifunction device (MFD) that can scan and print documents;
the system consists of a scanner and a printer;
your task is to create blueprints for it and deliver the implementations;
create an abstract class representing a scanner that enforces the following methods:
scan_document – returns a string indicating that the document has been scanned;
get_scanner_status – returns information about the scanner (max. resolution, serial number)
Create an abstract class representing a printer that enforces the following methods:
print_document – returns a string indicating that the document has been printed;
get_printer_status – returns information about the printer (max. resolution, serial number)
Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
MFD2 – should be a medium-priced device allowing additional operations like printing operation history,
and the resolution is better than the lower-priced device;
MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.
Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.
"""

import abc # Module for abstrat classes

class Scanner(abc.ABC):

    @abc.abstractmethod
    def scan_document():
        pass

    @abc.abstractmethod
    def get_scanner_status():
        pass

class Printer(abc.ABC):

    @abc.abstractmethod
    def print_document():
        pass

    @abc.abstractmethod
    def get_printer_status():
        pass


class MFD1(Scanner,Printer): # Inherits from 2 abstract classes Scanner & Printer
    
    __serial_number = 0
    __max_resolution = 100

    def __init__(self):
        MFD1.__serial_number += 1
        self._serial_number = MFD1.__serial_number # Every created MFD gets a uniqze incremented serial number

    def scan_document(self):
        print(f"Scanned 1 page") 

    @classmethod
    def get_scanner_status(cls):
        print(f"Scanner Max_Resolution: {cls.__max_resolution}")
        print(f"Scanner Serial Number: MFD-1-{cls.__serial_number}")

    def print_document(self):
        print("Printed 1 page") 

    @classmethod
    def get_printer_status(cls):
        print(f"Printer Max_Resolution: {cls.__max_resolution}")
        print(f"Scanner Serial Number: MFD-1-{cls.__serial_number}")


class MFD2(MFD1):
    
    __serial_number = 0
    __max_resolution = 200

    def __init__(self):
        MFD2.__serial_number += 1
        self._serial_number = MFD2.__serial_number
        self.__printed_pages = 0

    @classmethod
    def get_scanner_status(cls):
        print(f"Scanner Max_Resolution: {cls.__max_resolution}")
        print(f"Scanner Serial Number: MFD-2-{cls.__serial_number}")

    def print_document(self):
        super().print_document()
        self.__printed_pages +=1

    @classmethod
    def get_printer_status(cls):
        print(f"Printer Max_Resolution: {cls.__max_resolution}")
        print(f"Scanner Serial Number: MFD-2-{cls.__serial_number}")

    def printing_operation_history(self):
        print(f"You have printed in total {self.__printed_pages} pages")


class MFD3(MFD2):
    
    __serial_number = 0
    __max_resolution = 300

    def __init__(self):
        super().__init__()
        MFD3.__serial_number += 1
        self._serial_number = MFD3.__serial_number

    @classmethod
    def get_scanner_status(cls):
        print(f"Scanner Max_Resolution: {cls.__max_resolution}")
        print(f"Scanner Serial Number: MFD-3-{cls.__serial_number}")

    @classmethod
    def get_printer_status(cls):
        print(f"Printer Max_Resolution: {cls.__max_resolution}")
        print(f"Scanner Serial Number: MFD-3-{cls.__serial_number}")

    def send_fax(self):
        print("You have successfully sent a fax")


# MDF 1
print("-----MDF 1-----")
mdf1_1 = MFD1()
mdf1_1.scan_document()
mdf1_1.get_scanner_status()
mdf1_1.print_document()
mdf1_1.get_scanner_status()

mdf1_2 = MFD1()
mdf1_2.scan_document()
mdf1_2.get_scanner_status()
mdf1_2.print_document()
mdf1_2.get_scanner_status()

mdf1_3 = MFD1()
mdf1_3.scan_document()
mdf1_3.get_scanner_status()
mdf1_3.print_document()
mdf1_3.get_scanner_status()

# MDF 2
print("-----MDF 2-----")
mdf2_1 = MFD2()
mdf2_1.scan_document()
mdf2_1.get_scanner_status()
mdf2_1.print_document()
mdf2_1.get_scanner_status()
mdf2_1.printing_operation_history()

mdf2_2 = MFD2()
mdf2_2.scan_document()
mdf2_2.get_scanner_status()
mdf2_2.print_document()
mdf2_2.print_document()
mdf2_2.get_scanner_status()
mdf2_2.printing_operation_history()

mdf2_3 = MFD2()
mdf2_3.scan_document()
mdf2_3.get_scanner_status()
mdf2_3.print_document()
mdf2_3.print_document()
mdf2_3.print_document()
mdf2_3.get_scanner_status()
mdf2_3.printing_operation_history()


# MDF 3
print("-----MDF 3-----")
mdf3_1 = MFD3()
mdf3_1.scan_document()
mdf3_1.get_scanner_status()
mdf3_1.print_document()
mdf3_1.get_scanner_status()
mdf3_1.printing_operation_history()
mdf3_1.send_fax()

mdf3_2 = MFD3()
mdf3_2.scan_document()
mdf3_2.get_scanner_status()
mdf3_2.print_document()
mdf3_2.print_document()
mdf3_2.get_scanner_status()
mdf3_2.printing_operation_history()
mdf3_2.send_fax()

mdf3_3 = MFD3()
mdf3_3.scan_document()
mdf3_3.get_scanner_status()
mdf3_3.print_document()
mdf3_3.print_document()
mdf3_3.print_document()
mdf3_3.get_scanner_status()
mdf3_3.printing_operation_history()
mdf3_3.send_fax()
