# Initial state of boxes
boxes = {
    0: ['ring', 'apple'],
    1: ['shirt'],
    2: ['sock', 'coral', 'butterfly', 'candle'],
    3: [],
    4: [],
    5: ['planet', 'shampoo', 'rocket', 'dress'],
    6: ['paint', 'motorcycle', 'tie']
}

# Replace the butterfly and the coral and the candle with the fridge and the coin and the train in Box 2.
boxes[2].remove('butterfly')
boxes[2].remove('coral')
boxes[2].remove('candle')
boxes[2].append('fridge')
boxes[2].append('coin')
boxes[2].append('train')

# Put the toothbrush and the lion and the bird into Box 5.
boxes[5].append('toothbrush')
boxes[5].append('lion')
boxes[5].append('bird')

# Replace the ring and the apple with the bracelet and the mask in Box 0.
boxes[0].remove('ring')
boxes[0].remove('apple')
boxes[0].append('bracelet')
boxes[0].append('mask')

# Move the motorcycle and the tie from Box 6 to Box 4.
boxes[6].remove('motorcycle')
boxes[6].remove('tie')
boxes[4].append('motorcycle')
boxes[4].append('tie')

# Remove the shirt from Box 1.
boxes[1].remove('shirt')

# Replace the train with the console in Box 2.
boxes[2].remove('train')
boxes[2].append('console')

# Put the toothpaste and the bird into Box 4.
boxes[4].append('toothpaste')
boxes[4].append('bird')

# Replace the paint with the pan in Box 6.
boxes[6].remove('paint')
boxes[6].append('pan')

# Remove the tie from Box 4.
boxes[4].remove('tie')

# Move the toothpaste and the motorcycle and the bird from Box 4 to Box 0.
items_to_move = ['toothpaste', 'motorcycle', 'bird']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")