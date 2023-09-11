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
accuracy_map_1 = {9: 0.9458041958041958, 21: 0.7482078853046595, 10: 0.927027027027027, 12: 0.8735380116959064,
                  7: 0.9463470319634704, 22: 0.6922857142857143, 16: 0.8344489067380634, 14: 0.8940783986655546,
                  20: 0.79806598407281, 15: 0.8445353594389247, 6: 0.9012797074954296, 19: 0.7053398058252427,
                  13: 0.8164422395464209, 18: 0.8195372750642673, 11: 0.896588486140725, 17: 0.7531106745252129,
                  8: 0.8939617083946981}
accuracy_map_2 = {22: 0.45140845070422536, 19: 0.4515738498789346, 17: 0.4180821917808219, 16: 0.4937142857142857,
                  12: 0.5085679314565483, 21: 0.43495786002198605, 20: 0.4197936210131332, 7: 0.5979695431472081,
                  11: 0.4848746758859118, 8: 0.5425257731958762, 14: 0.4740484429065744, 15: 0.46116970278044106,
                  13: 0.51323706377858, 10: 0.5629343629343629, 6: 0.630048465266559, 9: 0.5047272727272727,
                  18: 0.46229228802726885}

methods = ["Python Code Representation", "Plaintext"]
dataset_name = "Complex Boxes Dataset"

multi_plotting([accuracy_map_1, accuracy_map_2], methods, dataset_name)
