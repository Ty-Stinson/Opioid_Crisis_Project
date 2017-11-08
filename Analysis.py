# Hussein, Ty, and Ongun

# Age Groups (15 - 64) vs. Years (01 - 15)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Import~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.interpolate as sc

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Data Table~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

filename = "Data.txt"

table = pd.read_table(filename)
print(table)
print(table.columns)
print()
print()
print()
print()
print()

#~~~~~~~~~~~~~~~~~~~Plots, Regression Models, and Error Bars~~~~~~~~~~~~~~~~~~~~

# Age Group: 15 - 24

deaths1 = table["Deaths"][0:15]
population1 = table["Population"][0:15]
y1 = (deaths1/population1) * 100 

years1 = table["Year"][0:15]

fig,ax1 = plt.subplots(1)
ax1.plot(years1, y1, "o")

plt.title("Opioid Death Rate for Age Group: 15 - 24")
plt.xlabel("Years")
plt.ylabel("Rate of Death")

p1 = np.polyfit(years1, y1, 3)
slope1 = p1[0]
intercept11 = p1[1]
intercept12 = p1[2]
intercept13 = p1[3]

yfit1 = (slope1 * (years1 ** 3)) + (intercept11 * (years1 ** 2)) + (intercept12 * years1) + intercept13

sd1 = np.std(y1, ddof = 1);
se1 = sd1 / (np.sqrt(15))
errors1 = [se1] * 15

plt.plot(years1, np.polyval(p1, years1), "r-")
plt.errorbar(years1, y1, yerr = errors1, fmt = "o")
plt.show()

results1 = {}
results1["polynomial_1"] = p1.tolist()

correlation1 = np.poly1d(p1)
y1hat = correlation1(years1)
y1bar = np.sum(y1)/len(y1)
ssreg1 = np.sum((y1hat - y1bar) ** 2)
sstot1 = np.sum((y1 - y1bar) ** 2)
results1["determination_1"] = ssreg1/sstot1
print(results1)
print()

# Age Group: 25 - 34

deaths2 = table["Deaths"][16:31]
population2 = table["Population"][16:31]
y2 = (deaths2/population2) * 100 

years2 = table["Year"][16:31]

fig,ax2 = plt.subplots(1)
ax2.plot(years2, y2, "o")

plt.title("Opioid Death Rate for Age Group: 25 - 34")
plt.xlabel("Years")
plt.ylabel("Rate of Death")

p2 = np.polyfit(years2, y2, 3)
slope2 = p2[0]
intercept21 = p2[1]
intercept22 = p2[2]
intercept23 = p2[3]

yfit2 = (slope2 * (years2 ** 3)) + (intercept21 * (years2 ** 2)) + (intercept22 * years2) + intercept23

sd2 = np.std(y2, ddof = 1);
se2 = sd2 / (np.sqrt(15))
errors2 = [se2] * 15

plt.plot(years2, np.polyval(p2, years2), "r-")
plt.errorbar(years2, y2, yerr = errors2, fmt = "o")
plt.show()

results2 = {}
results2["polynomial_2"] = p2.tolist()

correlation2 = np.poly1d(p2)
y2hat = correlation2(years2)
y2bar = np.sum(y2)/len(y2)
ssreg2 = np.sum((y2hat - y2bar) ** 2)
sstot2 = np.sum((y2 - y2bar) ** 2)
results2["determination_2"] = ssreg2/sstot2
print(results2)
print()

# Age Group: 35 - 44

deaths3 = table["Deaths"][32:47]
population3 = table["Population"][32:47]
y3 = (deaths3/population3) * 100 

years3 = table["Year"][32:47]

fig,ax3 = plt.subplots(1)
ax3.plot(years3, y3, "o")

plt.title("Opioid Death Rate for Age Group: 35 - 44")
plt.xlabel("Years")
plt.ylabel("Rate of Death")

p3 = np.polyfit(years3, y3, 4)
slope3 = p3[0]
intercept31 = p3[1]
intercept32 = p3[2]
intercept33 = p3[3]
intercept34 = p3[4]

yfit3 = (slope3 * (years3 ** 4)) + (intercept31 * (years3 ** 3)) + (intercept32 * (years3 ** 2)) + (intercept33 * years3) + intercept34

sd3 = np.std(y3, ddof = 1);
se3 = sd3 / (np.sqrt(15))
errors3 = [se3] * 15

plt.plot(years3, np.polyval(p3, years3), "r-")
plt.errorbar(years3, y3, yerr = errors3, fmt = "o")
plt.show()

results3 = {}
results3["polynomial_3"] = p3.tolist()

correlation3 = np.poly1d(p3)
y3hat = correlation3(years3)
y3bar = np.sum(y3)/len(y3)
ssreg3 = np.sum((y3hat - y3bar) ** 2)
sstot3 = np.sum((y3 - y3bar) ** 2)
results3["determination_3"] = ssreg3/sstot3
print(results3)
print()

# Age Group: 45 - 54

deaths4 = table["Deaths"][48:63]
population4 = table["Population"][48:63]
y4 = (deaths4/population4) * 100 

years4 = table["Year"][48:63]

fig,ax4 = plt.subplots(1)
ax4.plot(years4, y4, "o")

plt.title("Opioid Death Rate for Age Group: 45 - 54")
plt.xlabel("Years")
plt.ylabel("Rate of Death")

p4 = np.polyfit(years4, y4, 4)
slope4 = p4[0]
intercept41 = p4[1]
intercept42 = p4[2]
intercept43 = p4[3]
intercept44 = p4[4]

yfit4 = (slope4 * (years4 ** 4)) + (intercept41 * (years4 ** 3)) + (intercept42 * (years4 ** 2)) + (intercept43 * years4) + intercept44

sd4 = np.std(y4, ddof = 1);
se4 = sd4 / (np.sqrt(15))
errors4 = [se4] * 15

plt.plot(years4, np.polyval(p4, years4), "r-")
plt.errorbar(years4, y4, yerr = errors4, fmt = "o")
plt.show()

results4 = {}
results4["polynomial_4"] = p4.tolist()

correlation4 = np.poly1d(p4)
y4hat = correlation4(years4)
y4bar = np.sum(y4)/len(y4)
ssreg4 = np.sum((y4hat - y4bar) ** 2)
sstot4 = np.sum((y4 - y4bar) ** 2)
results4["determination_4"] = ssreg4/sstot4
print(results4)
print()

# Age Group: 55 - 64

deaths5 = table["Deaths"][64:79]
population5 = table["Population"][64:79]
y5 = (deaths5/population5) * 100 

years5 = table["Year"][64:79]

fig,ax5 = plt.subplots(1)
ax5.plot(years5, y5, "o")

plt.title("Opioid Death Rate for Age Group: 55 - 64")
plt.xlabel("Years")
plt.ylabel("Rate of Death")

p5 = np.polyfit(years5, y5, 1)
slope5 = p5[0]
intercept51 = p5[1]

yfit5 = (slope5 * years5) + intercept51

sd5 = np.std(y5, ddof = 1);
se5 = sd5 / (np.sqrt(15))
errors5 = [se5] * 15

plt.plot(years5, np.polyval(p5, years5), "r-")
plt.errorbar(years5, y5, yerr = errors5, fmt = "o")
plt.show()

results5 = {}
results5["polynomial_5"] = p5.tolist()

correlation5 = np.poly1d(p5)
y5hat = correlation5(years5)
y5bar = np.sum(y5)/len(y5)
ssreg5 = np.sum((y5hat - y5bar) ** 2)
sstot5 = np.sum((y5 - y5bar) ** 2)
results5["determination_5"] = ssreg5/sstot5
print(results5)
print()

#~~~~~~~~~~~~~~~~~~Predicted Rate of Death Plots for 2016 - 2026~~~~~~~~~~~~~~~~

x = np.array(range(2016, 2027))

plt.plot(x, np.polyval(p1, x), "r-")
plt.title("Opioid Death Rate for Age Group: 15 - 24")
plt.xlabel("Years")
plt.ylabel("Rate of Death")
plt.show()

plt.plot(x, np.polyval(p2, x), "r-")
plt.title("Opioid Death Rate for Age Group: 25 - 34")
plt.xlabel("Years")
plt.ylabel("Rate of Death")
plt.show()

plt.plot(x, np.polyval(p3, x), "r-")
plt.title("Opioid Death Rate for Age Group: 35 - 44")
plt.xlabel("Years")
plt.ylabel("Rate of Death")
plt.show()

plt.plot(x, np.polyval(p4, x), "r-")
plt.title("Opioid Death Rate for Age Group: 45 - 54")
plt.xlabel("Years")
plt.ylabel("Rate of Death")
plt.show()

plt.plot(x, np.polyval(p5, x), "r-")
plt.title("Opioid Death Rate for Age Group: 55 - 64")
plt.xlabel("Years")
plt.ylabel("Rate of Death")
plt.show()

#~~~~~~~~~~~~~~~~Algorithm: Predicted Rate of Death from Year Input~~~~~~~~~~~~~

quit = False

while (not quit):

	year_str = input("Please enter a year or enter 'q' to quit: ")
	print()
	
	if (year_str != "q"):

		year_int = int(year_str)

		value1 = (slope1 * (year_int ** 3)) + (intercept11 * (year_int ** 2)) + (intercept12 * year_int) + intercept13
		value2 = (slope2 * (year_int ** 3)) + (intercept21 * (year_int ** 2)) + (intercept22 * year_int) + intercept23
		value3 = (slope3 * (year_int ** 4)) + (intercept31 * (year_int ** 3)) + (intercept32 * (year_int ** 2)) + (intercept33 * year_int) + intercept34
		value4 = (slope4 * (year_int ** 4)) + (intercept41 * (year_int ** 3)) + (intercept42 * (year_int ** 2)) + (intercept43 * year_int) + intercept44
		value5 = (slope5 * year_int) + intercept51

		print("The predicated rate of death for ages 15 - 24: ", value1 * 100, "%")
		print()
		print("The predicated rate of death for ages 25 - 34: ", value2 * 100, "%")
		print()
		print("The predicated rate of death for ages 35 - 44: ", value3 * 100, "%")
		print()
		print("The predicated rate of death for ages 45 - 54: ", value4 * 100, "%")
		print()
		print("The predicated rate of death for ages 55 - 64: ", value5 * 100, "%")
		print()

	else:
		quit = True