import pandas as pd
import ast

# ================= CONFIGURATION =================
# INPUT: Your raw Round 1 output
INPUT_FILE = "annotated_instances.tsv"

# OUTPUT: The file Potato needs for Round 2
OUTPUT_FILE = "../data_files/round2_prepared_data.csv"

# Keys matching your Potato configuration
ID_KEY = "id"
TEXT_KEY = "text"
LABEL_KEY = "label"
EXPLANATION_KEY = "explanation"
CONFIDENCE_KEY = "confidence"  # <--- NEW: Capture confidence


# =================================================

def process_annotations():
    print(f"Reading data from {INPUT_FILE}...")

    try:
        df = pd.read_csv(INPUT_FILE, sep='\t')
    except:
        print("TSV load failed, trying CSV...")
        df = pd.read_csv(INPUT_FILE, sep=',')

    # Validate columns
    required_cols = [ID_KEY, TEXT_KEY, LABEL_KEY, EXPLANATION_KEY, CONFIDENCE_KEY]
    if not all(col in df.columns for col in required_cols):
        print(f"Error: Columns missing. Found: {df.columns.tolist()}")
        return

    grouped = df.groupby(ID_KEY)
    processed_rows = []

    for item_id, group in grouped:
        row_data = {
            "id": item_id,
            "text": group.iloc[0][TEXT_KEY]
        }

        for i, (_, annotation) in enumerate(group.iterrows()):
            annotator_num = i + 1
            if annotator_num > 4:
                break

                # Clean Label
            label_raw = annotation[LABEL_KEY]
            if isinstance(label_raw, str) and label_raw.startswith("['") and label_raw.endswith("']"):
                try:
                    label_raw = ast.literal_eval(label_raw)[0]
                except:
                    pass

                    # Save Label, Explanation, AND Confidence
            row_data[f"r1_label_{annotator_num}"] = label_raw
            row_data[f"r1_expl_{annotator_num}"] = annotation[EXPLANATION_KEY]
            row_data[f"r1_conf_{annotator_num}"] = annotation[CONFIDENCE_KEY]

        processed_rows.append(row_data)

    result_df = pd.DataFrame(processed_rows)
    result_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Success! Processed {len(result_df)} items.")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    process_annotations()