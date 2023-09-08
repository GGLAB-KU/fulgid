# Initial state of boxes
boxes = {
    0: ['cloud', 'mountain', 'shark', 'lock'],
    1: ['rain', 'battery', 'spoon'],
    2: [],
    3: ['shampoo'],
    4: ['submarine', 'card', 'lipstick'],
    5: ['moon', 'bell', 'violin', 'skirt', 'horse'],
    6: ['seaweed', 'river', 'earring'],
    7: ['microscope', 'coat', 'car'],
    8: ['clock'],
    9: ['starfish', 'sun', 'pants'],
    10: ['storm', 'scarf', 'boot', 'boat'],
    11: ['bracelet', 'comb', 'sculpture', 'butterfly', 'belt'],
    12: ['scissors', 'dress'],
    13: [],
    14: ['bus']
}

# Swap the scarf in Box 10 with the rain in Box 1.
boxes[10].remove('scarf')
boxes[1].remove('rain')
boxes[10].append('rain')
boxes[1].append('scarf')

# Replace the microscope and the car and the coat with the octopus and the bicycle and the plate in Box 7.
boxes[7].remove('microscope')
boxes[7].remove('car')
boxes[7].remove('coat')
boxes[7].append('octopus')
boxes[7].append('bicycle')
boxes[7].append('plate')

# Replace the storm and the boat with the jungle and the clock in Box 10.
boxes[10].remove('storm')
boxes[10].remove('boat')
boxes[10].append('jungle')
boxes[10].append('clock')

# Replace the shark and the cloud and the mountain with the polish and the flower and the shirt in Box 0.
boxes[0].remove('shark')
boxes[0].remove('cloud')
boxes[0].remove('mountain')
boxes[0].append('polish')
boxes[0].append('flower')
boxes[0].append('shirt')

# Move the seaweed from Box 6 to Box 13.
boxes[6].remove('seaweed')
boxes[13].append('seaweed')

# Swap the clock in Box 8 with the starfish in Box 9.
boxes[8].remove('clock')
boxes[9].remove('starfish')
boxes[8].append('starfish')
boxes[9].append('clock')

# Put the boat into Box 4.
boxes[10].remove('boat')
boxes[4].append('boat')

# Replace the battery and the spoon with the starfish and the button in Box 1.
boxes[1].remove('battery')
boxes[1].remove('spoon')
boxes[1].append('starfish')
boxes[1].append('button')

# Replace the shirt and the flower with the fork and the tiger in Box 0.
boxes[0].remove('shirt')
boxes[0].remove('flower')
boxes[0].append('fork')
boxes[0].append('tiger')

# Replace the sun with the note in Box 9.
boxes[9].remove('sun')
boxes[9].append('note')

# Replace the fork and the tiger with the grass and the spoon in Box 0.
boxes[0].remove('fork')
boxes[0].remove('tiger')
boxes[0].append('grass')
boxes[0].append('spoon')

# Put the moon into Box 14.
boxes[5].remove('moon')
boxes[14].append('moon')

# Swap the scarf in Box 1 with the starfish in Box 8.
boxes[1].remove('scarf')
boxes[8].remove('starfish')
boxes[1].append('starfish')
boxes[8].append('scarf')

# Remove the seaweed from Box 13.
boxes[13].remove('seaweed')

# Empty Box 4.
boxes[4] = []

# Remove the scissors and the dress from Box 12.
boxes[12].remove('scissors')
boxes[12].remove('dress')

# Swap the belt in Box 11 with the scarf in Box 8.
boxes[11].remove('belt')
boxes[8].remove('scarf')
boxes[11].append('scarf')
boxes[8].append('belt')

# Put the scissors and the razor and the tape into Box 14.
items_to_move = ['scissors', 'razor', 'tape']
for item in items_to_move:
    boxes[14].append(item)

# Replace the note and the clock with the river and the coral in Box 9.
boxes[9].remove('note')
boxes[9].remove('clock')
boxes[9].append('river')
boxes[9].append('coral')

# Replace the razor and the bus with the jacket and the planet in Box 14.
boxes[14].remove('razor')
boxes[14].remove('bus')
boxes[14].append('jacket')
boxes[14].append('planet')

# Put the oven and the cat and the moon into Box 1.
items_to_move = ['oven', 'cat', 'moon']
for item in items_to_move:
    boxes[1].append(item)

# Swap the rain in Box 10 with the belt in Box 8.
boxes[10].remove('rain')
boxes[8].remove('belt')
boxes[10].append('belt')
boxes[8].append('rain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")