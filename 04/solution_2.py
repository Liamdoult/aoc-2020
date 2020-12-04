# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

def validate_byr(value):
    try:
        value = int(value)
    except: return False
    return 1920 <= value <= 2002

def validate_iyr(value):
    try:
        value = int(value)
    except: return False
    return 2010 <= value <= 2020

def validate_eyr(value):
    try:
        value = int(value)
    except: return False
    return 2020 <= value <= 2030

def validate_hgt(value):
    if len(value) < 4: return False
    metric = value[-2:]
    try:
        value = int(value[:-2])
    except: return False
    if metric == "cm":
        return 150 <= value <= 193 
    if metric == "in":
        return 59 <= value <= 76 
    return False

def validate_hcl(value):
    if len(value) != 7: return False
    if value[0] != "#": return False
    valid = set("0123456789abcdef")
    for l in value[1:]:
        if l not in valid: return False
    return True

def validate_ecl(value):
    valid = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    return value in valid

def validate_pid(value):
    if len(value) != 9: return False
    try:
        value = int(value)
    except: return False
    return True

def validate_passport(passport, cid_required=False):
    fields = [
        ("byr", validate_byr), 
        ("iyr", validate_iyr),
        ("eyr", validate_eyr),
        ("hgt", validate_hgt),
        ("hcl", validate_hcl), 
        ("ecl", validate_ecl),
        ("pid", validate_pid),
    ]

    passport_fields = set(passport.keys())

    for field, validator in fields: 
        if field not in passport_fields: return False
        if not validator(passport[field]): return False

    return True


def get_passports(input):
    passport = {}
    for line in input:
        if not line or line == "":
            yield passport
            passport ={}
        else:
            for k,v in map(lambda x: x.split(":"), line.split(" ")):
                passport[k] = v
    yield passport
    return None 


passports = list(get_passports(f))
print(sum(map(lambda x: validate_passport(x), passports)))
