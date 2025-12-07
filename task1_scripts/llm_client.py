import os
import requests
import json

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("Please set OPENROUTER_API_KEY environment variable.")

        # Confirmed working free model from your list
        self.model = "google/gemma-3-4b-it"

    def generate(self, prompt, max_tokens=200, temperature=0.3):
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        try:
            response = requests.post(url, headers=headers, json=data, timeout=40)
            data_json = response.json()

            if "choices" in data_json:
                return data_json["choices"][0]["message"]["content"]
            else:
                return f"ERROR_NO_CHOICES: {data_json}"

        except Exception as e:
            return f"ERROR_EXCEPTION: {str(e)}"
