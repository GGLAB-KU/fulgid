# Initial state of boxes
boxes = {
    0: ['comb'],
    1: ['mountain', 'oven', 'charger', 'drum', 'chair'],
    2: ['basket', 'blender', 'bracelet'],
    3: ['island'],
    4: [],
    5: ['fish'],
    6: ['seaweed', 'blanket'],
    7: ['clock'],
    8: []
}

# Swap the fish in Box 5 with the clock in Box 7.
boxes[5].remove('fish')
boxes[7].remove('clock')
boxes[5].append('clock')
boxes[7].append('fish')

# Swap the basket in Box 2 with the fish in Box 7.
boxes[2].remove('basket')
boxes[7].remove('fish')
boxes[2].append('fish')
boxes[7].append('basket')

# Swap the island in Box 3 with the clock in Box 5.
boxes[3].remove('island')
boxes[5].remove('clock')
boxes[3].append('clock')
boxes[5].append('island')

# Swap the basket in Box 7 with the clock in Box 3.
boxes[7].remove('basket')
boxes[3].remove('clock')
boxes[7].append('clock')
boxes[3].append('basket')

# Replace the comb with the helmet in Box 0.
boxes[0].remove('comb')
boxes[0].append('helmet')

# Put the coral and the freezer and the console into Box 0.
boxes[0].extend(['coral', 'freezer', 'console'])

# Remove the mountain and the drum and the chair from Box 1.
items_to_remove = ['mountain', 'drum', 'chair']
for item in items_to_remove:
    boxes[1].remove(item)

# Empty Box 3.
boxes[3] = []

# Remove the oven and the charger from Box 1.
boxes[1].remove('oven')
boxes[1].remove('charger')

# Swap the helmet in Box 0 with the island in Box 5.
boxes[0].remove('helmet')
boxes[5].remove('island')
boxes[0].append('island')
boxes[5].append('helmet')

# Move the helmet from Box 5 to Box 8.
boxes[5].remove('helmet')
boxes[8].append('helmet')

# Remove the freezer and the console from Box 0.
boxes[0].remove('freezer')
boxes[0].remove('console')

# Swap the fish in Box 2 with the clock in Box 7.
boxes[2].remove('fish')
boxes[7].remove('clock')
boxes[2].append('clock')
boxes[7].append('fish')

# Remove the helmet from Box 8.
boxes[8].remove('helmet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")