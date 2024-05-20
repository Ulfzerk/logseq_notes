- **Definition (Conjugate Prior) (Sprzężony Prior)**
- Let D and x be a data-set and a variable to be inferred, respectively, connected by the likelihood $p(D|x) = \mathcal{l}(D;x)$. A conjugate prior to $\mathcal{l}$ for x is a probability measure with pdf p(x)=g(x;\theta), such that
  $p(x|D) = \frac{\mathcal{l}(D;x)g(x;\Theta)}{\int \mathcal{l}(D;x)g(x;\Theta) dx}=g(x;\Theta + \phi(D)$
  That is, such that the posterior arising from $\mathcal{l}$ is of the same functional form as the prior, with updated parameters arising by adding some sufficient statistics of the observation D to the prior's parameters.**
- ## Chat Gpt says on ConjugatePrior
	- In Bayesian statistics, a **conjugate prior** is a type of prior distribution that, when combined with a particular likelihood function through Bayes' theorem, results in a posterior distribution that belongs to the same family as the prior distribution. This mathematical property greatly simplifies the process of updating beliefs with new data, as the resulting posterior distribution remains in a form that is easy to work with and analyze.
	- ### Key Concepts
	- **Prior Distribution**: This is the distribution that represents the initial belief about a parameter before observing any data. It's denoted as 𝑝(𝜃)*p*(*θ*).
	- **Likelihood Function**: This is the probability of observing the data given a parameter value, denoted as 𝑝(𝐷∣𝜃)*p*(*D*∣*θ*).
	- **Posterior Distribution**: This is the updated belief about the parameter after observing the data, obtained by applying Bayes' theorem:
	  
	  𝑝(𝜃∣𝐷)=𝑝(𝐷∣𝜃)𝑝(𝜃)𝑝(𝐷)*p*(*θ*∣*D*)=*p*(*D*)*p*(*D*∣*θ*)*p*(*θ*)​
	- **Conjugacy**: A prior is conjugate to a likelihood if the posterior distribution 𝑝(𝜃∣𝐷)*p*(*θ*∣*D*) is in the same family as the prior distribution 𝑝(𝜃)*p*(*θ*).
	- ### Example
	  
	  Consider the case of a binomial distribution, which is commonly used for modeling the number of successes in a fixed number of independent trials.
	- **Likelihood Function**: The likelihood for a binomial distribution with parameter 𝜃*θ* (probability of success) and data 𝐷*D* (number of successes out of 𝑛*n* trials) is:
	  
	  𝑝(𝐷∣𝜃)=(𝑛𝐷)𝜃𝐷(1−𝜃)𝑛−𝐷*p*(*D*∣*θ*)=(*D**n*​)*θ**D*(1−*θ*)*n*−*D*
	- **Conjugate Prior**: For the binomial likelihood, the conjugate prior is the Beta distribution, parameterized by 𝛼*α* and 𝛽*β*:
	  
	  𝑝(𝜃)=𝜃𝛼−1(1−𝜃)𝛽−1𝐵(𝛼,𝛽)*p*(*θ*)=*B*(*α*,*β*)*θ**α*−1(1−*θ*)*β*−1​
	  
	  where 𝐵(𝛼,𝛽)*B*(*α*,*β*) is the Beta function, ensuring that the distribution is properly normalized.
	- **Posterior Distribution**: When you combine the binomial likelihood with the Beta prior using Bayes' theorem, the resulting posterior distribution is also a Beta distribution:
	  
	  𝑝(𝜃∣𝐷)∝𝜃𝐷+𝛼−1(1−𝜃)𝑛−𝐷+𝛽−1*p*(*θ*∣*D*)∝*θ**D*+*α*−1(1−*θ*)*n*−*D*+*β*−1
	  
	  This posterior distribution is a Beta distribution with updated parameters:
	  
	  𝜃∣𝐷∼Beta(𝐷+𝛼,𝑛−𝐷+𝛽)*θ*∣*D*∼Beta(*D*+*α*,*n*−*D*+*β*)$
	- ### Advantages of Using Conjugate Priors
	- **Analytical Simplicity**: The mathematical form of the posterior is straightforward and within the same family as the prior, making it easier to compute and understand.
	- **Computational Efficiency**: The use of conjugate priors reduces the computational complexity, as there is no need for numerical integration to obtain the posterior distribution.
	- **Interpretability**: The parameters of the posterior distribution can be interpreted as an updated form of the prior parameters, providing a clear understanding of how new data updates beliefs.
	- ### Conclusion
	  
	  Conjugate priors are a powerful concept in Bayesian analysis, enabling efficient and intuitive updating of beliefs in the presence of new data. They are particularly useful in cases where the same type of inference needs to be performed repeatedly, as the computational and analytical processes are streamlined.