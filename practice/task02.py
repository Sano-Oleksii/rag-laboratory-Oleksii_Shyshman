from llm.prompt_builder import build_prompt

query = "Где находится магазин?"
chunks = [("Адрес нашего магазина - город Берлин.", 0.85)]

prompt = build_prompt(query, chunks)
print(prompt)
print(query in prompt)
# Есть ли строка "Где находится магазин?" внутри строки prompt?
print("Берлин" in prompt)
# Встречается ли слово "Берлин" внутри строки prompt?

# query содержит только вопрос пользователя.
# prompt содержит инструкции, контекст и сам вопрос.
