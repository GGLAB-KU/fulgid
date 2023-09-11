# Initial state of boxes
boxes = {
    0: ['rocket', 'chair', 'key'],
    1: ['bear', 'river', 'toothpaste', 'bowl', 'clock'],
    2: ['sun', 'apple'],
    3: [],
    4: ['telescope', 'microwave', 'fridge', 'watch']
}

# Put the mask into Box 0.
boxes[0].append('mask')

# Put the river into Box 2.
boxes[2].append('river')

# Swap the clock in Box 1 with the river in Box 2.
boxes[1].remove('clock')
boxes[2].remove('river')
boxes[1].append('river')
boxes[2].append('clock')

# Put the controller into Box 1.
boxes[1].append('controller')

# Swap the sun in Box 2 with the fridge in Box 4.
boxes[2].remove('sun')
boxes[4].remove('fridge')
boxes[2].append('fridge')
boxes[4].append('sun')

# Remove the telescope and the watch from Box 4.
boxes[4].remove('telescope')
boxes[4].remove('watch')

# Put the forest and the tiger and the charger into Box 0.
items_to_put = ['forest', 'tiger', 'charger']
for item in items_to_put:
    boxes[0].append(item)

# Remove the sun and the microwave from Box 4.
boxes[4].remove('sun')
boxes[4].remove('microwave')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")