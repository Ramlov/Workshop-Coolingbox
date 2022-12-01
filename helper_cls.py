'''
@author Ramlov
      ___            _         
     | _ \__ _ _ __ | |_____ __
     |   / _` | '  \| / _ \ V /
     |_|_\__,_|_|_|_|_\___/\_/ 



Fil der indeholder alle helper_cls

'''

import numpy as np
from math import e


useSmart = True #Sæt til False for Simple, eller True for smart thermostat

class Cooler:
    totalcost = 0

    def door(self, Tperiode):
        '''Functionen her returnere temperatur udviklingen afhængigt af om døren er åben eller ikke'''
        return 3*10**-5*Tperiode**-1 if np.random.randint(0, 100) %10 == 0 else 5*10**-7*Tperiode**-1

    def simple_thermostat(self, Tdegrees: int) -> bool:
        '''Simple termostat'''
        return True if Tdegrees > 5 else False

    def compressor(self, Tdegrees: int, Tperiode: int, df, Current_N: int):
        '''Kompresseren der returnere hvordan temperaturudviklingen skal håndteres'''
        if useSmart:
            if Cooler.ai_thermostat(self, Current_N, df):
                return 8*10**-6*Tperiode**-1
            else:
                if Tdegrees > 6.5:
                    return 8*10**-6*Tperiode**-1
                else:
                    return 0*Tperiode**-1
        else:
            if Cooler.simple_thermostat(self, Tdegrees):
                return 8*10**-6*Tperiode**-1
            else:
                return 0*Tperiode**-1

    def calc_usage(self, Current_N: int, df):
        '''Her beregnes prisen ved brug af df loaded i main.'''
        df_new = df.loc[df.index[Current_N], 'Pris']
        return df_new

    def ai_thermostat(self, Current_N: int, df):
        '''Her tjekkes der for om det er billigere at vente med at køle.'''
        if float(df.loc[df.index[Current_N-1], 'Pris']) < float(df.loc[df.index[Current_N], 'Pris']):
            return True

    def food_waste(self, Tdegress: int):
        '''Her beregnes foodwaste, hvis temperaturen er under 3.5 eller over 6.5'''
        if Tdegress < 3.5:
            return 4.39*e**-0.49*Tdegress
        elif 3.5 <= Tdegress < 6.5:
            return 0
        elif Tdegress > 6.5:
            return 0.11*e**0.31*Tdegress
        