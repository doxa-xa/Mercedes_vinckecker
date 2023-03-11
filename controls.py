from sqlalchemy import text

##################################################################
#                       TABLE POPULATE                           #
##################################################################

class Controls:

    @staticmethod
    def polulate_mercedes_vds(data, engine):
            with engine.connect() as conn:
                for row in range(0,len(data)):
                    stmt = text(f'''
                        INSERT INTO vds_mb_new (code, model, chassis, year, year_to)
                        VALUES("{data[row][0]}","{data[row][1]}","{data[row][2]}","{data[row][3]}","{data[row][4]}");
                    ''')
                    conn.execute(stmt)
                conn.commit()

    @staticmethod
    def populate_wmi(data,engine):
        with engine.connect() as conn:
                for row in range(0,len(data)):
                    stmt = text(f'''
                    INSERT INTO wmi (code,wmi)
                    VALUES('{data[row][0]}','{data[row][1]}')
                    ''')
                    conn.execute(stmt)
                conn.commit()

    @staticmethod
    def populate_factory(data,engine):
        with engine.connect() as conn:
                for row in range(0,len(data)):
                    stmt = text(f'''
                    INSERT INTO factory (code,factory,country)
                    VALUES('{data[row][0]}','{data[row][1]}','{data[row][2]}')
                    ''')
                    conn.execute(stmt)
                conn.commit()
        
    @staticmethod
    def populate_safety(data, engine):
            with engine.connect() as conn:
                for row in range(0,len(data)):
                    stmt = text(f'''
                        INSERT INTO safety (code, safety)
                        VALUES('{data[row][0]}','{data[row][1]}');
                    ''')
                    conn.execute(stmt)
                conn.commit()

    @staticmethod
    def populate_year(data, engine):
            with engine.connect() as conn:
                for row in range(0,len(data)):
                    stmt = text(f'''
                        INSERT INTO year (code, year)
                        VALUES("{data[row][0]}",{data[row][1]});
                    ''')
                    conn.execute(stmt)
                conn.commit()

    @staticmethod
    def populate_body(data, engine):
            with engine.connect() as conn:
                for row in range(0,len(data)):
                    stmt = text(f'''
                        INSERT INTO body (code, body_type)
                        VALUES("{data[row][0]}",'{data[row][1]}');
                    ''')
                    conn.execute(stmt)
                conn.commit()

    ##################################################################
    #                             TABLES                             #
    ##################################################################

class Tables:

    @staticmethod
    def create_vds_mercedes_table(engine):
            with engine.connect() as conn:
                conn.execute(text('''
                CREATE TABLE IF NOT EXISTS "vds_mb_new" (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT,
                    model TEXT,
                    chassis TEXT,
                    year TEXT,
                    year_to TEXT)
                '''))
                conn.commit()
    @staticmethod
    def create_wmi_table(engine):
            with engine.connect() as conn:
                conn.execute(text('''
                CREATE TABLE IF NOT EXISTS "wmi" (
                    code INT PRIMARY KEY,
                    wmi TEXT)
                '''))
                conn.commit()

    @staticmethod
    def create_factory_table(engine):
            with engine.connect() as conn:
                conn.execute(text('''
                CREATE TABLE IF NOT EXISTS "factory" (
                    code TEXT PRIMARY KEY,
                    factory TEXT,
                    country TEXT)
                '''))
                conn.commit()

    @staticmethod
    def create_safety_table(engine):
            with engine.connect() as conn:
                conn.execute(text('''
                CREATE TABLE IF NOT EXISTS "safety" (
                    code INT PRIMARY KEY,
                    safety TEXT)
                '''))
                conn.commit()

    @staticmethod
    def create_year_table(engine):
        with engine.connect() as conn:
            conn.execute(text('''
            CREATE TABLE IF NOT EXISTS "year" (
                code TEXT,
                year INT PRIMARY KEY)
            '''))
            conn.commit()

    @staticmethod
    def create_body_table(engine):
        with engine.connect() as conn:
            conn.execute(text('''
            CREATE TABLE IF NOT EXISTS "body" (
                code TEXT PRIMARY KEY,
                body_type TEXT)
            '''))
            conn.commit()

