box_0 = ['crown', 'charger']
box_1 = ['card', 'cow', 'game', 'dog', 'pot']
box_2 = ['speaker', 'sculpture', 'truck', 'telescope', 'bus']
box_3 = []
box_4 = ['console', 'usb']
box_5 = ['blanket']
box_6 = ['paint', 'car', 'toothpaste']
box_7 = ['horn', 'plane']
box_8 = []
box_9 = ['island']
box_10 = ['mixer', 'meteor']
box_11 = ['note', 'submarine']
box_12 = ['polish', 'fork', 'ship', 'coral', 'mirror']

# Swap the ship in Box 12 with the island in Box 9
box_9.remove('island')
box_12.remove('ship')
box_9.append('ship')
box_12.append('island')

# Remove the bus and the speaker from Box 2
box_2.remove('bus')
box_2.remove('speaker')

# Replace the blanket with the shark in Box 5
box_5.remove('blanket')
box_5.append('shark')

# Remove the meteor from Box 10
box_10.remove('meteor')

# Remove the mixer from Box 10
box_10.remove('mixer')

# Remove the pot and the card from Box 1
box_1.remove('pot')
box_1.remove('card')

# Remove the ship from Box 9
box_9.remove('ship')

# Replace the game and the cow with the river and the clock in Box 1
box_1.remove('game')
box_1.remove('cow')
box_1.append('river')
box_1.append('clock')

# Swap the console in Box 4 with the dog in Box 1
box_1.remove('dog')
box_4.remove('console')
box_1.append('console')
box_4.append('dog')

# Replace the sculpture with the oven in Box 2
box_2.remove('sculpture')
box_2.append('oven')

# Swap the telescope in Box 2 with the charger in Box 0
box_0.remove('charger')
box_2.remove('telescope')
box_0.append('telescope')
box_2.append('charger')

# Put the jacket and the charger and the thread into Box 3
box_3.append('jacket')
box_3.append('charger')
box_3.append('thread')

# Replace the usb and the dog with the zipper and the plate in Box 4
box_4.remove('usb')
box_4.remove('dog')
box_4.append('zipper')
box_4.append('plate')

# Swap the zipper in Box 4 with the note in Box 11
box_4.remove('zipper')
box_11.remove('note')
box_4.append('note')
box_11.append('zipper')

# Remove the submarine and the zipper from Box 11
box_11.remove('submarine')
box_11.remove('zipper')

# Remove the console and the clock from Box 1
box_1.remove('console')
box_1.remove('clock')

# Swap the coral in Box 12 with the plane in Box 7
box_7.remove('plane')
box_12.remove('coral')
box_7.append('coral')
box_12.append('plane')

# Replace the truck and the oven with the leaf and the shirt in Box 2
box_2.remove('truck')
box_2.remove('oven')
box_2.append('leaf')
box_2.append('shirt')

# Move the note and the plate from Box 4 to Box 7
box_4.remove('note')
box_4.remove('plate')
box_7.append('note')
box_7.append('plate')

# Print the contents of each box
for i, box in enumerate([box_0, box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9, box_10, box_11, box_12]):
    print(f"Box {i}: {box}")