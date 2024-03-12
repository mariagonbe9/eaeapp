import json
import pg8000

def lambda_handler(event, context):

    # Setup MySQL Connection
    conn = pg8000.connect(
        host= 'database-1.chgsgumkmqt2.us-east-1.rds.amazonaws.com',
        user= 'postgres',
        password= '12345678',
        database= 'salaries',
        ssl_context= True
    )

    cursor = conn.cursor()

    # Execute MySQL Query
    query = """
    SELECT employee_residence, CAST(ROUND(AVG(salary_in_usd), 0) AS UNSIGNED) as average_salary 
    FROM salaries 
    GROUP BY employee_residence 
    ORDER BY average_salary 
    DESC LIMIT 20
    """
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Get column names
    column_names = [i[0] for i in cursor.description]

    # Convert data to JSON format
    result = []
    for row in rows:
        data_dict = {}
        for i in range(len(column_names)):
            data_dict[column_names[i]] = row[i]
        result.append(data_dict)

    # Close connections
    cursor.close()
    conn.close()

    # Construct response
    response = {
        "statusCode": 200,
        "data": json.dumps(result)  # Convert data to JSON
    }

    return response
