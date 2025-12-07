# task1_scripts/prompts.py

DIRECT_PROMPT_TEMPLATE = """
You are a review classifier. Given the Yelp review below, assign a star rating from 1 to 5.
Return only a JSON object with keys:
  "predicted_stars": (int),
  "explanation": (brief string)

Review:
\"\"\"{review}\"\"\"
"""

CHAIN_REASONING_PROMPT_TEMPLATE = """
You are an assistant that reasons briefly about the sentiment and assigns a rating.

1) Give a short reasoning (1–2 sentences).
2) Then output a SINGLE JSON object with keys predicted_stars and explanation.

Review:
\"\"\"{review}\"\"\"

Reasoning:
"""

FEWSHOT_PROMPT_PREFIX = """
You are a helpful classifier. Examples:

Review: "Great food and quick service"
→ {{ "predicted_stars": 5, "explanation": "Positive mention of food and service." }}

Review: "Food was cold and the waiter was rude"
→ {{ "predicted_stars": 2, "explanation": "Negative food quality and poor service." }}

Review: "Okay place, not bad but overpriced"
→ {{ "predicted_stars": 3, "explanation": "Mixed sentiment; price is an issue." }}

Review: "Terrible, found hair in my soup"
→ {{ "predicted_stars": 1, "explanation": "Severe negative hygiene issue." }}

Review: "Decent food, friendly staff"
→ {{ "predicted_stars": 4, "explanation": "Mostly positive overall." }}

Now classify the following review.
Output ONLY a JSON object with predicted_stars and explanation.

Review:
\"\"\"{review}\"\"\" 

Return output using this format:
{{ 
  "predicted_stars": number,
  "explanation": "short explanation"
}}
"""

