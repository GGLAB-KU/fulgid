# Initial state of boxes
boxes = {
    0: ['card', 'horse', 'brush', 'leaf', 'seaweed'],
    1: ['comb', 'train', 'perfume', 'mountain', 'apple'],
    2: ['toaster', 'gloves', 'shoe', 'pants', 'controller'],
    3: ['cat', 'branch', 'boot'],
    4: ['lamp', 'plane'],
    5: ['watch', 'bag', 'hat', 'dice', 'speaker'],
    6: ['frame', 'dog', 'grinder', 'tie', 'doll'],
    7: [],
    8: ['book', 'oven']
}

# Put the motorcycle into Box 6.
boxes[6].append('motorcycle')

# Swap the book in Box 8 with the lamp in Box 4.
boxes[8].remove('book')
boxes[4].remove('lamp')
boxes[8].append('lamp')
boxes[4].append('book')

# Move the plane and the book from Box 4 to Box 2.
items_to_move = ['plane', 'book']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Remove the boot and the branch and the cat from Box 3.
items_to_remove = ['boot', 'branch', 'cat']
for item in items_to_remove:
    boxes[3].remove(item)

# Replace the apple and the perfume with the blanket and the zipper in Box 1.
boxes[1].remove('apple')
boxes[1].remove('perfume')
boxes[1].append('blanket')
boxes[1].append('zipper')

# Empty Box 8.
boxes[8] = []

# Replace the gloves and the shoe with the dice and the sun in Box 2.
boxes[2].remove('gloves')
boxes[2].remove('shoe')
boxes[2].append('dice')
boxes[2].append('sun')

# Swap the sun in Box 2 with the tie in Box 6.
boxes[2].remove('sun')
boxes[6].remove('tie')
boxes[2].append('tie')
boxes[6].append('sun')

# Remove the frame from Box 6.
boxes[6].remove('frame')

# Put the mountain and the coral and the thunder into Box 2.
items_to_add = ['mountain', 'coral', 'thunder']
for item in items_to_add:
    boxes[2].append(item)

# Remove the speaker and the hat from Box 5.
items_to_remove = ['speaker', 'hat']
for item in items_to_remove:
    boxes[5].remove(item)

# Replace the card and the seaweed with the soap and the rain in Box 0.
boxes[0].remove('card')
boxes[0].remove('seaweed')
boxes[0].append('soap')
boxes[0].append('rain')

# Put the lion and the towel into Box 1.
boxes[1].append('lion')
boxes[1].append('towel')

# Swap the train in Box 1 with the leaf in Box 0.
boxes[1].remove('train')
boxes[0].remove('leaf')
boxes[1].append('leaf')
boxes[0].append('train')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")