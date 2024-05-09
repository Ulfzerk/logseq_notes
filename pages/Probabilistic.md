### Inference problem
	- An inference problem requires statements about the value of an unobserved (latent) variable X based on observations y which are related to x, but may not be sufficient to fully determine x. This requires a notation of uncertainty
	-
- Keywords / Glossary :
	- Observed, Observations - data etc.
	- Unobserved (latent) - hypothesis - latent quantity etc.
- Notes
	- This kind of reasoning is computably expensive, so it is common to use approximations, tricks and tricks.
- Baysian Teorem
	- $P(A|B)=\frac{P(B|A)P(A)}{P(B|A)P(A) +P(A|~B)P(~B)}$
	- P(A|B) - Posterior probability, so probability after seeing observations. Result of inference?
	- P(A) - Prior - probability of event before inference e.g. How often someone is ill with covid? It is unconditioned.
	- P(B|A) - Likelihood - conditional probability of an event given observations. e.g. How probable is to have covid given a positive test.
	- Denominator - where we relate probabilities with all possible observations of the data. So it is a normalization based on all possibilities.
	- ![image.png](../assets/image_1715256177018_0.png)
- ### Probability axioms (Kolmogorov axioms)
	- What are axioms?
		- These axioms are foundations of probability theory introduced by Andrey Kolmogorov in 1933
		  Axioms are fundamental principles or statements taken to be true without requiring proof within a particular system of thought of field of study. They serve as starting point or foundational concepts upon which other propositions and theorems are built.
	- Defintions:
	  A - Event
	  P(A) - function of probability/occurance of event A
	  \Omega - All possible outcomes
	  F - event space - all possible events
	  Not that events are not outcomes of events.
	-
	- Axiom 1 - Non-Negativity
	  The probability of an event is a non-negative real number. 
	  P(A) \in $\mathcal{R}$, P(A) > 0,  \forall A \in F \]
	- Axiom 2 - Normalization
	  P(\Omega) = 1
	  This assumption of unit measure: The probability that at least one of the elementary events in the entire sample space will occur is 1. 
	  That means that probability that any of the events from sample space occur is 1.
	- Axiom 3 - Additivity
	  If we have a sequence of mutually exclusive events (events that cannot occur simultaneusly), then the probability of the union of these events is equal to the sum of their individual probabilities. Mathematically if A_1, A_2, A_3... are mutually exclusive events then the probability of their union is 
	  $*P(⋃*i*=1∞​*A**i*​)=∑*i*=1∞​*P*(*A**i*​)$
	-
	- Why do we need them?
-