# Initial state of boxes
boxes = {
    0: ['coin'],
    1: ['brush', 'dolphin', 'mask', 'starfish', 'glasses'],
    2: ['sock', 'fridge', 'lamp', 'scissors', 'controller'],
    3: ['bear', 'hat', 'frame', 'whistle', 'note'],
    4: ['toaster'],
    5: ['telescope', 'boat', 'console', 'perfume'],
    6: [],
    7: ['cow', 'chair', 'desert', 'freezer', 'sun'],
    8: ['harmonica', 'lipstick', 'scarf', 'violin', 'cup'],
    9: ['boot', 'moon', 'charger', 'thread']
}

# Move the dolphin and the glasses from Box 1 to Box 0.
boxes[0].extend(boxes[1].pop(boxes[1].index('dolphin')))
boxes[0].extend(boxes[1].pop(boxes[1].index('glasses')))

# Remove the glasses and the coin from Box 0.
boxes[0].remove('glasses')
boxes[0].remove('coin')

# Remove the chair from Box 7.
boxes[7].remove('chair')

# Replace the freezer and the sun with the speaker and the tie in Box 7.
boxes[7].remove('freezer')
boxes[7].remove('sun')
boxes[7].append('speaker')
boxes[7].append('tie')

# Remove the lamp and the sock from Box 2.
boxes[2].remove('lamp')
boxes[2].remove('sock')

# Swap the scissors in Box 2 with the whistle in Box 3.
boxes[2].remove('scissors')
boxes[3].remove('whistle')
boxes[2].append('whistle')
boxes[3].append('scissors')

# Put the scarf and the shorts into Box 9.
boxes[9].append('scarf')
boxes[9].append('shorts')

# Put the guitar and the pillow and the butterfly into Box 6.
boxes[6].append('guitar')
boxes[6].append('pillow')
boxes[6].append('butterfly')

# Swap the butterfly in Box 6 with the thread in Box 9.
boxes[6].remove('butterfly')
boxes[9].remove('thread')
boxes[6].append('thread')
boxes[9].append('butterfly')

# Move the whistle and the controller and the fridge from Box 2 to Box 6.
items_to_move = ['whistle', 'controller', 'fridge']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[6].append(item)

# Swap the thread in Box 6 with the telescope in Box 5.
boxes[6].remove('thread')
boxes[5].remove('telescope')
boxes[6].append('telescope')
boxes[5].append('thread')

# Put the gloves and the coral and the umbrella into Box 5.
boxes[5].append('gloves')
boxes[5].append('coral')
boxes[5].append('umbrella')

# Move the toaster from Box 4 to Box 9.
boxes[4].remove('toaster')
boxes[9].append('toaster')

# Swap the fridge in Box 6 with the brush in Box 1.
boxes[6].remove('fridge')
boxes[1].remove('brush')
boxes[6].append('brush')
boxes[1].append('fridge')

# Remove the perfume from Box 5.
boxes[5].remove('perfume')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")