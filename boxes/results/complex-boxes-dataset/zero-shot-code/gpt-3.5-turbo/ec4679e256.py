box0 = ['motorcycle', 'river']
box1 = ['lamp', 'polish', 'game', 'button', 'submarine']
box2 = ['belt', 'boat', 'island']
box3 = []
box4 = []
box5 = []

# Swap button in box1 with river in box0
box0[1], box1[3] = box1[3], box0[1]

# Put coin, lipstick, and boat into box5
box5.extend(['coin', 'lipstick', 'boat'])

# Remove motorcycle from box0
box0.remove('motorcycle')

# Replace lamp with dice in box1
box1[0] = 'dice'

# Replace boat and island with thunder and soap in box2
box2[1:3] = ['thunder', 'soap']

# Swap polish in box1 with button in box0
box0[1], box1[1] = box1[1], box0[1]

# Move thunder and soap from box2 to box1
box1.extend(box2[1:3])
box2[1:3] = []

# Move lipstick, coin, and boat from box5 to box4
box4.extend(box5)
box5 = []

# Swap lipstick in box4 with polish in box0
box4[0], box0[1] = box0[1], box4[0]

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)