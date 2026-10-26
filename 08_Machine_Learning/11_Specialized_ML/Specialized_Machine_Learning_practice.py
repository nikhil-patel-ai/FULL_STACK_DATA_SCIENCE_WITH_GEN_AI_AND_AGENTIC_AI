"""
Specialized Machine Learning

Goal: Explore a simple recommendation baseline using item popularity.

Run from this folder with:
    python "Specialized_Machine_Learning_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

import pandas as pd

# Example interaction data. Real recommendation systems need careful evaluation.
interactions = pd.DataFrame({
    "user": ["A", "A", "B", "B", "C", "C", "C"],
    "item": ["Python", "SQL", "Python", "ML", "Python", "SQL", "Excel"],
    "rating": [5, 4, 4, 5, 5, 3, 4]
})
popular_items = (
    interactions.groupby("item")
    .agg(rating_count=("rating", "size"), mean_rating=("rating", "mean"))
    .sort_values(["rating_count", "mean_rating"], ascending=False)
)
print("Popularity-based recommendation baseline:")
print(popular_items)
print("\nFor a real system, split interactions by user/time and evaluate recommendations.")
