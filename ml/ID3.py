import numpy as np
import pandas as pd 
from math import log 

# 定义墒的函数
def entropy(ele):
    '''
    function: Calculating entropy value
    input: A list contain categorical value.
    output: Entropy value
    entropy = -sum(p*log(p)),p is a prob value.
    '''
    # Calculating the probability distribution