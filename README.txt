CS534 AI Project 1 (search methods)

TO RUN THE CODE:
1. MAKE SURE THE SYSTEM HAVE Python 3.6 INSTALLED
2. make sure that Expand.py, Graph,py, Heap.py, main.py, Path.py, Queue.py, Vertex.py are all in the project folder
3. type 'python main.py' in commandline to run
4. The program will ask user to provide the path to the graph file
5. Enter the graph file path, hit enter
6. The program reads the file, and show the loaded graph
7. Press enter to continue
8. All search methods run

Sample output from two example graphs

Sample output for graph.txt:

Please enter a file path... Then press enter... (Please note the Program will NOT validate the input file) graph.txt

Graph read from file:
id: S Heuristic: 11.0 Connections: ['A', 'D']
id: A Heuristic: 10.4 Connections: ['S', 'B', 'D']
id: D Heuristic: 8.9 Connections: ['S', 'A', 'E']
id: B Heuristic: 6.7 Connections: ['A', 'C', 'E']
id: C Heuristic: 4.0 Connections: ['B']
id: E Heuristic: 6.9 Connections: ['B', 'D', 'F']
id: F Heuristic: 3.0 Connections: ['E', 'G']
id: G Heuristic: 0.0 Connections: ['F']
Press Enter to continue...
Running: DFS
         Expanded     Queue
         S              [<S>]
         A              [<A, S>, <D, S>]
         B              [<B, A, S>, <D, A, S>, <D, S>]
         C              [<C, B, A, S>, <E, B, A, S>, <D, A, S>, <D, S>]
         E              [<E, B, A, S>, <D, A, S>, <D, S>]
         D              [<D, E, B, A, S>, <F, E, B, A, S>, <D, A, S>, <D, S>]
         F              [<F, E, B, A, S>, <D, A, S>, <D, S>]
         G              [<G, F, E, B, A, S>, <D, A, S>, <D, S>]
         goal reached! Time taken by DFS is 0.0009710788726806641 seconds
Running: BFS
         Expanded     Queue
         S              [<S>]
         A              [<A, S>, <D, S>]
         D              [<D, S>, <B, A, S>, <D, A, S>]
         B              [<B, A, S>, <D, A, S>, <A, D, S>, <E, D, S>]
         D              [<D, A, S>, <A, D, S>, <E, D, S>, <C, B, A, S>, <E, B, A, S>]
         A              [<A, D, S>, <E, D, S>, <C, B, A, S>, <E, B, A, S>, <E, D, A, S>]
         E              [<E, D, S>, <C, B, A, S>, <E, B, A, S>, <E, D, A, S>, <B, A, D, S>]
         C              [<C, B, A, S>, <E, B, A, S>, <E, D, A, S>, <B, A, D, S>, <B, E, D, S>, <F, E, D, S>]
         E              [<E, B, A, S>, <E, D, A, S>, <B, A, D, S>, <B, E, D, S>, <F, E, D, S>]
         E              [<E, D, A, S>, <B, A, D, S>, <B, E, D, S>, <F, E, D, S>, <D, E, B, A, S>, <F, E, B, A, S>]
         B              [<B, A, D, S>, <B, E, D, S>, <F, E, D, S>, <D, E, B, A, S>, <F, E, B, A, S>, <B, E, D, A, S>, <F, E, D, A, S>]
         B              [<B, E, D, S>, <F, E, D, S>, <D, E, B, A, S>, <F, E, B, A, S>, <B, E, D, A, S>, <F, E, D, A, S>, <C, B, A, D, S>, <E, B, A, D, S>]
         F              [<F, E, D, S>, <D, E, B, A, S>, <F, E, B, A, S>, <B, E, D, A, S>, <F, E, D, A, S>, <C, B, A, D, S>, <E, B, A, D, S>, <A, B, E, D, S>, <C, B, E, D, S>]
         D              [<D, E, B, A, S>, <F, E, B, A, S>, <B, E, D, A, S>, <F, E, D, A, S>, <C, B, A, D, S>, <E, B, A, D, S>, <A, B, E, D, S>, <C, B, E, D, S>, <G, F, E, D, S>]
         F              [<F, E, B, A, S>, <B, E, D, A, S>, <F, E, D, A, S>, <C, B, A, D, S>, <E, B, A, D, S>, <A, B, E, D, S>, <C, B, E, D, S>, <G, F, E, D, S>]
         B              [<B, E, D, A, S>, <F, E, D, A, S>, <C, B, A, D, S>, <E, B, A, D, S>, <A, B, E, D, S>, <C, B, E, D, S>, <G, F, E, D, S>, <G, F, E, B, A, S>]
         F              [<F, E, D, A, S>, <C, B, A, D, S>, <E, B, A, D, S>, <A, B, E, D, S>, <C, B, E, D, S>, <G, F, E, D, S>, <G, F, E, B, A, S>, <C, B, E, D, A, S>]
         C              [<C, B, A, D, S>, <E, B, A, D, S>, <A, B, E, D, S>, <C, B, E, D, S>, <G, F, E, D, S>, <G, F, E, B, A, S>, <C, B, E, D, A, S>, <G, F, E, D, A, S>]
         E              [<E, B, A, D, S>, <A, B, E, D, S>, <C, B, E, D, S>, <G, F, E, D, S>, <G, F, E, B, A, S>, <C, B, E, D, A, S>, <G, F, E, D, A, S>]
         A              [<A, B, E, D, S>, <C, B, E, D, S>, <G, F, E, D, S>, <G, F, E, B, A, S>, <C, B, E, D, A, S>, <G, F, E, D, A, S>, <F, E, B, A, D, S>]
         C              [<C, B, E, D, S>, <G, F, E, D, S>, <G, F, E, B, A, S>, <C, B, E, D, A, S>, <G, F, E, D, A, S>, <F, E, B, A, D, S>]
         G              [<G, F, E, D, S>, <G, F, E, B, A, S>, <C, B, E, D, A, S>, <G, F, E, D, A, S>, <F, E, B, A, D, S>]
         goal reached! Time taken by BFS is 0.00090789794921875 seconds
Running: DLS
         Expanded     Queue
         S              [<S>]
         A              [<A, S>, <D, S>]
         B              [<B, A, S>, <D, A, S>, <D, S>]
         D              [<D, A, S>, <D, S>]
         D              [<D, S>]
         A              [<A, D, S>, <E, D, S>]
         E              [<E, D, S>]
Running: IDDFS
L = 0     Expanded     Queue
         S              [<S>]
Running: IDDFS
L = 1     Expanded     Queue
         S              [<S>]
         A              [<A, S>, <D, S>]
         D              [<D, S>]
Running: IDDFS
L = 2     Expanded     Queue
         S              [<S>]
         A              [<A, S>, <D, S>]
         B              [<B, A, S>, <D, A, S>, <D, S>]
         D              [<D, A, S>, <D, S>]
         D              [<D, S>]
         A              [<A, D, S>, <E, D, S>]
         E              [<E, D, S>]
Running: IDDFS
L = 3     Expanded     Queue
         S              [<S>]
         A              [<A, S>, <D, S>]
         B              [<B, A, S>, <D, A, S>, <D, S>]
         C              [<C, B, A, S>, <E, B, A, S>, <D, A, S>, <D, S>]
         E              [<E, B, A, S>, <D, A, S>, <D, S>]
         D              [<D, A, S>, <D, S>]
         E              [<E, D, A, S>, <D, S>]
         D              [<D, S>]
         A              [<A, D, S>, <E, D, S>]
         B              [<B, A, D, S>, <E, D, S>]
         E              [<E, D, S>]
         B              [<B, E, D, S>, <F, E, D, S>]
         F              [<F, E, D, S>]
Running: IDDFS
L = 4     Expanded     Queue
         S              [<S>]
         A              [<A, S>, <D, S>]
         B              [<B, A, S>, <D, A, S>, <D, S>]
         C              [<C, B, A, S>, <E, B, A, S>, <D, A, S>, <D, S>]
         E              [<E, B, A, S>, <D, A, S>, <D, S>]
         D              [<D, E, B, A, S>, <F, E, B, A, S>, <D, A, S>, <D, S>]
         F              [<F, E, B, A, S>, <D, A, S>, <D, S>]
         D              [<D, A, S>, <D, S>]
         E              [<E, D, A, S>, <D, S>]
         B              [<B, E, D, A, S>, <F, E, D, A, S>, <D, S>]
         F              [<F, E, D, A, S>, <D, S>]
         D              [<D, S>]
         A              [<A, D, S>, <E, D, S>]
         B              [<B, A, D, S>, <E, D, S>]
         C              [<C, B, A, D, S>, <E, B, A, D, S>, <E, D, S>]
         E              [<E, B, A, D, S>, <E, D, S>]
         E              [<E, D, S>]
         B              [<B, E, D, S>, <F, E, D, S>]
         A              [<A, B, E, D, S>, <C, B, E, D, S>, <F, E, D, S>]
         C              [<C, B, E, D, S>, <F, E, D, S>]
         F              [<F, E, D, S>]
         G              [<G, F, E, D, S>]
         goal reached! Time taken by IDDFS is 0.0006039142608642578 seconds
Running: UCS
         Expanded     Queue
         S              [0<S>]
         A              [3<A, S>, 4<D, S>]
         D              [4<D, S>, 7<B, A, S>, 8<D, A, S>]
         E              [6<E, D, S>, 7<B, A, S>, 8<D, A, S>, 9<A, D, S>]
         B              [7<B, A, S>, 8<D, A, S>, 9<A, D, S>, 10<F, E, D, S>, 11<B, E, D, S>]
         D              [8<D, A, S>, 9<A, D, S>, 10<F, E, D, S>, 11<B, E, D, S>, 11<C, B, A, S>, 12<E, B, A, S>]
         A              [9<A, D, S>, 10<E, D, A, S>, 10<F, E, D, S>, 11<B, E, D, S>, 11<C, B, A, S>, 12<E, B, A, S>]
         E              [10<E, D, A, S>, 10<F, E, D, S>, 11<B, E, D, S>, 11<C, B, A, S>, 12<E, B, A, S>, 13<B, A, D, S>]
         F              [10<F, E, D, S>, 11<B, E, D, S>, 11<C, B, A, S>, 12<E, B, A, S>, 13<B, A, D, S>, 14<F, E, D, A, S>, 15<B, E, D, A, S>]
         B              [11<B, E, D, S>, 11<C, B, A, S>, 12<E, B, A, S>, 13<B, A, D, S>, 13<G, F, E, D, S>, 14<F, E, D, A, S>, 15<B, E, D, A, S>]
         C              [11<C, B, A, S>, 12<E, B, A, S>, 13<B, A, D, S>, 13<G, F, E, D, S>, 14<F, E, D, A, S>, 15<A, B, E, D, S>, 15<B, E, D, A, S>, 15<C, B, E, D, S>]
         E              [12<E, B, A, S>, 13<B, A, D, S>, 13<G, F, E, D, S>, 14<F, E, D, A, S>, 15<A, B, E, D, S>, 15<B, E, D, A, S>, 15<C, B, E, D, S>]
         B              [13<B, A, D, S>, 13<G, F, E, D, S>, 14<D, E, B, A, S>, 14<F, E, D, A, S>, 15<A, B, E, D, S>, 15<B, E, D, A, S>, 15<C, B, E, D, S>, 16<F, E, B, A, S>]
         G              [13<G, F, E, D, S>, 14<D, E, B, A, S>, 14<F, E, D, A, S>, 15<A, B, E, D, S>, 15<B, E, D, A, S>, 15<C, B, E, D, S>, 16<F, E, B, A, S>, 17<C, B, A, D, S>, 18<E, B, A, D, S>]
         goal reached! Time taken by UCS is 0.001317739486694336 seconds
Running: GS
         Expanded     Queue
         S              [11.0<S>]
         D              [8.9<D, S>, 10.4<A, S>]
         E              [6.9<E, D, S>, 10.4<A, S>, 10.4<A, D, S>]
         F              [3.0<F, E, D, S>, 6.7<B, E, D, S>, 10.4<A, S>, 10.4<A, D, S>]
         G              [0.0<G, F, E, D, S>, 6.7<B, E, D, S>, 10.4<A, S>, 10.4<A, D, S>]
         goal reached! Time taken by GS is 0.00037026405334472656 seconds
Running: AS
         Expanded     Queue
         S              [11.0<S>]
         D              [12.9<D, S>, 13.4<A, S>]
         E              [12.9<E, D, S>, 13.4<A, S>]
         F              [13.0<F, E, D, S>, 13.4<A, S>, 17.7<B, E, D, S>]
         G              [13.0<G, F, E, D, S>, 13.4<A, S>, 17.7<B, E, D, S>]
         goal reached! Time taken by AS is 0.00034618377685546875 seconds
Running: HC
         Expanded     Queue
         S              [11.0<S>]
         D              [8.9<D, S>, 10.4<A, S>]
         E              [6.9<E, D, S>, 10.4<A, D, S>, 10.4<A, S>]
         F              [3.0<F, E, D, S>, 6.7<B, E, D, S>, 10.4<A, D, S>, 10.4<A, S>]
         G              [0.0<G, F, E, D, S>, 6.7<B, E, D, S>, 10.4<A, D, S>, 10.4<A, S>]
         goal reached! Time taken by HC is 0.00033283233642578125 seconds
Running: BMS
         Expanded     Queue
         S              [11.0<S>]
         A              [10.4<A, S>, 8.9<D, S>]
         D              [8.9<D, S>, 6.7<B, A, S>, 8.9<D, A, S>]
         B              [6.7<B, A, S>, 6.9<E, D, S>]
         E              [6.9<E, D, S>, 4.0<C, B, A, S>, 6.9<E, B, A, S>]
         C              [4.0<C, B, A, S>, 3.0<F, E, D, S>]
         F              [3.0<F, E, D, S>]
         G              [0.0<G, F, E, D, S>]
         goal reached! Time taken by BMS is 0.0003719329833984375 seconds


Sample output for second_graph.txt:

Please enter a file path... Then press enter... (Please note the Program will NOT validate the input file) second_graph.txt

Graph read from file:
id: O Heuristic: 380.0 Connections: ['Z', 'A']
id: Z Heuristic: 374.0 Connections: ['O', 'S']
id: A Heuristic: 253.0 Connections: ['O', 'S', 'F', 'R']
id: S Heuristic: 366.0 Connections: ['Z', 'A', 'T']
id: T Heuristic: 329.0 Connections: ['S', 'L']
id: F Heuristic: 178.0 Connections: ['A', 'G']
id: R Heuristic: 193.0 Connections: ['A', 'C', 'P']
id: L Heuristic: 244.0 Connections: ['T', 'M']
id: M Heuristic: 241.0 Connections: ['L', 'D']
id: D Heuristic: 242.0 Connections: ['M', 'C']
id: C Heuristic: 160.0 Connections: ['D', 'R', 'P']
id: P Heuristic: 98.0 Connections: ['R', 'C', 'G']
id: G Heuristic: 0.0 Connections: ['F', 'P', 'B', 'U']
id: B Heuristic: 77.0 Connections: ['G']
id: U Heuristic: 80.0 Connections: ['G', 'H', 'V']
id: H Heuristic: 151.0 Connections: ['U', 'E']
id: V Heuristic: 199.0 Connections: ['U', 'I']
id: E Heuristic: 161.0 Connections: ['H']
id: I Heuristic: 226.0 Connections: ['V', 'N']
id: N Heuristic: 234.0 Connections: ['I']
Press Enter to continue...
Running: DFS
         Expanded     Queue
         S              [<S>]
         A              [<A, S>, <T, S>, <Z, S>]
         F              [<F, A, S>, <O, A, S>, <R, A, S>, <T, S>, <Z, S>]
         G              [<G, F, A, S>, <O, A, S>, <R, A, S>, <T, S>, <Z, S>]
         goal reached! Time taken by DFS is 0.0002510547637939453 seconds
Running: BFS
         Expanded     Queue
         S              [<S>]
         A              [<A, S>, <T, S>, <Z, S>]
         T              [<T, S>, <Z, S>, <F, A, S>, <O, A, S>, <R, A, S>]
         Z              [<Z, S>, <F, A, S>, <O, A, S>, <R, A, S>, <L, T, S>]
         F              [<F, A, S>, <O, A, S>, <R, A, S>, <L, T, S>, <O, Z, S>]
         O              [<O, A, S>, <R, A, S>, <L, T, S>, <O, Z, S>, <G, F, A, S>]
         R              [<R, A, S>, <L, T, S>, <O, Z, S>, <G, F, A, S>, <Z, O, A, S>]
         L              [<L, T, S>, <O, Z, S>, <G, F, A, S>, <Z, O, A, S>, <C, R, A, S>, <P, R, A, S>]
         O              [<O, Z, S>, <G, F, A, S>, <Z, O, A, S>, <C, R, A, S>, <P, R, A, S>, <M, L, T, S>]
         G              [<G, F, A, S>, <Z, O, A, S>, <C, R, A, S>, <P, R, A, S>, <M, L, T, S>, <A, O, Z, S>]
         goal reached! Time taken by BFS is 0.0003609657287597656 seconds
Running: DLS
         Expanded     Queue
         S              [<S>]
         A              [<A, S>, <T, S>, <Z, S>]
         F              [<F, A, S>, <O, A, S>, <R, A, S>, <T, S>, <Z, S>]
         O              [<O, A, S>, <R, A, S>, <T, S>, <Z, S>]
         R              [<R, A, S>, <T, S>, <Z, S>]
         T              [<T, S>, <Z, S>]
         L              [<L, T, S>, <Z, S>]
         Z              [<Z, S>]
         O              [<O, Z, S>]
Running: IDDFS
L = 0     Expanded     Queue
         S              [<S>]
Running: IDDFS
L = 1     Expanded     Queue
         S              [<S>]
         A              [<A, S>, <T, S>, <Z, S>]
         T              [<T, S>, <Z, S>]
         Z              [<Z, S>]
Running: IDDFS
L = 2     Expanded     Queue
         S              [<S>]
         A              [<A, S>, <T, S>, <Z, S>]
         F              [<F, A, S>, <O, A, S>, <R, A, S>, <T, S>, <Z, S>]
         O              [<O, A, S>, <R, A, S>, <T, S>, <Z, S>]
         R              [<R, A, S>, <T, S>, <Z, S>]
         T              [<T, S>, <Z, S>]
         L              [<L, T, S>, <Z, S>]
         Z              [<Z, S>]
         O              [<O, Z, S>]
Running: IDDFS
L = 3     Expanded     Queue
         S              [<S>]
         A              [<A, S>, <T, S>, <Z, S>]
         F              [<F, A, S>, <O, A, S>, <R, A, S>, <T, S>, <Z, S>]
         G              [<G, F, A, S>, <O, A, S>, <R, A, S>, <T, S>, <Z, S>]
         goal reached! Time taken by IDDFS is 0.0001327991485595703 seconds
Running: UCS
         Expanded     Queue
         S              [0<S>]
         Z              [75<Z, S>, 118<T, S>, 140<A, S>]
         T              [118<T, S>, 140<A, S>, 146<O, Z, S>]
         A              [140<A, S>, 146<O, Z, S>, 229<L, T, S>]
         O              [146<O, Z, S>, 220<R, A, S>, 229<L, T, S>, 239<F, A, S>, 291<O, A, S>]
         R              [220<R, A, S>, 229<L, T, S>, 239<F, A, S>, 291<O, A, S>, 297<A, O, Z, S>]
         L              [229<L, T, S>, 239<F, A, S>, 291<O, A, S>, 297<A, O, Z, S>, 317<P, R, A, S>, 366<C, R, A, S>]
         F              [239<F, A, S>, 291<O, A, S>, 297<A, O, Z, S>, 299<M, L, T, S>, 317<P, R, A, S>, 366<C, R, A, S>]
         O              [291<O, A, S>, 297<A, O, Z, S>, 299<M, L, T, S>, 317<P, R, A, S>, 366<C, R, A, S>, 450<G, F, A, S>]
         A              [297<A, O, Z, S>, 299<M, L, T, S>, 317<P, R, A, S>, 362<Z, O, A, S>, 366<C, R, A, S>, 450<G, F, A, S>]
         M              [299<M, L, T, S>, 317<P, R, A, S>, 362<Z, O, A, S>, 366<C, R, A, S>, 377<R, A, O, Z, S>, 396<F, A, O, Z, S>, 450<G, F, A, S>]
         P              [317<P, R, A, S>, 362<Z, O, A, S>, 366<C, R, A, S>, 374<D, M, L, T, S>, 377<R, A, O, Z, S>, 396<F, A, O, Z, S>, 450<G, F, A, S>]
         Z              [362<Z, O, A, S>, 366<C, R, A, S>, 374<D, M, L, T, S>, 377<R, A, O, Z, S>, 396<F, A, O, Z, S>, 418<G, P, R, A, S>, 450<G, F, A, S>, 455<C, P, R, A, S>]
         C              [366<C, R, A, S>, 374<D, M, L, T, S>, 377<R, A, O, Z, S>, 396<F, A, O, Z, S>, 418<G, P, R, A, S>, 450<G, F, A, S>, 455<C, P, R, A, S>]
         D              [374<D, M, L, T, S>, 377<R, A, O, Z, S>, 396<F, A, O, Z, S>, 418<G, P, R, A, S>, 450<G, F, A, S>, 455<C, P, R, A, S>, 486<D, C, R, A, S>, 504<P, C, R, A, S>]
         R              [377<R, A, O, Z, S>, 396<F, A, O, Z, S>, 418<G, P, R, A, S>, 450<G, F, A, S>, 455<C, P, R, A, S>, 486<D, C, R, A, S>, 494<C, D, M, L, T, S>, 504<P, C, R, A, S>]
         F              [396<F, A, O, Z, S>, 418<G, P, R, A, S>, 450<G, F, A, S>, 455<C, P, R, A, S>, 474<P, R, A, O, Z, S>, 486<D, C, R, A, S>, 494<C, D, M, L, T, S>, 504<P, C, R, A, S>, 523<C, R, A, O, Z, S>]
         G              [418<G, P, R, A, S>, 450<G, F, A, S>, 455<C, P, R, A, S>, 474<P, R, A, O, Z, S>, 486<D, C, R, A, S>, 494<C, D, M, L, T, S>, 504<P, C, R, A, S>, 523<C, R, A, O, Z, S>, 607<G, F, A, O, Z, S>]
         goal reached! Time taken by UCS is 0.001363992691040039 seconds
Running: GS
         Expanded     Queue
         S              [366.0<S>]
         A              [253.0<A, S>, 329.0<T, S>, 374.0<Z, S>]
         F              [178.0<F, A, S>, 193.0<R, A, S>, 329.0<T, S>, 374.0<Z, S>, 380.0<O, A, S>]
         G              [0.0<G, F, A, S>, 193.0<R, A, S>, 329.0<T, S>, 374.0<Z, S>, 380.0<O, A, S>]
         goal reached! Time taken by GS is 0.00040602684020996094 seconds
Running: AS
         Expanded     Queue
         S              [366.0<S>]
         A              [393.0<A, S>, 447.0<T, S>, 449.0<Z, S>]
         R              [413.0<R, A, S>, 417.0<F, A, S>, 447.0<T, S>, 449.0<Z, S>, 671.0<O, A, S>]
         P              [415.0<P, R, A, S>, 417.0<F, A, S>, 447.0<T, S>, 449.0<Z, S>, 526.0<C, R, A, S>, 671.0<O, A, S>]
         F              [417.0<F, A, S>, 418.0<G, P, R, A, S>, 447.0<T, S>, 449.0<Z, S>, 526.0<C, R, A, S>, 671.0<O, A, S>]
         G              [418.0<G, P, R, A, S>, 447.0<T, S>, 449.0<Z, S>, 526.0<C, R, A, S>, 671.0<O, A, S>]
         goal reached! Time taken by AS is 0.0009942054748535156 seconds
Running: HC
         Expanded     Queue
         S              [366.0<S>]
         A              [253.0<A, S>, 374.0<Z, S>, 329.0<T, S>]
         F              [178.0<F, A, S>, 193.0<R, A, S>, 380.0<O, A, S>, 374.0<Z, S>, 329.0<T, S>]
         G              [0.0<G, F, A, S>, 193.0<R, A, S>, 380.0<O, A, S>, 374.0<Z, S>, 329.0<T, S>]
         goal reached! Time taken by HC is 0.00025582313537597656 seconds
Running: BMS
         Expanded     Queue
         S              [366.0<S>]
         A              [253.0<A, S>, 329.0<T, S>, 374.0<Z, S>]
         T              [329.0<T, S>, 178.0<F, A, S>, 380.0<O, A, S>, 193.0<R, A, S>]
         R              [193.0<R, A, S>, 0.0<G, F, A, S>]
         G              [0.0<G, F, A, S>, 160.0<C, R, A, S>, 98.0<P, R, A, S>]
         goal reached! Time taken by BMS is 0.0002949237823486328 seconds
