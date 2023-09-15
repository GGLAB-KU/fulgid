box_0 = ['frame', 'pot', 'starfish', 'coat', 'mask']
box_1 = ['note', 'boot', 'needle', 'toothbrush', 'branch']
box_2 = ['ocean', 'meteor']
box_3 = ['shark', 'candle', 'horn', 'swimsuit', 'beach']
box_4 = ['laptop', 'rock', 'shoes', 'speaker', 'glasses']
box_5 = ['sock']
box_6 = ['mixer', 'tree', 'clock', 'shampoo', 'bell']
box_7 = ['glove', 'dolphin', 'necklace', 'leaf', 'comb']
box_8 = ['boat', 'wire', 'bicycle']
box_9 = ['cat', 'freezer']
box_10 = ['drum', 'microscope', 'blanket']
box_11 = ['phone']
box_12 = ['brush', 'toaster', 'vase', 'harmonica', 'bus']
box_13 = ['apple', 'puzzle', 'plate', 'moon']

def print_box(box_index, box_items):
    if len(box_items) == 0:
        print(f"Box {box_index}: []")
    else:
        print(f"Box {box_index}: {box_items}")

# Swap the laptop in Box 4 with the sock in Box 5
box_4.remove('laptop')
box_5.remove('sock')
box_4.append('sock')
box_5.append('laptop')

# Swap the ocean in Box 2 with the harmonica in Box 12
box_2.remove('ocean')
box_12.remove('harmonica')
box_2.append('harmonica')
box_12.append('ocean')

# Remove the frame and the coat from Box 0
box_0.remove('frame')
box_0.remove('coat')

# Move the laptop from Box 5 to Box 12
box_5.remove('laptop')
box_12.append('laptop')

# Swap the ocean in Box 12 with the drum in Box 10
box_12.remove('ocean')
box_10.remove('drum')
box_12.append('drum')
box_10.append('ocean')

# Move the leaf and the comb and the necklace from Box 7 to Box 3
box_7.remove('leaf')
box_7.remove('comb')
box_7.remove('necklace')
box_3.append('leaf')
box_3.append('comb')
box_3.append('necklace')

# Remove the starfish and the pot from Box 0
box_0.remove('starfish')
box_0.remove('pot')

# Swap the freezer in Box 9 with the shampoo in Box 6
box_9.remove('freezer')
box_6.remove('shampoo')
box_9.append('shampoo')
box_6.append('freezer')

# Move the apple from Box 13 to Box 12
box_13.remove('apple')
box_12.append('apple')

# Move the ocean and the blanket from Box 10 to Box 4
box_10.remove('ocean')
box_10.remove('blanket')
box_4.append('ocean')
box_4.append('blanket')

# Swap the swimsuit in Box 3 with the needle in Box 1
box_3.remove('swimsuit')
box_1.remove('needle')
box_3.append('needle')
box_1.append('swimsuit')

# Replace the microscope with the apple in Box 10
box_10.remove('microscope')
box_10.append('apple')

# Remove the phone from Box 11
box_11.remove('phone')

# Swap the leaf in Box 3 with the note in Box 1
box_3.remove('leaf')
box_1.remove('note')
box_3.append('note')
box_1.append('leaf')

# Remove the dolphin and the glove from Box 7
box_7.remove('dolphin')
box_7.remove('glove')

# Replace the boat and the bicycle and the wire with the puzzle and the pen and the necklace in Box 8
box_8.remove('boat')
box_8.remove('bicycle')
box_8.remove('wire')
box_8.append('puzzle')
box_8.append('pen')
box_8.append('necklace')

# Swap the cat in Box 9 with the mask in Box 0
box_9.remove('cat')
box_0.remove('mask')
box_9.append('mask')
box_0.append('cat')

# Swap the pen in Box 8 with the moon in Box 13
box_8.remove('pen')
box_13.remove('moon')
box_8.append('moon')
box_13.append('pen')

# Remove the shampoo from Box 9
box_9.remove('shampoo')

# Swap the leaf in Box 1 with the mask in Box 9
box_1.remove('leaf')
box_9.remove('mask')
box_1.append('mask')
box_9.append('leaf')

# Remove the tree and the freezer and the mixer from Box 6
box_6.remove('tree')
box_6.remove('freezer')
box_6.remove('mixer')

# Print the final state of the boxes
print_box(0, box_0)
print_box(1, box_1)
print_box(2, box_2)
print_box(3, box_3)
print_box(4, box_4)
print_box(5, box_5)
print_box(6, box_6)
print_box(7, box_7)
print_box(8, box_8)
print_box(9, box_9)
print_box(10, box_10)
print_box(11, box_11)
print_box(12, box_12)
print_box(13, box_13)