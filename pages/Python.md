# Math related
	- array_to_latex - allows to cast numpy arrays into tex strings.
	- Gamma function is a efficient implementation of factorial k! etc.
- # Matrixes
	- Jax - accelerator-oriented array computation and program transformation designed for high-performance numerical computing and large-scale machine learning
		- Autograd
		- XLA
- # Cool features
	- Annotations
		- ```py
		  from __future__ import annotations
		  ```
		- Type hints
- # Base
	- functools (combinations, permutations etc)
	- abc (abstract base class)
		- inheritence etc.
- Function params -> function(x , / ) - it means that this function is not supposed to receive keywards arguments. https://peps.python.org/pep-0570/
-
- # My Setup
	- ```python
	  pip install jupyter
	  python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
	  ```