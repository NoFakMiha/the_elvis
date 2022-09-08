commands = (
    '''CREATE TABLE projects(
    project_id SERIAL PRIMARY KEY,
    title VARCHAR(50) UNIQUE NOT NULL,
    created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP
    )''',
    '''CREATE TABLE all_tasks(
    task_id SERIAL PRIMARY KEY,
    task_title VARCHAR(50)  NOT NULL,
    )
    ''',
    '''CREATE TABLE working_on(
    task_id SERIAL PRIMARY KEY,
    task_title VARCHAR(50)  NOT NULL,
    )
    ''',
    '''
    CREATE TABLE done(
    task_id SERIAL PRIMARY KEY,
    task_title VARCHAR(50)  NOT NULL,
    )
    ''',
    '''
    CREATE TABLE bug(
    task_id SERIAL PRIMARY KEY,
    task_title VARCHAR(50)  NOT NULL,
    )
    '''
)