name = input('Введите ваше имя >')
#result = 'Привет,%s' % name
result = 'Привет,{nm}'.format(nm=name)
print(result) 