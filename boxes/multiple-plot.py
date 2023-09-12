import matplotlib.pyplot as plt


def multi_plotting(accuracy_dicts, methods, dataset_name):
    # Create a plot
    plt.figure(figsize=(15, 12))

    # Define some markers for distinction
    markers = ['o', 's', '^', 'v', 'D', '*', 'p']

    for idx, accuracy_dict in enumerate(accuracy_dicts):
        # Prepare data for the plot
        operations_nums = sorted(accuracy_dict.keys())
        accuracies = [accuracy_dict[num] for num in operations_nums]

        # Plot the data
        plt.plot(operations_nums, accuracies, marker=markers[idx], label=methods[idx])

    # Add labels, title, and legend
    plt.xlabel('operations_num')
    plt.ylabel('Accuracy')
    plt.title(dataset_name + " Comparison", fontsize=16)  # Main title with bigger font size
    plt.legend(loc="best")

    # Show grid
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()


# Your data


accuracy_map_1 = {22: 0.4385758998435055, 19: 0.44449499545040944, 17: 0.4180821917808219, 16: 0.4818941504178273,
                  12: 0.5186846038863976, 21: 0.44220665499124345, 20: 0.4197936210131332, 7: 0.592944369063772,
                  11: 0.4848746758859118, 8: 0.5425257731958762, 14: 0.4740484429065744, 15: 0.4546023794614903,
                  13: 0.5087719298245614, 10: 0.5561450044208665, 6: 0.630048465266559, 9: 0.5196182396606575,
                  18: 0.45981905268759976}

accuracy_map_2 = {10: 0.9164086687306502, 12: 0.8527062999112689, 7: 0.9418960244648318, 22: 0.6677820267686424,
                  14: 0.8940783986655546, 20: 0.79806598407281, 21: 0.7762947143619862, 15: 0.8449074074074074,
                  6: 0.9012797074954296, 19: 0.693069306930693, 9: 0.9608091024020228, 18: 0.8198198198198198,
                  13: 0.7940941739824421, 11: 0.896588486140725, 17: 0.7531106745252129, 8: 0.8939617083946981,
                  16: 0.8519003931847968}

accuracy_map_3 = {10: 0.6696078431372549, 12: 0.6945392491467577, 7: 0.6873156342182891, 22: 0.29356505401596994,
                  14: 0.5136, 20: 0.3520891364902507, 21: 0.3841719077568134, 15: 0.5275938189845475,
                  6: 0.7933450087565674, 19: 0.5348468848996832, 9: 0.7239709443099274, 18: 0.4276649746192893,
                  13: 0.624113475177305, 11: 0.625, 17: 0.4859872611464968, 8: 0.6242857142857143,
                  16: 0.5172855313700384}

methods = ["One-Shot Plaintext Prompt", "One-Shot Python Code Representation", "Zero-Shot Python Code Representation"]
dataset_name = "Complex Boxes Dataset"

multi_plotting([accuracy_map_1, accuracy_map_2, accuracy_map_3], methods, dataset_name)
