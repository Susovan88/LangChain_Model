from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    max_output_tokens=15,
    top_p=0.9,
    top_k=40,
    convert_system_message_to_human=True,
    timeout=30,
    max_retries=2
)

result=llm.invoke("Answer in ONE sentence only. Who is the football GOAT?")
print(result.content)