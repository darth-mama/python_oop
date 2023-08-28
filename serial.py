"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        '''Making a new generator with the 'start' and 'next' value the same'''
        self.start = start
        self.next = start

    def __repr__(self):
        '''Prints the outline of the class'''
        return ("Generates a new number, incremented by one, with an optional starting number\n"
            f"Serial number: start = {self.start}, next={self.next}")


    def generate(self):
        '''Generate the next serial number'''
        self.next += 1
        return self.next - 1

    def reset(self):
        '''Reset 'next' number to default 'start' number'''
        self.next = self.start
        return self.next
