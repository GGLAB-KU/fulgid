# Initial state of boxes
boxes = {
    0: ['lion', 'spoon'],
    1: [],
    2: ['bear', 'dice', 'jacket', 'planet'],
    3: ['ring', 'microwave', 'starfish'],
    4: ['beach', 'coat', 'usb'],
    5: ['butterfly', 'horn', 'watch', 'coin'],
    6: ['pants', 'toothpaste', 'wallet'],
    7: ['shirt', 'shorts', 'tree'],
    8: ['keyboard', 'thunder', 'mirror'],
    9: ['shelf', 'flute', 'guitar', 'razor'],
    10: ['dress', 'hat', 'scarf', 'doll']
}

# Swap the thunder in Box 8 with the pants in Box 6.
boxes[8].remove('thunder')
boxes[6].remove('pants')
boxes[8].append('pants')
boxes[6].append('thunder')

# Remove the thunder from Box 6.
boxes[6].remove('thunder')

# Remove the shelf from Box 9.
boxes[9].remove('shelf')

# Put the speaker and the pan into Box 10.
boxes[10].append('speaker')
boxes[10].append('pan')

# Replace the beach and the coat with the pan and the mirror in Box 4.
boxes[4].remove('beach')
boxes[4].remove('coat')
boxes[4].append('pan')
boxes[4].append('mirror')

# Put the towel and the phone into Box 5.
boxes[5].append('towel')
boxes[5].append('phone')

# Remove the spoon and the lion from Box 0.
boxes[0].remove('spoon')
boxes[0].remove('lion')

# Swap the starfish in Box 3 with the mirror in Box 8.
boxes[3].remove('starfish')
boxes[8].remove('mirror')
boxes[3].append('mirror')
boxes[8].append('starfish')

# Swap the guitar in Box 9 with the scarf in Box 10.
boxes[9].remove('guitar')
boxes[10].remove('scarf')
boxes[9].append('scarf')
boxes[10].append('guitar')

# Put the fish into Box 4.
boxes[4].append('fish')

# Swap the tree in Box 7 with the razor in Box 9.
boxes[7].remove('tree')
boxes[9].remove('razor')
boxes[7].append('razor')
boxes[9].append('tree')

# Put the charger and the brush and the tie into Box 8.
boxes[8].append('charger')
boxes[8].append('brush')
boxes[8].append('tie')

# Put the moon into Box 3.
boxes[3].append('moon')

# Swap the toothpaste in Box 6 with the coin in Box 5.
boxes[6].remove('toothpaste')
boxes[5].remove('coin')
boxes[6].append('coin')
boxes[5].append('toothpaste')

# Replace the guitar and the speaker and the pan with the bell and the toaster and the violin in Box 10.
boxes[10].remove('guitar')
boxes[10].remove('speaker')
boxes[10].remove('pan')
boxes[10].append('bell')
boxes[10].append('toaster')
boxes[10].append('violin')

# Put the apple and the makeup and the shorts into Box 0.
boxes[0].append('apple')
boxes[0].append('makeup')
boxes[0].append('shorts')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")