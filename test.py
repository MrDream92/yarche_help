

import psycopg2
db_connection = psycopg2.connect('postgres://fkvwzabaokdhjt:2f9133f794d76362a927e499867869bbf330f27e4bfbf9e6a1aa0bf13cddbca5@ec2-52-201-124-168.compute-1.amazonaws.com:5432/dd36tcghqpg0if', sslmode='require')
db_object = db_connection.cursor()

db_object.execute(f'SELECT * FROM users_mag WHERE user_number = 11')
result = db_object.fetchall()

for item in enumerate(result):
    print(item[1][1])