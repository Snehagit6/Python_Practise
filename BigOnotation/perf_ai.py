from groq import Groq

client = Groq(api_key="")

def get_perf_ai_response(program):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that computes the time complexity of a given program. Please provide the time complexity in Big O notation with detailed explanation.Suggest optimized code if possible."
        },
        {
            "role": "user",
            "content": program
        }
        ],
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )


    return completion.choices[0].message.content
