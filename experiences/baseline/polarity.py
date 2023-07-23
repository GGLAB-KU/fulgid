import json
from tqdm import tqdm
from sklearn.metrics import f1_score

from settings import Settings

# Load your data
with open(Settings.wiqa_test_path, 'r') as json_file:
    data = list(json_file)

# List to store the true and predicted labels
y_true = []
y_pred = []

# Map text to corresponding label
text_to_label = {'more': 0, 'less': 1, 'no_effect': 2}

# Now you can predict the most common label for any question
for entry in tqdm(data):
    entry = json.loads(entry)
    question = entry['question']['stem']
    true_answer = entry['question']['answer_label']

    if 'more' in question:
        predicted_answer = 'more'
    elif 'less' in question:
        predicted_answer = 'less'
    else:
        predicted_answer = 'no_effect'

    y_true.append(true_answer)
    y_pred.append(predicted_answer)

# Calculate the F1 score
f1 = f1_score(y_true, y_pred, average='weighted')

print(f'F1 score: {f1}')
