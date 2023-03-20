# Probability Distributions

> Distributions refer to the probability of occurrence for all possible outcomes. Distributions can be graphed. The kind of distribution associated with a set of events can tell us about the properties the events have and how to appropriately analyze them. (Note: the sum of all probabilities over an entire distribution is one)

## Types of Distributions
### Know Well
#### Uniform
- **What it is**
	- Every possible outcome has the same probability (Can use integral to get sum of all probabilities).
- **Discrete vs. Continouos**
	- Continuous
- **What it looks like**
	- <img src="https://user-images.githubusercontent.com/53871641/226483994-03311011-4e87-4aa3-9fe0-0c92c47fdab0.png" width="300" height="200">
	
- **Examples**
	- Drawing a 6 from a deck of cards.

#### Bernoulli
- **What it is** 
	- Distribution of probability for an event which takes on the value of zero or one (binary). Does not literally have to be zero or one, just means that the even has only two possible outcomes.
- **Discrete vs. Continouos**
	- Discrete
- **What it looks like**
	- <img src="https://user-images.githubusercontent.com/53871641/226484372-8820d831-8632-4863-b7c5-f66574168e1b.png" width="300" height="200">
	
- **Examples**
	- Coin flip

#### Binomial
- **What it is** 
	- The number of successes (or has the value one) in *n* independent Bernoulli trials.
	- Note: Bernoulli relates to distribution of single trial of event, binomial refers to multiple trials
- **Discrete vs. Continouos**
	- Discrete
- **What it looks like**
	- <img src="https://user-images.githubusercontent.com/53871641/226484532-853973ee-4093-43cc-bb48-d5cd632acfaa.png" width="300" hwight="200">
	
- **Examples**
	- Flipping coin 100 times.

#### Normal
- **What it is**
	- In this distribution, the probability of events cluster towards the center of all possible events and taper off towards the ends. 
	- Note: shape of binomial and normal distribution are similar, but normal is continuous and binomial is discrete
- **Discrete vs. Continouos**
	- Continuous
- **What it looks like**
	- <img src="https://user-images.githubusercontent.com/53871641/226484806-926edbf3-5857-4857-993c-97a85723ac6b.png" width="300" height="150">

- **Examples**
	- Population height

#### Poisson
- **What it is** 
	- Describes how many times an event will occur in a specified time frame.
- **Discrete vs. Continuous**
	- Discrete
- **What it looks like**
	- <img src="https://user-images.githubusercontent.com/53871641/226484974-99ad91b7-ddc0-4314-8332-82b805d30e9e.png" width="300" height="200">

- **Examples**
	- Number of customers entering a strore every fifteen minutes
- **Note**
	- Zero-inflated poisson is a poisson distribution with a high number of zeroes. In this case the zeroes can be ignored.

### Less Common
#### Power Law
- **What it is** 
	- In this distribution a small set of events have a large probability while the remaining set of events have a small probability
- **Discrete vs. Continuous**
	- Continuous
- **Examples**
	- Wealth distribution in the U.S.

#### Chi-Squared
- **What it is** 
	- Distribution of sum of squared random variables. Used when there are many categorical variables.
- **Discrete vs. Continuous**
	- Continuous

#### Exponential
- **What it is** 
	- Usually concerns that amount of time until a specific event happens. (can think of poisson as having exponential between each event)
- **Discrete vs. Continuous**
	- Continuous

#### Gamma
- **What it is** 
	- Wait time for a fixed number of events
- **Discrete vs. Continuous**
	- Continuous

#### Weibull
- **What it is** 
	- Describes a waiting time for one event, if that event becomes more or less likely with time.
- **Discrete vs. Continuous**
	- Continuous

## Central Limit Theorem
- The central limit theorem states that as sample size becomes significantly large, the distribution of events approaches the normal distribution.




