**Vehicle Routing Problem with Time Windows - Genetic Algorithms:**

Vehicle routing problem with time windows (VRPTW) can be defined as choosing routes for limited number of mini trucks to serve at a delivery Point in defined time windows. Each mini truck has a limited capacity. It starts from the depot and terminates at the depot. Each delivery Point should be served exactly once.  If mini trucks arrive before the time window &quot;opens&quot; or after the time window &quot;closes,&quot; there will be waiting cost and late cost. Assume that there are _K_ mini trucks in depot 0. _N_ customers are waiting to be served and each of the customers has a demand of _gi (i=1,2,3,…N)_ units. The distance between delivery point _i_ and _j_ is _dij_. Each mini truck has a capacity of _qk (k=1,2,3….K)_ units. That is, the total demands at the delivery points served by each mini truck cannot _qk_ exceed units. Therefore, a new mini truck needed to be arranged for delivery. Besides, each customer must be visited once and only once by exactly one mini truck. _Si_ represents service time needed by delivery point _i_ . Therefore, the mini truck has to stay at the location of delivery point _i_ for a time interval at least _Si( s0_=0is associated with the depot 0) for service. A time window [_ETi,LTi_] is considered. Therefore, if a mini truck arrives at customer _i_ before _ETi_, it has to wait until the beginning of the time window to serve at the delivery point. Thus, there is a cost _e_ for waiting. On the other hand, if a mini truck cannot arrive at _I_ before _LTi_, there will be a cost _f_ for late. _ti_ represents the moment when the mini truck arrives _I_ from the depot. And the unit freight of each mini truck is _Ck_.

![](RackMultipart20200810-4-h5xtw8_html_af3d2d50f0a9bdaa.png)

**Dataset:**

For solving the above problem we are using, the Solomon instances, the entire set of instances can be obtained from [here](http://web.cba.neu.edu/~msolomon/problems.htm).

![](RackMultipart20200810-4-h5xtw8_html_ee196db46bb14cc2.png)

Solomon generates 6 different types of problems, these factors include:

- Geographical Co-ordinates of the delivery points
- The number of customers serviced by vehicle
- percent of time-constrained customers

The geographical data are randomly generated in problem sets R1 and R2, clustered in problem sets C1 and C2, and a mix of random and clustered structures in problem sets by RC1 and RC2, the delivery point coordinates are identical within one type (i.e. R, C, RC)

Other Remarks:

1. All the constants are integers
2. CUST NO. 0 denotes the depot, where all the mini- trucks must start and finish
3. K is the maximum number of mini-trucks
4. Q is the capacity of the mini-trucks
5. READY TIME is the earliest time at which service may start at the given delivery point/depot
6. DUE DATE is the latest time at which service may start at the given delivery point/ depot
7. The value of time is equal to the value of distance

**Implementation of standard GA in the above scenario:**

**Individual (Chromosome):**

Individual Coding: All the visited delivery points of a route (including several sub route) are coded into an individual in turn.The following route

_ **Sub-Route 1: 0 – 5 – 3 – 2 – 0** _

_ **Sub-Route 2: 0 – 7 – 1 – 6 – 9 – 0** _

_ **Sub-Route 3: 0 – 8 – 4 – 0** _

are coded as _ **5 3 2 7 1 6 9 8 4** _, which is stored in a Python list

Individual Decoding: The function ind2route (individual, instance) decodes **individual** to **route** representation. This function is also responsible for subtour elimination, which is responsible for the accumulation the capacity constraint.

**Selection:** This process is important as it helps to determine which parents will be used to create a child for the next generation, the approach used here is **Fitness Proportionate selection** or **Roulette Wheel selection**. It selects _K_ individuals from the input using _K_ spins of the Roulette. The selection is made by looking at the first objective only. It returns a python list of the _K_ individuals. The selection function is called from the DEAP package via _deap.tools.selRoulette()_

**Crossover:** Here we execute a **partially matched crossover (PMX**) on the input individuals. The two individuals are modified in place.

![](RackMultipart20200810-4-h5xtw8_html_7db7fccd68a8cc2.png)

The above crossover performed the best over the several crossovers which were tried, namely cyclic crossover and ordered crossover.

**Mutation:** The **inverse mutation** has been performed here, where the attributes between two random points of the input individual are inverted and the mutant id returned.

**Parameters of the final algorithm** _gavrptw ():_

There is no provision for creation of the mating pool here i.e. the entire culmination of all individuals into a population manually. This is because we have introduced the DEAP framework here, takes care of the following. The attributes of the individuals and population are generated using an instance of the Toolbox() class of the DEAP package. Moreover, we are not using any predefined functions for mutation and crossover and creating are very own for a better evaluation and finally registering them to the framework.

The above function implements a genetic algorithm-based solution to vehicle routing problem with time windows

- instName: A problem instance name provided in Solomon&#39;s VRPTW benchmark problems.
- unitCost: The transportation cost of one vehicle for a unit distance.
- initCost: The start-up cost of a mini truck
- waitCost: Cost per unit time if the mini truck arrives early than the delivery point&#39;s ready time
- delayCost: Cost per unit time if the mini truck arrives later than due time.
- indSIze: Size of an individual
- popSize: Size of a population
- cxPb: Probability of crossover
- mutPb: Probability of mutation
- NGen: Maximum number of generations to terminate evolution
- exportCSV: If &#39;True&#39;, a CSV format log file will be exported to the results\ directory
- customizeData -If &#39;True&#39;, customised JSON format problem instance file will be loaded from data\json\_customised\directory

**Running the Code:**

Change to current directory in the terminal window .i.e. VRPTW-GA

# python Problem.py

The instances available to run the code are:

- C101,C201,R101,R201,RC101,RC201

Change the required instance as mentioned in the Problem.py
