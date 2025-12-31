#!/usr/bin/python3
"""hello i am Shixi Ibrahimov"""

def write_file(filename="", text=""):
     with open(filename, "r", encoding="utf-8") as f:
          text += f.read()
          text = len(text)
