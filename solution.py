import pandas as pd
import numpy as np
from scipy.stats import ttest_ind



chat_id = 808572568 # Ваш chat ID, не меняйте название переменной

def solution(control, test, alpha=0.03) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    stat, p_value = ttest_ind(control, test, equal_var=False)

    return p_value < alpha # Ваш ответ, True или False
