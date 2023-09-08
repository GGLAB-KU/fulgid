# Initial state of boxes
boxes = {
    0: ['camera', 'jungle', 'toaster', 'fork'],
    1: ['bag', 'skirt', 'horse', 'thread'],
    2: ['ocean', 'scarf', 'truck'],
    3: ['coat', 'speaker', 'candle', 'comet'],
    4: ['swimsuit', 'chair', 'desert'],
    5: [],
    6: ['meteor', 'book'],
    7: ['harmonica', 'scissors', 'river', 'pants', 'umbrella'],
    8: ['shorts', 'rocket', 'toy', 'usb']
}

# Move the thread and the bag and the skirt from Box 1 to Box 4.
items_to_move = ['thread', 'bag', 'skirt']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Put the crown and the belt into Box 2.
boxes[2].append('crown')
boxes[2].append('belt')

# Move the horse from Box 1 to Box 7.
boxes[1].remove('horse')
boxes[7].append('horse')

# Empty Box 0.
boxes[0] = []

# Replace the thread with the usb in Box 4.
boxes[4].remove('thread')
boxes[4].append('usb')

# Move the candle and the comet from Box 3 to Box 0.
items_to_move = ['candle', 'comet']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Swap the meteor in Box 6 with the usb in Box 8.
boxes[6].remove('meteor')
boxes[8].remove('usb')
boxes[6].append('usb')
boxes[8].append('meteor')

# Move the scarf from Box 2 to Box 8.
boxes[2].remove('scarf')
boxes[8].append('scarf')

# Move the ocean and the belt from Box 2 to Box 4.
items_to_move = ['ocean', 'belt']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[4].append(item)

# Put the usb into Box 5.
boxes[5].append('usb')

# Remove the candle from Box 0.
boxes[0].remove('candle')

# Replace the coat and the speaker with the whistle and the cloud in Box 3.
boxes[3].remove('coat')
boxes[3].remove('speaker')
boxes[3].append('whistle')
boxes[3].append('cloud')

# Put the fork into Box 4.
boxes[4].append('fork')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")