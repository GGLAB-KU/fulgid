# Initial state of boxes
boxes = {
    0: ['brush', 'shirt', 'vase'],
    1: ['needle', 'razor', 'headphone', 'chair', 'fish'],
    2: ['tree', 'star', 'perfume', 'island'],
    3: ['skirt', 'plane'],
    4: [],
    5: ['bear'],
    6: ['octopus', 'puzzle'],
    7: ['grinder', 'freezer', 'basket'],
    8: ['wig', 'cow'],
    9: ['branch', 'rain', 'rocket'],
    10: ['thunder', 'fridge', 'river', 'earring', 'meteor'],
    11: ['dolphin', 'flute', 'gloves', 'cloud', 'umbrella'],
    12: ['phone', 'car'],
    13: ['paint', 'game', 'console', 'pants', 'charger']
}

# Move the phone and the car from Box 12 to Box 1.
boxes[12].remove('phone')
boxes[12].remove('car')
boxes[1].append('phone')
boxes[1].append('car')

# Put the bicycle into Box 4.
boxes[4].append('bicycle')

# Replace the bicycle with the laptop in Box 4.
boxes[4].remove('bicycle')
boxes[4].append('laptop')

# Put the button and the drum and the umbrella into Box 9.
boxes[9].append('button')
boxes[9].append('drum')
boxes[9].append('umbrella')

# Move the game and the paint and the console from Box 13 to Box 11.
items_to_move = ['game', 'paint', 'console']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[11].append(item)

# Put the lightning and the cat into Box 12.
boxes[12].append('lightning')
boxes[12].append('cat')

# Move the cat from Box 12 to Box 2.
boxes[12].remove('cat')
boxes[2].append('cat')

# Remove the octopus and the puzzle from Box 6.
boxes[6].remove('octopus')
boxes[6].remove('puzzle')

# Replace the wig with the helmet in Box 8.
boxes[8].remove('wig')
boxes[8].append('helmet')

# Replace the perfume with the glasses in Box 2.
boxes[2].remove('perfume')
boxes[2].append('glasses')

# Replace the plane with the skirt in Box 3.
boxes[3].remove('plane')
boxes[3].append('skirt')

# Put the basket and the note into Box 0.
boxes[0].append('basket')
boxes[0].append('note')

# Move the skirt and the skirt from Box 3 to Box 13.
boxes[3].remove('skirt')
boxes[13].append('skirt')
boxes[3].remove('skirt')
boxes[13].append('skirt')

# Move the cow and the helmet from Box 8 to Box 5.
boxes[8].remove('cow')
boxes[5].append('cow')
boxes[8].remove('helmet')
boxes[5].append('helmet')

# Swap the skirt in Box 13 with the phone in Box 1.
boxes[13].remove('skirt')
boxes[1].remove('phone')
boxes[13].append('phone')
boxes[1].append('skirt')

# Move the branch and the button from Box 9 to Box 10.
boxes[9].remove('branch')
boxes[9].remove('button')
boxes[10].append('branch')
boxes[10].append('button')

# Replace the button and the earring and the meteor with the freezer and the paint and the mountain in Box 10.
boxes[10].remove('button')
boxes[10].remove('earring')
boxes[10].remove('meteor')
boxes[10].append('freezer')
boxes[10].append('paint')
boxes[10].append('mountain')

# Remove the charger from Box 13.
boxes[13].remove('charger')

# Swap the fish in Box 1 with the dolphin in Box 11.
boxes[1].remove('fish')
boxes[11].remove('dolphin')
boxes[1].append('dolphin')
boxes[11].append('fish')

# Swap the basket in Box 7 with the brush in Box 0.
boxes[7].remove('basket')
boxes[0].remove('brush')
boxes[7].append('brush')
boxes[0].append('basket')

# Remove the rain from Box 9.
boxes[9].remove('rain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")