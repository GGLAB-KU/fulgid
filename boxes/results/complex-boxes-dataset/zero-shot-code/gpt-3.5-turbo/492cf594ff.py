box0 = ['pan', 'blanket', 'speaker', 'oven']
box1 = ['snow', 'shirt', 'pillow']
box2 = ['tiger', 'helmet', 'wallet', 'river', 'toy']
box3 = []

# Move the pillow and the shirt from Box 1 to Box 2
box2.extend([box1.pop(box1.index('pillow')), box1.pop(box1.index('shirt'))])

# Put the meteor and the zipper into Box 1
box1.extend(['meteor', 'zipper'])

# Replace the blanket and the speaker with the keyboard and the comet in Box 0
box0[1] = 'keyboard'
box0[2] = 'comet'

# Remove the pan and the keyboard and the oven from Box 0
box0.remove('pan')
box0.remove('keyboard')
box0.remove('oven')

# Put the sculpture and the razor into Box 1
box1.extend(['sculpture', 'razor'])

# Move the helmet and the wallet and the toy from Box 2 to Box 3
box3.extend([box2.pop(box2.index('helmet')), box2.pop(box2.index('wallet')), box2.pop(box2.index('toy'))])

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)