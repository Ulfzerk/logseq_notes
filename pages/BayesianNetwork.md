# Definition
- A Dritected Graphical Model (DGM), aka Bayesian Network is a probability distribution over variables {X_1,...,_X_D} that can be written as 
  
  $P(X_1,X_2,....,X_D) = \prod_{i=1}^{D} p(X_i | pa(X_i))$
- Where pa(X_i) are the parental variables of X_i, that is, X_i \notin pa(X_j) \forall X_j \in pa(X_i). A DGM can be represented by a Directed Acyclic Graph (DAG) with the propositional variables as nodes, and arrows from parents to children
-
- # Notes
- It is Acyclic!!!
- "every probability distribution can be written as a graph" Dense graph
- By the Product Rule, every joint can be factorized into a (dense) DAG
- The direction of the arrows is **not** a  causal statement.
	- The alarm doesn't causes earthquakes ;)
- We want to remove edges from graph to simplyfiy model.
- Chain Graph - all nodes goes with the same direction A->B->C etc.
	- P(A,B,C) = P(A) * P(B|A) * P(C|B)
	- A is independent from B and C
	- B is dependent on A
	- C is dependent on B but not A.
- Colider structure - A->B<-C
	- A is dependent on C |B
		- but is independent on C itself
	-
- out - A<-B->C (Probably doesn't have a name)
-