commands = (
    '''
    CREATE TABLE projects(
    project_id SERIAL PRIMARY KEY,
    data JSONB
    )
    ''',
    '''  CREATE TABLE projects_and_task(
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(50) UNIQUE NOT NULL,
    project_created_on TIMESTAMP NOT NULL,
    project_last_change TIMESTAMP NOT NULL,
    task JSONB
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