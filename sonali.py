# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:39:11 2020

@author: sonali chatterjee
"""

# importing packages
import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

def main():
  st.title("Statistical Tests")
  st.sidebar.title("Which test would you like to do today")

  #uploading the data
  data = st.file_uploader("Upload a Dataset", type=["csv", "txt","xlsx"])
  df=pd.read_csv(data)
  st.dataframe(df.head())
  #the category of tests to select
  activities = ['Parametric Test', 'Non-Parametric Test','Normality Tests','Testing Assumptions for Linear Regression','Correlation']
  choice = st.sidebar.selectbox("Select a Statistical Testing",activities)

  if choice == 'Parametric test':
    Parametric= ["student's t-test","Pairwise t-test","F-test","ANOVA"]
    tests = st.sidebar.multiselect("Select the tests you want to conduct",Parametric)

    if tests == "student's t-test":
      data1,data2 = st.multiselect("Select the variables you want to perform the test on (2 variables only)", df.columns.tolist())
      stat, p = stats.ttest_ind(data1, data2)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably the same distribution')
      else:
	      st.write('Probably different distributions')
    
    if tests == "Pairwise t-test":
      data1,data2 = st.multiselect("Select the variables you want to perform the test on (2 variables only)", df.columns.tolist())
      stat, p = stats.ttest_rel(data1, data2)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably the same distribution')
      else:
	      st.write('Probably different distributions')

    if tests == "F-test":
      data = st.multiselect("Select the variables you want to perform the test on", df.columns.tolist())
      stat, p = stats.f_oneway(data)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	    st.write('Probably the same distribution') 
      else:
	    st.write('Probably different distributions')
     
    if tests == "chi_square":
      variables = st.multiselect("Select the variables you want to perform the test on", df.columns.tolist())
      table = st.table(variables)
      stat, p, dof, expected = stats.chi2_contingency(table)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably independent')
      else:
	      st.write('Probably dependent')
    
    