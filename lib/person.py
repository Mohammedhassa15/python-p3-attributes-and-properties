#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Guido", job="sales"):
        if (not isinstance(name, str)) or len(name)<1 or len(name)>25:
           print("Name must be string between 1 and 25 characters.")
           return
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        self.job=job
        name=name.title()
        self.name=name
        

