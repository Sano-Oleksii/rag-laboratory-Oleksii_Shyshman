from rag.ingestion.loader import get_content
# Подключаем чтение source/source.txt.
from rag.ingestion.cleaner import clean_content
# Подключаем очистку исходного текста.
from rag.ingestion.chunker import get_chunks
# Подключаем разделение на четыре факта.
from rag.ingestion.embedder import get_vector, get_vectors
# Подключаем кодирование одной строки и списка чанков.
chunks = get_chunks(clean_content(get_content()))
# Читаем файл и готовим очищенные фрагменты.
vector = get_vector("Как оплатить заказ?")
# Получаем вектор одного вопроса.
vectors = get_vectors(chunks)
# Получаем пары вектор и текст для всех фактов.
print(vector.shape)
# Проверяем форму вектора вопроса.
print(len(vectors))
# Проверяем количество пар по количеству фактов.
print(vectors[0][1])
# Показываем текст первой пары.
print(vectors[0][0].shape)
# Проверяем форму вектора первой пары.