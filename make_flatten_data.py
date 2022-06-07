import sqlite3
import csv

'''
Exports a CSV file of the flatten data

args
    none

return 
    none
'''
def main():
    database_path = 'exercise01.sqlite'
    csv_path = 'flatten_data.csv'

    connection = make_database_connection(database_path)
    data = datadump_flatten_data_table(connection)

    make_csv(data, csv_path)


'''
Makes a connection to a sqlite database

args
    database_path (string): path to the sql database file

return 
    sqlite connection object: sqlite database connection object
'''
def make_database_connection(database_path):
    connection = None

    try:
        connection = sqlite3.connect(database_path)
    except:
        print('Cant connect to database')
    else:
        print(f"connected! \t {database_path}\n")

    return connection


'''
grabs all data and all fields from the flatten_data table

args
    connection (sqlite connection object): object used to connect to a sqlite database

return 
    list: all the data from the flatten_data table. list[0] == heads / list[1] == data
'''
def datadump_flatten_data_table(connection):
    query = "select * from flatten_data;"

    cur = connection.cursor()
    cur.execute(query)

    headers = [header[0] for header in cur.description]
    rows = cur.fetchall()
    data = [headers, rows]

    return data


'''
takes data and puts it into a csv file

args
    data (list): list object of data. list[0] == heads / list[1] == data
    file_path (string): the path to which you want the csv file to be kicked out too
 
return 
    none
'''
def make_csv(data, file_path):
    headers = data[0]
    rows = data[1]

    print(f"Creating file: {file_path}")

    with open(file_path, 'w') as file:
        writer = csv.writer(file)

        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)

    print("Done!")


if __name__ == '__main__':
    main()
