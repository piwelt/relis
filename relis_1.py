def read():
    # Получим данные всех колонок на доске:  
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()  
  
    # Теперь выведем название каждой колонки и всех заданий, которые к ней относятся:  
    for column in column_data:
        # Получим данные всех задач в колонке. Мы и раньше делали это, но до этого мы только перебирали элементы этих данных, 
        # А теперь мы ещё получим общее количество задач при помощи встроенной функции `len()`:
        task_data = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()  
        print(column['name'] + " - ({})".format(len(task_data)))  
  
        if not task_data:  
            print('\t' + 'Нет задач!')  
            continue  
        for task in task_data:  
            print('\t' + task['name'])