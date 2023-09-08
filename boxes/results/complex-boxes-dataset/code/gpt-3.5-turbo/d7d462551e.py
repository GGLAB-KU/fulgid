# Initial state of boxes
boxes = {
    0: ['toothpaste', 'river'],
    1: ['basket'],
    2: ['makeup', 'dog', 'watch', 'jacket', 'toothbrush'],
    3: ['desert', 'rocket', 'fridge'],
    4: ['branch', 'necklace', 'motorcycle', 'telescope'],
    5: ['skirt'],
    6: ['puzzle', 'cat'],
    7: ['shark', 'vase', 'soap', 'cow', 'toaster'],
    8: [],
    9: ['boot'],
    10: ['jungle', 'flower'],
    11: ['shoes', 'ship', 'needle', 'controller']
}

# Move the jungle and the flower from Box 10 to Box 1.
boxes[10].remove('jungle')
boxes[10].remove('flower')
boxes[1].append('jungle')
boxes[1].append('flower')

# Replace the branch with the mask in Box 4.
boxes[4].remove('branch')
boxes[4].append('mask')

# Put the pillow and the lipstick and the comet into Box 7.
boxes[7].append('pillow')
boxes[7].append('lipstick')
boxes[7].append('comet')

# Put the perfume and the doll into Box 8.
boxes[8].append('perfume')
boxes[8].append('doll')

# Swap the perfume in Box 8 with the mask in Box 4.
boxes[8].remove('perfume')
boxes[4].remove('mask')
boxes[8].append('mask')
boxes[4].append('perfume')

# Swap the lipstick in Box 7 with the mask in Box 8.
boxes[7].remove('lipstick')
boxes[8].remove('mask')
boxes[7].append('mask')
boxes[8].append('lipstick')

# Remove the toothpaste and the river from Box 0.
boxes[0].remove('toothpaste')
boxes[0].remove('river')

# Swap the motorcycle in Box 4 with the lipstick in Box 8.
boxes[4].remove('motorcycle')
boxes[8].remove('lipstick')
boxes[4].append('lipstick')
boxes[8].append('motorcycle')

# Put the meteor and the wig and the necklace into Box 1.
boxes[1].append('meteor')
boxes[1].append('wig')
boxes[1].append('necklace')

# Put the cloud and the fish and the thread into Box 9.
boxes[9].append('cloud')
boxes[9].append('fish')
boxes[9].append('thread')

# Put the forest and the river and the pants into Box 8.
boxes[8].append('forest')
boxes[8].append('river')
boxes[8].append('pants')

# Move the mask and the cow and the shark from Box 7 to Box 4.
boxes[7].remove('mask')
boxes[7].remove('cow')
boxes[7].remove('shark')
boxes[4].append('mask')
boxes[4].append('cow')
boxes[4].append('shark')

# Remove the needle and the controller from Box 11.
boxes[11].remove('needle')
boxes[11].remove('controller')

# Move the cat from Box 6 to Box 0.
boxes[6].remove('cat')
boxes[0].append('cat')

# Put the towel and the clock into Box 6.
boxes[6].append('towel')
boxes[6].append('clock')

# Move the towel and the clock from Box 6 to Box 3.
boxes[6].remove('towel')
boxes[6].remove('clock')
boxes[3].append('towel')
boxes[3].append('clock')

# Swap the jacket in Box 2 with the toaster in Box 7.
boxes[2].remove('jacket')
boxes[7].remove('toaster')
boxes[2].append('toaster')
boxes[7].append('jacket')

# Put the skirt into Box 3.
boxes[5].remove('skirt')
boxes[3].append('skirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")