from transformers import pipeline


SELECTED_TASK = "text-generation"
MODEL = "gpt2"
task_pipe = pipeline(f"{SELECTED_TASK}", model = MODEL)


INPUT = "Hello, I am a data scientist."
OUTPUT = task_pipe(INPUT, max_length = 30, num_return_sequences=3)


print(OUTPUT)

