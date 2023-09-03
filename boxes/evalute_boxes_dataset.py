import os
from settings import Settings
import json


def check_diff_operations(numops):
    diff_operations_count = 0
    if numops["Move"] > 0:
        diff_operations_count += 1
    if numops["Remove"] > 0:
        diff_operations_count += 1
    if numops["Put"] > 0:
        diff_operations_count += 1
    return diff_operations_count


aggregated_data_path = os.path.join(Settings.boxes_dataset_path, "aggregated_data.jsonl")

aggregated_boxes_file = open(aggregated_data_path, 'r')
aggregated_boxes = list(aggregated_boxes_file)

boxes_count = []
operations_count = []
different_operations_count = []

# data_dict = json.loads('{"sentence_hash": "0f2615feca", "sentence": "Box 0 contains the note, Box 1 contains nothing, Box 2 contains the ball, Box 3 contains nothing, Box 4 contains the bus and the camera and the radio, Box 5 contains the cream and the tie, Box 6 contains the document. Move the bus and the camera and the radio from Box 4 to Box 1. Put the mirror into Box 0. Move the document from Box 6 to Box 0. Remove the bus and the radio from Box 1. Put the bell and the jacket into Box 6. Put the plate into Box 3. Move the jacket from Box 6 to Box 4. Remove the plate from Box 3. Move the ball from Box 2 to Box 1. Put the bill into Box 5. Put the computer into Box 2. Put the ring into Box 1.", "sample_id": 789, "numops": {"Move": 4, "Remove": 2, "Put": 6, "Total": 12}, "final_states": {"Box 0": ["the document", "the mirror", "the note"], "Box 1": ["the ball", "the camera", "the ring"], "Box 2": ["the computer"], "Box 3": ["nothing"], "Box 4": ["the jacket"], "Box 5": ["the bill", "the cream", "the tie"], "Box 6": ["the bell"]}}')
# print(len(data_dict["final_states"]))
# print(data_dict["numops"]["Total"])
# print(check_diff_operations(data_dict["numops"]))

for example in aggregated_boxes:
    data_dict = json.loads(example)  # convert it to a dictionary
    boxes_count.append(len(data_dict["final_states"]))
    operations_count.append(data_dict["numops"]["Total"])
    different_operations_count.append(check_diff_operations(data_dict["numops"]))

print("Number of examples in the dataset: ", len(aggregated_boxes))
print("Average number of boxes: ", sum(boxes_count) / len(boxes_count))
print("Average number of operations: ", sum(operations_count) / len(operations_count))
print("Average number of different operations used: ", sum(different_operations_count) / len(different_operations_count))
