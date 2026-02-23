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
    
