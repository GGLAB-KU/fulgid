# Initial state of boxes
boxes = {
    0: ['toothpaste', 'frame', 'lightning', 'magnet'],
    1: [],
    2: ['scarf', 'pot'],
    3: ['fish', 'cat', 'dog', 'belt', 'shelf'],
    4: ['harmonica', 'seaweed'],
    5: ['tie'],
    6: ['island', 'scissors', 'branch'],
    7: [],
    8: ['comet'],
    9: [],
    10: ['ring', 'dress'],
    11: ['mask', 'bear', 'tiger'],
    12: ['apple', 'bracelet']
}

# Swap the fish in Box 3 with the lightning in Box 0.
boxes[3].remove('fish')
boxes[0].remove('lightning')
boxes[3].append('lightning')
boxes[0].append('fish')

# Put the gloves into Box 11.
boxes[11].append('gloves')

# Put the leaf and the toy into Box 12.
boxes[12].append('leaf')
boxes[12].append('toy')

# Replace the tie with the pants in Box 5.
boxes[5].remove('tie')
boxes[5].append('pants')

# Swap the scissors in Box 6 with the scarf in Box 2.
boxes[6].remove('scissors')
boxes[2].remove('scarf')
boxes[6].append('scarf')
boxes[2].append('scissors')

# Move the ring and the dress from Box 10 to Box 6.
boxes[10].remove('ring')
boxes[10].remove('dress')
boxes[6].append('ring')
boxes[6].append('dress')

# Move the dress from Box 6 to Box 9.
boxes[6].remove('dress')
boxes[9].append('dress')

# Remove the apple from Box 12.
boxes[12].remove('apple')

# Replace the toy and the bracelet with the dolphin and the toothbrush in Box 12.
boxes[12].remove('toy')
boxes[12].remove('bracelet')
boxes[12].append('dolphin')
boxes[12].append('toothbrush')

# Move the scarf and the branch and the island from Box 6 to Box 11.
items_to_move = ['scarf', 'branch', 'island']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[11].append(item)

# Remove the dress from Box 9.
boxes[9].remove('dress')

# Replace the pants with the zipper in Box 5.
boxes[5].remove('pants')
boxes[5].append('zipper')

# Replace the ring with the island in Box 6.
boxes[6].remove('ring')
boxes[6].append('island')

# Remove the seaweed and the harmonica from Box 4.
boxes[4].remove('seaweed')
boxes[4].remove('harmonica')

# Swap the toothbrush in Box 12 with the island in Box 6.
boxes[12].remove('toothbrush')
boxes[6].remove('island')
boxes[12].append('island')
boxes[6].append('toothbrush')

# Remove the leaf and the island from Box 12.
boxes[12].remove('leaf')
boxes[12].remove('island')

# Remove the pot and the scissors from Box 2.
boxes[2].remove('pot')
boxes[2].remove('scissors')

# Swap the zipper in Box 5 with the frame in Box 0.
boxes[5].remove('zipper')
boxes[0].remove('frame')
boxes[5].append('frame')
boxes[0].append('zipper')

# Remove the toothbrush from Box 6.
boxes[6].remove('toothbrush')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")