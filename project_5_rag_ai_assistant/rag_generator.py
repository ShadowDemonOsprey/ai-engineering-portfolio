import ollama



def generate_answer(question, context):


    response = ollama.chat(

        model="qwen2.5:0.5b",

        messages=[

            {
                "role":"system",
                "content":
                "Answer only from the context. If the context does not contain the answer, say 'I don't know'."
            },


            {
                "role":"user",
                "content":
                f"""
Context:

{context}


Question:

{question}
"""
            }

        ]
    )


    return response["message"]["content"]