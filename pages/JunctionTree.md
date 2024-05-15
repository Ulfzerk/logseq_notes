- It is also known as clique Tree
- In essence, it entails peforming belief propagation on a modified graph called a junction tree
- Nodes of variable are the branches
- goal is to eliminate cycles by clustering them into single nodes
- ### Properties
	- Singly connected: there is exactly one path between each pair of clusters
	- covering: for each clique A of G there is some cluster C such that A \in C
	- Running intersection: for each pair of clusters B and C that contain i, each cluster on the unique path between B and C also contains i.
	-
- https://ai.stanford.edu/~paskin/gm-short-course/lec3.pdf
- ![image.png](../assets/image_1715753330418_0.png)
-