# Initial state of boxes
boxes = {
    0: ['pan'],
    1: ['umbrella', 'flute', 'watch'],
    2: ['bowl', 'paint'],
    3: ['speaker'],
    4: ['microscope', 'headphone', 'seaweed', 'coin'],
    5: ['fish', 'blanket', 'motorcycle', 'helmet', 'horn'],
    6: [],
    7: ['snow', 'fridge', 'battery', 'keyboard'],
    8: [],
    9: [],
    10: ['guitar', 'leaf', 'branch', 'polish', 'desert'],
    11: ['perfume', 'coat', 'cat'],
    12: ['ship', 'sock', 'belt', 'mixer', 'ocean']
}

# Put the crown into Box 11.
boxes[11].append('crown')

# Move the speaker from Box 3 to Box 0.
boxes[0].append(boxes[3].pop())

# Replace the pan with the boot in Box 0.
boxes[0].remove('pan')
boxes[0].append('boot')

# Remove the paint from Box 2.
boxes[2].remove('paint')

# Move the sock from Box 12 to Box 9.
boxes[9].append(boxes[12].pop(1))

# Replace the coin and the seaweed and the headphone with the moon and the freezer and the truck in Box 4.
boxes[4].remove('coin')
boxes[4].remove('seaweed')
boxes[4].remove('headphone')
boxes[4].append('moon')
boxes[4].append('freezer')
boxes[4].append('truck')

# Remove the microscope from Box 4.
boxes[4].remove('microscope')

# Remove the mixer from Box 12.
boxes[12].remove('mixer')

# Put the thunder into Box 11.
boxes[11].append('thunder')

# Move the sock from Box 9 to Box 0.
boxes[0].append(boxes[9].pop())

# Replace the speaker and the boot and the sock with the moon and the ship and the tape in Box 0.
boxes[0].remove('speaker')
boxes[0].remove('boot')
boxes[0].remove('sock')
boxes[0].append('moon')
boxes[0].append('ship')
boxes[0].append('tape')

# Remove the branch from Box 10.
boxes[10].remove('branch')

# Move the leaf and the guitar and the polish from Box 10 to Box 6.
items_to_move = ['leaf', 'guitar', 'polish']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[6].append(item)

# Remove the freezer from Box 4.
boxes[4].remove('freezer')

# Put the ocean into Box 7.
boxes[7].append('ocean')

# Swap the umbrella in Box 1 with the belt in Box 12.
boxes[1].remove('umbrella')
boxes[12].remove('belt')
boxes[1].append('belt')
boxes[12].append('umbrella')

# Move the desert from Box 10 to Box 12.
boxes[12].append(boxes[10].pop(3))

# Move the crown and the coat and the perfume from Box 11 to Box 12.
items_to_move = ['crown', 'coat', 'perfume']
for item in items_to_move:
    boxes[11].remove(item)
    boxes[12].append(item)

# Remove the truck from Box 4.
boxes[4].remove('truck')

# Remove the moon from Box 4.
boxes[4].remove('moon')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")