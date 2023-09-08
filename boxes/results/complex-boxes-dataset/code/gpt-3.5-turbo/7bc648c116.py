# Initial state of boxes
boxes = {
    0: ['boat', 'toothpaste'],
    1: ['fish', 'apple'],
    2: [],
    3: ['toothbrush', 'chair'],
    4: ['necklace', 'horse', 'hat', 'truck'],
    5: ['helmet'],
    6: ['fork', 'sandals', 'wig', 'bus'],
    7: [],
    8: ['skirt', 'grinder', 'harmonica'],
    9: ['keyboard'],
    10: ['lock', 'pan', 'piano', 'flute', 'clock'],
    11: ['paint', 'note'],
    12: ['oven', 'makeup', 'microwave'],
    13: []
}

# Swap the flute in Box 10 with the chair in Box 3.
boxes[10].remove('flute')
boxes[3].remove('chair')
boxes[10].append('chair')
boxes[3].append('flute')

# Move the fish and the apple from Box 1 to Box 7.
items_to_move = ['fish', 'apple']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[7].append(item)

# Move the harmonica and the grinder and the skirt from Box 8 to Box 11.
items_to_move = ['harmonica', 'grinder', 'skirt']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[11].append(item)

# Remove the bus and the fork and the sandals from Box 6.
items_to_remove = ['bus', 'fork', 'sandals']
for item in items_to_remove:
    boxes[6].remove(item)

# Put the rain and the phone into Box 0.
boxes[0].append('rain')
boxes[0].append('phone')

# Replace the keyboard with the usb in Box 9.
boxes[9].remove('keyboard')
boxes[9].append('usb')

# Move the helmet from Box 5 to Box 0.
boxes[5].remove('helmet')
boxes[0].append('helmet')

# Replace the chair with the cup in Box 10.
boxes[10].remove('chair')
boxes[10].append('cup')

# Replace the usb with the table in Box 9.
boxes[9].remove('usb')
boxes[9].append('table')

# Empty Box 9.
boxes[9] = []

# Remove the pan from Box 10.
boxes[10].remove('pan')

# Remove the cup from Box 10.
boxes[10].remove('cup')

# Put the elephant and the tape into Box 12.
boxes[12].append('elephant')
boxes[12].append('tape')

# Remove the wig from Box 6.
boxes[6].remove('wig')

# Swap the grinder in Box 11 with the lock in Box 10.
boxes[11].remove('grinder')
boxes[10].remove('lock')
boxes[11].append('lock')
boxes[10].append('grinder')

# Remove the hat and the truck and the horse from Box 4.
items_to_remove = ['hat', 'truck', 'horse']
for item in items_to_remove:
    boxes[4].remove(item)

# Swap the microwave in Box 12 with the phone in Box 0.
boxes[12].remove('microwave')
boxes[0].remove('phone')
boxes[12].append('phone')
boxes[0].append('microwave')

# Empty Box 12.
boxes[12] = []

# Remove the necklace from Box 4.
boxes[4].remove('necklace')

# Put the whistle into Box 1.
boxes[1].append('whistle')

# Put the bag and the river into Box 9.
boxes[9].append('bag')
boxes[9].append('river')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")