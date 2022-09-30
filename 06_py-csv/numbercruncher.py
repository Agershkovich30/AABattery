import random

def readfile(f):
    with open(f,"r") as a:
        return a.read()

def split_by_last_comma(occupation):
    comma_index = occupation.rindex(",")
    splits = [occupation[:comma_index],float(occupation[comma_index+1:])]
    if splits[0][0] == "\"":
        splits[0]=splits[0][1:-1]
    return splits

def generate_occupation_dict(txt):
    occupations = txt.split("\n")[1:-1]
    occ_dict = {}
    for occupation in occupations:
        occ_list = split_by_last_comma(occupation)
        occ_dict[occ_list[0]] = occ_list[1]
    return occ_dict

def pick_random_occupation(occ_dict):
    total = occ_dict["Total"]
    occ_dict.pop("Total")
    num = random.random()*total
    for occ in occ_dict:
        num -= occ_dict[occ]
        if num < 0:
            return occ

occ_dict = generate_occupation_dict(readfile("occupations.csv"))
print(pick_random_occupation(occ_dict))
