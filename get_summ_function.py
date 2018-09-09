def get_summ(arg_one, arg_two, delimiter=' fucking '):
    return (str(arg_one) +str(delimiter) + str(arg_two)).upper() 

result=get_summ('Learn','Python')
print(result)