- What is a goal of NER task? (Named entity recognition) #card
	- Named entity recognition (NER) is a task where the model has to find which parts of the input text correspond to entities such as persons, locations, organizations etc.
- Example:
	- ````
	  "My name is Sylvain and I work at Hugging Face in Brooklyn."
	  ````
	- ```json
	  [{'entity_group': 'PER', 'score': 0.99816, 'word': 'Sylvain', 'start': 11, 'end': 18}, 
	   {'entity_group': 'ORG', 'score': 0.97960, 'word': 'Hugging Face', 'start': 33, 'end': 45}, 
	   {'entity_group': 'LOC', 'score': 0.99321, 'word': 'Brooklyn', 'start': 49, 'end': 57}
	  ]
	  ```