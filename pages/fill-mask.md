- What is a goal of fill mask task? #card
	- The goal of this task it to predict a masked word or image pixels
- Prompt with masked text:
	- ```This course will teach you all about <mask> models.```
	- Possible output:
		- ```json
		  [{'sequence': 'This course will teach you all about mathematical models.',
		    'score': 0.19619831442832947,
		    'token': 30412,
		    'token_str': ' mathematical'},
		   {'sequence': 'This course will teach you all about computational models.',
		    'score': 0.04052725434303284,
		    'token': 38163,
		    'token_str': ' computational'}]
		  ```