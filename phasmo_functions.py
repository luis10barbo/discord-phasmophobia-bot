import json
import random
import phasmo_functions
from useful_functions import get_random_list_value

def open_names():
    with open("names.json", "r") as file:
        return json.load(file)

possible_names = open_names()

def generate_partial_osu(first_name:str="", second_name:str=""):

    names = possible_names["osu_nicknames"]
    surnames = possible_names["surnames"]
    
    if first_name == "":
        first_name = get_random_list_value(names)
    if second_name == "":
        second_name = get_random_list_value(surnames)
        
    name = f"{first_name} {second_name}"
    
    return name, None

def generate_full_phasmo(first_name:str="", second_name:str=""):

    names = possible_names["names"]
    surnames = possible_names["surnames"]
    
    if first_name == "":
        first_name = get_random_list_value(names)
    if second_name == "":
        second_name = get_random_list_value(surnames)
    
    name = f"{first_name} {second_name}"
    
    return name, None

def osu_roll(max_number:str="100"):
    if max_number.isnumeric() == False:
        return None, "**max_number** isn't a number!"
    
    max_number = int(max_number)
    if max_number < 1:
        return None, "**max_number** should not be smaller than 1!"
    return random.randint(1, max_number), None