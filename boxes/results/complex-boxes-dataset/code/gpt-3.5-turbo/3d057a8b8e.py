# Initial state of boxes
boxes = {
    0: ['bell', 'headphone', 'dog', 'book', 'speaker'],
    1: ['dice', 'wig'],
    2: ['telescope', 'microwave'],
    3: [],
    4: ['boot'],
    5: ['charger', 'rain', 'freezer', 'bear'],
    6: [],
    7: ['storm', 'note', 'train', 'lamp'],
    8: ['drum', 'toothbrush', 'cup', 'pants'],
    9: ['bicycle', 'magnet', 'tie'],
    10: ['coral']
}

# Replace the bicycle with the microscope in Box 9.
boxes[9].remove('bicycle')
boxes[9].append('microscope')

# Move the dog from Box 0 to Box 9.
boxes[0].remove('dog')
boxes[9].append('dog')

# Swap the pants in Box 8 with the boot in Box 4.
boxes[8].remove('pants')
boxes[4].remove('boot')
boxes[8].append('boot')
boxes[4].append('pants')

# Replace the charger and the rain with the toothpaste and the zipper in Box 5.
boxes[5].remove('charger')
boxes[5].remove('rain')
boxes[5].append('toothpaste')
boxes[5].append('zipper')

# Remove the microscope from Box 9.
boxes[9].remove('microscope')

# Replace the coral with the fish in Box 10.
boxes[10].remove('coral')
boxes[10].append('fish')

# Replace the toothpaste and the bear with the leaf and the sandals in Box 5.
boxes[5].remove('toothpaste')
boxes[5].remove('bear')
boxes[5].append('leaf')
boxes[5].append('sandals')

# Swap the pants in Box 4 with the drum in Box 8.
boxes[4].remove('pants')
boxes[8].remove('drum')
boxes[4].append('drum')
boxes[8].append('pants')

# Swap the leaf in Box 5 with the speaker in Box 0.
boxes[5].remove('leaf')
boxes[0].remove('speaker')
boxes[5].append('speaker')
boxes[0].append('leaf')

# Remove the telescope from Box 2.
boxes[2].remove('telescope')

# Put the dress and the oven into Box 9.
boxes[9].append('dress')
boxes[9].append('oven')

# Remove the dress and the oven from Box 9.
boxes[9].remove('dress')
boxes[9].remove('oven')

# Remove the microwave from Box 2.
boxes[2].remove('microwave')

# Swap the drum in Box 4 with the train in Box 7.
boxes[4].remove('drum')
boxes[7].remove('train')
boxes[4].append('train')
boxes[7].append('drum')

# Move the freezer and the sandals from Box 5 to Box 1.
boxes[5].remove('freezer')
boxes[5].remove('sandals')
boxes[1].append('freezer')
boxes[1].append('sandals')

# Remove the cup and the toothbrush and the pants from Box 8.
boxes[8].remove('cup')
boxes[8].remove('toothbrush')
boxes[8].remove('pants')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")