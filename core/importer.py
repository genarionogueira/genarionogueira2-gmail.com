import pandas as pd
import yaml
import datetime as dt

class importer():
    def __init__(self,*args,**kwargs):
        pass
    def read_file_ETrade(self,filePath,year):

        mov_df = pd.read_excel(filePath)
        mov_file = {}

        for mov in mov_df.index:
            one_line = mov_df.loc[mov]
            
            one_mov_dict = {}
            for idx in one_line.index:                 
                if isinstance(one_line[idx],dt.datetime):
                    date = one_line[idx]
                    one_mov_dict[idx.replace(" ","_").lower()] = date.strftime("%Y-%m-%d")
                elif str(one_line[idx]).strip().isnumeric() or isinstance(one_line[idx],float) :
                    one_mov_dict[idx.replace(" ","_").lower()] = float(one_line[idx])        
                else:
                    one_mov_dict[idx.replace(" ","_").lower()] = str(one_line[idx])        
            mov_file[one_mov_dict['date']] = one_mov_dict        
        
        yaml.dump(mov_file,open('files/movements/'+'{0:04}'.format(year)+'.yaml','w'))    
