from django.db import models

class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField()

    ai_summary = models.TextField(blank=True, null=True)
    ai_action = models.TextField(blank=True, null=True)
    ai_reply = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id} - Rating {self.rating}"
