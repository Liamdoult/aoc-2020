# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    f = f.read().splitlines()

def validate_passport(passport, cid_required=False):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    if cid_required is True:
        fields.append("cid")

    passport_fields = set(passport.keys())

    for field in fields: 
        if field not in passport_fields: return False

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
