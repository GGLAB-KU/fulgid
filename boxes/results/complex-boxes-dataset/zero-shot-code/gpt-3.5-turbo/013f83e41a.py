box = {
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

def print_boxes():
    for i in range(11):
        if box[i]:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Swap the basket in Box 0 with the coin in Box 4
box[0], box[4] = box[4], box[0]

# Replace the coin with the bracelet in Box 0
box[0] = box[0] + box[4]
box[4] = []

# Replace the wire with the microwave in Box 3
box[3] = ['microwave'] + box[3]
box[3].remove('wire')

# Put the usb into Box 1
box[1].append('usb')

# Put the jacket and the cloud and the toy into Box 7
box[7] = box[7] + ['jacket', 'cloud', 'toy']

# Remove the bowl from Box 2
box[2].remove('bowl')

# Swap the bracelet in Box 0 with the tie in Box 2
box[0], box[2] = box[2], box[0]

# Remove the usb and the rocket from Box 1
box[1].remove('usb')
box[1].remove('rocket')

# Put the laptop and the shampoo into Box 6
box[6] = box[6] + ['laptop', 'shampoo']

# Replace the thread and the sandals with the watch and the mixer in Box 8
box[8] = ['watch', 'mixer']
box[8] = box[8] + box[8]

# Remove the tie from Box 0
box[0].remove('tie')

# Swap the bracelet in Box 2 with the basket in Box 4
box[2], box[4] = box[4], box[2]

# Replace the bracelet and the horse with the moon and the starfish in Box 3
box[3] = ['moon', 'starfish']
box[3] = box[3] + box[3]

# Remove the mixer from Box 8
box[8].remove('mixer')

# Replace the starfish and the microwave with the battery and the guitar in Box 3
box[3] = ['battery', 'guitar']
box[3] = box[3] + box[3]

# Swap the cat in Box 1 with the button in Box 6
box[1], box[6] = box[6], box[1]

# Move the basket from Box 2 to Box 0
box[0] = box[0] + box[2]
box[2] = []

print_boxes()