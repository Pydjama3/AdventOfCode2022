class BettePrint:
    def __init__(self, init_printable=True):
        self.do_print = init_printable

    def print(self, *values, separator=None):
        if self.do_print:
            print(*values, sep=separator)
    
    def set_print(self, val):
        self.do_print = val

    def toggle_print(self):
        self.do_print = not self.do_print