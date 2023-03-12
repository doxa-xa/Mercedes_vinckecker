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
          if series == '1':
               if year >= '2016' and year <='2018':
                    if body == 'P':
                         return{
                              'series':'E-Class',
                              'chassis':'W213',
                              'year':year
                         }
                    else:
                         return{
                              'series':'A-Class',
                              'chassis':'W176',
                              'year':year
                         }
               elif year>= '2004' and year <= '2012':
                    return{
                              'series':'A-Class',
                              'chassis':'W169',
                              'year':year
                         }
               elif year > 2018:
                     return{
                              'series':'E-Class',
                              'chassis':'W213',
                              'year':year
                         }
          if series == '4':
                if body == 'M':
                    return{
                              'series':'GLB-Class',
                              'chassis':'X247',
                              'year':year
                         }
                else:
                      return {
                         'series':'GLA-Class',
                         'chassis':'H247',
                         'year':year
                    }
          if series == 'A':
               if year >= 1982 and year <=1986:
                    return {
                         'series':'123',
                         'chassis':'W123',
                         'year':year
                    }
               elif year >=1997 and year<=2004:
                         return{
                         'series':'ML-class',
                         'chassis':'W163',
                         'year':year
                    }
               elif year >=2021 and year<=2023:
                         return{
                         'series':'C-class',
                         'chassis':'W206',
                         'year':year
                    }
          if series == 'B':
               if year >= 1971 and year <= 1989:
                     return {
                         'series':'SL-Class',
                         'chassis':'R107',
                         'year':year
                    }
               elif year>='2005' and year <='2009':
                     if body == 'B':
                        return {
                         'series':'ML-Class',
                         'chassis':'W164',
                         'year':year
                         }
                     else:
                         return {
                         'series':'GL-Class',
                         'chassis':'X165',
                         'year':year
                         }
               elif year >= 2010:
                    return {
                    'series':'ML-Class',
                    'chassis':'W164',
                    'year':year
                    }   
          if series == 'C':
               if year >= 1980 and year <=1991:
                    return {
                         'series':'S-Class',
                         'chassis':'W126',
                         'year':year
                    }
               elif year >=1972 and year<=1979:
                         return{
                         'series':'S-class',
                         'chassis':'W116',
                         'year':year
                    }
               elif year >=2005 and year<=2017:
                         return{
                         'series':'R-class',
                         'chassis':'W251',
                         'year':year
                    }
          if series == 'D':
                if year >= 2004 and year <= 2010:
                      return {
                              'series':'CLS-Class',
                              'chassis':'C219',
                              'year':year
                         }
                elif year >= 1982 and year <= 1993:
                      return {
                              'series':'190',
                              'chassis':'W201',
                              'year':year
                         }
                elif year >= 2009 and year <= 2019:
                      return {
                              'series':'GLE-Class or ML-Class',
                              'chassis':'W166',
                              'year':year
                         }
          if series == 'E':
                if year >= 1984 and year <= 1993:
                      return {
                              'series':'E-Class',
                              'chassis':'W124',
                              'year':year
                         }
                elif year >= 2006 and year <= 2014:
                      if body == 'J':
                         return {
                              'series':'CL-Class',
                              'chassis':'C216',
                              'year':year
                         }
                      else:
                         return {
                              'series':'GLE-Class',
                              'chassis':'W166',
                              'year':year
                         }
                elif year >=2014 and year <= 2019:
                      return {
                              'series':'GLE-Class',
                              'chassis':'W166',
                              'year':year
                         }
          if series == 'F':
               if year >= 1989 and year <= 2001 and body =='A':
                     return {
                              'series':'SL-Class',
                              'chassis':'R129',
                              'year':year
                         }
               elif year >= 2016 and year <= 2023 and body !='A':
                     if body == 'F':
                          return {
                              'series':'GLS-Class',
                              'chassis':'X167',
                              'year':year
                         }
                     else:
                           return {
                              'series':'GLE-Class',
                              'chassis':'X167',
                              'year':year
                         }
          if series == 'G':
               if year >= 1991 and year <= 1998:
                    if body != 'J':
                         return {
                              'series':'CL-Class',
                              'chassis':'W140',
                              'year':year
                         }
                    else:
                          return {
                              'series':'S-Class',
                              'chassis':'W140',
                              'year':year
                         }
               else:
                    if body == 'G':
                         return {
                              'series':'CLK-Class',
                              'chassis':'X204',
                              'year':year
                              }
                    else:
                         return {
                              'series':'C-Class',
                              'chassis':'W204',
                              'year':year
                              }                
          if series == 'H':
               if year >= 2009 and year <=2016:
                    return {
                         'series':'E-Class',
                         'chassis':'W212',
                         'year':year
                    }
               elif year >=1993 and year<=2000:
                         return{
                         'series':'C-class',
                         'chassis':'W202',
                         'year':year
                    }
          if series == 'J':
               if year >= 1995 and year <=2002:
                    return {
                         'series':'E-Class',
                         'chassis':'W210',
                         'year':year
                    }
               elif year >=2012 and year<=2020:
                         return{
                         'series':'SL-class',
                         'chassis':'R231',
                         'year':year
                    }
          if series == 'K':
               if year >= 1996 and year <=2004:
                    return {
                         'series':'SLK-Class',
                         'chassis':'R170',
                         'year':year
                    }
               elif year >2009 and year<=2016:
                         return{
                         'series':'E-class',
                         'chassis':'W212',
                         'year':year
                    }
          if series == 'L':
               if year >= 1997 and year <=2003:
                    return {
                         'series':'CLK-Class',
                         'chassis':'W208',
                         'year':year
                    }
               elif year >2010 and year<=2018:
                         return{
                         'series':'CLS-class',
                         'chassis':'C2018/X218',
                         'year':year
                    }
          if series == 'N':
               if year >= 1998 and year <=2005:
                    return {
                         'series':'S-class',
                         'chassis':'W220',
                         'year':year
                    }
               elif year >2005 and year<=2013:
                         return{
                         'series':'S-class',
                         'chassis':'W221',
                         'year':year
                    }
          if series == 'P':
               if year >= 1999 and year <=2006:
                    return {
                         'series':'CL-class',
                         'chassis':'C215',
                         'year':year
                    }
               elif year >=2011 and year<=2020:
                         return{
                         'series':'SLK-class',
                         'chassis':'R172',
                         'year':year
                    }
          if series == 'S':
               if year >= 2013 and year <=2019:
                    return {
                         'series':'CLA-class',
                         'chassis':'C117',
                         'year':year
                    }
               elif year >=2001 and year<=2011:
                         return{
                         'series':'SL-class',
                         'chassis':'R230',
                         'year':year
                    }
          if series == 'T':
               if year >= 2016 and year <=2023:
                    return {
                         'series':'GLA-class',
                         'chassis':'X156',
                         'year':year
                    }
               elif year >=1997 and year<=2009:
                         return{
                         'series':'CLK-class',
                         'chassis':'W209',
                         'year':year
                    }       
          if series == 'U':
               if year >= 2013 and year <=2020:
                    return {
                         'series':'S-class',
                         'chassis':'W222',
                         'year':year
                    }
               elif year >=2002 and year<=2009:
                         return {
                         'series':'E-class',
                         'chassis':'W211',
                         'year':year
                    }
          if series == 'V':
               if year >= 2005 and year <=2011:
                    return {
                         'series':'B-class',
                         'chassis':'W245',
                         'year':year
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
                         'year':year
                    }
               elif year >=2004 and year<=2010:
                         return {
                         'series':'SLK-class',
                         'chassis':'R171',
                         'year':year
                    }
     