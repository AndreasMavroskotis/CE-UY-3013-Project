# CE-UY-3013-Project

**_Cost Estimation_**

This project i created, interpolates the relationship between the total offer target variable and some feature values i believed affected the value of a building.

**_Process_**
 
For the purposes of this project i decided to try and examine the relationships between the total offer value of a building and some determinant values that i believe affected it. My Target variable was set as

**Target and Feature Variables **

Y="Values (total offer)"  
While the determinants (features) where :
X1=Values(before: bonding, profit and overhead)
X2=sqft (Area)
X3=floors (number of floors)
X4=Age (years old)
X5=binary (Hotel=1 Office=2 Appartment building=3 Dormitory=4)

After collecting the Data an OLS linear regression was utilised in order to examine this relationship.It can be said that the 50 lines of Data collected constitute a limitation since the p-values where found insignificant for most feature variables.  However this project is a first step in examining and visualising this intruiging relationship which cannot be done with ease in an excel file.

**Data Collection **

For the Data input this website was used : https://www.buildingjournal.com/construction-estimating.html
The final data input was an xls file consisting of **50** rows and **6** columns

**Results**

The P-values of the regression where found to be very large  (apart from the values before bonding,profit) immplying insignificance.

However some useful extrapolations were established. One example that was visualized was that Total offer increased with Square footage.
