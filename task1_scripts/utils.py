# task1_scripts/utils.py

import re
import json
import pandas as pd


def load_sample(csv_path, n=200):
    """
    Loads the Yelp dataset from csv_path and returns a sample of n rows.
    Assumes the CSV has columns: 'review' and 'stars'.
    """
    df = pd.read_csv(csv_path)

    # Try to identify review column if name differs
    if "review" not in df.columns:
        for col in df.columns:
            if "review" in col.lower():
                df = df.rename(columns={col: "review"})
                break

    # Try to identify stars column if name differs
    if "stars" not in df.columns:
        for col in df.columns:
            if "star" in col.lower():
                df = df.rename(columns={col: "stars"})
                break

    # Clean & sample
    df = df[["review", "stars"]].dropna().reset_index(drop=True)
    return df.sample(min(n, len(df)), random_state=42)


def extract_json_from_text(text):
    """
    Extracts the first valid JSON object from the LLM response.
    If parsing fails, return None.
    """
    # Find any {...} block
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        return None

    json_block = match.group(0)

    # Try to load as JSON
    try:
        return json.loads(json_block)
    except:
        # Attempt fix single quotes → double quotes
        try:
            return json.loads(json_block.replace("'", '"'))
        except:
            return None
