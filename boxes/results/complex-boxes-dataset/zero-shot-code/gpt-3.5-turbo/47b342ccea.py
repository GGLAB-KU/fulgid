box0 = ['shelf', 'dress', 'starfish', 'boot', 'lipstick']
box1 = ['desert', 'scissors', 'doll', 'wig']
box2 = ['perfume', 'pot', 'leaf', 'thread']
box3 = ['basket', 'crown', 'makeup', 'table', 'blender']
box4 = ['lightning', 'sun', 'wallet']
box5 = ['meteor', 'ship', 'sandals', 'flower']
box6 = ['magnet', 'harmonica', 'zipper']

# Move items from Box 2 to Box 0
box0.extend([box2.pop(box2.index('pot')), box2.pop(box2.index('thread')), box2.pop(box2.index('perfume'))])

# Swap meteor in Box 5 with sun in Box 4
box5[box5.index('meteor')], box4[box4.index('sun')] = box4[box4.index('sun')], box5[box5.index('meteor')]

# Swap makeup in Box 3 with meteor in Box 4
box3[box3.index('makeup')], box4[box4.index('meteor')] = box4[box4.index('meteor')], box3[box3.index('makeup')]

# Put wig and river into Box 4
box4.extend(['wig', 'river'])

# Put clock, sculpture, and bowl into Box 2
box2.extend(['clock', 'sculpture', 'bowl'])

# Put ocean and candle into Box 3
box3.extend(['ocean', 'candle'])

# Remove harmonica, zipper, and magnet from Box 6
box6.remove('harmonica')
box6.remove('zipper')
box6.remove('magnet')

# Put swimsuit into Box 3
box3.append('swimsuit')

# Put comet, vase, and tie into Box 5
box5.extend(['comet', 'vase', 'tie'])

# Move wallet and makeup from Box 4 to Box 1
box1.extend([box4.pop(box4.index('wallet')), box4.pop(box4.index('makeup'))])

# Swap meteor in Box 3 with lipstick in Box 0
box3[box3.index('meteor')], box0[box0.index('lipstick')] = box0[box0.index('lipstick')], box3[box3.index('meteor')]

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)