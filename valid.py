import json
with open('ccNasabah.json', 'r') as nasabah:
    output = json.load(nasabah)
print(type(output))

valid = []
invalid = []

valid = []
invalid = []
for data in output:
    nama, cc = data.items()
    n_cc = cc[1]
    if (n_cc[0] == '4') or (n_cc[0] == '5') or (n_cc[0] == '6') and len(n_cc) == 16:
        valid.append(data)
        for data1 in valid:
            nama, cc = data.items()
            index = valid.index(data1)
            n_cc = cc[1]
            if 'z' in n_cc:
                valid.pop(index)
                invalid.append(data) 
    else:
        invalid.append(data)
            
print(valid)
print('\n')
print(invalid)

with open('valid.json', 'w') as data_valid:
    json.dump(valid, data_valid)

with open('invalid.json', 'w') as data_invalid:
    json.dump(invalid, data_invalid)