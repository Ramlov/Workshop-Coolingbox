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
    Total_expence: list = []
    Total_expence_sum: list = []


    def __init__(self) -> None:
        super(Cooler)
        self.df = pd.read_csv("elpris.csv")
        
    def __call__(self):

        while len(self.N) < 8640: #Intervaller = 8640
            self.Tdegrees = self.Tdegrees + (Cooler.door(self, self.Tperiode)*(self.Toutside-self.Tdegrees)+Cooler.compressor(self, self.Tdegrees, self.Tperiode, self.df, len(self.N))*(self.Tkomp-self.Tdegrees))*self.Tperiode

            if Cooler.compressor(self, self.Tdegrees, self.Tperiode, self.df, len(self.N)) != 0.0:
                self.Total_cost.append(Cooler.calc_usage(self, len(self.N), self.df))
            else:
                self.Total_cost.append(0)
            self.N.append(self.Tdegrees)

            # Total udgift Monte Carlo
            expense = (self.Total_cost[-1]+Cooler.food_waste(self, self.N[-1]))
            self.Total_expence.append(expense)
            self.Total_expence_sum.append(sum(self.Total_expence)/len(self.N)) # 
        

        #print(self.N[np.argmax(self.N)])
        print(f'Gennemsnitteligt strøm forbrug i september {sum(self.Total_cost)/30: 10} DKK') #Gennemsnittelig pris
        print(f'Bugettet et overholdt? {sum(self.Total_cost) < 12000}')       
       
        print(f'Summen af alle udgifter, madspild+strømforbrug: {sum(self.Total_expence)}')

        fig, ax = plt.subplots(3)

            # For Sine Function
        ax[0].plot(self.N)
        ax[0].set_title("Temp")

        # For Cosine Function
        ax[1].plot(self.Total_cost)
        ax[1].set_title("Cost")

        # For Tangent Function
        ax[2].plot(self.Total_expence_sum)
        ax[2].set_title("Monte Carlo Sum")
        #plt.plot(self.Total_expence_sum)
        #plt.plot(self.N, label='Temp') #Plot temp
        #plt.legend()
        plt.show()
        
        #plt.plot(self.Total_cost, label='Cost') #Plot cost
        #plt.legend()
        #plt.show()


if __name__ == '__main__':
    '''Doctest module'''
    rest = Resturant()
    rest()    


