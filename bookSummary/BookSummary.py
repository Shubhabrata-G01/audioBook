import openai

openai.api_key = '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'

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="What is the meaning of life?"
)

print(response["choices"][0]["text"])
