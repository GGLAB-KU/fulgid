# Initial state of boxes
boxes = {
    0: [],
    1: ['earring', 'pants', 'rocket', 'octopus', 'truck'],
    2: ['dog', 'jacket', 'charger'],
    3: ['pan'],
    4: ['shirt'],
    5: [],
    6: ['flute', 'game', 'piano', 'lipstick'],
    7: ['coat', 'fridge', 'bicycle'],
    8: ['microwave', 'ship', 'grinder', 'dress'],
    9: ['tree', 'towel', 'blanket', 'table']
}

# Remove the ship from Box 8.
boxes[8].remove('ship')

# Remove the octopus from Box 1.
boxes[1].remove('octopus')

# Remove the coat from Box 7.
boxes[7].remove('coat')

# Replace the truck and the earring and the rocket with the phone and the dress and the umbrella in Box 1.
boxes[1].remove('truck')
boxes[1].remove('earring')
boxes[1].remove('rocket')
boxes[1].append('phone')
boxes[1].append('dress')
boxes[1].append('umbrella')

# Move the pan from Box 3 to Box 8.
boxes[3].remove('pan')
boxes[8].append('pan')

# Empty Box 6.
boxes[6] = []

# Empty Box 8.
boxes[8] = []

# Remove the umbrella from Box 1.
boxes[1].remove('umbrella')

# Remove the dog and the jacket from Box 2.
boxes[2].remove('dog')
boxes[2].remove('jacket')

# Replace the shirt with the skirt in Box 4.
boxes[4].remove('shirt')
boxes[4].append('skirt')

# Move the charger from Box 2 to Box 8.
boxes[2].remove('charger')
boxes[8].append('charger')

# Swap the charger in Box 8 with the phone in Box 1.
boxes[8].remove('charger')
boxes[1].remove('phone')
boxes[8].append('phone')
boxes[1].append('charger')

# Put the soap into Box 2.
boxes[2].append('soap')

# Swap the skirt in Box 4 with the towel in Box 9.
boxes[4].remove('skirt')
boxes[9].remove('towel')
boxes[4].append('towel')
boxes[9].append('skirt')

# Replace the pants and the charger and the dress with the sun and the elephant and the cat in Box 1.
boxes[1].remove('pants')
boxes[1].remove('charger')
boxes[1].remove('dress')
boxes[1].append('sun')
boxes[1].append('elephant')
boxes[1].append('cat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")