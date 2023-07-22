import os
import pathlib

current_dir = pathlib.Path(__file__).parent.resolve()
base_dir = os.path.dirname(current_dir)


class Settings:
    wiqa_train = os.path.join(base_dir, "datasets/wiqa-dataset-v2-october-2019/train.jsonl")
    wiqa_test = os.path.join(base_dir, "datasets/wiqa-dataset-v2-october-2019/test.jsonl")
    wiqa_dev = os.path.join(base_dir, "datasets/wiqa-dataset-v2-october-2019/dev.jsonl")
    boxes_dataset_v1 = os.path.join(base_dir, "datasets/boxes-only-needed/")

