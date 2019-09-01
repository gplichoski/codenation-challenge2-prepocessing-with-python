#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[5]:


def q1():
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[1]:


def q2():
    return len(black_friday[(black_friday['Gender'] == 'F') & (black_friday['Age'] == '26-35')])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[21]:


def q3():
    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    return black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem das colunas possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[133]:


def q5():
    df_na_any = black_friday.isna().any()
    df_has_na = df_na_any[df_na_any == True].count()
    return float(df_has_na/len(black_friday.columns))


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[136]:


def q6():
    df_na_values = black_friday.isna()
    df_na_count = df_na_values.apply(pd.Series.value_counts).loc[True]
    return int(df_na_count.max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    return int(black_friday['Product_Category_3'].dropna().mode())


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    return float(black_friday[['Purchase']].apply(lambda x: x/x.max()).mean())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    df_purchase = black_friday['Purchase']
    df_purchase_zscore = (df_purchase - df_purchase.mean())/df_purchase.std(ddof=0)
    return int(len(df_purchase_zscore[(df_purchase_zscore > -1) & (df_purchase_zscore < 1)]))


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    return black_friday['Product_Category_2'].equals(black_friday['Product_Category_3'])

