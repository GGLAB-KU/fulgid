# Initial state of boxes
boxes = {
    0: ['keyboard', 'battery', 'razor', 'toaster'],
    1: ['frame'],
    2: [],
    3: ['starfish', 'microwave'],
    4: ['controller', 'fork', 'necklace', 'glove', 'leaf'],
    5: ['guitar', 'scissors', 'jacket', 'horse'],
    6: ['soap', 'basket'],
    7: ['freezer', 'button', 'piano'],
    8: ['car', 'candle'],
    9: [],
    10: ['lipstick', 'harmonica', 'swimsuit', 'towel'],
    11: [],
    12: ['dog'],
    13: ['makeup', 'card']
}

# Put the shampoo and the cow and the bear into Box 13.
boxes[13].append('shampoo')
boxes[13].append('cow')
boxes[13].append('bear')

# Remove the scissors and the guitar and the horse from Box 5.
items_to_remove = ['scissors', 'guitar', 'horse']
for item in items_to_remove:
    boxes[5].remove(item)

# Replace the towel with the pan in Box 10.
boxes[10].remove('towel')
boxes[10].append('pan')

# Replace the car with the shelf in Box 8.
boxes[8].remove('car')
boxes[8].append('shelf')

# Put the sock into Box 9.
boxes[9].append('sock')

# Replace the shelf and the candle with the scarf and the fish in Box 8.
boxes[8].remove('shelf')
boxes[8].remove('candle')
boxes[8].append('scarf')
boxes[8].append('fish')

# Move the swimsuit and the lipstick from Box 10 to Box 0.
items_to_move = ['swimsuit', 'lipstick']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[0].append(item)

# Swap the starfish in Box 3 with the keyboard in Box 0.
boxes[0].remove('keyboard')
boxes[3].remove('starfish')
boxes[0].append('starfish')
boxes[3].append('keyboard')

# Put the gloves into Box 12.
boxes[12].append('gloves')

# Move the button and the freezer and the piano from Box 7 to Box 6.
items_to_move = ['button', 'freezer', 'piano']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[6].append(item)

# Move the soap and the freezer and the button from Box 6 to Box 8.
items_to_move = ['soap', 'freezer', 'button']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[8].append(item)

# Remove the frame from Box 1.
boxes[1].remove('frame')

# Move the pan and the harmonica from Box 10 to Box 13.
items_to_move = ['pan', 'harmonica']
for item in items_to_move:
    boxes[10].remove(item)
    boxes[13].append(item)

# Empty Box 9.
boxes[9] = []

# Put the shorts and the doll into Box 11.
boxes[11].append('shorts')
boxes[11].append('doll')

# Remove the razor and the battery and the lipstick from Box 0.
items_to_remove = ['razor', 'battery', 'lipstick']
for item in items_to_remove:
    boxes[0].remove(item)

# Empty Box 6.
boxes[6] = []

# Empty Box 11.
boxes[11] = []

# Move the jacket from Box 5 to Box 4.
boxes[5].remove('jacket')
boxes[4].append('jacket')

# Move the necklace and the controller and the fork from Box 4 to Box 11.
items_to_move = ['necklace', 'controller', 'fork']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[11].append(item)

# Move the pan and the cow and the makeup from Box 13 to Box 2.
items_to_move = ['pan', 'cow', 'makeup']
for item in items_to_move:
    boxes[13].remove(item)
    boxes[2].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")