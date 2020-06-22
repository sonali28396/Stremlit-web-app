# importing packages
import streamlit as st 
import pandas as pd 
import numpy as np 
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols


def main():
    #the category of tests to select
    activities = ['Parametric Test', 'Non-Parametric Test','Normality Tests','Correlation']
    choice = st.sidebar.selectbox("Select a Statistical Testing",activities)

    data = st.file_uploader("Upload a Dataset", type=["csv", "txt","xlsx"])
	if data is not None:
		df = pd.read_csv(data)
		st.dataframe(df.head())

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

                     #Code for more Options ["student's t-test","Pairwise t-test","F-test","chi-square"]

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

            #code for ['Mann-Whitney','Wilcoxon','Kruskal-Wallis','Friedman']



if __name__ == '__main__':
	main()