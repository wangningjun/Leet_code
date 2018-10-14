from functools import reduce
sentences = ['The Deep Learning textbook is a resource intended to help students and practitioners enter the field of machine learning in general and deep learning in particular. ']


word_count =reduce(lambda a,x:a+x.count("learning"),sentences,0)
# a设置的默认值为0，x第一次为‘The’，往后x都往sentence中取数

print(word_count)

