# Initial state of boxes
boxes = {
    0: ['basket'],
    1: ['cat', 'rocket'],
    2: ['tie', 'bowl'],
    3: ['wire', 'bracelet', 'horse'],
    4: ['coin'],
    5: [],
    6: ['button', 'comet'],
    7: ['river', 'skirt', 'pot'],
    8: ['sandals', 'thread'],
    9: [],
    10: []
}

# Swap the basket in Box 0 with the coin in Box 4.
boxes[0].remove('basket')
boxes[4].remove('coin')
boxes[0].append('coin')
boxes[4].append('basket')

# Replace the coin with the bracelet in Box 0.
boxes[0].remove('coin')
boxes[0].append('bracelet')

# Replace the wire with the microwave in Box 3.
boxes[3].remove('wire')
boxes[3].append('microwave')

# Put the usb into Box 1.
boxes[1].append('usb')

# Put the jacket and the cloud and the toy into Box 7.
boxes[7].append('jacket')
boxes[7].append('cloud')
boxes[7].append('toy')

# Remove the bowl from Box 2.
boxes[2].remove('bowl')

# Swap the bracelet in Box 0 with the tie in Box 2.
boxes[0].remove('bracelet')
boxes[2].remove('tie')
boxes[0].append('tie')
boxes[2].append('bracelet')

# Remove the usb and the rocket from Box 1.
boxes[1].remove('usb')
boxes[1].remove('rocket')

# Put the laptop and the shampoo into Box 6.
boxes[6].append('laptop')
boxes[6].append('shampoo')

# Replace the thread and the sandals with the watch and the mixer in Box 8.
boxes[8].remove('thread')
boxes[8].remove('sandals')
boxes[8].append('watch')
boxes[8].append('mixer')

# Remove the tie from Box 0.
boxes[0].remove('tie')

# Swap the bracelet in Box 2 with the basket in Box 4.
boxes[2].remove('bracelet')
boxes[4].remove('basket')
boxes[2].append('basket')
boxes[4].append('bracelet')

# Replace the bracelet and the horse with the moon and the starfish in Box 3.
boxes[3].remove('bracelet')
boxes[3].remove('horse')
boxes[3].append('moon')
boxes[3].append('starfish')

# Remove the mixer from Box 8.
boxes[8].remove('mixer')

# Replace the starfish and the microwave with the battery and the guitar in Box 3.
boxes[3].remove('starfish')
boxes[3].remove('microwave')
boxes[3].append('battery')
boxes[3].append('guitar')

# Swap the cat in Box 1 with the button in Box 6.
boxes[1].remove('cat')
boxes[6].remove('button')
boxes[1].append('button')
boxes[6].append('cat')

# Move the basket from Box 2 to Box 0.
boxes[2].remove('basket')
boxes[0].append('basket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")