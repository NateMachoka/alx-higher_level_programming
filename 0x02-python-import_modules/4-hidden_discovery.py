#!/usr/bin/python3
import importlib.util

if __name__ == '__main__':
    # Load the compiled module hidden_4.pyc
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get a list of all names defined in the module
    def_names = dir(hidden_4)

    for name in sorted(def_names):
        if not name.startswith('__'):
            print(name)
