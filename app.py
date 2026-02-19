import os

def vulnerable_function(user_data):
    # This is a security risk! Bandit will catch this 'shell=True'
    os.system(f"echo {user_data}") 

def safe_add(a, b):
    return a + b 
