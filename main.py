# importing packages
import streamlit as st 
import pandas as pd 
#import numpy as np 
from scipy import stats
import seaborn as sns



def main():
    st.title("Statistical Testing Web App")
    st.sidebar.title("Statistical Testing Web App")
    st.markdown("What would you like to do today?")
    st.sidebar.markdown("Select what would you like to do today")

    data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
    if data is not None:
        df = pd.read_csv(data)
        st.dataframe(df.head())
        activities = ['Parametric Test', 'Non-Parametric Test','Normality Tests','Correlation']
        choice = st.sidebar.selectbox("Select a Statistical Testing",activities)

        if choice == 'Parametric Test':
             Parametric= ["student's t-test","Pairwise t-test","F-test","chi-square"]
             tests = st.sidebar.selectbox("Select the tests you want to conduct",Parametric)
             if tests == "student's t-test":
                 data1 = st.sidebar.selectbox("Select the 1st variable you want to perform the test on", df.columns.tolist())
                 data2 = st.sidebar.selectbox("Select the 2nd variable you want to perform the test on", df.columns.tolist())
                 
                 if st.sidebar.button("Show results"):
                     st.subheader("student's t-test Results")
                     stat, p = stats.ttest_ind(df[data1],df[data2])
                     st.write("t-statistics: ", stat,"p-value: ", p)
            
                     if p > 0.05:
                         st.write('Do not reject the hypothesis')
                     else:
                         st.write('Reject the hypothesis')
             if tests == "Pairwise t-test":
                 data1 = st.sidebar.selectbox("Select the 1st variable you want to perform the test on", df.columns.tolist())
                 data2 = st.sidebar.selectbox("Select the 2nd variable you want to perform the test on", df.columns.tolist())
                 
                 if st.sidebar.button("Show results"):
                     st.subheader("Pairwise t-test Results")
                     stat, p = stats.ttest_rel(df[data1],df[data2])
                     st.write("t-statistics: ", stat,"p-value: ", p)
            
                     if p > 0.05:
                         st.write('Do not reject the hypothesis')
                     else:
                         st.write('Reject the Hypothesis')
             
             if tests == "F-test":
                 data1 = st.sidebar.selectbox("Select the 1st variable you want to perform the test on", df.columns.tolist())
                 data2 = st.sidebar.selectbox("Select the 2nd variable you want to perform the test on", df.columns.tolist())

                 if st.sidebar.button("Show results"):
                     st.subheader("F-test Results")
                     stat, p = stats.f_oneway(df[data1],df[data2])
                     st.write("F-statistics: ", stat,"p-value: ", p)
        
                     if p > 0.05:
                         st.write('Do not reject the hypothesis')
                     else:
                         st.write('Reject the Hypothesis')
             
             if tests == "chi-square" :
                 data1 = st.sidebar.selectbox("Select the observed frequency", df.columns.tolist())
                 data2 = st.sidebar.selectbox("Select the expected frequency", df.columns.tolist())
                 
                 if st.sidebar.button("Show results"):
                     st.subheader("Chi Square test Results")
                     stat, p = stats.chisquare(df[data1],df[data2],axis=0)
                     st.write("chi square-statistics: ", stat,"p-value: ", p)
        
                     if p > 0.05:
                         st.write('Do not reject the hypothesis')
                     else:
                         st.write('Reject the Hypothesis')

            
            

        elif choice == 'Non-Parametric Test':
            Non_parametric = ['Mann-Whitney','Wilcoxon','Kruskal-Wallis','Friedman']
            tests = st.sidebar.selectbox("Select the tests you want to conduct",Non_parametric)
            if tests == "Mann-Whitney" :
                 data1 = st.sidebar.selectbox("Select the 1st variable to perform the test on", df.columns.tolist())
                 data2 = st.sidebar.selectbox("Select the 2nd variable to perform the test on", df.columns.tolist())
                 
                 if st.sidebar.button("Show results"):
                     st.subheader("Mann Whitney test Results")
                     stat, p = stats.mannwhitneyu(df[data1], df[data2])
                     st.write("Mann Whitney statistics: ", stat,"p-value: ", p)
        
                     if p > 0.05:
                         st.write('Do not reject the hypothesis')
                     else:
                         st.write('Reject the hypothesis')
            
            if tests == "Wilcoxon" :
                 data1 = st.sidebar.selectbox("Select the 1st variable to perform the test on", df.columns.tolist())
                 data2 = st.sidebar.selectbox("Select the 2nd variable to perform the test on", df.columns.tolist())
                 
                 if st.sidebar.button("Show results"):
                     st.subheader("Wilcoxon test Results")
                     stat, p = stats.wilcoxon(df[data1], df[data2])
                     st.write("Wilcoxon statistics: ", stat,"p-value: ", p)
        
                     if p > 0.05:
                         st.write('Do not reject the hypothesis')
                     else:
                         st.write('Reject the hypothesis')
            
            if tests == "Kruskal-Wallis" :
                 data1 = st.sidebar.selectbox("Select the 1st variable to perform the test on", df.columns.tolist())
                 data2 = st.sidebar.selectbox("Select the 2nd variable to perform the test on", df.columns.tolist())
                 
                 if st.sidebar.button("Show results"):
                     st.subheader("Kruskal-Wallis test Results")
                     stat, p = stats.kruskal(df[data1], df[data2])
                     st.write("Kruskal-Wallis statistics: ", stat,"p-value: ", p)
        
                     if p > 0.05:
                         st.write('Do not reject the hypothesis')
                     else:
                         st.write('Reject the hypothesis')
            
            if tests == "Friedman" :
                 data1 = st.sidebar.selectbox("Select the 1st variable to perform the test on", df.columns.tolist())
                 data2 = st.sidebar.selectbox("Select the 2nd variable to perform the test on", df.columns.tolist())
                 data3 = st.sidebar.selectbox("Select the 3rd variable to perform the test on", df.columns.tolist())

                 if st.sidebar.button("Show results"):
                     st.subheader("Friedman Results")
                     stat, p = stats.friedmanchisquare(df[data1], df[data2],df[data3])
                     st.write("Friedman statistics: ", stat,"p-value: ", p)
        
                     if p > 0.05:
                         st.write('Do not reject the hypothesis')
                     else:
                         st.write('Reject the hypothesis')
                
   
        elif choice == 'Normality Tests':
            Normal= ["Shapiro–Wilk","Anderson–Darling","Kolmogorov–Smirnov","Normal-Test"]
            tests = st.sidebar.selectbox("Select the test you want to conduct",Normal)
            if tests == "Shapiro–Wilk" :
                user_input = str(st.text_input('Do you need specific columns? Y or N'))
                if user_input == "Y":
                     selected_columns = st.sidebar.multiselect("Select the variables you want to perform the test on", df.columns.tolist())
                     new_df = df[selected_columns]
                         
                     if st.sidebar.button("Show results"):
                         st.subheader("Shapiro Wilk test Results")
                         stat, p = stats.shapiro(new_df)
                         st.write("Shapiro Wilk statistics: ", stat,"p-value: ", p)
        
                         if p > 0.05:
                             st.write('Probably Gaussian')
                         else:
                             st.write('Probably not Gaussian')
            
                else:
                    if st.sidebar.button("Show results"):
                        stat, p = stats.shapiro(df)
                        st.write("Shapiro Wilk statistics: ", stat,"p-value: ", p)
                        if p > 0.05:
                            st.write('Probably Gaussian')
                        else:
                            st.write('Probably not Gaussian')
        
            if tests == "Anderson–Darling" :
                selected_columns = st.sidebar.multiselect("Select the variables you want to perform the test on", df.columns.tolist())
                new_df = df[selected_columns]
                    
                if st.sidebar.button("Show results"):
                    st.subheader("Anderson–Darling test Results")
                    result = stats.anderson(new_df,dist='norm')
                    st.write("Anderson–Darling statistics: ", result.statistics)
                    for i in range(len(result.critical_values)):
                         sl , cv = result.significance_level[i], result.critical_values[i]
                         if result.statistic < cv:
                                st.write('Probably Gaussian at the %.1f%% level' % (sl))
                         else:
                                st.write('Probably not Gaussian at the %.1f%% level' % (sl))
   
    
            if tests == "Kolmogorov–Smirnov":
                data1 = st.sidebar.selectbox("Select the 1st variable to perform the test on", df.columns.tolist())
                data2 = st.sidebar.selectbox("Select the 2nd variable to perform the test on", df.columns.tolist())
                 
                if st.sidebar.button("Show results"):
                     st.subheader("Kolmogorov–Smirnov test Results")
                     p,stat = stats.ks_2samp(df[data1], df[data2])
                     st.write("Kolmogorov–Smirnov statistics: ", stat,"p-value: ", p)
        
                     if p > 0.05:
                         st.write('Probably the same distribution')
                     else:
                         st.write('Probably different distributions')
                         
                         
            if tests == "Normal-Test" :
                user_input = st.text_input('Do you need specific columns?Y or N')
                if user_input == "Y":
                     selected_columns = st.sidebar.multiselect("Select the variables you want to perform the test on", df.columns.tolist())
                     new_df = df[selected_columns]
                         
                     if st.sidebar.button("Show results"):
                         st.subheader("Normal-Test test Results")
                         p, stat = stats.normaltest(new_df)
                         st.write("Normal-Test statistics: ", stat,"p-value: ", p)
        
                         if p > 0.05:
                             st.write('Probably Gaussian')
                         else:
                             st.write('Probably not Gaussian')
            
                else:
                    stat, p = stats.normaltest(df)
                    st.write("Normal-Test statistics: ", stat,"p-value: ", p)
                    if p > 0.05:
                        st.write('Probably Gaussian')
                    else:
                        st.write('Probably not Gaussian')         
            
        elif  choice == 'Correlation':
            corr= ["Spearman's Rank","Pearson","Kendall"]
            tests = st.sidebar.selectbox("Select the tests you want to conduct",corr)
            
            if tests == "Spearman's Rank":
                data1 = st.sidebar.selectbox("Select the 1st variable to perform the test on", df.columns.tolist())
                data2 = st.sidebar.selectbox("Select the 2nd variable to perform the test on", df.columns.tolist())
                 
                if st.sidebar.button("Show results"):
                    st.subheader(" Spearman's Rank Results")
                    p, stat = stats.spearmanr(df[data1], df[data2])
                    st.write("Spearman's Rank statistics: ", stat,"p-value: ", p)
        
                    if p > 0.05:
                        st.write('Probably dependent')
                    else:
                        st.write('Probably independent')
            
            if tests == "Pearson":
                data1 = st.sidebar.selectbox("Select the 1st variable to perform the test on", df.columns.tolist())
                data2 = st.sidebar.selectbox("Select the 2nd variable to perform the test on", df.columns.tolist())
                 
                if st.sidebar.button("Show results"):
                    st.subheader("Pearson Results")
                    p, stat = stats.pearsonr(df[data1], df[data2])
                    st.write("Pearson statistics: ", stat,"p-value: ", p)
        
                    if p > 0.05:
                        st.write('Probably dependent')
                    else:
                        st.write('Probably independent')
            
            if tests == "Kendall":
                data1 = st.sidebar.selectbox("Select the 1st variable to perform the test on", df.columns.tolist())
                data2 = st.sidebar.selectbox("Select the 2nd variable to perform the test on", df.columns.tolist())
                 
                if st.sidebar.button("Show results"):
                    st.subheader("Kendall Results")
                    p,stat = stats.kendalltau(df[data1], df[data2])
                    st.write("Kendall statistics: ", stat,"p-value: ", p)
        
                    if p > 0.05:
                        st.write('Probably dependent')
                    else:
                        st.write('Probably independent')
                        
    
            if st.sidebar.checkbox('Show Correlation plot'):
                 st.write('To see the correlation plot of all variables')
                 st.write(sns.heatmap(df.corr(),annot=True))
                 st.pyplot(height=800)
                 
        if st.sidebar.checkbox('EDA'):
        
            if st.sidebar.checkbox('Show data summary'):
                st.write(df.describe())
        
            if st.sidebar.checkbox('Show Value Counts'):
                st.write(df.iloc[:,-1].value_counts())
        
    
if __name__ == '__main__':
	main()