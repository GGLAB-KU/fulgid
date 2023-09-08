# Initial state of boxes
boxes = {
    0: ['cow'],
    1: ['violin', 'zipper', 'meteor'],
    2: ['key', 'dress', 'needle', 'starfish'],
    3: ['grass', 'rain', 'phone'],
    4: ['card', 'butterfly'],
    5: ['pants', 'ship'],
    6: ['leaf', 'towel', 'toaster'],
    7: ['puzzle', 'harmonica'],
    8: ['helmet', 'keyboard', 'frame', 'shoes'],
    9: ['bird', 'necklace', 'bag', 'skirt'],
    10: ['tree', 'scarf', 'coral', 'dog', 'swimsuit']
}

# Move the keyboard and the frame and the helmet from Box 8 to Box 1.
items_to_move = ['keyboard', 'frame', 'helmet']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[1].append(item)

# Move the harmonica from Box 7 to Box 2.
boxes[7].remove('harmonica')
boxes[2].append('harmonica')

# Put the piano and the brush into Box 8.
boxes[8].append('piano')
boxes[8].append('brush')

# Move the necklace from Box 9 to Box 2.
boxes[9].remove('necklace')
boxes[2].append('necklace')

# Swap the scarf in Box 10 with the rain in Box 3.
boxes[10].remove('scarf')
boxes[3].remove('rain')
boxes[10].append('rain')
boxes[3].append('scarf')

# Remove the leaf and the towel from Box 6.
boxes[6].remove('leaf')
boxes[6].remove('towel')

# Put the forest into Box 1.
boxes[1].append('forest')

# Move the puzzle from Box 7 to Box 2.
boxes[7].remove('puzzle')
boxes[2].append('puzzle')

# Put the meteor and the doll and the seaweed into Box 0.
boxes[0].append('meteor')
boxes[0].append('doll')
boxes[0].append('seaweed')

# Replace the scarf and the phone and the grass with the earring and the coin and the lamp in Box 3.
boxes[3].remove('scarf')
boxes[3].remove('phone')
boxes[3].remove('grass')
boxes[3].append('earring')
boxes[3].append('coin')
boxes[3].append('lamp')

# Replace the skirt with the shoe in Box 9.
boxes[9].remove('skirt')
boxes[9].append('shoe')

# Replace the bird and the bag and the shoe with the watch and the wire and the magnet in Box 9.
boxes[9].remove('bird')
boxes[9].remove('bag')
boxes[9].remove('shoe')
boxes[9].append('watch')
boxes[9].append('wire')
boxes[9].append('magnet')

# Replace the toaster with the umbrella in Box 6.
boxes[6].remove('toaster')
boxes[6].append('umbrella')

# Remove the piano from Box 8.
boxes[8].remove('piano')

# Move the lamp and the earring from Box 3 to Box 6.
boxes[3].remove('lamp')
boxes[3].remove('earring')
boxes[6].append('lamp')
boxes[6].append('earring')

# Remove the card from Box 4.
boxes[4].remove('card')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")