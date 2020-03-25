def create_column(column_name):  
    return requests.post(base_url.format('lists'), data={'name': column_name, 'idBoard': board_id, **auth_params}).json()



if __name__ == "__main__":
	elif sys.argv[1] == 'create_column':
    	create_column(sys.argv[2])


def column_check(column_name):  
    column_id = None  
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()  
    for column in column_data:  
        if column['name'] == column_name:  
            column_id = column['id']  
            return column_id



def create(name, column_name):  
    column_id = column_check(column_name)  
    if column_id is None:  
        column_id = create_column(column_name)['id']  
  
    requests.post(base_url.format('cards'), data={'name': name, 'idList': column_id, **auth_params})


def move(name, column_name):    
    column_data = requests.get(base_url.format('boards') + '/' + board_id + '/lists', params=auth_params).json()  
   
    task_id = None  
    for column in column_data:  
        column_tasks = requests.get(base_url.format('lists') + '/' + column['id'] + '/cards', params=auth_params).json()  
        for task in column_tasks:  
            if task['name'] == name:  
                task_id = task['id']  
                break  
        if task_id:  
            break  
  

    if column_id is None:  
        column_id = create_column(column_name)['id']  
      
    requests.put(base_url.format('cards') + '/' + task_id + '/idList', data={'value': column_id, **auth_params})

