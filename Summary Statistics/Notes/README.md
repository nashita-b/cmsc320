# Summary Statistics
1. [Purpose](#or)
2. [Types of Summary Statistics](#th)
3. [Miscellaneous](#mi)

# Purpose <a id="or"></a>
-  Summary statistics provide general overview of what data is telling us
- Summary statistics are useful for comparing datasets with similar distributions 
	- Example: can use summary statistics to compare the average weight of New York City rats to Baltimore rats
- Summary statistics can be misleading 

# Types of Summary Statistics <a id="th"></a>
- Central Tendency 
- Spread 
- Skew 

*Note: The kind of distribution determines what summary statistics are meaningful and which measures to use.*

## Central Tendency
> Central tendency shows where most of the data is centered. There are three types of central tendency: **mean**, **median**, and **mode**.

### Note on Distributions
Certain measures of central tendency are not meaningful for certain distributions:
- *Bimodal* 
	- Mean, median not useful
	- Mode may be useful 
- *Power law*
- *Uniform*
	- Mode not useful

### Measures of Central Tendency
- **Mean**: average of all numbers in dataset
- **Median**: middle element
- **Mode**: most common element in dataset

![image](https://user-images.githubusercontent.com/53871641/227394195-d4313e70-996c-4474-bee0-0a69f652384e.png)
*Depending on the properties of the dataset being evaluated, certain measures of central tendency are better suited for determining the center of the data.*

#### Types of Mean
##### Arithmetic mean  
![](https://lh4.googleusercontent.com/-y1-iFxaN2NFM1l9_42rCay0D-y_sHQjJCpawOqAps8nxo5x4RwBvGnaTYUfz0cJE5RYeUNyIfsZWDZNiIBXY_MQGLA_wvJ8zHgTc9EDS-vJxQsqPBcCzmvhIC83IACOfyt3nCfzq9U9RP47H_mKiI0)
- What people usually think about when they hear "average"
- **When to Use**
	- Good for distributions that have similar tails on either side (ex. normal distribution)

##### Geometric mean 
![](https://lh3.googleusercontent.com/QUrnjipWYBf4vZS-sXdqN5fSim_RksyN51Vl_HmKQ4xP0N7HdkYows23OqR_gTAEAjQ9sgqQZFD-ZIU9mELr3rlB9IyGXVp5cvcKYinLlH-PikgksH5ykb0Z8uCpFN-SeiGumsoku1KnSycLrKVZYk8)
- Cannot be used when datasets have 0 or negatives (in the case the data does, shift values with zero or negative to apply geometric mean)
- **Properties**
	- Less vulnerable to outliers than arithmetic mean
	- Large outliers exacerbated by geometric mean
- **Sample Application**
	- Length of stay in a hospital (most patients are there for a short period of time, some patients are there for orders of magnitude longer)

##### Harmonic mean 
![](https://lh6.googleusercontent.com/DS150_wrWtVi5oYtG5YYP-_P1nFKiDnctJV4k1H6biTvM99Ss3GcMTLyrVjfq4SzhNa0jCWZrTIOML4K1zpDBVJ3r8YTnt-1ee_TqVpN71jBNBze-jwjBS4msPH2Vi15nNw8_MuuPpBgBdnKXJbzXHw)
- Rarely used
- **When to Use**
	- Used in situations involving *rates and ratios*
- **Sample Application**
	- For instance, if a vehicle travels a certain distance d outbound at a speed x (e.g. 60 km/h) and returns the same distance at a speed y (e.g. 20 km/h), then its average speed is the harmonic mean of x and y (30 km/h) – not the arithmetic mean (40 km/h). The total travel time is the same as if it had traveled the whole distance at that average speed. 

### Mean and Median as Indicators
- When median and mean are different the distribution may have a skew or have many of outliers 

![[Pasted image 20230218132507.png]]

## Spread
> Spread measures how spread out a distribution is. The most common measures of spread is **standard deviation ** and **variance**. 

### Variance / Standard deviation
![400](https://lh3.googleusercontent.com/BClm4oMCc8MtT_RyPIDv9qt1G1enquwixE__5omgESt666WXqsbpQdT_k5VWyHu_g44PV6mSe8ag-h4jMeDDoAy8v1iAoJ10flhWUTCvWion2rfIMO_psnulrXTMUhMLT80uqynKouGxr2_dnovE_5E)

![300](https://lh4.googleusercontent.com/tE9r-9wskvgq8zue3FCDYozbvGPyciBxMf58hEVqvncUAa0Q4C8KAM5CoLP-h0FnLtF998gPUPrfO9HYA-4jmOpUVFaTSAGRLw_OVN17PnqgCHt9tvtERrIbg0ywKpKyTp2-3vgSME9JFCoK-SjVpSs)

- Standard deviation measures the average amount by which all the data points in a dataset deviate from the mean
- Large standard deviation means dataset is more spread out
- Standard deviation is in same units as actual data set
- Standard deviation and variance less useful with highly skewed distributions
- Standard deviation used when determining the confidence that a given data point came from the distribution in question

## Skew
> Skew measures how shifted a distribution is, or how many outliers it has.

![[Pasted image 20230216213445.png|400]]

### Kurtosis
- A measure of how likely a distribution is to produce outliers

### Skewness
- For a unimodal distribution,
	- **Negative skew**: indicates that the tail is on the left side of the distribution
	- **Positive skew**: indicates that the tail is on the right side of the distribution
- In cases where one tail is long but the other tail is fat, skewness does not obey a simple rule

### Normalcy
- How close to the normal distribution a given dataset is

# Miscellaneous <a id="mi"></a>
## Min / max
- Often as a data scientist it's useful to look at a collection of the data points at the edges 
	- Example: Determining the top and bottom 1%. This can help tell us if there is a fat tail, one or a few wild outliers, or some other pattern.

## Quartiles
-   Useful for seeing how tightly grouped the data is

*Note: Quintiles used as well, though not as common*

## Outlier detection
-   Z score:
![](https://lh4.googleusercontent.com/p0WDFz7BXV7mybrZCOTi8-gvoUwmrXvnM99Ie1MdjSerCe1GEBvmjZR9b24RuIJHBOzI5HpltU0-sPeKg0WscqlPoqb_gK0OV38sfAfBAmgfdRDRg4RXPjy9fg9H3snbFXYrBmLEHQim7b-NOxn3nnY)
-   Z-score is useful when comparing individuals in different metrics 
	- *Examples*
		- Are exceptionally tall women also exceptionally strong? 
		- Are lakes with average amounts of pollutants also of average size?
