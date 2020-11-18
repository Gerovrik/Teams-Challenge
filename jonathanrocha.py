#put imports here
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import os as _dir

working_dir = _dir.getcwd()
csv_path = "top10s.csv"
for root, dirs, files in _dir.walk(working_dir):
    if csv_path in files:
        csv_path = (_dir.path.join(root, csv_path))
        
song_df=pd.read_csv(csv_path,encoding="ISO-8859-1")

song_df.drop(song_df.columns[song_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

song_df.head()


(slope, intercept, rvalue, pvalue, stderr)=st.linregress(bpm,eng)
regress_values=bpm * slope + intercept

plt.xlabel("BPM Rating")
plt.ylabel("Energy Rating")
line_eq="y="+ str(round(slope,2)) + "x +" +str(round(intercept,2))
plt.scatter(bpm,eng, marker="o", facecolors="blue", edgecolors="black")
plt.plot(bpm,regress_values,"r-")
plt.annotate(line_eq,(10,10),fontsize=15,color="red")
print(f'The r-value is:{round(rvalue,3)}')
plt.show()

pop=song_df['pop']


(slope, intercept, rvalue, pvalue, stderr)=st.linregress(bpm,pop)
regress_values=bpm * slope + intercept

plt.xlabel("BPM Rating")
plt.ylabel("POP Rating")
line_eq="y="+ str(round(slope,2)) + "x +" +str(round(intercept,2))
plt.scatter(bpm,eng, marker="o", facecolors="blue", edgecolors="black")
plt.plot(bpm,regress_values,"r-")
plt.annotate(line_eq,(10,10),fontsize=15,color="red")
print(f'The r-value is:{round(rvalue,3)}')
plt.show()

(slope, intercept, rvalue, pvalue, stderr)=st.linregress(eng,pop)
regress_values=bpm * slope + intercept

plt.xlabel("Energy Rating")
plt.ylabel("POP Rating")
line_eq="y="+ str(round(slope,2)) + "x +" +str(round(intercept,2))
plt.scatter(bpm,eng, marker="o", facecolors="blue", edgecolors="black")
plt.plot(bpm,regress_values,"r-")
plt.annotate(line_eq,(10,10),fontsize=15,color="red")
print(f'The r-value is:{round(rvalue,3)}')
plt.show()

years_df=song_df.groupby(['year'])
#years_df.head()

bpm_stats=years_df['bpm'].describe()
fig1, ax1 = plt.subplots()
ax1.set_title('Box and Whisker ')

ax1.set_ylabel('BPM by Year')
ax1.boxplot(bpm_stats)
plt.show()


eng_stats=years_df['nrgy'].describe()

fig1, ax1 = plt.subplots()
ax1.set_title('Box and Whisker ')

ax1.set_ylabel('Energy Rating by Year')
ax1.boxplot(eng_stats)
plt.show()

pop=years_df['pop'].describe()
fig1, ax1 = plt.subplots()
ax1.set_title('Box and Whisker ')

ax1.set_ylabel('Popularity by Year')
ax1.boxplot(pop)
plt.show()

bpm_year=years_df['bpm'].mean()
engy_year=years_df['nrgy'].mean()
pop_year=years_df['pop'].mean()

corr_bpm_engy=st.pearsonr(bpm_year,engy_year)
print(f'Correlation of bpm and energy is {round(corr_bpm_engy[0],4)}')
corr_bpm_pop=st.pearsonr(bpm_year,pop_year)
print(f'Correlation of bpm and popularity is {round(corr_bpm_pop[0],4)}')
corr_engy_pop=st.pearsonr(engy_year,pop_year)
print(f'Correlation of energy and popularity is {round(corr_engy_pop[0],4)}')

yearavg=pd.DataFrame({'BPM Avgs':bpm_year,'Energy Avgs':engy_year,'Popularity Avgs':pop_year})

yearavg.boxplot()
plt.show()

bpm_yearstats=years_df['bpm']
engy_yearstats=years_df['nrgy']
pop_yearstats=years_df['pop']

(slope, intercept, rvalue, pvalue, stderr)=st.linregress(bpm_year,pop_year)
regress_values=bpm_year * slope + intercept

plt.xlabel("BPM")
plt.ylabel("POP Rating")
line_eq="y="+ str(round(slope,2)) + "x +" +str(round(intercept,2))
plt.scatter(bpm_year,pop_year, marker="o", facecolors="blue", edgecolors="black")
plt.plot(bpm_year,regress_values,"r-")
plt.annotate(line_eq,(114,80),fontsize=15,color="red")
print(f'The r-value is:{round(rvalue,3)}')
plt.show()

(slope, intercept, rvalue, pvalue, stderr)=st.linregress(pop_year,bpm_year)
regress_values=pop_year * slope + intercept

plt.xlabel("Popularity Rating")
plt.ylabel("Beats per minute")
line_eq="y="+ str(round(slope,2)) + "x +" +str(round(intercept,2))
plt.scatter(pop_year,bpm_year, marker="o", facecolors="blue", edgecolors="black")
plt.plot(pop_year,regress_values,"r-")
plt.annotate(line_eq,(70,120),fontsize=15,color="red")
print(f'The r-value is:{round(rvalue,3)}')
plt.show()

crit_val=st.chi2.ppf(q=0.95, df=9)
crit_val

st.chisquare(pop_year,bpm_year)
