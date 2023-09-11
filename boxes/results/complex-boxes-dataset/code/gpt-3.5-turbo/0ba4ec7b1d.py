# Initial state of boxes
boxes = {
    0: ['necklace', 'magnet', 'cat'],
    1: ['lamp'],
    2: ['shark', 'ocean'],
    3: ['piano', 'submarine'],
    4: ['pen', 'pot'],
    5: ['telescope', 'bear', 'scarf', 'comb', 'planet'],
    6: ['speaker', 'razor', 'toaster', 'hat']
}

# Empty Box 4.
boxes[4] = []

# Move the hat and the speaker from Box 6 to Box 4.
boxes[6].remove('hat')
boxes[6].remove('speaker')
boxes[4].append('hat')
boxes[4].append('speaker')

# Put the octopus and the dog and the horse into Box 6.
boxes[6].append('octopus')
boxes[6].append('dog')
boxes[6].append('horse')

# Swap the razor in Box 6 with the magnet in Box 0.
boxes[6].remove('razor')
boxes[0].remove('magnet')
boxes[6].append('magnet')
boxes[0].append('razor')

# Put the shoes into Box 6.
boxes[6].append('shoes')

# Replace the octopus and the magnet with the coat and the boot in Box 6.
boxes[6].remove('octopus')
boxes[0].remove('magnet')
boxes[6].append('coat')
boxes[6].append('boot')

# Remove the speaker and the hat from Box 4.
boxes[4].remove('speaker')
boxes[4].remove('hat')

# Move the scarf and the planet from Box 5 to Box 2.
boxes[5].remove('scarf')
boxes[5].remove('planet')
boxes[2].append('scarf')
boxes[2].append('planet')

# Replace the comb and the telescope and the bear with the dress and the coral and the bicycle in Box 5.
boxes[5].remove('comb')
boxes[5].remove('telescope')
boxes[5].remove('bear')
boxes[5].append('dress')
boxes[5].append('coral')
boxes[5].append('bicycle')

# Remove the lamp from Box 1.
boxes[1].remove('lamp')

# Swap the dress in Box 5 with the planet in Box 2.
boxes[5].remove('dress')
boxes[2].remove('planet')
boxes[5].append('planet')
boxes[2].append('dress')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")