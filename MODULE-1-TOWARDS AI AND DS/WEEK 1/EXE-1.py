warning_int = ' must be int'

def check_type_int(value):
    return type(value) is not int

def exercise1(tp, fp, fn):
    # check type int

    if check_type_int(tp):
        return print('tp' + warning_int)
    if check_type_int(fp):
        return print('fp' + warning_int)
    if check_type_int(fn):
        return print('fn' + warning_int)

    # check greater 0

    if tp <=0 or fp <= 0 or fn <=0:
        return print('tp and fp and fn must be greater than zero')

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)

    result = (f'precision is {precision}\n'
              f'recall is {recall}\n'
              f'f1-score is {f1_score}\n')

    return print(result)

print(exercise1(tp=2, fp=3, fn=4))
print(exercise1(tp='a', fp=3, fn=4))
print(exercise1(tp=2, fp='a', fn=4))
print(exercise1(tp=2, fp=3, fn='a'))
print(exercise1(tp=2, fp=3, fn=0))
print(exercise1(tp=2.1, fp=3, fn=0))