# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a , b , c = 100,50,10
print(a,b,c)
#tupple it is same like List the only difference is that it uses '()' list uses '[]' tupple can also store multiple type value inside
# it can not be change
tuple =("ravi",12.8,45,"kumar","Kesharwani")
print(tuple[:])
tuple1 = ("shruti",26)
tuple1+tuple

"""
Dictionary 
    it is a collection which works in form of key value pair 
    it works like an associated array where no duplicate keys can be same
    its value can be save in curly braces '{}'and value can be retrieve using square bracket '[]'
    
"""

dictionary = {"Name":"Ravi","SirName":"Kesharwani","Age":26,"SirName":"Android"}
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary["Name"])