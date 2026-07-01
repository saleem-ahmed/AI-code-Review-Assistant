from services.review_service import ReviewService

sample = """
def add(a,b):
    return a+b
"""

service = ReviewService()

result = service.prepare_review(
    "main.py",
    sample,
)

print(result["language"])
print(result["analysis"])
print(result["prompt"])