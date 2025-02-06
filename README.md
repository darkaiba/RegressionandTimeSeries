<h1 align="center">Time Series</h1>

Time Series
=================

<p align="justify">Let's use a more recent and suitable dataset, such as load_diabetes. This dataset contains information related to diabetes and can be used for time series analysis in a similar way.</p>
<p align="justify">The load_diabetes dataset has several variations, but for the sake of example, we will use variable data to perform time series analysis. We will also use the time series setup function to visualize it.</p>

<p align="justify">Explanation:</p>
<p align="justify"> 1 - The load_diabetes dataset is more recent and contains information about patients with diabetes. I have chosen to use the bmi (Body Mass Index) variable for time series analysis.</p>
<p align="justify"> 2 - Generating the time index: We create a data index to simulate a time series based on the data observations.</p>
<p align="justify"> 3 - Decomposing the time series: We use the season_decompose function from the statsmodels library to decompose the time series into trend, seasonality and error.</p>
<p align="justify"> 4 - Moving Average: We calculate the moving average to smooth the series and observe long-term trends.</p>

<p align="justify">Results:</p>
<p align="justify"> 1 - The time series graph shows how the body mass index varies over time.</p>
<p align="justify"> 2 - The suspension of the time series presents the trend, seasonality and error components.</p>
<p align="justify"> 3 - The moving average is used to smooth the fluctuations of the series and predict trends.</p>
