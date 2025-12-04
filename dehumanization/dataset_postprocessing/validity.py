import pandas as pd
import ast

# Load your Round 2 Output
INPUT_FILE = "annotated_instances.tsv"
df = pd.read_csv(INPUT_FILE, sep='\t')

# Counters
total_items = 0
items_with_errors = 0
items_with_variation = 0

print(f"{'ID':<10} | {'Status':<20} | {'Detail':<50}")
print("-" * 85)

for index, row in df.iterrows():
    item_id = row['id']
    valid_labels = set()
    rejected_labels = set()

    # Loop through the 4 potential annotator slots
    for i in range(1, 5):
        val_col = f"validity_{i}"
        lbl_col = f"r1_label_{i}"

        # Check if this column exists and has data (not empty/NaN)
        if val_col in row and pd.notna(row[val_col]) and pd.notna(row[lbl_col]):
            judgment = row[val_col]
            original_label = row[lbl_col]

            # VARIERR Logic: "Ja (Sinnvoll)" validates the label-explanation pair
            if judgment == "Ja (Sinnvoll)":
                valid_labels.add(original_label)
            elif judgment == "Nein (Ungültig)":
                rejected_labels.add(original_label)

    # --- Analysis Logic ---
    status = ""
    detail = ""

    # 1. ERROR: All explanations rejected (or none valid)
    if len(valid_labels) == 0 and len(rejected_labels) > 0:
        status = "ERROR / NOISE"
        detail = f"All {len(rejected_labels)} labels rejected."
        items_with_errors += 1

    # 2. VARIATION: Multiple DIFFERENT labels were validated
    elif len(valid_labels) > 1:
        status = "VALID VARIATION"
        detail = f"Valid Conflict: {valid_labels}"
        items_with_variation += 1

    # 3. CONSENSUS: Only one label type was valid
    elif len(valid_labels) == 1:
        status = "CONSENSUS"
        detail = f"Single Valid Label: {list(valid_labels)[0]}"

    # 4. INCOMPLETE
    else:
        status = "UNCLEAR"
        detail = "No validation data found."

    total_items += 1
    print(f"{item_id:<10} | {status:<20} | {detail:<50}")

print("-" * 85)
print(f"Total Items: {total_items}")
print(f"Detected Errors (Noise): {items_with_errors}")
print(f"Detected Valid Variation: {items_with_variation}")