from multiprocessing import RawValue
from turtle import RawPen
from unittest import result
import pbkdf2 as passhash
hash = passhash.crypt("Hacker")

enter = RawPen("Enter correct password:")

if passhash.crypt(enter, hash) == hash:
    print("good")
else:
    print("Incorect password")