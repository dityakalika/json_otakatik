import json

pertama = '''
{
    "data" : [
    {
        "nama": "Ditya Kalika Widyadiyanti",
        "umur": 20,
        "asal": "Jakarta"
    },
    {
        "nama": "Dinda Kalista Padmahati",
        "umur": 17,
        "asal": "Sumedang"
    }
]
}
'''
# merubah kedalam bentuk json
# JSON string selalu dalma double quote ""
datajson =json.loads(pertama)
print(datajson)
print(type(datajson))

# mengambil data json
for person in datajson['data']:
    print(person['nama'])

for age in datajson['data']:
    print(age['umur'])

for city in datajson['data']:
    print(city['asal'])

# menghapus data pada json

for hapus in datajson['data']:
    del hapus['asal']

# merubah python value menjadi JSON format ('' -> "")
new_string = json.dumps(datajson)
print(new_string)