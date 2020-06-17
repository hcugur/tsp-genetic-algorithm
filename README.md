# Symmetric Travelling Salesman Problem (TSP) with Genetic Algorithm


## Travelling Salesman Problem
Travelling salesman problem(TSP) is an NP-Hard combinatorial optimization problem. Given n-cities
and visiting all of them exactly once and at the end returning the first city. For n-cities, there are n! possible solutions.
As the objective, trying to find the optimal route. To learn more about [travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).


## Benchmark Problems
The program uses TSPLIB symmetric TSP problem samples in XML format. Sample files must be in ```/data``` folder and they must be in XML format.
To access other sample problems go to [benchmark problems in XML format](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/XML-TSPLIB/instances/).
Although most of the problems here are symmetric TSPs, careful not to choose other problem types. TSPLIB symmetric TSP benchmark problems list can be accessed 
[here](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/). If one wants to use custom problems, then the data must be converted to XML format.
Descriptions of TSPLIB XML format is [here](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/XML-TSPLIB/Description.pdf).


## Genetic Algorithm
A genetic algorithm is a metaheuristic, a subclass of evolutionary algorithms. It generally used to generate high-quality solutions to optimization and search problems. The algorithm first introduced by John Holland in 1960. Inspired by Charles Darwin's theory of evolution, it uses selection, crossover, and mutation mechanisms to work. That processes are applied to individuals when we are generating the next generations. Each individual represented as a chromosome. For the travelling salesman problem, each closed route is a chromosome. To learn more about [genetic algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm).


### Selection
The selection process in genetic algorithms is choosing chromosome pairs as parents for the next generation. For a population of n individuals, the selection process will produce n - 1 pairs. The fittest chromosome will be handed down to the next generation without being changed according to elitism. The selection strategy biased toward fittest, first two fittest individuals have a higher chance of selection than other individuals in the population of that generation.


### Crossover
The crossover process combines the chromosomes of parents generated in the selection process to form children. Traditional crossover methods include single-point crossover, two-point crossover, and uniform crossover. However, since there could be duplication of genes in chromosomes, traditional crossover methods are not suitable for travelling salesman problem. In this program, the **edge recombination(ER)** method applied to overcome this problem.

The edge recombination method first generates a neighbor list for each gene from both parents. Then using this neighbor list, from starting one of the parents' starting genes, and in each step adding current gene's neighbor that has the fewest neighbors, it creates a child chromosome. 


### Mutation
Mutation operation is using to overcome the sameness of individuals in a population and enhance genetic variability. If the crossover operator is used alone then after a certain number of generations will become the same, because only the fittest elements selecting from the population. If the local minimum is reached in previous populations, then, the current population should divert to the global minimum.

In this program, for the mutation process, a random swap operator is used. The random swap operator takes two random genes from the chromosome aside from the first and the last genes of the chromosome and swaps them.


## Tests
To run tests, in ```/tests``` folder execute:
```
pytest
```


## Usage
First to run the code install dependency libraries by executing:
```
pip install -r requirements.txt
```
To run the program, in ```/tsp``` folder execute:
```
python main.py <problem-instance-file-name> <generation-count> <mutation-rate> <population-size>
```
If ```<generation-count>, <mutation-rate>, <population-size>``` values are not given, then their default values will be used. They are ```750, 0.1, 75``` respectively.


## Licence
This project is licensed under the terms of the MIT license - see the [LICENSE](LICENSE.md) file for details