from sqlalchemy import create_engine, text
from utils import decompose_vin, r_sys
import logging
from verification_mb import model_conditions


engine = create_engine('sqlite+pysqlite:///vinchecker.db',echo=True)

FORMAT = '%(asctime)s: %(levelname)s: %(name)s %(message)s'
logging.basicConfig(filename='database.log', encoding='utf-8',level=logging.INFO, format=FORMAT)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)



def vin_check(number):
    vin = decompose_vin(number)
    with engine.connect() as conn:
        stmt = text(f"select wmi from wmi where code = '{vin['wmi']}'")
        result = conn.execute(stmt)
        wmi = [item for item in result]
        stmt = text(f"select year from year where code = '{vin['model year']}'")
        result = conn.execute(stmt)
        model_year = [item for item in result]
        stmt = text(f"select body_type from body where code = '{vin['vds']['type']}'")
        result = conn.execute(stmt)
        body = [item for item in result]
        safe = r_sys(vin['restraint system'])
        stmt = text(f"select safety from safety where code = '{safe}'")
        result = conn.execute(stmt)
        safety = [item for item in result]
        stmt = text(f"select factory, country from factory where code = '{vin['manufacturing plant']}'")
        result = conn.execute(stmt)
        factory = [item for item in result]


        details = model_conditions(vin['vds']['model'],vin['vds']['type'],model_year)

        vin_data = {
            'manufacturer':wmi[0][0],
            'details':details,
            'body':body[0][0],
            'restraint system' :safety[0][0],
            # 'check digit':check_digit,
            'manufacturing plant':{
            'Name':factory[0][0],
            'country':factory[0][1]
            },
            'serial number':vin['serial number']
            }
    return vin_data

print(vin_check('WDDVP9AB8EJ003726'))

# with engine.connect() as conn:
#     t = text ('select * from factory')
#     r = conn.execute(t)
#     for i in r:
#         print(i)
# wmi = read_csv('../Mercedes/mb_factory.csv')
# Controls.populate_factory(wmi,engine)





    
    
    



      
      
