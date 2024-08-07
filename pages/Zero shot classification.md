- What is Zero-Shot Classification? #card
	- Zero-shot text classification is a task in natural language processing where a model is trained on a set of labeled examples but is then able to classify new examples from previously **unseen** classes
- About the Zero shot classification task
	- Zero shot classification is the task of predicting a class that wasn't seen by the model during training.
	- Uses pre-trained language model
	- Can be thought of as an instance of transfer learning which generally refers to using a model trained for one task in a different application than what it was originally trained for. 
	  This is particularly useful for situations where the amount of labeled data is small
	- It is seem to be an emergent feature of [[LLMs]]
		- This feature seems to come about around model sizes of +100M parameters
			- Effectivness of a model at a zero, signle/few shot task seems to scale with model size,
			  so bigger models generally do better at this task
- Example zero-shot prompt for classifying the sentiment of a sequence of text:
	- ```
	  Classify the following input text into one of the following three categories: [positive, negative, neutral]
	  - Input Text: Hugging Face is awesome for making all of these
	  state of the art models available!
	  Sentiment: positive
	  ```
	-
- **Useful for:**
	- When we have small amount of labeled data
- **What is a difference between Zero shot classification and single/one few-shot classification** #card
	- In single/one/few shot classification, these tasks include a single or a few examples of the selected task.