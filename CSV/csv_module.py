import csv

file_csv = open('../ MovieList.csv') # bila direkotri file ada di folder sebelumnya tulis '../' (sebelum nama file)
file_read = csv.reader(file_csv)
file = list(file_read)
print(file)

print(file[0][0])
print(file[0][1])
print(file[0][2])
print(file[0][3])