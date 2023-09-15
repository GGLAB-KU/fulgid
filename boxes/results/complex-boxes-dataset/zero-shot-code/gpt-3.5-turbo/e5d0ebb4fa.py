box_0 = []
box_1 = ['bag', 'scarf', 'mirror', 'star', 'note']
box_2 = ['leaf', 'car', 'wallet', 'shampoo', 'river', 'pants']
box_3 = []
box_4 = ['battery', 'rocket']
box_5 = ['frame']
box_6 = ['guitar', 'jungle']
box_7 = ['sock', 'tiger', 'polish', 'plane', 'fridge', 'controller']
box_8 = ['seaweed']
box_9 = ['sun', 'comb', 'coat', 'forest', 'freezer']
box_10 = ['wig', 'sculpture', 'desert']
box_11 = []
box_12 = ['chair', 'cat', 'whistle', 'glove', 'toy']
box_13 = ['table', 'grass', 'violin', 'bus']
box_14 = []

def print_box(box_index):
    box = globals()[f'box_{box_index}']
    print(f"Box {box_index}: {box}")

# Initial state
for i in range(15):
    print_box(i)

# Perform operations
box_2.extend(['shampoo', 'river', 'pants'])
box_14.extend(['piano', 'sculpture'])
box_4.remove('battery')
box_7.remove('rocket')
box_4.append('rocket')
box_1.extend(['mirror', 'star', 'note'])
box_6.remove('jungle')
box_14.remove('sculpture')
box_14.append('jungle')
box_2.remove('river')
box_2.append('shampoo')
box_10.remove('star')
box_9.remove('freezer')
box_9.remove('forest')
box_9.extend(['horn', 'table'])
box_7.extend(['fridge', 'controller'])
box_9.remove('horn')
box_0.append('horn')
box_14.remove('jungle')
box_14.remove('piano')
box_5.remove('frame')
box_12.remove('cat')
box_13.extend(['wig', 'desert', 'sculpture'])
box_13.remove('table')
box_13.append('grass')
box_13.remove('sculpture')
box_13.append('toaster')
box_5.remove('cat')
box_10.extend(['violin', 'leaf'])
box_1.remove('bag')
box_1.remove('star')
box_4.extend(['star', 'bag'])
box_6.remove('guitar')
box_7.remove('fridge')
box_6.append('fridge')
box_13.remove('wig')
box_13.remove('desert')
box_13.remove('toaster')
box_13.extend(['guitar', 'violin', 'bus'])
box_6.remove('sculpture')
box_6.remove('fridge')
box_4.remove('leaf')
box_4.append('rocket')

# Final state
for i in range(15):
    print_box(i)