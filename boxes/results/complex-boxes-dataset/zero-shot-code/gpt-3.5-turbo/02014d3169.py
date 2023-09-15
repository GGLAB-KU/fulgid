box0 = []
box1 = ['belt', 'pan', 'mirror']
box2 = ['branch', 'guitar']
box3 = ['skirt', 'pillow', 'butterfly', 'shirt']
box4 = ['leaf']

# Swap the pillow in Box 3 with the leaf in Box 4
box3.remove('pillow')
box4.remove('leaf')
box3.append('leaf')
box4.append('pillow')

# Put the sculpture and the horn and the umbrella into Box 1
box1.extend(['sculpture', 'horn', 'umbrella'])

# Swap the pillow in Box 4 with the shirt in Box 3
box4.remove('pillow')
box3.remove('shirt')
box4.append('shirt')
box3.append('pillow')

# Replace the shirt with the toothpaste in Box 4
box4.remove('shirt')
box4.append('toothpaste')

# Move the butterfly and the leaf and the pillow from Box 3 to Box 4
box4.extend(['butterfly', 'leaf', 'pillow'])
box3.remove('butterfly')
box3.remove('leaf')
box3.remove('pillow')

# Replace the skirt with the boot in Box 3
box3.remove('skirt')
box3.append('boot')

# Empty Box 4
box4 = []

print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)