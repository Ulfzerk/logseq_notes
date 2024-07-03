- /
	-
-
- **pipeline**
	- Basic object int the Transformers library is the pipeline() function.
	- It connects a model with its necessary preprocessing and postprocessing steps, allowing us to directly input any text and get an intelligible answer.
	- ```python
	  from transformers import pipeline
	  
	  classifier = pipeline("sentiment-analysis")
	  classifier("I've been waiting for a HuggingFace course my whole life.")
	  
	  #output: [{'label': 'POSITIVE', 'score': 0.9598047137260437}]
	  ```