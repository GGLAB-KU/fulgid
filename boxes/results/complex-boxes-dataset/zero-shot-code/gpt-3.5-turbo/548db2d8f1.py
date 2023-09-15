box0 = ['magnet', 'mirror']
box1 = ['wig', 'seaweed', 'umbrella']
box2 = ['rain', 'crown', 'jungle', 'shorts']
box3 = ['toothpaste', 'soap', 'helmet']
box4 = ['leaf', 'cow', 'game']

# Remove the wig and the umbrella from Box 1
box1.remove('wig')
box1.remove('umbrella')

# Empty Box 3
box3 = []

# Replace the mirror and the magnet with the swimsuit and the submarine in Box 0
box0.remove('mirror')
box0.remove('magnet')
box0.append('swimsuit')
box0.append('submarine')

# Put the island into Box 4
box4.append('island')

# Move the swimsuit from Box 0 to Box 3
box0.remove('swimsuit')
box3.append('swimsuit')

# Move the game and the island from Box 4 to Box 2
box4.remove('game')
box4.remove('island')
box2.append('game')
box2.append('island')

# Move the cow from Box 4 to Box 3
box4.remove('cow')
box3.append('cow')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)