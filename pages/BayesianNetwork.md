# Definition
- A Dritected Graphical Model (DGM), aka Bayesian Network is a probability distribution over variables {X_1,...,_X_D} that can be written as 
  
  $P(X_1,X_2,....,X_D) = \prod_{i=1}^{D} p(X_i | pa(X_i))$
- Where pa(X_i) are the parental variables of X_i, that is, X_i \notin pa(X_j) \forall X_j \in pa(X_i). A DGM can be represented by a Directed Acyclic Graph (DAG) with the propositional variables as nodes, and arrows from parents to children
-
- # Notes
- It is Acyclic!!!
-