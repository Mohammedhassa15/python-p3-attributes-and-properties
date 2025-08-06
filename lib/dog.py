#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, breed="Human",name="fido"):
        if (not isinstance(name,str) or len(name) < 1 or len(name) > 25):
            print("Name must be string between 1 and 25 characters.")
            return
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            
        self.breed=breed
        self.name=name
