# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:39:11 2020

@author: sonali chatterjee
"""

# importing packages
import streamlit as st 
import pandas as pd 
import numpy as np 
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

def main():
  st.title("Statistical Tests")
  st.sidebar.title("Which test would you like to do today")

  #uploading the data
  data = st.file_uploader("Upload a Dataset", type=["csv", "txt","xlsx"])
  if data is not None:
    df = pd.read_csv(data)
    st.dataframe(df.head())
  #the category of tests to select
  activities = ['Parametric Test', 'Non-Parametric Test','Normality Tests','Correlation']
  choice = st.sidebar.selectbox("Select a Statistical Testing",activities)

  if choice == 'Parametric Test':
    Parametric= ["student's t-test","Pairwise t-test","F-test","chi-square"]
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
  elif choice == 'Non-Parametric Test':
    Non_parametric = ['Mann-Whitney','Wilcoxon','Kruskal-Wallis','Friedman']
    tests = st.multiselect("Select the tests you want to conduct",Non_parametric)
    if tests == "Mann-Whitney":
      data1,data2 = st.multiselect("Select the variables you want to perform the test on (2 variables only)", df.columns.tolist())
      stat, p = stats.mannwhitneyu(data1, data2)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably the same distribution')
      else:
	      st.write('Probably different distributions')
    
    if tests == "Wilcoxon":
      data1,data2 = st.multiselect("Select the variables you want to perform the test on (2 variables only)", df.columns.tolist())
      stat, p = stats.wilcoxon(data1, data2)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably the same distribution')
      else:
	      st.write('Probably different distributions')
    
    if tests == "Kruskal-Wallis":
      data1,data2 = st.multiselect("Select the variables you want to perform the test on (2 variables only)", df.columns.tolist())
      stat, p = stats.kruskal(data1, data2)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably the same distribution')
      else:
	      st.write('Probably different distributions')
    
    if tests == "Friedman":
      data = st.multiselect("Select the variables you want to perform the test on", df.columns.tolist())
      stat, p = stats.friedmanchisquare(data)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably the same distribution')
      else:
	      st.write('Probably different distributions')
  
  elif choice == 'Normality Tests':
    Normal= ["Shapiro–Wilk","Anderson–Darling","Kolmogorov–Smirnov","Normal-Test"]
    tests = st.sidebar.multiselect("Select the tests you want to conduct",Normal)
    
    if tests == "Shapiro–Wilk":
      user_input = st.text_input('Do you need specific columns?Y/N',N)
      if user_input == "Y":
        data = st.multiselect("Select the variables you want to perform the test on", df.columns.tolist())
        stat, p = stats.shapiro(data)
        st.write('stat=%.3f, p=%.3f' % (stat, p))
        if p > 0.05:
	        st.write('Probably Gaussian')
        else:
	        st.write('Probably not Gaussian')
      else:
        stat, p = stats.shapiro(df)
        st.write('stat=%.3f, p=%.3f' % (stat, p))
        if p > 0.05:
	        st.write('Probably Gaussian')
        else:
	        st.write('Probably not Gaussian')

    if tests == "Anderson–Darling":
      user_input = st.text_input('Do you need specific columns?Y/N',N)
      if user_input == "Y":
        data = st.multiselect("Select the variables you want to perform the test on", df.columns.tolist())
        result = stats.anderson(data)
        st.write('stat=%.3f' % (result.statistic))
        for i in range(len(result.critical_values)):
	          sl, cv = result.significance_level[i], result.critical_values[i]
	          if result.statistic < cv:
		          st.write('Probably Gaussian at the %.1f%% level' % (sl))
	          else:
		          st.write('Probably not Gaussian at the %.1f%% level' % (sl))
      else:
        result = stats.anderson(df)
        st.write('stat=%.3f' % (result.statistic))
        for i in range(len(result.critical_values)):
	          sl, cv = result.significance_level[i], result.critical_values[i]
	          if result.statistic < cv:
		          st.write('Probably Gaussian at the %.1f%% level' % (sl))
	          else:
		          st.write('Probably not Gaussian at the %.1f%% level' % (sl))

    if tests == "Kolmogorov–Smirnov":
      data1,data2 = st.multiselect("Select the variables you want to perform the test on (2 variables only)", df.columns.tolist())
      stat, p = stats.ks_2samp(data1, data2) 
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably the same distribution')
      else:
	      st.write('Probably different distributions')
    
    if tests == "Normal-Test":
      user_input = st.text_input('Do you need specific columns?Y/N',N)
      if user_input == "Y":
        data = st.multiselect("Select the variables you want to perform the test on", df.columns.tolist())
        stat, p = stats.normaltest(data)
        st.write('stat=%.3f, p=%.3f' % (stat, p))
        if p > 0.05:
	        st.write('Probably Gaussian')
        else:
	        st.write('Probably not Gaussian')
      else:
        stat, p = stats.normaltest(df)
        st.write('stat=%.3f, p=%.3f' % (stat, p))
        if p > 0.05:
	        st.write('Probably Gaussian')
        else:
	        st.write('Probably not Gaussian')
  
  elif choice == "Correlation":
    Corr= ["Spearman's Rank","Pearson","Kendall"]
    tests = st.sidebar.multiselect("Select the tests you want to conduct",corr)

    if tests == "Spearman's Rank":
      data1,data2 = st.multiselect("Select the variables you want to perform the test on (2 variables only)", df.columns.tolist())
      stat, p = stats.spearmanr(data1, data2)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably independent')
      else:
	      st.write('Probably dependent')
    
    if tests == "Pearson":
      data1,data2 = st.multiselect("Select the variables you want to perform the test on (2 variables only)", df.columns.tolist())
      stat, p = stats.pearsonr(data1, data2)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably independent')
      else:
	      st.write('Probably dependent')
    
    if tests == "Kendall":
      stat, p = stats.kendalltau(data1, data2)
      st.write('stat=%.3f, p=%.3f' % (stat, p))
      if p > 0.05:
	      st.write('Probably independent')
      else:
	      st.write('Probably dependent')

if __name__ == '__main__':
	main()
       



         
  




       
    


    

    



    


       

       
  


    

    

  
  
