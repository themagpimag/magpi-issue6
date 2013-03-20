file_object = open('load.txt','r')
raw_data = file_object.readlines()
file_object.close()

ages = {}

for line in raw_data:
    name_and_age = line.split(':')
    name = name_and_age[0]
    age = int(name_and_age[1])
    ages[name]=age

print 'Dictionary loaded.\n\n'

while True:
    lookup = raw_input('Enter name to look up (exit to quit): ')
    if lookup == 'exit':
        break
    elif lookup in ages:
        print lookup+'\'s age is', ages[lookup]
    else:
        print 'Couldn\'t find', lookup, 'in the dictionary'
