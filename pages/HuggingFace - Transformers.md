icon:: 🤗

	-
- **pipeline**
	- Basic object int the Transformers library is the pipeline() function.
	- It connects a model with its necessary preprocessing and postprocessing steps, allowing us to directly input any text and get an intelligible answer.
	-
	- ```python
	  from transformers import pipeline
	  
	  classifier = pipeline("sentiment-analysis")
	  classifier("I've been waiting for a HuggingFace course my whole life.")
	  
	  #output: [{'label': 'POSITIVE', 'score': 0.9598047137260437}]
	  ```
- Pipeline steps
	- Text is preprocessed into a format the model can understand
	- Preprocessed input are passed to the model
	- predictions of the model are post-processed so you can make sense of them
- **Available pipelines**:
	- feature-extraction ([[word embeddings]])
	- (Fill mask)[[fill-mask]]
	- (ner)[[Named entity recognition]]
	- (question-answering)[[Question answering]]
	- (sentiment-analysis)[[Sentiment analysis]]
	- (summarization)[[Text summarization]]
	- (text-generation)[[Text-generation]]
	- (translation)[[Translation]]
	- (zero-shot-classification)[[zero shot classification]]
	-