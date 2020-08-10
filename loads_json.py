import json

# meload data json
with open('states.json') as f:
    data = json.load(f)

# memprint object data json
for state in data['states']:
    print(state)

for state in data['states']:
    print(state['name'])

# merubah data dan upload ke teks json
for hapus in data['states']:
    del hapus['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)