# Ins are supposed to be faster than Gets.
# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary

drinks = {"jabroni":"Patron Tequila",
    "school counselor":"Anything with Alcohol",
    "programmer":"Hipster Craft Beer",
    "bike gang member":"Moonshine",
    "politician":"Your tax dollars",
    "rapper":"Cristal"}
    
def get_drink_by_profession(param):
    key = param.lower()
    
    if key in drinks:
        return drinks[key]
    else:
        return "Beer"
