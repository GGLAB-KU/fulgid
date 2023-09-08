# Initial state of boxes
boxes = {
    0: ['bear', 'book', 'shirt'],
    1: ['game', 'glasses', 'wallet'],
    2: ['gloves', 'lock', 'fridge'],
    3: ['drum', 'scarf', 'bag', 'brush', 'fork'],
    4: ['perfume'],
    5: ['hat', 'microscope', 'puzzle', 'shoe', 'clock'],
    6: [],
    7: ['mirror'],
    8: ['dog', 'bracelet', 'cow', 'towel', 'branch'],
    9: ['magnet'],
    10: ['grass', 'needle'],
    11: ['lamp'],
    12: [],
    13: ['headphone', 'ocean', 'keyboard', 'jungle']
}

# Replace the mirror with the starfish in Box 7.
boxes[7].remove('mirror')
boxes[7].append('starfish')

# Put the boot and the lock and the tie into Box 7.
items_to_put = ['boot', 'lock', 'tie']
for item in items_to_put:
    boxes[7].append(item)

# Put the watch into Box 4.
boxes[4].append('watch')

# Remove the watch and the perfume from Box 4.
boxes[4].remove('watch')
boxes[4].remove('perfume')

# Remove the puzzle and the clock from Box 5.
boxes[5].remove('puzzle')
boxes[5].remove('clock')

# Put the grinder into Box 0.
boxes[0].append('grinder')

# Swap the magnet in Box 9 with the boot in Box 7.
boxes[9].remove('magnet')
boxes[7].remove('boot')
boxes[9].append('boot')
boxes[7].append('magnet')

# Replace the headphone and the ocean with the shoes and the polish in Box 13.
boxes[13].remove('headphone')
boxes[13].remove('ocean')
boxes[13].append('shoes')
boxes[13].append('polish')

# Put the button into Box 6.
boxes[6].append('button')

# Swap the fridge in Box 2 with the needle in Box 10.
boxes[2].remove('fridge')
boxes[10].remove('needle')
boxes[2].append('needle')
boxes[10].append('fridge')

# Swap the bear in Box 0 with the hat in Box 5.
boxes[0].remove('bear')
boxes[5].remove('hat')
boxes[0].append('hat')
boxes[5].append('bear')

# Move the microscope from Box 5 to Box 11.
boxes[5].remove('microscope')
boxes[11].append('microscope')

# Replace the bear and the shoe with the doll and the sun in Box 5.
boxes[5].remove('bear')
boxes[5].remove('shoe')
boxes[5].append('doll')
boxes[5].append('sun')

# Move the button from Box 6 to Box 2.
boxes[6].remove('button')
boxes[2].append('button')

# Replace the dog and the branch with the pants and the rock in Box 8.
boxes[8].remove('dog')
boxes[8].remove('branch')
boxes[8].append('pants')
boxes[8].append('rock')

# Move the boot from Box 9 to Box 0.
boxes[9].remove('boot')
boxes[0].append('boot')

# Remove the towel from Box 8.
boxes[8].remove('towel')

# Replace the doll with the zipper in Box 5.
boxes[5].remove('doll')
boxes[5].append('zipper')

# Remove the sun and the zipper from Box 5.
boxes[5].remove('sun')
boxes[5].remove('zipper')

# Swap the jungle in Box 13 with the fridge in Box 10.
boxes[13].remove('jungle')
boxes[10].remove('fridge')
boxes[13].append('fridge')
boxes[10].append('jungle')

# Swap the drum in Box 3 with the lamp in Box 11.
boxes[3].remove('drum')
boxes[11].remove('lamp')
boxes[3].append('lamp')
boxes[11].append('drum')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")