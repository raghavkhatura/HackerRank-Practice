#!/bin/python3

import math
import os
import random
import re
import sys



x=int(input(""))
if x%2==1:
    print("Weird")
if 2<=x<=5 and x%2==0:
    print("Not Weird")
if 6<=x<=20 and x%2==0:
    print("Weird")
if x>20 and x%2==0:
    print("Not Weird")
