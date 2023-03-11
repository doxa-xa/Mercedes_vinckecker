from utils import c_list_to_str

def read_vin(vin):
      vin = list(vin)
      vehicle_details = {
        'wmi' : c_list_to_str(vin[0:3]),
        'series' : vin[3],
        'body' : vin[4],
        'model' : c_list_to_str(vin[6:7]),
        'safety' : vin[7],
        'check' : vin[8],
        'year' : vin[9],
        'factory' : vin[10],
        'serial_number' : c_list_to_str(vin[12:17])
      }
      return vehicle_details


def model_conditions(series,body,years):
     for y in range(0,len(years)):
          year = years[y][0]
          if (series == '1') and (year >= '2016' and year <='2018'):
               if body == 'P':
                    #E-Class W213 database withdrawal
                    pass
               else:
                    #A-Class W176 database withdrawal
                    pass
          elif (series == '1') and (year>= '2004' and year <= '2012'):
                    pass # A-Class W169 database withdrawal
          else: 
                    pass # A-Class W168 database withdrawal
          
          if(series == '4') and (body =='M'):
               pass # GLB-Class 
          else:
               pass # GLA-Class

          if series == 'A' and year <= '1986':
               pass # W123
          elif series == 'A' and year <= '2004':
               pass # W163 ML-Class
          else:
               pass # W206 C-Class
          
          if (series == 'B') and (year>='2005' and year <='2009'):
               if(body=='B'):
                    pass # ML
               else:
                    pass # GL
          elif series =='B' and year <= '1989':
               pass # SL-Class R107
          elif (series =='B') and (year>='2002' and year<='2005'):
               pass #GL-Class X164
          
          if series == "C" and year >= '2005':
               pass # R-Class
          elif series =='C' and year > '1979':
               pass # S-Class W126
          else:
               pass # S-Class W116
          
          if series == 'D' and year < '1994':
               pass # 190 W201
          elif series =='D' and body == 'J':
               pass # CLS-Class # C219
          else:
               pass # GLS-Class X166 or W166 ML-Class
          
          if series == 'E' and year < '1994':
               pass # W124 E-Class
          elif series == 'E' and body == 'J':
               pass # CL-Class C216
          else:
               pass # GLE-Class W166
          
          if series == 'F' and year < '2002':
               pass # R129 SL-Class
          elif series == 'F' and body == 'F':
               pass # GLS-Class X167
          else:
               pass # GLE-Class W167
          
          if series == 'G':
               if year <= '1998':
                    if body == 'J':
                         pass # CL-Class W140
                    else:
                         pass # S-Class W140
               else:
                    if body == 'G':
                         pass # GLK-Class X204
                    else:
                         pass # C-Class W204
          
          if series == 'H' and year <= '2000':
               pass # C-Class W202
          else: 
               pass # E-Class W212
          
          if series == 'J' and year <= '2002':
               pass # E-Class W210
          else:
               pass # SL-Class R231
          
          if series == 'K' and year >= '2009':
               pass # E-Class W212
          else:
               pass # SLK-Class R170
          
          if series == 'L' and year >= '2010':
               pass # CLS-Class C218/X218
          else:
               pass # CLK-Class W208
          
          if series == 'N' and year > '2005':
               pass # S-Class W221
          else:
               pass # S-Class W220
          
          if series == 'P' and year > '2010':
               pass # SLK-Class R172
          else:
               pass # CL-Class C215
          
          if series == 'S' and year > '2012':
               pass # CLA-Class C117
          else:
               pass # SL-Class R230
          
          if series == 'T' and year > '2015':
               pass # GLA-Class X156
          else:
               pass # CLK-Class W209
          
          if series == 'U' and year > '2012':
               pass # S-Class W222
          else:
               pass # E-Class W211
          
          if series == 'V':
               if year >= 2005 and year <=2011:
                    return {
                         'series':'B-class',
                         'chassis':'W245',
                         'year':years[y]
                    }
               elif year >=2011 and year<=2019:
                         return {
                         'series':'B-class',
                         'chassis':'W246',
                         'year':year
                    }
               elif year >=2019 and year<=2023:
                         return {
                         'series':'B-class',
                         'chassis':'W247',
                         'year':year
                    }
          if series == 'W':
               if year >= 2014 and year <=2021:
                    return {
                         'series':'C-class',
                         'chassis':'W205',
                         'year':years[y]
                    }
               elif year >=2004 and year<=2010:
                         return {
                         'series':'SLK-class',
                         'chassis':'R171',
                         'year':year
                    }
     