from django.shortcuts import render, redirect
from django.db.models import Avg, Count
from .forms import ReviewForm
from .models import Review
from .llm_client import LLMClient
import json

def user_dashboard(request):
    llm = LLMClient()
    result = None
    error = None

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_obj = form.save(commit=False)

            prompt = f"""
You are a customer support assistant.

Given this user review and rating, return JSON ONLY:

{{
  "summary": "1–2 sentence summary",
  "action": "one recommended business action",
  "reply": "friendly short reply to the user"
}}

Rating: {review_obj.rating}
Review: \"\"\"{review_obj.review_text}\"\"\"
"""

            response = llm.generate(prompt)

            try:
                start = response.find("{")
                end = response.rfind("}")
                json_str = response[start:end+1]
                data = json.loads(json_str)

                review_obj.ai_summary = data.get("summary", "")
                review_obj.ai_action = data.get("action", "")
                review_obj.ai_reply = data.get("reply", "")
                review_obj.save()

                result = review_obj

            except Exception:
                error = f"Could not parse AI response. Raw output: {response}"

    else:
        form = ReviewForm()

    return render(request, "feedback/user_dashboard.html", {
        "form": form,
        "result": result,
        "error": error
    })


def admin_dashboard(request):
    reviews = Review.objects.order_by("-created_at")

    stats = reviews.aggregate(
        avg_rating=Avg("rating"),
        total_reviews=Count("id")
    )

    rating_counts = (
        reviews.values("rating")
        .order_by("rating")
        .annotate(count=Count("rating"))
    )

    labels = [str(item["rating"]) for item in rating_counts]
    counts = [item["count"] for item in rating_counts]

    return render(request, "feedback/admin_dashboard.html", {
        "reviews": reviews,
        "stats": stats,
        "chart_labels": json.dumps(labels),
        "chart_data": json.dumps(counts)
    })
