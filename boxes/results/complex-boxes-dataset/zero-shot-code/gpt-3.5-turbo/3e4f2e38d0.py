box_0 = ['sandals', 'laptop', 'console', 'blanket']
box_1 = ['doll', 'wallet', 'toothpaste', 'pillow']
box_2 = ['train', 'truck', 'branch', 'desert']
box_3 = ['coral']
box_4 = ['phone', 'chair']
box_5 = ['key']
box_6 = ['belt', 'scarf', 'lock', 'car', 'planet']
box_7 = ['bell']
box_8 = ['pot']
box_9 = ['blender', 'tiger']
box_10 = ['watch', 'card', 'basket', 'elephant', 'lipstick']
box_11 = ['river']

def print_box(box_index, box_items):
    if len(box_items) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box_items}")

# Swap the pillow in Box 1 with the planet in Box 6
box_1[box_1.index('pillow')] = box_6.pop(box_6.index('planet'))
print_box(1, box_1)
print_box(6, box_6)

# Empty Box 5
box_5 = []
print_box(5, box_5)

# Replace the tiger and the blender with the harmonica and the vase in Box 9
box_9.remove('tiger')
box_9.remove('blender')
box_9.extend(['harmonica', 'vase'])
print_box(9, box_9)

# Replace the wallet and the doll and the toothpaste with the scarf and the whistle and the microwave in Box 1
box_1.remove('wallet')
box_1.remove('doll')
box_1.remove('toothpaste')
box_1.extend(['scarf', 'whistle', 'microwave'])
print_box(1, box_1)

# Put the drum into Box 5
box_5.append('drum')
print_box(5, box_5)

# Remove the desert and the branch from Box 2
box_2.remove('desert')
box_2.remove('branch')
print_box(2, box_2)

# Empty Box 11
box_11 = []
print_box(11, box_11)

# Replace the bell with the sock in Box 7
box_7[box_7.index('bell')] = 'sock'
print_box(7, box_7)

# Move the chair and the phone from Box 4 to Box 11
box_11.extend([box_4.pop(box_4.index('chair')), box_4.pop(box_4.index('phone'))])
print_box(4, box_4)
print_box(11, box_11)

# Swap the scarf in Box 6 with the drum in Box 5
box_6[box_6.index('scarf')] = box_5.pop(box_5.index('drum'))
box_5.append('scarf')
print_box(5, box_5)
print_box(6, box_6)

# Replace the blanket with the camera in Box 0
box_0[box_0.index('blanket')] = 'camera'
print_box(0, box_0)

# Swap the truck in Box 2 with the drum in Box 6
box_2[box_2.index('truck')] = box_6.pop(box_6.index('drum'))
box_6.append('truck')
print_box(2, box_2)
print_box(6, box_6)

# Remove the lock from Box 6
box_6.remove('lock')
print_box(6, box_6)

# Put the mask and the bracelet and the pot into Box 0
box_0.extend(['mask', 'bracelet', 'pot'])
print_box(0, box_0)

# Swap the planet in Box 1 with the drum in Box 2
box_1[box_1.index('planet')] = box_2.pop(box_2.index('drum'))
box_2.append('planet')
print_box(1, box_1)
print_box(2, box_2)

# Replace the sock with the dice in Box 7
box_7[box_7.index('sock')] = 'dice'
print_box(7, box_7)

# Put the candle into Box 0
box_0.append('candle')
print_box(0, box_0)

# Remove the card from Box 10
box_10.remove('card')
print_box(10, box_10)