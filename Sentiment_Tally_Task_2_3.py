python_reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]



positive_words = ["good", "excellent"] 
print('length of positive words:',len(positive_words))
negative_words = ["bad", "poor",]
print('length of negative words:',len(negative_words))



summary_reviews = []

for reviews in python_reviews:
    summary = reviews[:30]
    v = 30
    while summary[-1] != " ":
        v += 1
        summary = reviews[:v]
    summary = summary + "..."
    summary_reviews.append(summary)
print(summary_reviews)