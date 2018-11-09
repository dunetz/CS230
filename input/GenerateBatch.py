import math
import numpy as np
import pandas as pd

class GenerateBatch():
    """A class for loading and transforming data for the lstm model"""

    def __init__(self,datx,daty):
        self.datx = datx
        self.daty = daty
        self.len= self.datx.shape[0]

       
    def GenerateBatch(self, seq_len, batch_size):
        '''Yield a generator of training data from filename on given list of cols split for train/test'''
        i = 0
        while i <= (self.len - seq_len):
            x_batch = []
            y_batch = []
            for b in range(batch_size):
                if (i <=(self.len - seq_len)): # short batch if reach end of data
                    x, y = self._next_window(i, seq_len)
                    x_batch.append(x)
                    y_batch.append(y)
                    i+=1
 
            if i>(self.len-seq_len):i=0 # batch used up all data - start again
            yield np.array(x_batch), np.array(y_batch)

    def _next_window(self, i, seq_len):
        '''Generates the next data window from the given index location i'''
        x = self.datx[i:i+seq_len]
        y = self.daty[i+seq_len-1]
        return x, y

   