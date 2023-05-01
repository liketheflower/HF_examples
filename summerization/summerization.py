
from transformers import pipeline


SELECTED_TASK = "summarization"
task_pipe = pipeline(f"{SELECTED_TASK}")


INPUT = "Mobi grew out of several labs at MIT in 2012. Over the past 10 years we have come to understand that great technology takes more than amazing code; it also requires art, design, enthusiasm for human psychology, and study of the existing forces in the world. Mobi brings together three key elements:1) Cutting edge technology: Mobi draws upon state of the art techniques including constraint programming, natural language processing, computer vision, and preference learning in order to execute sophisticated collaborative tasks. These tasks include routing, planning, forecasting, preference elicitation, and auto-scaling. 2) Understanding of where AI fits in: Even amazing AI fails when its creators don’t understand its strengths and limitations. Knowing how our technology fits with human skills helps us create the best possible user experience to make and execute plans in the real world. 3) Real world context: Providing great plans requires a deep understanding of place as well individual needs and preferences. We have created a “genome of place” that characterizes locations beyond simple filters to reveal how, when, and why they fit into plans."
OUTPUT = task_pipe(INPUT)


print(OUTPUT)

