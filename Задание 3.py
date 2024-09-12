length = int(input('Введите длину текста:   '))
st = input('Введите текст:   ').split()
length_of_st = []
for i in st:
    length_of_st.append(len(i))
mx_length_of_st = max(length_of_st)
for j in st:
    if st.index(j) == length_of_st.index(mx_length_of_st):
        print(j)
        break
print(max(length_of_st))