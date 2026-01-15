import pandas as pd

# Configuration
OUTPUT_FILE = "annotated_instances.tsv"

# Dummy Data: 2 Items, 4 Annotators each
# Column names match EXACTLY what Potato outputs for Round 1
data = [
    # --- Item 1: The "Rats" Example (High Agreement on Dehumanization) ---
    {
        "user": "annotator1@example.com",
        "instance_id": "item_1",
        "displayed_text": "Diese Ratten müssen aus unserem Land vertrieben werden. Sie sind eine Plage.",
        "label:::Dehumanizing": "label:::Dehumanizing",
        "explanation:::text_box": "Der Vergleich von Menschen mit Ratten und Plagen ist ein klassisches Beispiel für Dehumanisierung (Animalisierung).",
        "confidence:::scale_5": 5,
        "I have read and understood the instructions.:::Yes": None,
        "I want to participate in this research and continue with the study.:::Yes": None,
        "I understand that I might see offensive content.:::Yes": None
    },
    {
        "user": "annotator2@example.com",
        "instance_id": "item_1",
        "displayed_text": "Diese Ratten müssen aus unserem Land vertrieben werden. Sie sind eine Plage.",
        "label:::Dehumanizing": "label:::Dehumanizing",
        "explanation:::text_box": "Die Bezeichnung als 'Plage' spricht der Gruppe das Menschsein ab.",
        "confidence:::scale_5": 4,
        "I have read and understood the instructions.:::Yes": None,
        "I want to participate in this research and continue with the study.:::Yes": None,
        "I understand that I might see offensive content.:::Yes": None
    },
    {
        "user": "annotator3@example.com",
        "instance_id": "item_1",
        "displayed_text": "Diese Ratten müssen aus unserem Land vertrieben werden. Sie sind eine Plage.",
        "label:::Dehumanizing": "label:::Dehumanizing",
        "explanation:::text_box": "Metaphorische Herabwürdigung.",
        "confidence:::scale_5": 5,
        "I have read and understood the instructions.:::Yes": None,
        "I want to participate in this research and continue with the study.:::Yes": None,
        "I understand that I might see offensive content.:::Yes": None
    },
    {
        "user": "annotator4@example.com",
        "instance_id": "item_1",
        "displayed_text": "Diese Ratten müssen aus unserem Land vertrieben werden. Sie sind eine Plage.",
        "label:::Dehumanizing": None,  # The dissenter - did NOT select Dehumanizing
        "explanation:::text_box": "Es ist eine sehr harte Beleidigung, aber keine direkte Dehumanisierung im technischen Sinne.",
        "confidence:::scale_5": 2,
        "I have read and understood the instructions.:::Yes": None,
        "I want to participate in this research and continue with the study.:::Yes": None,
        "I understand that I might see offensive content.:::Yes": None
    },

    # --- Item 2: The "Politicians" Example (Consensus on Non-Dehumanization) ---
    {
        "user": "annotator1@example.com",
        "instance_id": "item_2",
        "displayed_text": "Die Politiker haben völlig versagt und sollten zurücktreten.",
        "label:::Dehumanizing": None,  # NOT dehumanizing
        "explanation:::text_box": "Das ist normale politische Kritik, keine Herabwürdigung des Menschseins.",
        "confidence:::scale_5": 5,
        "I have read and understood the instructions.:::Yes": None,
        "I want to participate in this research and continue with the study.:::Yes": None,
        "I understand that I might see offensive content.:::Yes": None
    },
    {
        "user": "annotator2@example.com",
        "instance_id": "item_2",
        "displayed_text": "Die Politiker haben völlig versagt und sollten zurücktreten.",
        "label:::Dehumanizing": None,
        "explanation:::text_box": "Kritik an Kompetenz, nicht an der Würde.",
        "confidence:::scale_5": 5,
        "I have read and understood the instructions.:::Yes": None,
        "I want to participate in this research and continue with the study.:::Yes": None,
        "I understand that I might see offensive content.:::Yes": None
    },
    {
        "user": "annotator3@example.com",
        "instance_id": "item_2",
        "displayed_text": "Die Politiker haben völlig versagt und sollten zurücktreten.",
        "label:::Dehumanizing": None,
        "explanation:::text_box": "Keine Tiermetaphern oder Objektifizierung vorhanden.",
        "confidence:::scale_5": 5,
        "I have read and understood the instructions.:::Yes": None,
        "I want to participate in this research and continue with the study.:::Yes": None,
        "I understand that I might see offensive content.:::Yes": None
    },
    {
        "user": "annotator4@example.com",
        "instance_id": "item_2",
        "displayed_text": "Die Politiker haben völlig versagt und sollten zurücktreten.",
        "label:::Dehumanizing": None,
        "explanation:::text_box": "Ich sehe hier keine hasserfüllte Sprache.",
        "confidence:::scale_5": 4,
        "I have read and understood the instructions.:::Yes": None,
        "I want to participate in this research and continue with the study.:::Yes": None,
        "I understand that I might see offensive content.:::Yes": None
    }
]

df = pd.DataFrame(data)
# Save as TSV to match Potato's standard output format
df.to_csv(OUTPUT_FILE, sep='\t', index=False)

print(f"Dummy data created: {OUTPUT_FILE}")
print(f"Columns: {df.columns.tolist()}")
print(f"Contains {len(df)} rows (annotation data only, no surveyflow pages).")