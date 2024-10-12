- What is a goal of fill mask task? #card
  card-last-interval:: -1
  card-repeats:: 1
  card-ease-factor:: 2.5
  card-next-schedule:: 2024-07-09T22:00:00.000Z
  card-last-reviewed:: 2024-07-09T20:09:44.599Z
  card-last-score:: 1
	- The goal of this task it to predict a masked word or image pixels
	  Example:
	  `this is a <mask> word. Nobody knows that word.`
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