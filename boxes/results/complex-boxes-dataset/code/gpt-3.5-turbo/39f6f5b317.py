# Initial state of boxes
boxes = {
    0: ['doll', 'bus', 'scissors', 'ocean', 'fork'],
    1: ['microwave', 'gloves', 'vase', 'boot'],
    2: ['blanket', 'jacket', 'perfume'],
    3: [],
    4: ['headphone', 'planet']
}

# Swap the boot in Box 1 with the perfume in Box 2.
boxes[1].remove('boot')
boxes[2].remove('perfume')
boxes[1].append('perfume')
boxes[2].append('boot')

# Move the fork from Box 0 to Box 4.
boxes[0].remove('fork')
boxes[4].append('fork')

# Replace the blanket and the boot with the console and the cow in Box 2.
boxes[2].remove('blanket')
boxes[2].remove('boot')
boxes[2].append('console')
boxes[2].append('cow')

# Remove the jacket and the console from Box 2.
boxes[2].remove('jacket')
boxes[2].remove('console')

# Remove the cow from Box 2.
boxes[2].remove('cow')

# Remove the scissors and the ocean from Box 0.
boxes[0].remove('scissors')
boxes[0].remove('ocean')

# Move the microwave from Box 1 to Box 2.
boxes[1].remove('microwave')
boxes[2].append('microwave')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")