import os
import requests
import json

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError(
                "OPENROUTER_API_KEY environment variable is not set. "
                "Please set it in your deployment environment (Render dashboard) "
                "or in your local .env file."
            )

        # free model that worked for you earlier
        self.model = "mistralai/mistral-7b-instruct:free"

    def generate(self, prompt, max_tokens=300, temperature=0.4):
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
                content = data_json["choices"][0]["message"]["content"]
                return content.strip() if content else "EMPTY_RESPONSE"

            # Check for auth errors
            if "error" in data_json:
                error_msg = data_json["error"].get("message", "Unknown error")
                if "401" in str(data_json) or "auth" in error_msg.lower():
                    return f"ERROR: Authentication failed. Check OPENROUTER_API_KEY is valid: {error_msg}"
                return f"ERROR: {error_msg}"

            return f"ERROR: Unexpected response format - {data_json}"

        except Exception as e:
            return f"ERROR_EXCEPTION: {str(e)}"
