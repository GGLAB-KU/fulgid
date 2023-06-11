import json
from collections import Counter

from sklearn.metrics import f1_score
from tqdm import tqdm

from src.settings import Settings

# Load your data
with open(Settings.wiqa_test, 'r') as json_file:
    data = list(json_file)

# Counter for the labels
counter = Counter()

# List to store the true and predicted labels
y_true = []
y_pred = []

# Count the labels in the data
for entry in data:
    entry = json.loads(entry)
    answer_label = entry['question']['answer_label']
    counter[answer_label] += 1

# Get the most common label
most_common_label = counter.most_common(1)[0][0]


# Now you can predict the most common label for any question
for entry in tqdm(data):
    entry = json.loads(entry)
    question = entry['question']['stem']
    true_answer = entry['question']['answer_label']

    y_true.append(true_answer)
    y_pred.append(most_common_label)

# Calculate the F1 score
f1 = f1_score(y_true, y_pred, average='weighted')

print(f'F1 score: {f1}')

