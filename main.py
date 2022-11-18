''''@author Ramlov
      ___            _         
     | _ \__ _ _ __ | |_____ __
     |   / _` | '  \| / _ \ V /
     |_|_\__,_|_|_|_|_\___/\_/ 

'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from helper_cls import Cooler
matplotlib.use('tkagg')
import pandas as pd


class Resturant():
    Tdegrees: float = 5. #Temp 5 grader
    N: list = [] #Nuværende interval
    n: int = 1
    Tperiode: int = 300
    Toutside: int = 20
    Tkomp: int = -5
    Total_cost: list = []

    def __init__(self) -> None:
        super(Cooler)
        self.df = pd.read_csv("elpris.csv")
        
    def main(self):

        while len(self.N) < 8640: #Intervaller = 8640
            self.Tdegrees = self.Tdegrees + (Cooler.door(self, self.Tperiode)*(self.Toutside-self.Tdegrees)+Cooler.compressor(self, self.Tdegrees, self.Tperiode)*(self.Tkomp-self.Tdegrees))*self.Tperiode

            if Cooler.compressor(self, self.Tdegrees, self.Tperiode) != 0.0:
                self.Total_cost.append(Cooler.calc_usage(self, len(self.N), self.df))
            self.N.append(self.Tdegrees)

        #print(self.N[np.argmax(self.N)])
        print(f'Gennemsnitteligt forbrug i september {sum(self.Total_cost)/30: 10} DKK') #Gennemsnittelig pris
        print(f'Bugettet et overholdt? {sum(self.Total_cost) < 1200}')       
       
        plt.plot(self.N, label='Temp') #Plot temp
        plt.legend()
        plt.show()
        
        plt.plot(self.Total_cost, label='Cost') #Plot cost
        plt.legend()
        plt.show()


if __name__ == '__main__':
    '''Doctest module'''
    test = Resturant()
    test.main()



