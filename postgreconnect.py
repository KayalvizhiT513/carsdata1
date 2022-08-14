import psycopg2

def runquery(sql):
    try:
        #Connect to the heroku postgresql database
        connection=psycopg2.connect(user="dozmnjvuoahhes",
                                    password="50216fac18e7668ee67b1ad3e2e78a5af2eee2ebc267763d5a004f4cca29ba1d",
                                    host="ec2-3-228-235-79.compute-1.amazonaws.com",
                                    database="d13r72g3hjf57n")

        #Create a cursor to perform database operations
        cursor=connection.cursor()

        #Use the cursor to run an SQL. The exact SQL is defined in another python script.
        cursor.execute(sql)

        #Fetch all records from the table using the SQL
        record=cursor.fetchall()

        #Return the fetched record to the calling program.
        return(record)
    except:
        print("Error while fetching data")
    finally:
        #Close Cursor and Database Connection
        cursor.close()
        connection.close()
