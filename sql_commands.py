sql_create_data_table = """CREATE TABLE IF NOT EXISTS data (
                                id integer PRIMARY KEY,
                                unix_time integer NOT NULL,
                                ticker text NOT NULL,
                                acceleration integer NOT NULL,
                                velocity integer NOT NULL,
                                counts integer NOT NULL
                            );"""

sql_insert = ''' INSERT INTO data(unix_time,ticker,acceleration,velocity,counts)
                 VALUES(?,?,?,?,?) '''
