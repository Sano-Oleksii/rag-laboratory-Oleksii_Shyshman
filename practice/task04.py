from rag.ingestion.embedder import get_vector
from rag.ingestion.repository import get_similar_chunks
from llm.llm import get_ai_response 

query = "Сколько дней занимает доставка?"
vector = get_vector(query)
chunks = get_similar_chunks(vector, top_k=2)
print(len(chunks))

# Распаковка кортежа прямо в цикле.
# Каждый элемент chunks — пара (текст, оценка).
# text получает 1-е значение, score — 2-е.
# То же самое, что text, score = item, только сразу в for
# Python распределяет значения по порядку, а не по названиям переменных.
for text, score in chunks:
    print(text , f"{score:.3f}")
print(get_ai_response(query, chunks, mode="demo"))
