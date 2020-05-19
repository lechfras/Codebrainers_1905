# creating a new dictionary
my_dict =dict({"Leszek": 44, "Ania": 40, "Adam": 45, "Magda": 38, "Kamil": 38})

# list out keys and values separately
key_list = list(my_dict.keys())
val_list = list(my_dict.values())

print(key_list[val_list.index(40)])
print(key_list[val_list.index(38)])

# one-liner
#print(list(my_dict.keys())[list(my_dict.values()).index(44)])

"""
def get_key(val):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"

print(get_key(40))
print(get_key(38))
"""
a=my_dict['Leszek']
b=my_dict['Ania']
print(a, b)