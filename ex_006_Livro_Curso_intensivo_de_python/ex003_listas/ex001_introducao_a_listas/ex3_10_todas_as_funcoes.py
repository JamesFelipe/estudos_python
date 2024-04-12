idiomas = ['português', 'inglês', 'espanhol', 'japonês']

print(idiomas)
idiomas[-1] = 'madarim'
print(idiomas)

idiomas.append('italiano')
print(idiomas)

idiomas.insert(2, 'grego')
print(idiomas)

print(sorted(idiomas))

idiomas.reverse()
print(idiomas)

idiomas.sort()
print(idiomas)

idiomas.sort(reverse=True)
print(idiomas)

print(idiomas.pop())

del idiomas[1]
print(idiomas)

idiomas.remove('grego')
print(idiomas)

idiomas.clear()
print(idiomas)
