# Initial state of boxes
boxes = {
    0: ['paint', 'dice'],
    1: ['sculpture', 'grass', 'coral', 'shoe'],
    2: ['scarf'],
    3: ['sun', 'toothpaste', 'rock', 'leaf', 'tie'],
    4: ['speaker', 'helmet', 'mixer', 'laptop'],
    5: ['seaweed', 'phone', 'earring', 'note'],
    6: []
}

# Remove the mixer and the speaker and the laptop from Box 4.
boxes[4].remove('mixer')
boxes[4].remove('speaker')
boxes[4].remove('laptop')

# Remove the helmet from Box 4.
boxes[4].remove('helmet')

# Swap the dice in Box 0 with the scarf in Box 2.
boxes[0].remove('dice')
boxes[2].remove('scarf')
boxes[0].append('scarf')
boxes[2].append('dice')

# Replace the seaweed and the note and the phone with the bicycle and the fish and the desert in Box 5.
boxes[5].remove('seaweed')
boxes[5].remove('note')
boxes[5].remove('phone')
boxes[5].append('bicycle')
boxes[5].append('fish')
boxes[5].append('desert')

# Remove the scarf from Box 0.
boxes[0].remove('scarf')

# Move the dice from Box 2 to Box 0.
boxes[2].remove('dice')
boxes[0].append('dice')

# Remove the paint and the dice from Box 0.
boxes[0].remove('paint')
boxes[0].remove('dice')

# Put the island into Box 4.
boxes[4].append('island')

# Put the umbrella and the lion and the lock into Box 3.
boxes[3].append('umbrella')
boxes[3].append('lion')
boxes[3].append('lock')

# Remove the earring and the bicycle from Box 5.
boxes[5].remove('earring')
boxes[5].remove('bicycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")