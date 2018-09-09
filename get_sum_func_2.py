def get_sum(one,two,delimiter='&'):
    result = str(one) + str(delimiter) + str(two)
    return result.upper()

sum_string=get_sum('Learn','Python')
print(sum_string)