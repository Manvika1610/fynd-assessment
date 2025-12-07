import time
import pandas as pd

from .prompts import (
    DIRECT_PROMPT_TEMPLATE,
    CHAIN_REASONING_PROMPT_TEMPLATE,
    FEWSHOT_PROMPT_PREFIX
)

from .utils import extract_json_from_text


class PromptEvaluator:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.prompt_versions = {
            "direct": DIRECT_PROMPT_TEMPLATE,
            "chain": CHAIN_REASONING_PROMPT_TEMPLATE,
            "fewshot": FEWSHOT_PROMPT_PREFIX
        }

    def run_on_df(self, df, version_key, delay_s=0.2):
        """
        Returns a DataFrame. Never returns None.
        """
        results = []
        prompt_template = self.prompt_versions[version_key]

        for idx, row in df.iterrows():
            review = row["review"]
            gold = int(row["stars"])

            prompt = prompt_template.format(review=review)

            # Get LLM response safely
            try:
                response = self.llm.generate(prompt)
            except Exception as e:
                response = f"ERROR: {str(e)}"

            # Parse JSON
            parsed_json = extract_json_from_text(response)
            if parsed_json:
                predicted = parsed_json.get("predicted_stars")
            else:
                predicted = None

            results.append({
                "review": review,
                "gold": gold,
                "raw_response": response,
                "parsed_json": parsed_json,
                "predicted": predicted
            })

            time.sleep(1.0)

        return pd.DataFrame(results)

    def compute_metrics(self, df):
        """
        Computes accuracy and JSON validity.
        """
        total = len(df)

        valid_json = df["parsed_json"].notnull().sum()
        correct = (df["predicted"] == df["gold"]).sum()

        return {
            "total_samples": total,
            "accuracy": correct / total if total > 0 else 0,
            "json_valid_rate": valid_json / total if total > 0 else 0
        }
