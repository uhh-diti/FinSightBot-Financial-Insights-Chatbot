
def get_financial_response(question):
    responses = {
        "What is the total revenue for Apple in 2024?":
            "Apple's total revenue in 2024 was $391.04 billion.",
        "How did Tesla's net income change from 2023 to 2024?":
            "Tesla's net income dropped from $14.99B to $7.09B — a 52.7% decrease.",
        "Which company had the highest cash flow in 2024?":
            "Microsoft had the highest cash flow with $118.45B.",
        "How much did Microsoft's revenue grow from 2023 to 2024?":
            "It grew from $198.27B to $245.07B — a 23.6% increase.",
        "What are Apple's total assets in 2024?":
            "Apple's assets were $364.98B in 2024."
    }
    return responses.get(question, "Sorry, I don't have data for that.")

dataset['Response'] = dataset['Question'].apply(get_financial_response)
