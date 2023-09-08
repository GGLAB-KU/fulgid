# Initial state of boxes
boxes = {
    0: ['crown', 'charger'],
    1: ['card', 'cow', 'game', 'dog', 'pot'],
    2: ['speaker', 'sculpture', 'truck', 'telescope', 'bus'],
    3: [],
    4: ['console', 'usb'],
    5: ['blanket'],
    6: ['paint', 'car', 'toothpaste'],
    7: ['horn', 'plane'],
    8: [],
    9: ['island'],
    10: ['mixer', 'meteor'],
    11: ['note', 'submarine'],
    12: ['polish', 'fork', 'ship', 'coral', 'mirror']
}

# Swap the ship in Box 12 with the island in Box 9.
boxes[12].remove('ship')
boxes[9].remove('island')
boxes[12].append('island')
boxes[9].append('ship')

# Remove the bus and the speaker from Box 2.
boxes[2].remove('bus')
boxes[2].remove('speaker')

# Replace the blanket with the shark in Box 5.
boxes[5].remove('blanket')
boxes[5].append('shark')

# Remove the meteor from Box 10.
boxes[10].remove('meteor')

# Remove the mixer from Box 10.
boxes[10].remove('mixer')

# Remove the pot and the card from Box 1.
boxes[1].remove('pot')
boxes[1].remove('card')

# Remove the ship from Box 9.
boxes[9].remove('ship')

# Replace the game and the cow with the river and the clock in Box 1.
boxes[1].remove('game')
boxes[1].remove('cow')
boxes[1].append('river')
boxes[1].append('clock')

# Swap the console in Box 4 with the dog in Box 1.
boxes[4].remove('console')
boxes[1].remove('dog')
boxes[4].append('dog')
boxes[1].append('console')

# Replace the sculpture with the oven in Box 2.
boxes[2].remove('sculpture')
boxes[2].append('oven')

# Swap the telescope in Box 2 with the charger in Box 0.
boxes[2].remove('telescope')
boxes[0].remove('charger')
boxes[2].append('charger')
boxes[0].append('telescope')

# Put the jacket and the charger and the thread into Box 3.
items_to_move = ['jacket', 'charger', 'thread']
for item in items_to_move:
    boxes[3].append(item)

# Replace the usb and the dog with the zipper and the plate in Box 4.
boxes[4].remove('usb')
boxes[1].remove('dog')
boxes[4].append('zipper')
boxes[1].append('plate')

# Swap the zipper in Box 4 with the note in Box 11.
boxes[4].remove('zipper')
boxes[11].remove('note')
boxes[4].append('note')
boxes[11].append('zipper')

# Remove the submarine and the zipper from Box 11.
boxes[11].remove('submarine')
boxes[11].remove('zipper')

# Remove the console and the clock from Box 1.
boxes[1].remove('console')
boxes[1].remove('clock')

# Swap the coral in Box 12 with the plane in Box 7.
boxes[12].remove('coral')
boxes[7].remove('plane')
boxes[12].append('plane')
boxes[7].append('coral')

# Replace the truck and the oven with the leaf and the shirt in Box 2.
boxes[2].remove('truck')
boxes[2].remove('oven')
boxes[2].append('leaf')
boxes[2].append('shirt')

# Move the note and the plate from Box 4 to Box 7.
boxes[4].remove('note')
boxes[4].remove('plate')
boxes[7].append('note')
boxes[7].append('plate')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")