from llm.prompt_builder import build_context

chunks = [("Доставка занимает 3-5 дней", 0.9), ("В нашем магазине предусмотрен возврат", 0.6)]
print(build_context(chunks))
# Потому что хоть мы и вытянули целый Item в функции duild_context мы используем только текст и номер.
# text, score = item - мы делим наш кортеж и в text идет первое значение кортежа("Доставка занимает 3-5 дней") а в score 0.9 , но дальше в build_context мы используем только text , поэтому оно и не попало в вывод
# так работает text, score = item поэлементно разделяет кортеж если бы у нас было больше элементов в кортеже, то text, score = item был бы с тремя переменными (text, score, ... = item)
print(repr(build_context([])))