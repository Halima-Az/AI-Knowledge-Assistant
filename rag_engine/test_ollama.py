from llm import LLMProvider

llm= LLMProvider().get_llm()

res=llm.invoke("exlplique RAG multimodal en une phrase bien resumée")

print(res.content)