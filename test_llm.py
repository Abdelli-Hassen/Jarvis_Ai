from llm_client import ask_simple

print("Jarvis LLM Test — type 'exit' to quit")
while True:
    q = input("You: ")
    if q.lower() in ["exit", "quit"]:
        break
    ans = ask_simple(q)
    print("Jarvis:", ans)
