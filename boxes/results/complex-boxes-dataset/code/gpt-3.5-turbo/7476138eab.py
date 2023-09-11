# Initial state of boxes
boxes = {
    0: ['zipper', 'pillow', 'star'],
    1: ['needle'],
    2: [],
    3: ['soap', 'tiger', 'watch', 'truck'],
    4: ['console', 'wig', 'shirt', 'basket'],
    5: ['freezer', 'wire', 'boat', 'bracelet', 'river'],
    6: ['headphone', 'shelf', 'scissors', 'harmonica', 'blender']
}

# Swap the zipper in Box 0 with the needle in Box 1.
boxes[0].remove('zipper')
boxes[1].remove('needle')
boxes[0].append('needle')
boxes[1].append('zipper')

# Swap the wire in Box 5 with the scissors in Box 6.
boxes[5].remove('wire')
boxes[6].remove('scissors')
boxes[5].append('scissors')
boxes[6].append('wire')

# Move the shirt and the basket from Box 4 to Box 3.
items_to_move = ['shirt', 'basket']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Move the wire and the headphone and the shelf from Box 6 to Box 2.
items_to_move = ['wire', 'headphone', 'shelf']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[2].append(item)

# Empty Box 3.
boxes[3] = []

# Move the freezer and the bracelet and the scissors from Box 5 to Box 4.
items_to_move = ['freezer', 'bracelet', 'scissors']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Move the zipper from Box 1 to Box 3.
boxes[1].remove('zipper')
boxes[3].append('zipper')

# Move the needle and the star from Box 0 to Box 1.
boxes[0].remove('needle')
boxes[0].remove('star')
boxes[1].append('needle')
boxes[1].append('star')

# Remove the zipper from Box 3.
boxes[3].remove('zipper')

# Remove the shelf and the headphone from Box 2.
boxes[2].remove('shelf')
boxes[2].remove('headphone')

# Move the pillow from Box 0 to Box 4.
boxes[0].remove('pillow')
boxes[4].append('pillow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")