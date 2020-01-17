#!/usr/bin/python3
from Trace import Trace

try:
    with open('non-existent', 'r') as f:
        print("Should never execute this unless you created a file called 'non-existent'");
except Exception as e:
        tr = Trace()
        tr.Trace(e)
        tr.EndTrace()

