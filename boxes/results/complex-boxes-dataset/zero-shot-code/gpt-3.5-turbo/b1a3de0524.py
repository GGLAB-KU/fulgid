box0 = ['bowl', 'comb', 'shoes']
box1 = ['starfish']
box2 = ['elephant', 'clock', 'horn', 'planet', 'thread']
box3 = ['blanket']

# Empty Box 0
box0 = []

# Swap the blanket in Box 3 with the starfish in Box 1
box1[0], box3[0] = box3[0], box1[0]

# Remove the planet and the thread and the horn from Box 2
box2.remove('planet')
box2.remove('thread')
box2.remove('horn')

# Put the cow and the note and the game into Box 3
box3.extend(['cow', 'note', 'game'])

# Swap the note in Box 3 with the blanket in Box 1
box1[0], box3[1] = box3[1], box1[0]

# Remove the clock from Box 2
box2.remove('clock')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)