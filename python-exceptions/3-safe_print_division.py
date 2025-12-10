#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = ({} / {}).format(a, b)
    except ZeroDivisionError:
        return None
    finally:
        print("Operation attempted")
    return result