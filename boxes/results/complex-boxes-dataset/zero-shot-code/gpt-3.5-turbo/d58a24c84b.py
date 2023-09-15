box_0 = ['lightning', 'rocket', 'toothpaste']
box_1 = ['star', 'snow', 'butterfly', 'soap', 'puzzle']
box_2 = ['ship', 'scarf']
box_3 = ['chair']
box_4 = []
box_5 = []
box_6 = ['telescope', 'book', 'boat', 'candle', 'gloves']
box_7 = []
box_8 = ['crown', 'violin', 'perfume', 'train', 'razor']
box_9 = ['glasses', 'makeup', 'guitar']
box_10 = ['vase']

def print_boxes():
    boxes = [box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10]
    for i, box in enumerate(boxes):
        print(f"Box {i}: {box}")

# Initial state
print_boxes()

# Swap ship in Box 2 with vase in Box 10
box_2.remove('ship')
box_10.remove('vase')
box_2.append('vase')
box_10.append('ship')

# Put elephant and cup into Box 4
box_4.extend(['elephant', 'cup'])

# Remove telescope and book from Box 6
box_6.remove('telescope')
box_6.remove('book')

# Move vase and scarf from Box 2 to Box 6
box_2.remove('vase')
box_2.remove('scarf')
box_6.extend(['vase', 'scarf'])

# Remove train, violin, and razor from Box 8
box_8.remove('train')
box_8.remove('violin')
box_8.remove('razor')

# Put ship, octopus, and star into Box 6
box_6.extend(['ship', 'octopus', 'star'])

# Remove gloves from Box 6
box_6.remove('gloves')

# Swap guitar in Box 9 with perfume in Box 8
box_9.remove('guitar')
box_8.remove('perfume')
box_9.append('perfume')
box_8.append('guitar')

# Swap puzzle in Box 1 with cup in Box 4
box_1.remove('puzzle')
box_4.remove('cup')
box_1.append('cup')
box_4.append('puzzle')

# Put lamp, gloves, and bear into Box 0
box_0.extend(['lamp', 'gloves', 'bear'])

# Swap octopus in Box 6 with guitar in Box 8
box_6.remove('octopus')
box_8.remove('guitar')
box_6.append('guitar')
box_8.append('octopus')

# Replace chair with desert in Box 3
box_3.remove('chair')
box_3.append('desert')

# Swap octopus in Box 8 with puzzle in Box 4
box_8.remove('octopus')
box_4.remove('puzzle')
box_8.append('puzzle')
box_4.append('octopus')

# Swap octopus in Box 4 with star in Box 1
box_4.remove('octopus')
box_1.remove('star')
box_4.append('star')
box_1.append('octopus')

# Swap desert in Box 3 with ship in Box 10
box_3.remove('desert')
box_10.remove('ship')
box_3.append('ship')
box_10.append('desert')

# Swap glasses in Box 9 with desert in Box 10
box_9.remove('glasses')
box_10.remove('desert')
box_9.append('desert')
box_10.append('glasses')

# Replace glasses with cloud in Box 10
box_10.remove('glasses')
box_10.append('cloud')

# Final state
print_boxes()