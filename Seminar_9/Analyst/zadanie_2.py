# Иван решил создать самый большой словарь в мире. Для этого он придумал функцию 
# biggest_dict(**kwargs), которая принимает неограниченное количество параметров 
# «ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из 
# одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию
my_dict = {'first_one': 'we can do it'}

def biggest_dict(**kwargs):
    my_dict.update(**kwargs)

biggest_dict(name='Давид', surname = 'Аветян', age = '18', phone_number = '89237775544')
print(my_dict)