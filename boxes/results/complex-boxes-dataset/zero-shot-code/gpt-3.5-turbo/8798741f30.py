box0 = ['rock', 'shark', 'boot', 'cat', 'fish']
box1 = ['tape', 'sculpture', 'pan']
box2 = ['wallet', 'pants', 'controller']
box3 = ['snow', 'necklace', 'leaf']
box4 = ['microwave', 'motorcycle', 'watch', 'submarine']

# Put the jungle and the dog into Box 3
box3.append('jungle')
box3.append('dog')

# Remove the fish from Box 0
box0.remove('fish')

# Put the makeup and the dog and the lamp into Box 1
box1.append('makeup')
box1.append('dog')
box1.append('lamp')

# Remove the jungle and the leaf from Box 3
box3.remove('jungle')
box3.remove('leaf')

# Move the cat and the shark and the rock from Box 0 to Box 1
box1.extend(box0)
box0.clear()

# Put the swimsuit and the spoon and the harmonica into Box 2
box2.append('swimsuit')
box2.append('spoon')
box2.append('harmonica')

# Move the motorcycle and the watch and the microwave from Box 4 to Box 1
box1.extend(box4)
box4.clear()

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)