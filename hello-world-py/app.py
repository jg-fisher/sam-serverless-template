import os

def my_handler(event, context):
    
    conn_string = os.environ.get('DATABASE_CONN_STRING')
    
    table_name = os.environ.get('TABLE_NAME')
              
    return { 
        'table_name' : table_name,
        'conn_string': conn_string
    }