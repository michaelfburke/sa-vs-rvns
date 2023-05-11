## Metaheuristic Showdown: Simulated Annealing vs Reduced Variable Neighborhood Search for the Uncapacitated Single Allocation p-hub Location Problem

## Abstract

Ever wonder how different metaheuristic methods stack up against each other in solving complex problems? This project dives into just that! We're comparing simulated annealing (SA) and reduced variable neighbourhood search (RVNS) and their effectiveness in tackling a specific logistics problem - the Uncapacitated Single Allocation p-hub Location Problem (USApHLP), with a twist - we're including a flow-dependent cost. We're not holding back either, we're testing these methods against benchmarks with varying numbers of nodes and hubs. Stay tuned to see how they perform!

## Introduction and Problem Description

Alright, let's set the stage. We have a logistics network with nodes and hubs, and our mission is to figure out the best way to position our hubs to minimise the total flow cost. No easy task, right? But that's where our chosen methods - SA and RVNS - come into play. 

We've got three sets of problems to tackle: CAB with 25 nodes and either 3 or 5 hubs, TR with 55 nodes and 3 or 5 hubs or 81 nodes with 5 and 7 hubs, and RGP with a hefty 100 nodes and either 7 or 10 hubs.

But there's a catch - the links between hubs experience a flow-dependent discount factor to simulate economies of scale. Check out the table below to get the details:

Table 1: Piecewise parameters for flow-dependent discount factor

| Flow (km x1000) | Slope | Intercept |
| --- | --- | --- |
| 0 ≤ fkrm < 50 | 1 | 0 |
| 50 ≤ fkrm < 100 | 0.8 | 10,000 |
| 100 ≤ fkrm < 200 | 0.6 | 30,000 |
| 200 ≤ fkrm | 0.4 | 70,000 |

Over the course of this project, I'll be diving into the literature that surrounds this problem and our chosen methods, taking a deep dive into the nitty-gritty of the algorithms, and then putting them to the test against our datasets. And of course, I'll be sharing the results and insights I gather along the way, as well as any potential future directions this project could take.

**Python Notebooks**

* `data_preparation.ipynb`: This is where we roll up our sleeves and get our hands dirty with the data. We're importing our benchmark problems (CAB, TR, RGP) and prepping them for the big showdown. We'll also be modeling our flow-dependent discount factor here.

* `simulated_annealing.ipynb`: Let's see what Simulated Annealing can do! This notebook is all about implementing the SA method.

* `rvns.ipynb`: Time for Reduced Variable Neighborhood Search to shine. This notebook is dedicated to RVNS and its implementation.

* `results_analysis.ipynb`: The moment of truth - let's see how our methods performed. We'll compare the results between SA and RVNS, analyze their performance across different problem sizes, and draw some interesting conclusions.

## Background and Literature

So, let's start with a bit of background. We're diving into the realm of Hub Location Problems (HLPs), specifically the Single Allocation p-Hub Location Problem (SApHLP). Along the way, we'll look at how economies of scale factor into the mix and delve into the methods typically used to solve these problems, focusing on metaheuristics. And of course, we'll talk about the two stars of our show, Simulated Annealing and Reduced Variable Neighbourhood Search.

### Hub Location Problems

Hub Location Problems have been around for quite some time. The first discrete model for SApHLP was introduced by O’Kelly in 1987. It's a fascinating area with two main types of problems - single and multiple allocation. Single allocation restricts nodes to interacting with just one hub, while multiple allocation lets them mingle a bit more, using more than one hub. 

These types of problems come up in a bunch of different industries, from cargo delivery and airlines to telecommunications and even neuroscience. 

### Modeling Economies of Scale

A lot of the time, HLPs use a fixed factor `a` on transportation costs that doesn't depend on flow, ignoring any economies of scale. But reality is a bit more complex, and some studies account for this by using a discount factor that changes with the amount of flow. There are several ways to bring flow-dependent economies of scale into the HLP picture, like modeling `a` as a piecewise linear concave function.

### Solving HLPs with Metaheuristics

When O’Kelly first formulated the USApHLP, he showed that determining the number of hubs in advance is a tough, NP-hard problem. He provided a couple of enumeration-based heuristics to solve the quadratic integer problem. Since then, many different flavors of metaheuristics have been used to tackle the USApHLP. 

In the broad spectrum of metaheuristics, we've seen the application of Genetic Algorithms, Branch and Bound approaches, Tabu Search, Simulated Annealing, Particle Swarm Optimisation, and many others.

### Simulated Annealing

Simulated Annealing (SA) is a crowd favorite - it's easy to implement and can produce high-quality solutions without hogging all your CPU time. It's a stochastic optimization algorithm that's inspired by the process of annealing in metallurgy. 

The SA method starts with an initial solution and then iteratively generates new candidate solutions. If a candidate solution is better than the current one, it's accepted. If not, it still has a chance to be accepted based on a certain transition probability that depends on a temperature parameter. As the algorithm progresses, this temperature parameter gradually decreases, reducing the chances of accepting worse solutions and helping the algorithm approach a local minimum of the objective function.

### Reduced Variable Neighbourhood Search

The Variable Neighbourhood Search (VNS) is another optimization algorithm that improves local search methods by systematically changing the neighbourhood structures during the search. Reduced Variable Neighbourhood Search (RVNS) is a variant of VNS that aims to reduce the computational cost of exploring large and diverse neighbourhoods. 

In RVNS, the algorithm compares the cost of solutions in different neighbourhood structures with the current solution, and updates the current solution if it finds a better one. The quality of the solution obtained by RVNS depends on various factors, such as the choice of neighbourhood structures, the selection strategy for the neighbourhoods, and the stopping criteria used by the algorithm.

## Results and discussion

The chosen algorithms, Simulated Annealing (SA) and Reduced Variable Neighbourhood Search (RVNS), were run 10 times each for various problems. The performance of these algorithms exhibited interesting trends. For smaller problems, SA demonstrated superior performance, while RVNS showed better results for mid-sized and larger problems when considering the mean network cost. However, focusing on minimum cost achieved over 10 experiments, SA produced better results for larger problems, while RVNS excelled in mid-sized problems.

The results also highlighted the importance of the stopping criteria. RVNS was found to approach better solutions more efficiently in the short term, while SA, due to its ability to escape local optima, outperformed RVNS in the long term. These observations suggest that future work could benefit from experimenting with different stopping criteria, such as a maximum number of iterations since the last improvement or maximum total CPU time.

The results from both algorithms are compared directly in Table 2.

*Table 2: Comparison of results between SA and RVNS*

| Problem | Best NC (SA) | Best NC (RVNS) | Average TNC (SA) | Average TNC (RVNS) |
|---------|--------------|----------------|-------------------|--------------------|
| CAB 25 (p = 3) | 8374475034.114 | 8374475034.114 | 8590459096.285 | 8874983823.663 |
| CAB 25 (p = 5) | 7658571002.397 | 7678738446.551 | 7839340117.167 | 8021243077.260 |
| TR 55 (p = 3) | 28147615297.000 | 28147615297.000 | 28222403532.700 | 28630318497.220 |
| TR 55 (p = 5) | 24534856784.200 | 23901453402.400 | 25249414787.140 | 25181348630.200 |
| TR 81 (p = 5) | 43949942949.892 | 43632312525.974 | 45196975677.935 | 44959755116.830 |
| TR 81 (p = 7) | 39854191611.840 | 39965806115.204 | 41047892555.324 | 40787579625.590 |
| RGP 100 (p = 7) | 134917272832.190 | 135127053345.851 | 136233276179.495 | 136974062858.205 |
| RGP 100 (p = 10) | 133170265954.954 | 133487461644.761 | 134674324457.128 | 134587743267.602 |

## Conclusion and Future Work

The comparative study of SA and RVNS revealed that both metaheuristics approach their solutions efficiently, but their performance varies with problem size. SA consistently outperforms RVNS for smaller problems, while RVNS shows better results for larger problems when considering mean network cost.

In terms of future work, it would be beneficial to experiment with different stopping criteria to further reveal the differences in performance between the two algorithms. This could provide valuable insights for optimising these metaheuristics for different problem sizes and complexities.

## References

Abdinnour-Helm, S. (1998), ‘A hybrid heuristic for the uncapacitated hub location problem’, *European journal of operational research* 106(2-3), 489–499.

Abdinnour-Helm, S. & Venkataramanan, M. (1998), ‘Solution approaches to hub location problems’, *Annals of Operations research* 78(0), 31–50.

Alkaabneh, F., Diabat, A. & Elhedhli, S. (2019), ‘A lagrangian heuristic and grasp for the hub-and- spoke network system with economies-of-scale and congestion’, *Transportation Research Part C: Emerging Technologies* 102, 249–273.

Alumur, S. A., Campbell, J. F., Contreras, I., Kara, B. Y., Marianov, V. & O’Kelly, M. E. (2021), ‘Perspectives on modeling hub location problems’, *European Journal of Operational Research* 291(1), 1–17.

Azizi, N. (2019), ‘Managing facility disruption in hub-and-spoke networks: formulations and efficient solution methods’, *Annals of Operations Research* 272(1-2), 159–185.

Azizi, N. & Salhi, S. (2022), ‘Reliable hub-and-spoke systems with multiple capacity levels and flow dependent discount factor’, *European Journal of Operational Research* 298(3), 834–854.

Collins, N., Eglese, R. & Golden, B. (1988), ‘Simulated annealing–an annotated bibliography’, *American Journal of Mathematical and Management Sciences* 8(3-4), 209–307.

Ernst, A. T. & Krishnamoorthy, M. (1996), ‘Efficient algorithms for the uncapacitated single allocation p-hub median problem’, *Location science* 4(3), 139–154.

Ernst, A. T. & Krishnamoorthy, M. (1999), ‘Solution algorithms for the capacitated single allocation hub location problem’, *Annals of operations Research* 86(0), 141–159.

Hansen, P., Mladenovic, N. & Moreno Perez, J. A. (2010), ‘Variable neighbourhood search: methods and applications’, *Annals of Operations Research* 175, 367–407.

O’Kelly, M. E. (1987), ‘A quadratic integer program for the location of interacting hub facilities’, *European journal of operational research* 32(3), 393–404.

O’Kelly, M. E. & Bryan, D. (1998), ‘Hub location with flow economies of scale’, *Transportation research part B: Methodological* 32(8), 605–616.

Racunica, I. & Wynter, L. (2005), ‘Optimal location of intermodal freight hubs’, *Transportation Research Part B: Methodological* 39(5), 453–477.

Silva, M. R. & Cunha, C. B. (2009), ‘New simple and efficient heuristics for the uncapacitated single allocation hub location problem’, *Computers & Operations Research* 36(12), 3152–3165.

