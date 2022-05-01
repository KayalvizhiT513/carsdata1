import psycopg2

def runquery(sql):
    try:
        #Connect to the heroku postgresql database
        connection=psycopg2.connect(user="ltwosumfpujrzw",
                                    password="97feb2e636cf62e0bca9e55acc1398b30a944244b64c5adeb5fb9e88da116ba6",
                                    host="ec2-3-218-171-44.compute-1.amazonaws.com",
                                    database="dfmhcqu5mokg9n")

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
