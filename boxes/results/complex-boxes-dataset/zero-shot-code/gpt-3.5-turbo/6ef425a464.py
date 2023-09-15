box0 = []
box1 = ['jacket', 'belt', 'boat', 'fork', 'keyboard']
box2 = ['starfish']
box3 = ['sculpture', 'mirror', 'shirt', 'note', 'ring']
box4 = ['speaker']
box5 = []
box6 = []

# Move the keyboard and the boat from Box 1 to Box 3
box3.extend([item for item in box1 if item in ['keyboard', 'boat']])
box1 = [item for item in box1 if item not in ['keyboard', 'boat']]

# Put the octopus and the thread into Box 6
box6.extend(['octopus', 'thread'])

# Replace the sculpture with the game in Box 3
box3 = [item if item != 'sculpture' else 'game' for item in box3]

# Swap the speaker in Box 4 with the octopus in Box 6
box4, box6 = box6, box4

# Swap the shirt in Box 3 with the jacket in Box 1
box1, box3 = box3, box1

# Move the speaker and the thread from Box 6 to Box 2
box2.extend([item for item in box6 if item in ['speaker', 'thread']])
box6 = [item for item in box6 if item not in ['speaker', 'thread']]

# Remove the shirt and the belt and the fork from Box 1
box1 = [item for item in box1 if item not in ['shirt', 'belt', 'fork']]

# Put the mountain and the dolphin and the thunder into Box 3
box3.extend(['mountain', 'dolphin', 'thunder'])

# Put the shelf and the perfume into Box 2
box2.extend(['shelf', 'perfume'])

# Put the lipstick and the watch and the lock into Box 6
box6.extend(['lipstick', 'watch', 'lock'])

# Empty Box 3
box3 = []

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)