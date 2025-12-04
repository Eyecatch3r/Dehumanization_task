import pandas as pd
import time

# Configuration
OUTPUT_FILE = "annotated_instances.tsv"

# Dummy Data: 2 Items, 4 Annotators each, WITH CONFIDENCE SCORES
data = [
    # --- Item 1: The "Rats" Example (High Agreement on Dehumanization) ---
    {
        "id": "item_1",
        "text": "Diese Ratten müssen aus unserem Land vertrieben werden. Sie sind eine Plage.",
        "label": "['Dehumanisierend']",
        "explanation": "Der Vergleich von Menschen mit Ratten und Plagen ist ein klassisches Beispiel für Dehumanisierung (Animalisierung).",
        "confidence": "5 - Sehr zuversichtlich", # <--- NEW FIELD
        "_annotation_status": "submitted",
        "_timestamp": time.time()
    },
    {
        "id": "item_1",
        "text": "Diese Ratten müssen aus unserem Land vertrieben werden. Sie sind eine Plage.",
        "label": "['Dehumanisierend']",
        "explanation": "Die Bezeichnung als 'Plage' spricht der Gruppe das Menschsein ab.",
        "confidence": "4 - Zuversichtlich", # <--- NEW FIELD
        "_annotation_status": "submitted",
        "_timestamp": time.time()
    },
    {
        "id": "item_1",
        "text": "Diese Ratten müssen aus unserem Land vertrieben werden. Sie sind eine Plage.",
        "label": "['Dehumanisierend']",
        "explanation": "Metaphorische Herabwürdigung.",
        "confidence": "5 - Sehr zuversichtlich", # <--- NEW FIELD
        "_annotation_status": "submitted",
        "_timestamp": time.time()
    },
    {
        "id": "item_1",
        "text": "Diese Ratten müssen aus unserem Land vertrieben werden. Sie sind eine Plage.",
        "label": "['Nicht dehumanisierend']", # The dissenter
        "explanation": "Es ist eine sehr harte Beleidigung, aber keine direkte Dehumanisierung im technischen Sinne.",
        "confidence": "2 - Wenig zuversichtlich", # <--- NEW FIELD
        "_annotation_status": "submitted",
        "_timestamp": time.time()
    },

    # --- Item 2: The "Politicians" Example (Consensus on Non-Dehumanization) ---
    {
        "id": "item_2",
        "text": "Die Politiker haben völlig versagt und sollten zurücktreten.",
        "label": "['Nicht dehumanisierend']",
        "explanation": "Das ist normale politische Kritik, keine Herabwürdigung des Menschseins.",
        "confidence": "5 - Sehr zuversichtlich",
        "_annotation_status": "submitted",
        "_timestamp": time.time()
    },
    {
        "id": "item_2",
        "text": "Die Politiker haben völlig versagt und sollten zurücktreten.",
        "label": "['Nicht dehumanisierend']",
        "explanation": "Kritik an Kompetenz, nicht an der Würde.",
        "confidence": "5 - Sehr zuversichtlich",
        "_annotation_status": "submitted",
        "_timestamp": time.time()
    },
    {
        "id": "item_2",
        "text": "Die Politiker haben völlig versagt und sollten zurücktreten.",
        "label": "['Nicht dehumanisierend']",
        "explanation": "Keine Tiermetaphern oder Objektifizierung vorhanden.",
        "confidence": "5 - Sehr zuversichtlich",
        "_annotation_status": "submitted",
        "_timestamp": time.time()
    },
    {
        "id": "item_2",
        "text": "Die Politiker haben völlig versagt und sollten zurücktreten.",
        "label": "['Nicht dehumanisierend']",
        "explanation": "Ich sehe hier keine hasserfüllte Sprache.",
        "confidence": "4 - Zuversichtlich",
        "_annotation_status": "submitted",
        "_timestamp": time.time()
    }
]

df = pd.DataFrame(data)
# Save as TSV to match Potato's standard output format
df.to_csv(OUTPUT_FILE, sep='\t', index=False)

print(f"Dummy data created: {OUTPUT_FILE}")
print(f"Columns: {df.columns.tolist()}")
print(f"Contains {len(df)} rows.")