def find_even_index(arr):
    for i, item in enumerate(arr):
        left = sum(arr[0:i])
        right = sum(arr[i + 1:])
        if left == right:
            return i
    else:
        return '-1'


print(f'это он{find_even_index([1, 2, 3, 4, 5, 6])}')

number = 10
res = []
for i in range(number):
    if i % 3 == 0 and i % 5 == 0:
        res.append(i)
    elif i % 3 == 0 or i % 5 == 0:
        res.append(i)

print(sum(res))

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

def anagrams(word, words):
    a = sorted(word)
    a.sort()
    res = []
    for i in words:
        b = list(i)
        b.sort()
        if a == b:
            res.append(i)
    return res

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))


def anagrams1(word, words): return [item for item in words if sorted(item)==sorted(word)]

print(anagrams1('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

print(sorted('bbff')) # sorted работает со строкой!