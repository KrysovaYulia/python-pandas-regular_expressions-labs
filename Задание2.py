import pandas as pd



person = pd.DataFrame([[0, 'Анна Петровна Смирнова', '47', 'женский', 0, 20], [1, 'Иван Сергеевич Петров', '26', 'мужской', 3, 16], [2, 'Мария Ивановна Сидорова', '38', 'женский', 9, 23], [3, 'Сергей Михайлович Иванов', '33', 'мужской', 3, 9], [4, 'Ольга Дмитриевна Васильева', '29', 'женский', 7, 5], [5, 'Дмитрий Викторович Соколов', '44', 'мужской', 5, 27], [6, 'Елена Николаевна Петрова', '32', 'женский', 6, 8], [7, 'Андрей Константинович Васильев', '50', 'мужской', 7, 24], [8, 'Татьяна Михайловна Соколова', '23', 'женский', 8, 2], [9, 'Алексей Викторович Смирнов', '36', 'мужской', 9, 12], [10, 'Екатерина Сергеевна Иванова', '25', 'женский', 10, 0], [11, 'Виктор Дмитриевич Петров', '49', 'мужской', 9, 3], [12, 'Юлия Константиновна Сидорова', '42', 'женский', 0, 19], [13, 'Михаил Сергеевич Васильев', '28', 'мужской', 1, 22], [14, 'Ирина Николаевна Соколова', '39', 'женский', 2, 26], [15, 'Николай Викторович Петров', '35', 'мужской', 3, 17], [16, 'Светлана Михайловна Сидорова', '22', 'женский', 4, 4], [17, 'Константин Дмитриевич Иванов', '46', 'мужской', 5, 14], [18, 'Галина Николаевна Васильева', '41', 'женский', 6, 6], [19, 'Павел Викторович Смирнов', '24', 'мужской', 7, 28], [20, 'Роман Сергеевич Иванов', '34', 'женский', 8, 13], [21, 'Виктория Михайловна Сидорова', '59', 'мужской', 9, 21], [22, 'Александр Дмитриевич Васильев', '27', 'женский', 10, 18], [23, 'Дарья Николаевна Соколова', '43', 'мужской', 11, 7], [24, 'Григорий Викторович Петров', '48', 'женский', 0, 25], [25, 'Виталий Сергеевич Сидоров', '31', 'мужской', 1, 10], [26, 'Ксения Михайловна Иванова', '45', 'женский', 2, 29], [27, 'Максим Викторович Васильев', '20', 'мужской', 3, 1], [28, 'Валерия Николаевна Соколова', '37', 'женский', 4, 15], [29, 'Артём Сергеевич Петров', '40', 'мужской', 5, 11]], columns=['id', 'ФИО', 'Возраст', 'Пол', 'ID_Фирмы', 'ID_Должности'])
position = pd.DataFrame([[0, 'Системный администратор'], [1, 'Веб-разработчик'], [2, 'Инженер по тестированию'], [3, 'Специалист по информационной безопасности'], [4, 'Администратор баз данных'], [5, 'UX/UI-дизайнер'], [6, 'Разработчик мобильных приложений'], [7, 'Аналитик данных'], [8, 'DevOps-инженер'], [9, 'Архитектор решений'], [10, 'Технический писатель'], [11, 'Менеджер проектов'], [12, 'Бизнес-аналитик'], [13, 'Сетевой инженер'], [14, 'Специалист технической поддержки'], [15, 'Data Scientist'], [16, 'Специалист по машинному обучению'], [17, 'Администратор серверов'], [18, 'Программист'], [19, 'Инженер облачных технологий'], [20, 'Инженер-исследователь'], [21, 'Специалист по кибербезопасности'], [22, 'Специалист по работе с большими данными'], [23, 'Инженер по автоматизации процессов'], [24, 'Инженер машинного обучения'], [25, 'Инженер искусственного интеллекта'], [26, 'Инженер по разработке алгоритмов'], [27, 'Инженер по оптимизации производительности'], [28, 'Инженер по внедрению новых технологий'], [29, 'Инженер по анализу и обработке данных']], columns=['id', 'Название_Должности'])
firm = pd.DataFrame([[0, 'Цифровые технологии'], [1, 'IT-решения'], [2, 'ИнфоТех'], [3, 'Информационные системы'], [4, 'Техноком'], [5, 'Интеллект-системы'], [6, 'Интеллектуальные технологии'], [7, 'Кибернетика'], [8, 'Сети и системы'], [9, 'Технологии будущего'], [10, 'ИТ-эксперт'], [11, 'Инновационные технологии']], columns=['id', 'Название_Фирмы'])


union = person.merge(position, left_on="ID_Должности", right_on="id").merge(firm, left_on="ID_Фирмы", right_on="id")
pd.options.display.expand_frame_repr = False
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

def choose_number():
    print('Функции:', '  ', sep='\n')
    print('1=Удалить', '2=Добавить', '3=Изменить', sep='\n')
    name_func = ['Удалить', 'Добавить', 'Изменить']
    print()
    while True:
        number_func = input('Введите номер функции(1,2,3): ')
        if number_func == '1' or number_func == '2' or number_func == '3':
            a = f'{name_func[int(number_func) - 1]}'
            return a
            break
        else:
            print("Вы ввели некорректные символы! Попробуйте ещё раз ввести номер функции(1, 2, 3)!", sep='\n')


name_user = None
name_position = None
name_firm = None
name_pol = None
age = None

def choose_data(ch_num):
    global name_user
    global name_position
    global name_firm
    global age
    global name_pol
    while True:
        print('Введите значения! Если значение неизвестно, введите знак "-"')
        name_user = input('Введите имя сотрудника: ')
        age = input('Возраст сотрудника: ')
        name_pol = input('Введите пол сотрудника: ')
        name_position = input('Введите название должности: ')
        name_firm = input('Введите название фирмы: ')
        data_base = [name_user, age, name_pol, name_position, name_firm]
        data_base_without_none = [i for i in data_base if i != '-']
        name_column = ['ФИО', 'Возраст', 'Пол', 'Название_Должности', 'Название_Фирмы']
        if ch_num == 'Удалить' or ch_num == 'Изменить':
            c = 0
            for i in range(len(data_base)):
                if data_base[i]!= '-' and data_base[i] in union[name_column[i]].values:
                    c += 1
            if c == len(data_base_without_none):
                print('Все данные обнаружены успешно!')
                return data_base
                break
            else:
                print('Данные не обнаружены! попробуйте снова!')
        elif ch_num == 'Добавить':
            c = 0
            for i in range(len(data_base)):
                if data_base[i] != '-' and data_base[i] in union[name_column[i]].values:
                    c += 1
            if c != len(data_base_without_none):
                return data_base
                break


def selection():
    print(f'Ваш выбор: "Функция: {ch_num}", "Данные: ФИО: {ch_d[0]}, Возраст сотрудника: {ch_d[1]}, Пол сотрудника: {ch_d[2]}, Название должности: {ch_d[3]}, Название фирмы: {ch_d[4]}"', '  ', sep='\n')
    while True:
        answer = input('Введите подтверженик своего выбора: Да/Нет: ')
        if answer == 'Да':
            print('Выбор подверждён')
            return 'True'
            break
        elif answer == 'Нет':
            print('Выбор не подверждён')
            return 'False'
            break
        else:
            print('Некорректное значение!')



def append_data_func(union):
    data_base = [name_user, age, name_pol, name_position, name_firm]
    id_position1 = - 1
    for i in position.values:
        if i[1] == name_position:
            id_position = i[0]
    if id_position1 == - 1:
        id_position1 = position['id'].max() + 1
    id_firm = - 1
    for i in firm.values:
        if name_firm in i:
            id_firm = i[0]
    if id_firm == - 1:
        id_firm = firm['id'].max() + 1
    new_row = pd.DataFrame([[(union['id_x'].values)[-1] + 1, name_user, age, name_pol, id_firm, id_position1, id_position1,name_position, id_firm, name_firm]], columns=['id_x', 'ФИО', 'Возраст', 'Пол', 'ID_Фирмы', 'ID_Должности', 'id_y', 'Название_Должности', 'id', 'Название_Фирмы'])
    union = union._append(new_row, ignore_index=True)
    print(union)

def del_data(union):
    union2 = union.copy()
    data_base = [name_user, age, name_pol, name_position, name_firm]
    data_base_without_none = [i for i in data_base if i != '-']
    name_column = ['ФИО', 'Возраст', 'Пол', 'Название_Должности', 'Название_Фирмы']
    old_data_column = [name_column[i] for i in range(len(data_base)) if data_base[i] != '-']
    del_line = 0
    for i in range(len(old_data_column)):
        if old_data_column[i] == 'Название_Должности' or old_data_column[i] == 'Название_Фирмы':
            drop_data = union2[union2[old_data_column[i]] == data_base_without_none[i]].index
            union2.drop(drop_data, inplace=True)
            del_line += 1
        elif old_data_column[i] == 'ФИО':
            drop_data = union2[union2[old_data_column[i]] == data_base_without_none[i]].index
            union2.iloc[drop_data] = 0
            del_line += 1


    print(union2, f'Удалено строк: {len(union.values) - len(union2.values)}', sep="\n")


def replace_data(union):
    union2 = union.copy()
    data_base = [name_user, age, name_pol, name_position, name_firm]
    data_base_without_none = [i for i in data_base if i != '-']
    name_column = ['ФИО', 'Возраст', 'Пол', 'Название_Должности', 'Название_Фирмы']
    old_data_column = [name_column[i] for i in range(len(data_base)) if data_base[i] != '-']
    new_name_user = input('Новое имя пользователя   ')
    new_age_user = input('Новый возраст пользователя   ')
    new_p_user = input('Новый пол пользователя   ')
    new_name_position = input('Новая должность пользователя  ')
    new_name_firm = input('Новая фирма пользователя   ')
    new_data_base = [i for i in [new_name_user, new_age_user, new_p_user, new_name_position, new_name_firm] if i != '-']
    for i in range(len(old_data_column)):
        union2.loc[union2[old_data_column[i]] == data_base_without_none[i], [old_data_column[i]]] = new_data_base[i]
    print(union2)

ch_num = choose_number()
print(ch_num)
ch_d = choose_data(ch_num)
print(ch_d)
ch_sel = selection()
if ch_sel == 'True' and ch_num == 'Добавить':
    append_data_func(union)
if ch_sel == 'True' and ch_num == 'Изменить':
    replace_data(union)
if ch_sel == 'True' and ch_num == 'Удалить':
    del_data(union)