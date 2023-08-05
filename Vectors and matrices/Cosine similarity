import numpy as np
import re
from scipy import spatial as sp
from collections import Counter


# Задание: Дан набор предложений, каждое из которых содержит слово "lead" в разных значениях.
# Необходимо с помощью косинусной близости найти 3 предложения, которые ближе всего к первому в корпусе и вывести их


def main():
    sents = open('sentences.txt').readlines()
    # 1) Привести строки к нижнему регистру
    sents_lower = []
    n = 0
    for sent in sents:
        sents_lower.append(sent.lower())
        n += 1
    print('Количество предложений:', n)
    # 2) Произведите токенизацию (например, с помощью регулярного выражения re.split('[^a-z]', t))
    tokens = []
    for sent in sents_lower:
        tokens.append(re.split('[^a-z]', sent))
    # 3) Составьте словарь всех уникальных слов, встречающихся в предложениях: каждому слову должен соответствовать
    #    индекс от нуля до (d - 1), где d - размер словаря.
    dictionary = {}
    for sent in tokens:
        for token in sent:
            dictionary[token] = 0

    new_dictionary = {}
    d = 0
    for word in dictionary:
        new_dictionary[d] = word
        d += 1
    print('Размер словаря:', d)
    # 4) Создайте пустую матрицу размера n x d, где n — число предложений.
    matrix = np.zeros((n, d))
    # 5) Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен
    #    количеству вхождений j-го слова в i-е предложение.

    for i in range(n):
        for j in range(d):
            matrix[i][j] = sents_lower[i].count(new_dictionary[j])
    # 6) Найдите косинусное расстояние от предложения в самой первой строке до всех остальных с помощью функции scipy.spatial.distance.cosine.
    results = {}
    for x in range(len(sents_lower)):
        result = (sp.distance.cosine(matrix[0], matrix[x]))
        results[x] = result

    top3_results = sorted(results, key=results.get, reverse=True)[:3]

    # <-- здесь необходимо вывести 3 ближайших предложения: каждое на своей строчке
    print('\nТри ближайшие предложения:\n')
    for result in top3_results:
        print(sents[result])


if __name__ == '__main__':
    main()
