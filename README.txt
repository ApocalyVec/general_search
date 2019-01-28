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


Sample output for graph.txt
Sample output for second_graph.txt

  Depth First Search
  Expanded	Queue
  S		[<S>]
  A		[<A,S> <D,S>]
  B		[<B,A,S> <D,A,S> <D,S>]
  C		[<C,B,A,S> <E,B,A,S> <D,A,S> <D,S>]
  E		[<E,B,A,S> <D,A,S> <D,S>]
  D		[<D,E,B,A,S> <F,E,B,A,S> <D,A,S> <D,S>]
  F		[<F,E,B,A,S> <D,A,S> <D,S>]
  G		[<G,F,E,B,A,S> <D,A,S> <D,S>]
  Goal has been found!

  Breadth First Search
  Expanded	Queue
  S		[<S>]
  A		[<A,S> <D,S>]
  D		[<D,S> <B,A,S> <D,A,S>]
  B		[<B,A,S> <D,A,S> <A,D,S> <E,D,S>]
  D		[<D,A,S> <A,D,S> <E,D,S> <C,B,A,S> <E,B,A,S>]
  A		[<A,D,S> <E,D,S> <C,B,A,S> <E,B,A,S> <E,D,A,S>]
  E		[<E,D,S> <C,B,A,S> <E,B,A,S> <E,D,A,S> <B,A,D,S>]
  C		[<C,B,A,S> <E,B,A,S> <E,D,A,S> <B,A,D,S> <B,E,D,S> <F,E,D,S>]
  E		[<E,B,A,S> <E,D,A,S> <B,A,D,S> <B,E,D,S> <F,E,D,S>]
  E		[<E,D,A,S> <B,A,D,S> <B,E,D,S> <F,E,D,S> <D,E,B,A,S> <F,E,B,A,S>]
  B		[<B,A,D,S> <B,E,D,S> <F,E,D,S> <D,E,B,A,S> <F,E,B,A,S> <B,E,D,A,S> <F,E,D,A,S>]
  B		[<B,E,D,S> <F,E,D,S> <D,E,B,A,S> <F,E,B,A,S> <B,E,D,A,S> <F,E,D,A,S> <C,B,A,D,S> <E,B,A,D,S>]
  F		[<F,E,D,S> <D,E,B,A,S> <F,E,B,A,S> <B,E,D,A,S> <F,E,D,A,S> <C,B,A,D,S> <E,B,A,D,S> <A,B,E,D,S> <C,B,E,D,S>]
  D		[<D,E,B,A,S> <F,E,B,A,S> <B,E,D,A,S> <F,E,D,A,S> <C,B,A,D,S> <E,B,A,D,S> <A,B,E,D,S> <C,B,E,D,S> <G,F,E,D,S>]
  F		[<F,E,B,A,S> <B,E,D,A,S> <F,E,D,A,S> <C,B,A,D,S> <E,B,A,D,S> <A,B,E,D,S> <C,B,E,D,S> <G,F,E,D,S>]
  B		[<B,E,D,A,S> <F,E,D,A,S> <C,B,A,D,S> <E,B,A,D,S> <A,B,E,D,S> <C,B,E,D,S> <G,F,E,D,S> <G,F,E,B,A,S>]
  F		[<F,E,D,A,S> <C,B,A,D,S> <E,B,A,D,S> <A,B,E,D,S> <C,B,E,D,S> <G,F,E,D,S> <G,F,E,B,A,S> <C,B,E,D,A,S>]
  C		[<C,B,A,D,S> <E,B,A,D,S> <A,B,E,D,S> <C,B,E,D,S> <G,F,E,D,S> <G,F,E,B,A,S> <C,B,E,D,A,S> <G,F,E,D,A,S>]
  E		[<E,B,A,D,S> <A,B,E,D,S> <C,B,E,D,S> <G,F,E,D,S> <G,F,E,B,A,S> <C,B,E,D,A,S> <G,F,E,D,A,S>]
  A		[<A,B,E,D,S> <C,B,E,D,S> <G,F,E,D,S> <G,F,E,B,A,S> <C,B,E,D,A,S> <G,F,E,D,A,S> <F,E,B,A,D,S>]
  C		[<C,B,E,D,S> <G,F,E,D,S> <G,F,E,B,A,S> <C,B,E,D,A,S> <G,F,E,D,A,S> <F,E,B,A,D,S>]
  G		[<G,F,E,D,S> <G,F,E,B,A,S> <C,B,E,D,A,S> <G,F,E,D,A,S> <F,E,B,A,D,S>]
  Goal has been found!

  Depth Limited Search (Depth Limit = 2)
  Expanded	Queue
  S		[<S>]
  A		[<A,S> <D,S>]
  B		[<B,A,S> <D,A,S> <D,S>]
  D		[<D,A,S> <D,S>]
  D		[<D,S>]
  A		[<A,D,S> <E,D,S>]
  E		[<E,D,S>]
  Failed to find goal!

  Iterative Deepening Search
  Expanded	Queue
  L = 0
  S		[<S>]
  L = 1
  S		[<S>]
  A		[<A,S> <D,S>]
  D		[<D,S>]
  L = 2
  S		[<S>]
  A		[<A,S> <D,S>]
  B		[<B,A,S> <D,A,S> <D,S>]
  D		[<D,A,S> <D,S>]
  D		[<D,S>]
  A		[<A,D,S> <E,D,S>]
  E		[<E,D,S>]
  L = 3
  S		[<S>]
  A		[<A,S> <D,S>]
  B		[<B,A,S> <D,A,S> <D,S>]
  C		[<C,B,A,S> <E,B,A,S> <D,A,S> <D,S>]
  E		[<E,B,A,S> <D,A,S> <D,S>]
  D		[<D,A,S> <D,S>]
  E		[<E,D,A,S> <D,S>]
  D		[<D,S>]
  A		[<A,D,S> <E,D,S>]
  B		[<B,A,D,S> <E,D,S>]
  E		[<E,D,S>]
  B		[<B,E,D,S> <F,E,D,S>]
  F		[<F,E,D,S>]
  L = 4
  S		[<S>]
  A		[<A,S> <D,S>]
  B		[<B,A,S> <D,A,S> <D,S>]
  C		[<C,B,A,S> <E,B,A,S> <D,A,S> <D,S>]
  E		[<E,B,A,S> <D,A,S> <D,S>]
  D		[<D,E,B,A,S> <F,E,B,A,S> <D,A,S> <D,S>]
  F		[<F,E,B,A,S> <D,A,S> <D,S>]
  D		[<D,A,S> <D,S>]
  E		[<E,D,A,S> <D,S>]
  B		[<B,E,D,A,S> <F,E,D,A,S> <D,S>]
  F		[<F,E,D,A,S> <D,S>]
  D		[<D,S>]
  A		[<A,D,S> <E,D,S>]
  B		[<B,A,D,S> <E,D,S>]
  C		[<C,B,A,D,S> <E,B,A,D,S> <E,D,S>]
  E		[<E,B,A,D,S> <E,D,S>]
  E		[<E,D,S>]
  B		[<B,E,D,S> <F,E,D,S>]
  A		[<A,B,E,D,S> <C,B,E,D,S> <F,E,D,S>]
  C		[<C,B,E,D,S> <F,E,D,S>]
  F		[<F,E,D,S>]
  G		[<G,F,E,D,S>]
  Goal has been found!

  Uniform Cost Search
  Expanded	Queue
  S		[0<S>]
  A		[3<A,S> 4<D,S>]
  D		[4<D,S> 7<B,A,S> 8<D,A,S>]
  E		[6<E,D,S> 7<B,A,S> 8<D,A,S> 9<A,D,S>]
  B		[7<B,A,S> 8<D,A,S> 9<A,D,S> 10<F,E,D,S> 11<B,E,D,S>]
  D		[8<D,A,S> 9<A,D,S> 10<F,E,D,S> 11<B,E,D,S> 11<C,B,A,S> 12<E,B,A,S>]
  A		[9<A,D,S> 10<E,D,A,S> 10<F,E,D,S> 11<B,E,D,S> 11<C,B,A,S> 12<E,B,A,S>]
  E		[10<E,D,A,S> 10<F,E,D,S> 11<B,E,D,S> 11<C,B,A,S> 12<E,B,A,S> 13<B,A,D,S>]
  F		[10<F,E,D,S> 11<B,E,D,S> 11<C,B,A,S> 12<E,B,A,S> 13<B,A,D,S> 14<F,E,D,A,S> 15<B,E,D,A,S>]
  B		[11<B,E,D,S> 11<C,B,A,S> 12<E,B,A,S> 13<B,A,D,S> 13<G,F,E,D,S> 14<F,E,D,A,S> 15<B,E,D,A,S>]
  C		[11<C,B,A,S> 12<E,B,A,S> 13<B,A,D,S> 13<G,F,E,D,S> 14<F,E,D,A,S> 15<A,B,E,D,S> 15<B,E,D,A,S> 15<C,B,E,D,S>]
  E		[12<E,B,A,S> 13<B,A,D,S> 13<G,F,E,D,S> 14<F,E,D,A,S> 15<A,B,E,D,S> 15<B,E,D,A,S> 15<C,B,E,D,S>]
  B		[13<B,A,D,S> 13<G,F,E,D,S> 14<D,E,B,A,S> 14<F,E,D,A,S> 15<A,B,E,D,S> 15<B,E,D,A,S> 15<C,B,E,D,S> 16<F,E,B,A,S>]
  G		[13<G,F,E,D,S> 14<D,E,B,A,S> 14<F,E,D,A,S> 15<A,B,E,D,S> 15<B,E,D,A,S> 15<C,B,E,D,S> 16<F,E,B,A,S> 17<C,B,A,D,S> 18<E,B,A,D,S>]
  Goal has been found!

  Greedy Search
  Expanded	Queue
  S		[11<S>]
  D		[8.9<D,S> 10.4<A,S>]
  E		[6.9<E,D,S> 10.4<A,S> 10.4<A,D,S>]
  F		[3<F,E,D,S> 6.7<B,E,D,S> 10.4<A,S> 10.4<A,D,S>]
  G		[0<G,F,E,D,S> 6.7<B,E,D,S> 10.4<A,S> 10.4<A,D,S>]
  Goal has been found!

  A* Search
  Expanded	Queue
  S		[11<S>]
  D		[12.9<D,S> 13.4<A,S>]
  E		[12.9<E,D,S> 13.4<A,S>]
  F		[13<F,E,D,S> 13.4<A,S> 17.7<B,E,D,S>]
  G		[13<G,F,E,D,S> 13.4<A,S> 17.7<B,E,D,S>]
  Goal has been found!

  Hill Climbing Search
  Expanded	Queue
  S		[11<S>]
  D		[8.9<D,S>]
  E		[6.9<E,D,S>]
  F		[3<F,E,D,S>]
  G		[0<G,F,E,D,S>]
  Goal has been found!

  Beam Search (w = 2)
  Expanded	Queue
  S		[11<S>]
  A		[10.4<A,S> 8.9<D,S>]
  D		[8.9<D,S> 6.7<B,A,S> 8.9<D,A,S>]
  B		[6.7<B,A,S> 6.9<E,D,S>]
  E		[6.9<E,D,S> 4<C,B,A,S> 6.9<E,B,A,S>]
  C		[4<C,B,A,S> 3<F,E,D,S>]
  F		[3<F,E,D,S>]
  G		[0<G,F,E,D,S>]
  Goal has been found!
