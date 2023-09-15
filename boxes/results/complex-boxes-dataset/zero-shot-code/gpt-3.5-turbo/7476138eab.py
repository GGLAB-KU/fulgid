box0 = ['zipper', 'pillow', 'star']
box1 = ['needle']
box2 = []
box3 = ['soap', 'tiger', 'watch', 'truck']
box4 = ['console', 'wig', 'shirt', 'basket']
box5 = ['freezer', 'wire', 'boat', 'bracelet', 'river']
box6 = ['headphone', 'shelf', 'scissors', 'harmonica', 'blender']

# Swap zipper and needle
box0.remove('zipper')
box1.append('zipper')
box1.remove('needle')
box0.append('needle')

# Swap wire and scissors
box5.remove('wire')
box6.append('wire')
box6.remove('scissors')
box5.append('scissors')

# Move shirt and basket from box4 to box3
box4.remove('shirt')
box3.append('shirt')
box4.remove('basket')
box3.append('basket')

# Move wire, headphone, and shelf from box6 to box2
box6.remove('wire')
box2.append('wire')
box6.remove('headphone')
box2.append('headphone')
box6.remove('shelf')
box2.append('shelf')

# Empty box3
box3.clear()

# Move freezer, bracelet, and scissors from box5 to box4
box5.remove('freezer')
box4.append('freezer')
box5.remove('bracelet')
box4.append('bracelet')
box5.remove('scissors')
box4.append('scissors')

# Move zipper from box1 to box3
box1.remove('zipper')
box3.append('zipper')

# Move needle and star from box0 to box1
box0.remove('needle')
box1.append('needle')
box0.remove('star')
box1.append('star')

# Remove zipper from box3
box3.remove('zipper')

# Remove shelf and headphone from box2
box2.remove('shelf')
box2.remove('headphone')

# Move pillow from box0 to box4
box0.remove('pillow')
box4.append('pillow')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)
print("Box 6:", box6)