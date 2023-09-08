# Initial state of boxes
boxes = {
    0: ['ring', 'phone', 'violin', 'wig', 'glasses'],
    1: [],
    2: ['shoes', 'tree', 'razor', 'tie'],
    3: ['wallet', 'headphone'],
    4: ['blender'],
    5: ['shark', 'planet'],
    6: ['beach', 'river', 'meteor', 'train'],
    7: [],
    8: ['hat', 'octopus'],
    9: ['rain'],
    10: ['lamp', 'shoe'],
    11: ['coin', 'crown', 'bear', 'shampoo', 'shorts'],
    12: ['star']
}

# Replace the glasses with the laptop in Box 0.
boxes[0].remove('glasses')
boxes[0].append('laptop')

# Replace the lamp with the guitar in Box 10.
boxes[10].remove('lamp')
boxes[10].append('guitar')

# Replace the star with the plate in Box 12.
boxes[12].remove('star')
boxes[12].append('plate')

# Move the plate from Box 12 to Box 0.
boxes[12].remove('plate')
boxes[0].append('plate')

# Swap the rain in Box 9 with the crown in Box 11.
boxes[9].remove('rain')
boxes[11].remove('crown')
boxes[9].append('crown')
boxes[11].append('rain')

# Replace the ring and the laptop and the plate with the mountain and the guitar and the bicycle in Box 0.
boxes[0].remove('ring')
boxes[0].remove('laptop')
boxes[0].remove('plate')
boxes[0].append('mountain')
boxes[0].append('guitar')
boxes[0].append('bicycle')

# Move the meteor and the beach and the train from Box 6 to Box 8.
items_to_move = ['meteor', 'beach', 'train']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[8].append(item)

# Remove the wallet from Box 3.
boxes[3].remove('wallet')

# Move the planet from Box 5 to Box 0.
boxes[5].remove('planet')
boxes[0].append('planet')

# Move the blender from Box 4 to Box 9.
boxes[4].remove('blender')
boxes[9].append('blender')

# Remove the shoes from Box 2.
boxes[2].remove('shoes')

# Replace the headphone with the helmet in Box 3.
boxes[3].remove('headphone')
boxes[3].append('helmet')

# Move the guitar from Box 10 to Box 11.
boxes[10].remove('guitar')
boxes[11].append('guitar')

# Move the river from Box 6 to Box 3.
boxes[6].remove('river')
boxes[3].append('river')

# Remove the bear from Box 11.
boxes[11].remove('bear')

# Move the shorts and the coin and the shampoo from Box 11 to Box 2.
items_to_move = ['shorts', 'coin', 'shampoo']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[2].append(item)

# Replace the guitar and the rain with the comb and the needle in Box 11.
boxes[11].remove('guitar')
boxes[11].remove('rain')
boxes[11].append('comb')
boxes[11].append('needle')

# Swap the shark in Box 5 with the octopus in Box 8.
boxes[5].remove('shark')
boxes[8].remove('octopus')
boxes[5].append('octopus')
boxes[8].append('shark')

# Put the toaster and the tape into Box 6.
boxes[6].append('toaster')
boxes[6].append('tape')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")