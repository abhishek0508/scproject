from transformers import pipeline, GPT2Tokenizer


# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# tokenizer.pad_token = tokenizer.eos_token

classifier = pipeline('sentiment-analysis')

results = classifier(["We are very happy to show you the 🤗 Transformers library."
                        ,"We hope you don't hate it."])
for result in results:
    print(f"label: {result['label']}, with score: {round(result['score'], 4)}")