# ============================
# Practice Question 1
# ============================
def split_temperatures(readings: list) -> tuple:
    """
    Given a list of tuples (min_temp, max_temp),
    return two separate lists:
    ([all_min_temps], [all_max_temps])
    """
    
    new = zip(*readings)
    return [list(i) for i in new]
    


# ============================
# Practice Question 2
# ============================
def build_product_index(products: list) -> dict:
    """
    Given a list of product names, return a dictionary
    mapping product name -> index position.
    """
    return {x:y for x,y in enumerate(products)}

# ============================
# Practice Question 3
# ============================
def normalize_unique_categories(categories: list) -> set:
    """
    Normalize a list of category strings to lowercase
    and return only unique values.
    """
    return {i.lower() for i in categories}

# ============================
# Practice Question 4
# ============================
def group_students_by_course(students: list) -> dict:
    """
    Given a list of dictionaries:
    {"name": str, "course": str}
    
    Return a dictionary:
    {
        "course_name": [student_names]
    }
    """
    
    new_students = {}
    
    for student in students:
        course = student['course']
        name = student['name']
        if student not in new_students:
            new_students[student] = []
        new_students[student].append(name)
        
    


# ============================
# Practice Question 5
# ============================
def chunk_transactions(transaction_ids: list | tuple, size: int = 3) -> list:
    """
    Split transaction IDs into batches of given size.
    Default batch size is 3.
    """
    
    chunk = []
    for i in range(0,len(transaction_ids),size):
        chunk.append(transaction_ids[i:i+size])
    
    return chunk
    
    
    


# ============================
# Practice Question 6
# ============================
def invert_employee_manager_map(mapping: dict) -> dict:
    """
    Given:
    {"Alice": "Manager1", "Bob": "Manager1", "Clara": "Manager2"}

    Return:
    {"Manager1": ["Alice", "Bob"], "Manager2": ["Clara"]}
    """
    employee = {}
    for key, value in mapping.items():
        if value not in employee:
            employee[value] = []
        employee[value].append(key)
    return employee
print(invert_employee_manager_map({"Alice": "Manager1", "Bob": "Manager1", "Clara": "Manager2"}))

# ============================
# Practice Question 7
# ============================
def fibonacci_sequence(n: int) -> list:
    """
    Return the first n Fibonacci numbers.
    Raise ValueError for negative numbers.
    """
    
    while n >=0:
        if n == 0:
            return []
        elif n == 1:
            return [1]
        else:
            new_list = []
            a,b = 0,1
            new_list.append(a)
            new_list.append(b)
            for i in range(n):
                a,b = b,a+b
                new_list.append(b)
    else:
        raise ValueError
    

# ============================
# TODO: Question 1
# ============================
def split_coords(coordinates: list) -> tuple:
    """
    Given a list of tuples (x, y), split them into two separate lists 
    contained within a single tuple: ( [x-coords], [y-coords] ).
    """
    if len(coordinates)== 0:
        return []
    else:
        new_cord = zip(*coordinates)
        return [list(i) for i in new_cord]
    
    
print(split_coords([(1, 2), (3, 4), (5, 6)]))


# ============================
# TODO: Question 2
# ============================
def create_id_lookup(user_data: list) -> dict:
    """
    Create a dictionary where the user names are keys and their 
    index in the original list is the value.
    """
    
    if not user_data:
        return {}
    else:
        return {name:index for index,name in enumerate(user_data)}
        
print(create_id_lookup(["Peter", "Busang", "Mpho"]))

# ============================
# TODO: Question 3
# ============================
def extract_unique_tags(posts: list) -> set:
    """
    Take a list of strings (tags), normalize them to lowercase, 
    and return a set of unique tags.
    """
    if not posts:
        return {}
    else:
        return {i.lower() for i in posts}
        
   
print(extract_unique_tags(["Python", "python", "PyThOn"]))
    



# ============================
# TODO: Question 4
# ============================
def group_by_category(items: list) -> dict:
    """
    Given a list of dictionaries (each containing 'name' and 'type'), 
    group the names into a dictionary categorized by their type.
    """
    
    if len(items) == 0:
        return {}
    else:
        new_items = {}
        for item in items:
            name = item['name']
            type = item['type']
            
            if type not in new_items:
                new_items[type] = []   
            new_items[type].append(name)  
    return new_items           
    
print(group_by_category([ 
            {"name": "Boerewors", "type": "Meat"}, 
            {"name": "Charcoal", "type": "Hardware"}, 
            {"name": "Lamb Chops", "type": "Meat"}, 
            {"name": "Chakalaka", "type": "Canned Goods"} 
        ]))

# ============================
# TODO: Question 5
# ============================
def batch_api_dispatcher(user_ids: list | tuple) -> list:
    """
    Split a long list of user IDs into smaller batches (e.g., max 5 per batch)
    to be sent to an API.
    """
    if len(user_ids) ==0:
        return []
    else:
        chunks = []
        for i in range(0,len(user_ids),5):
            chunks.append(user_ids[i:i+5])
        return chunks    

print(batch_api_dispatcher(['ID1','ID2','ID3','ID4','ID5','ID6','ID7']))
# ============================
# TODO: Question 6
# ============================
def social_graph_inverter(following_list: dict) -> dict:
    """
    Invert a dictionary representing a social graph (who follows whom) 
    to show followers for each user.
    """
    if not following_list:
        return {}
    else:
        followers = {}
        for key,people in following_list.items():
            for person in people:
                if person not in followers:
                    followers[person] = []
                followers[person].append(key)
        return followers
print(social_graph_inverter({"Alice": ["Bob", "Charlie"], "Bob": ["Charlie"]}))

# ============================
# TODO: Question 7
# ============================
def fibonacci_generator(n: int) -> list:
    """
    Generate a list containing the first n numbers of the Fibonacci sequence.
    Handle cases for n <= 0 and raise a ValueError for negative integers.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    
    fib = fibonacci_generator(n-1)
    fib.append(fib[-1]+fib[-2])
    
    return fib
    

      
print(fibonacci_generator(6))  


def countdown(n):
    
    if n <=0:
        return []
    else:
        count = countdown(n-1)
        
    return [n] +count
print(countdown(5))

