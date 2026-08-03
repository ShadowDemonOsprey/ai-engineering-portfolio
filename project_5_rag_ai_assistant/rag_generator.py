# Import Ollama library to communicate with the local LLM
import ollama


# Create function to generate an answer
def generate_answer(question, context):

    # Send question and retrieved context to Qwen model
    response = ollama.chat(
        model="qwen2.5:0.5b",

        # Create the conversation messages
        messages=[
            {
                # System message defines AI behavior
                "role": "system",

                # Tell the model to answer using provided context
                "content": "Answer only using the provided context."
            },
            {
                # User message contains the question and context
                "role": "user",

                # Combine retrieved document with user question
                "content": f"""
Context:
{context}

Question:
{question}
"""
            }
        ]
    )


    # Return the generated answer text
    return response["message"]["content"]


# Test function
if __name__ == "__main__":

    answer = generate_answer(
        "What is machine learning?",
        "Machine Learning is a branch of AI that allows computers to learn patterns from data."
    )

    print(answer)