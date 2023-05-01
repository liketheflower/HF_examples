SELECTED_TASK = "sentiment-analysis"
INPUT = ["Mobi DS is awesome!", "I hate coffee as it makes me sleepless", "cat", "dog"]


from transformers import pipeline


task_pipe = pipeline(f"{SELECTED_TASK}")


OUTPUT = task_pipe(INPUT)
for text, output in zip(INPUT, OUTPUT):
    print(text, output)
