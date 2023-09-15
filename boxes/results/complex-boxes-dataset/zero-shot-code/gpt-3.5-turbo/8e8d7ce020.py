box = {
    0: ['wire'],
    1: ['perfume', 'toaster'],
    2: ['microscope'],
    3: ['belt'],
    4: ['swimsuit', 'rocket', 'puzzle', 'tie'],
    5: ['telescope', 'grass', 'spoon', 'starfish', 'glove'],
    6: ['book'],
    7: ['comet', 'guitar', 'cat', 'tiger'],
    8: [],
    9: ['comb', 'toy', 'pen'],
    10: ['scissors', 'coral'],
    11: [],
    12: ['butterfly']
}

# Replace the cat with the beach in Box 7
box[7].remove('cat')
box[7].append('beach')

# Move the pen from Box 9 to Box 0
box[0].append('pen')
box[9].remove('pen')

# Put the horn and the telescope and the glasses into Box 6
box[6].extend(['horn', 'telescope', 'glasses'])

# Replace the pen and the wire with the jungle and the boot in Box 0
box[0].remove('pen')
box[0].remove('wire')
box[0].extend(['jungle', 'boot'])

# Put the telescope and the planet into Box 4
box[4].extend(['telescope', 'planet'])

# Move the perfume from Box 1 to Box 3
box[3].append('perfume')
box[1].remove('perfume')

# Put the speaker and the glasses into Box 1
box[1].extend(['speaker', 'glasses'])

# Move the microscope from Box 2 to Box 11
box[11].append('microscope')
box[2].remove('microscope')

# Move the toaster and the glasses and the speaker from Box 1 to Box 8
box[8].extend(['toaster', 'glasses', 'speaker'])
box[1].remove('toaster')
box[1].remove('glasses')
box[1].remove('speaker')

# Put the tape into Box 7
box[7].append('tape')

# Move the comb and the toy from Box 9 to Box 1
box[1].extend(['comb', 'toy'])
box[9].remove('comb')
box[9].remove('toy')

# Swap the scissors in Box 10 with the perfume in Box 3
box[3].remove('perfume')
box[10].remove('scissors')
box[3].append('scissors')
box[10].append('perfume')

# Put the soap into Box 4
box[4].append('soap')

# Swap the toy in Box 1 with the glasses in Box 6
box[1].remove('toy')
box[6].remove('glasses')
box[1].append('glasses')
box[6].append('toy')

# Remove the jungle and the boot from Box 0
box[0].remove('jungle')
box[0].remove('boot')

# Put the brush and the wig and the button into Box 7
box[7].extend(['brush', 'wig', 'button'])

# Swap the puzzle in Box 4 with the glasses in Box 8
box[4].remove('puzzle')
box[8].remove('glasses')
box[4].append('glasses')
box[8].append('puzzle')

# Remove the comet and the brush from Box 7
box[7].remove('comet')
box[7].remove('brush')

# Put the doll and the mixer and the game into Box 2
box[2].extend(['doll', 'mixer', 'game'])

# Print the contents of each box
for i in range(13):
    print(f"Box {i}: {box[i]}")