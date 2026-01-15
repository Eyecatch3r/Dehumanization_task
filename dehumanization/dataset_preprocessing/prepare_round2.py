import pandas as pd
import ast
from pathlib import Path

# ================= CONFIGURATION =================
# Get the script's directory and construct paths relative to project root
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_FILES_DIR = PROJECT_ROOT / "data_files"

# INPUT: Your raw Round 1 output (in the same directory as this script)
INPUT_FILE = SCRIPT_DIR / "annotated_instances.tsv"

# OUTPUT: The file Potato needs for Round 2
OUTPUT_FILE = DATA_FILES_DIR / "round2_prepared_data.csv"

# Keys matching Potato's ACTUAL output column names from Round 1
USER_KEY = "user"
ID_KEY = "instance_id"
TEXT_KEY = "displayed_text"
LABEL_KEY = "label:::Dehumanizing"
EXPLANATION_KEY = "explanation:::text_box"
CONFIDENCE_KEY = "confidence:::scale_5"


# =================================================

def process_annotations():
    print(f"Reading data from {INPUT_FILE}...")

    try:
        df = pd.read_csv(INPUT_FILE, sep='\t')
    except Exception as e:
        print(f"TSV load failed with error: {e}")
        print("Trying CSV...")
        try:
            df = pd.read_csv(INPUT_FILE, sep=',')
        except Exception as e2:
            print(f"CSV load also failed: {e2}")
            return

    print(f"Loaded {len(df)} total rows")
    print(f"Columns found: {df.columns.tolist()}")
    
    # Filter out surveyflow pages (consent, end, definition, etc.)
    df = df[~df[ID_KEY].astype(str).str.contains('html|consent|end|definition|instruction', case=False, na=False)]
    print(f"After filtering surveyflow pages: {len(df)} annotation rows")

    # Validate columns
    required_cols = [USER_KEY, ID_KEY, TEXT_KEY, LABEL_KEY, EXPLANATION_KEY, CONFIDENCE_KEY]
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        print(f"Error: Required columns missing: {missing_cols}")
        print(f"Expected: {required_cols}")
        print(f"Found: {df.columns.tolist()}")
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
            
            # Get the actual user ID from the 'user' column
            r1_annotator_id = annotation[USER_KEY]
            
            # Handle the label - if it's "label:::Dehumanizing", mark as dehumanizing
            # If it's NaN or empty, mark as non-dehumanizing
            label_raw = annotation[LABEL_KEY]
            if pd.notna(label_raw) and label_raw == "label:::Dehumanizing":
                label_value = "Dehumanisierend"
            else:
                label_value = "Nicht dehumanisierend"

            row_data[f"r1_label_{annotator_num}"] = label_value
            row_data[f"r1_expl_{annotator_num}"] = annotation[EXPLANATION_KEY]
            row_data[f"r1_conf_{annotator_num}"] = annotation[CONFIDENCE_KEY]
            row_data[f"r1_annotator_{annotator_num}"] = r1_annotator_id

        processed_rows.append(row_data)

    result_df = pd.DataFrame(processed_rows)
    
    # CREATE DIRECTORY IF IT DOESN'T EXIST
    DATA_FILES_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Ensured directory exists: {DATA_FILES_DIR}")
    
    result_df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nSuccess! Processed {len(result_df)} items.")
    print(f"Saved to: {OUTPUT_FILE}")
    print(f"Output columns: {result_df.columns.tolist()}")


if __name__ == "__main__":
    process_annotations()
