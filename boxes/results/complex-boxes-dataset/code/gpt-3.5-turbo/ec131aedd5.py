# Initial state of boxes
boxes = {
    0: [],
    1: ['snow', 'elephant'],
    2: [],
    3: ['dog', 'cloud', 'horn', 'mirror'],
    4: ['lightning', 'key', 'wig', 'phone', 'cup'],
    5: ['lamp', 'sock', 'forest', 'telescope'],
    6: ['harmonica', 'frame'],
    7: [],
    8: [],
    9: ['grinder', 'whistle', 'tree', 'wire', 'headphone'],
    10: ['rock', 'mountain', 'plane'],
    11: [],
    12: ['blender', 'soap'],
    13: ['beach', 'boot', 'island'],
    14: ['lock']
}

# Put the starfish and the microscope and the earring into Box 11.
boxes[11].extend(['starfish', 'microscope', 'earring'])

# Replace the wire and the whistle with the apple and the towel in Box 9.
boxes[9].remove('wire')
boxes[9].remove('whistle')
boxes[9].append('apple')
boxes[9].append('towel')

# Put the crown and the button into Box 5.
boxes[5].extend(['crown', 'button'])

# Move the key and the phone from Box 4 to Box 12.
boxes[4].remove('key')
boxes[4].remove('phone')
boxes[12].extend(['key', 'phone'])

# Replace the harmonica with the coat in Box 6.
boxes[6].remove('harmonica')
boxes[6].append('coat')

# Put the table and the planet into Box 14.
boxes[14].extend(['table', 'planet'])

# Remove the snow from Box 1.
boxes[1].remove('snow')

# Put the piano and the coin and the telescope into Box 5.
boxes[5].extend(['piano', 'coin', 'telescope'])

# Remove the soap and the blender from Box 12.
boxes[12].remove('soap')
boxes[12].remove('blender')

# Swap the earring in Box 11 with the frame in Box 6.
boxes[11].remove('earring')
boxes[6].remove('frame')
boxes[11].append('frame')
boxes[6].append('earring')

# Remove the elephant from Box 1.
boxes[1].remove('elephant')

# Empty Box 13.
boxes[13] = []

# Swap the coin in Box 5 with the starfish in Box 11.
boxes[5].remove('coin')
boxes[11].remove('starfish')
boxes[5].append('starfish')
boxes[11].append('coin')

# Remove the button and the shampoo and the lamp from Box 5.
boxes[5].remove('button')
boxes[5].remove('shampoo')
boxes[5].remove('lamp')

# Replace the rock with the drum in Box 10.
boxes[10].remove('rock')
boxes[10].append('drum')

# Replace the lightning and the wig with the basket and the blender in Box 4.
boxes[4].remove('lightning')
boxes[4].remove('wig')
boxes[4].append('basket')
boxes[4].append('blender')

# Move the tree from Box 9 to Box 12.
boxes[9].remove('tree')
boxes[12].append('tree')

# Put the starfish and the glasses into Box 14.
boxes[14].extend(['starfish', 'glasses'])

# Replace the basket and the cup and the blender with the helmet and the lion and the wig in Box 4.
boxes[4].remove('basket')
boxes[4].remove('cup')
boxes[4].remove('blender')
boxes[4].append('helmet')
boxes[4].append('lion')
boxes[4].append('wig')

# Move the table and the lock and the planet from Box 14 to Box 11.
boxes[14].remove('table')
boxes[14].remove('lock')
boxes[14].remove('planet')
boxes[11].extend(['table', 'lock', 'planet'])

# Remove the starfish and the forest from Box 5.
boxes[5].remove('starfish')
boxes[5].remove('forest')

# Replace the towel and the headphone and the apple with the sun and the shampoo and the starfish in Box 9.
boxes[9].remove('towel')
boxes[9].remove('headphone')
boxes[9].remove('apple')
boxes[9].append('sun')
boxes[9].append('shampoo')
boxes[9].append('starfish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")