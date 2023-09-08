# Initial state of boxes
boxes = {
    0: ['boat', 'rain', 'toy', 'snow', 'fridge'],
    1: [],
    2: ['spoon', 'apple', 'beach', 'cup', 'lock'],
    3: [],
    4: ['harmonica', 'pants', 'candle'],
    5: ['horse', 'camera', 'mirror', 'table', 'dress'],
    6: ['toothpaste', 'toothbrush'],
    7: ['elephant', 'controller', 'razor', 'microwave'],
    8: ['necklace', 'sun'],
    9: ['storm'],
    10: ['zipper', 'freezer', 'thunder', 'phone', 'star'],
    11: []
}

# Swap the toothpaste in Box 6 with the toy in Box 0.
boxes[0].remove('toy')
boxes[6].remove('toothpaste')
boxes[0].append('toothpaste')
boxes[6].append('toy')

# Swap the dress in Box 5 with the storm in Box 9.
boxes[5].remove('dress')
boxes[9].remove('storm')
boxes[5].append('storm')
boxes[9].append('dress')

# Remove the toy from Box 6.
boxes[6].remove('toy')

# Move the microwave and the controller and the razor from Box 7 to Box 10.
items_to_move = ['microwave', 'controller', 'razor']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[10].append(item)

# Swap the mirror in Box 5 with the snow in Box 0.
boxes[0].remove('snow')
boxes[5].remove('mirror')
boxes[0].append('mirror')
boxes[5].append('snow')

# Swap the beach in Box 2 with the elephant in Box 7.
boxes[2].remove('beach')
boxes[7].remove('elephant')
boxes[2].append('elephant')
boxes[7].append('beach')

# Remove the beach from Box 7.
boxes[7].remove('beach')

# Remove the toothbrush from Box 6.
boxes[6].remove('toothbrush')

# Remove the sun and the necklace from Box 8.
boxes[8].remove('sun')
boxes[8].remove('necklace')

# Remove the cup and the apple and the lock from Box 2.
items_to_remove = ['cup', 'apple', 'lock']
for item in items_to_remove:
    boxes[2].remove(item)

# Move the star and the razor and the thunder from Box 10 to Box 8.
items_to_move = ['star', 'razor', 'thunder']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[8].append(item)

# Swap the dress in Box 9 with the horse in Box 5.
boxes[5].remove('horse')
boxes[9].remove('dress')
boxes[5].append('dress')
boxes[9].append('horse')

# Remove the horse from Box 9.
boxes[9].remove('horse')

# Remove the star from Box 8.
boxes[8].remove('star')

# Replace the controller and the zipper and the phone with the hat and the sculpture and the paint in Box 10.
boxes[10].remove('controller')
boxes[10].remove('zipper')
boxes[10].remove('phone')
boxes[10].append('hat')
boxes[10].append('sculpture')
boxes[10].append('paint')

# Replace the pants with the meteor in Box 4.
boxes[4].remove('pants')
boxes[4].append('meteor')

# Replace the elephant with the perfume in Box 2.
boxes[2].remove('elephant')
boxes[2].append('perfume')

# Swap the freezer in Box 10 with the perfume in Box 2.
boxes[10].remove('freezer')
boxes[2].remove('perfume')
boxes[10].append('perfume')
boxes[2].append('freezer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")