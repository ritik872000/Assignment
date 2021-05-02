-------------------------------------------------(b)-------------------------------------------------

<li>Yearly Analysis: We can notice that prices mostly increase till the month of november and suddenly drops in the last month.</li>

Probable reasons are :
<ol>
  <li>In december supply increase due to which price falls. </li>
  <li>There are many factors behind the increase in prices(Weather, Soil condition.</li>
</ol>

<li>Quarterly Analysis</li>
<ol>
<li>If we see quarter wise theres <b>not much difference in 1st and 2nd quarter</b> but theres a <b>substantial difference in 3rd quater</b> i.e<br>
  During the months of July, August and September prices are the highest</li>
</ol>

<li> Analysis regarding variety, Market and Prices</li>

<ol>
  <li>We can notice that<b> Fatehpur and samsabad market mostly sell local variety</b> while <b>others sell Desi</b></li>
  </ol>
-------------------------------------------------(c)-------------------------------------------------

<li>Data Pre-processing techniques</li>
<ol>
    <li>Checking for missing values</li>
    <li>Converting categorical values to numeric</li>
    <li>Scaling values(normalization/standardization) it'll help converge the values faster while building models</li>
    <li>After analysing(refer Price Trends notebook) I figured that theres one data point of variety potato in achmera market and one of other in jagnair so we need to take care of those points either we can remove them or change there variety by the top variety which is Desi.
</ol>

<li>Relevant Features</li>
<ol>
    <li>Commodity</li>
    <li>Variety because different varieties have different prices</li>
    <li>Time</li>
    <li>Market Name because prices differ market to market</li>
</ol>

<li>ML problem</li>
-As time is the greatest factor here we can treat this problem as a forecasting problem i.e using time as our independent variable we can forecast prices for future.

Why Forecasting?<br>
-Prices depends on features like time or simply we have time series data 

<ol>
    <li>Classic ARIMA/SARIMA</li>
    <li>Deep Learning(RNN or LSTM)</li>
    
</ol>

<li>Target Variable</li>


<ol>
    <li>Modal Price</li>

    
</ol>

<li>Loss function</li>
-As the data is linear 
<ol>
    <li>We could use mean squared error(MSE) because it would directly  us the difference between predicted/forecasted and real prices.</li>
    
</ol>

------------------------------------------Uploaded file Info-----------------------------------------
<ol>
  <li> crawler.py - It consists the scrawler but it only scapres table from first page.</li>
  <li>crawler.ipynb- step by step explanation of what the crawler does.</li>
  <li>(b) price trends analysis- It consists of data and visualization from which the observations are derived</li>
  <li> I was not able to scrape the tables from each page(But I am willing to learn how to do it) so, instead I took the data from export to csv option and did the analysis.
</ol>

PS: I have used references from medium and pluralsight articles to build the crawler.
