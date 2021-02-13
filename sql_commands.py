sql_create_data_table = """CREATE TABLE IF NOT EXISTS data (
                                unix_time integer NOT NULL,
                                ticker text NOT NULL,
                                counts integer NOT NULL,
                                PRIMARY KEY (unix_time, ticker)
                            );"""

sql_insert = ''' INSERT INTO data(unix_time,ticker,counts)
                 VALUES(?,?,?) '''
