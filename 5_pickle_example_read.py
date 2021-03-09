import pickle

infile = open("names_pickle_file_write.dat", "rb")

names = pickle.load(infile)

print(type(names))

print(names)

for n in range(2):
    name = input("Add a name to the list: ")
    names.append(name)

outfile = open("names_pickle_file_write.dat", "wb")
pickle.dump(names, outfile)

print(names)
