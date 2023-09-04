import dis
import types

def magic_calculation(a, b):
    def dummy():
        return 98 ** a + b
