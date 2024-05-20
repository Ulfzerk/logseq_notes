- **Definition (Conjugate Prior) (Sprzężony Prior)**
- Let D and x be a data-set and a variable to be inferred, respectively, connected by the likelihood $p(D|x) = \mathcal{l}(D;x)$. A conjugate prior to $\mathcal{l}$ for x is a probability measure with pdf p(x)=g(x;\Theta), such that
  $p(x|D) = \frac{\mathcal{l}(D;x)g(x;\Theta)}{\int \mathcal{l}(D;x)g(x;\Theta) dx}=g(x;\Theta + \phi(D)$
  That is, such that the posterior arising from $\mathcal{l}$ is of the same functional form as the prior, with updated parameters arising by adding some sufficient statistics of the observation D to the prior's parameters.**
-