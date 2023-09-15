box_0 = ['gloves', 'pen', 'desert', 'bowl', 'jungle']
box_1 = ['elephant', 'chair', 'piano', 'cow']
box_2 = ['rocket', 'razor', 'bracelet', 'bag']
box_3 = ['fish', 'butterfly', 'sandals']
box_4 = ['jacket', 'wallet', 'table', 'bicycle']
box_5 = ['moon', 'pot', 'clock', 'dolphin', 'necklace']
box_6 = ['mixer', 'swimsuit', 'coral', 'card']
box_7 = ['mask', 'flute', 'skirt', 'beach']
box_8 = ['plane', 'lock', 'perfume', 'pants']
box_9 = ['shampoo', 'camera']

def print_boxes():
    for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9]):
        print(f"Box {i}: {box}")

print_boxes()

# Move the cow and the elephant and the piano from Box 1 to Box 0
box_0.extend(box_1.pop(box_1.index('cow')))
box_0.extend(box_1.pop(box_1.index('elephant')))
box_0.extend(box_1.pop(box_1.index('piano')))

# Move the chair from Box 1 to Box 5
box_5.append(box_1.pop(box_1.index('chair')))

# Empty Box 8
box_8 = []

# Remove the cow from Box 0
box_0.remove('cow')

# Move the piano and the jungle and the gloves from Box 0 to Box 9
box_9.extend(box_0.pop(box_0.index('piano')))
box_9.extend(box_0.pop(box_0.index('jungle')))
box_9.extend(box_0.pop(box_0.index('gloves')))

# Remove the elephant from Box 0
box_0.remove('elephant')

# Swap the bicycle in Box 4 with the rocket in Box 2
box_4[box_4.index('bicycle')], box_2[box_2.index('rocket')] = box_2[box_2.index('rocket')], box_4[box_4.index('bicycle')]

# Replace the mask and the skirt and the flute with the camera and the snow and the boot in Box 7
box_7[box_7.index('mask')] = 'camera'
box_7[box_7.index('skirt')] = 'snow'
box_7[box_7.index('flute')] = 'boot'

# Remove the pen and the desert from Box 0
box_0.remove('pen')
box_0.remove('desert')

# Remove the bowl from Box 0
box_0.remove('bowl')

# Replace the necklace and the pot with the beach and the scarf in Box 5
box_5[box_5.index('necklace')] = 'beach'
box_5[box_5.index('pot')] = 'scarf'

# Remove the snow and the boot and the camera from Box 7
box_7.remove('snow')
box_7.remove('boot')
box_7.remove('camera')

# Empty Box 6
box_6 = []

# Remove the fish from Box 3
box_3.remove('fish')

# Move the bracelet from Box 2 to Box 8
box_8.append(box_2.pop(box_2.index('bracelet')))

print_boxes()