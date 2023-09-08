# Initial state of boxes
boxes = {
    0: ['sock', 'boot', 'lock', 'gloves'],
    1: [],
    2: ['bell', 'shoes', 'microscope'],
    3: ['needle'],
    4: ['lipstick', 'earring'],
    5: ['skirt', 'mask', 'bracelet', 'plate', 'grass'],
    6: ['shirt'],
    7: ['storm', 'book', 'pants', 'flute'],
    8: ['phone'],
    9: [],
    10: ['dress', 'frame', 'crown', 'moon'],
    11: ['bird', 'bowl', 'mirror', 'horse', 'console'],
    12: ['branch', 'rock', 'spoon', 'harmonica', 'sculpture'],
    13: ['cow', 'freezer', 'violin'],
    14: ['tape', 'cup', 'glove', 'lamp', 'dice']
}

# Move the phone from Box 8 to Box 4.
boxes[8].remove('phone')
boxes[4].append('phone')

# Replace the needle with the pot in Box 3.
boxes[3].remove('needle')
boxes[3].append('pot')

# Remove the skirt and the grass and the plate from Box 5.
items_to_remove = ['skirt', 'grass', 'plate']
for item in items_to_remove:
    boxes[5].remove(item)

# Move the pot from Box 3 to Box 9.
boxes[3].remove('pot')
boxes[9].append('pot')

# Swap the shirt in Box 6 with the dress in Box 10.
boxes[6].remove('shirt')
boxes[10].remove('dress')
boxes[6].append('dress')
boxes[10].append('shirt')

# Move the dress from Box 6 to Box 5.
boxes[6].remove('dress')
boxes[5].append('dress')

# Put the submarine into Box 2.
boxes[2].append('submarine')

# Swap the shoes in Box 2 with the book in Box 7.
boxes[2].remove('shoes')
boxes[7].remove('book')
boxes[2].append('book')
boxes[7].append('shoes')

# Remove the mask and the bracelet and the dress from Box 5.
items_to_remove = ['mask', 'bracelet', 'dress']
for item in items_to_remove:
    boxes[5].remove(item)

# Remove the dice and the lamp from Box 14.
items_to_remove = ['dice', 'lamp']
for item in items_to_remove:
    boxes[14].remove(item)

# Move the submarine and the book from Box 2 to Box 10.
boxes[2].remove('submarine')
boxes[10].append('submarine')
boxes[2].remove('book')
boxes[10].append('book')

# Replace the bowl with the boat in Box 11.
boxes[11].remove('bowl')
boxes[11].append('boat')

# Put the toothbrush into Box 13.
boxes[13].append('toothbrush')

# Replace the pot with the motorcycle in Box 9.
boxes[9].remove('pot')
boxes[9].append('motorcycle')

# Move the microscope from Box 2 to Box 9.
boxes[2].remove('microscope')
boxes[9].append('microscope')

# Remove the cow and the freezer and the toothbrush from Box 13.
items_to_remove = ['cow', 'freezer', 'toothbrush']
for item in items_to_remove:
    boxes[13].remove(item)

# Put the bracelet and the branch into Box 7.
boxes[7].append('bracelet')
boxes[12].remove('branch')
boxes[7].append('branch')

# Replace the cup with the train in Box 14.
boxes[14].remove('cup')
boxes[14].append('train')

# Swap the bell in Box 2 with the train in Box 14.
boxes[2].remove('bell')
boxes[14].remove('train')
boxes[2].append('train')
boxes[14].append('bell')

# Put the battery into Box 4.
boxes[4].append('battery')

# Put the frame and the dolphin and the coral into Box 13.
boxes[10].remove('frame')
boxes[13].append('frame')
boxes[13].append('dolphin')
boxes[13].append('coral')

# Move the train from Box 2 to Box 5.
boxes[2].remove('train')
boxes[5].append('train')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")