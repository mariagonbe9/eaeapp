import json
import pg8000

def lambda_handler(event, context):

    # Setup Postgres Connection
  conn = pg8000.connect(
        host= 'database-1.chgsgumkmqt2.us-east-1.rds.amazonaws.com',
        user= 'postgres',
        password= '12345678',
        database= 'postgres',
        ssl_context= True
    )

    cursor = conn.cursor()

    # Execute MySQL Query
    query = """
    SELECT
        CASE
            WHEN remote_ratio = 100 THEN 'Remote'
            WHEN remote_ratio = 50 THEN 'Hybrid'
            WHEN remote_ratio = 0 THEN 'On Site'
            ELSE 'other'
        END AS remote_type,
        COUNT(remote_ratio) as remote_count FROM salaries GROUP BY remote_ratio;
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
