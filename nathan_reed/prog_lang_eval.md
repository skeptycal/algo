# Programming Language Evaluation

A list of simple tasks to perform when learning or evaluating a new language. Each of these should be able to be completed in a few hours, and will help to get the feel of the language and its standard libraries. A well-rounded set of evaluation tasks will help ensure all parts of the language are exercised. You might also write some tests to demonstrate implementation correctness.

## Basics

1. Hello world
1. Read lines from a text file and output them in sorted order
1. Read numbers from a text file and output the mean and standard deviation
1. Given an amount of money and a list of coin denominations provided on the command line, output all the possible ways to make change
1. Port a random number generator such as [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)

## General

1. Parse configuration files in a simple text format such as .ini and build a key-value store
1. Simple regex matcher
1. Port a compression lib such as [LZ4](https://github.com/Cyan4973/lz4)
1. Interactive tic-tac-toe game with [minimax AI](https://en.wikipedia.org/wiki/Minimax)
1. Recursive [maze generation](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
1. [Maze solving](https://en.wikipedia.org/wiki/Maze_solving_algorithm)

## Data Structures

All these should be generic (compile-time parameterized by element type) and constructor/destructor-safe, if applicable.

1. Dynamic array
1. Intrusive linked list
1. Open addressing hash table
1. B-tree
1. Slab allocator for fixed-sized items
1. Chunk-linear allocator (not destructor-safe)
1. Intrusive reference counting, with strong and weak references

## Concurrency

1. Parallel map
1. Producer/consumer threads with semaphores
1. Lock-free append buffer
1. Work-stealing thread pool
1. HTTP server with multithreaded request handling and caching

## Graphics

1. Generate an image from a simple mathematical function and output it as a .bmp (bonus points for SIMD evaluation)
1. Implement Bresenham's line-drawing algorithm
1. Implement a simple vector/matrix math library
1. Port [Perlin's improved noise](http://mrl.nyu.edu/~perlin/noise/)
1. Port [stb_image_resize.h](https://github.com/nothings/stb/blob/master/stb_image_resize.h)
1. Recursive raytracer with dynamic-dispatch shapes (e.g. spheres and boxes) and materials (e.g. diffuse, shiny, emissive)

## Realtime

1. Realtime 2D particle system with a complex flow field, using SDL or similar (bonus points for SIMD evaluation)
1. Simple realtime 3D renderer that loads an .obj mesh and draws it using DX/GL
1. Simple realtime audio mixer that tracks one-shot and looping sounds, with different volume and pan settings

## GUI

1. Simple calculator, with buttons for digits and operations
1. GUI version of the tic-tac-toe game above
1. Simple file system explorer, with tree view for directories and list view for files, showing metadata such as file size and mod date
1. Simple [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) app for a text localization database, storing Unicode strings identified by an integer ID and a language code
1. Simple image viewer that allows you to zoom in and out, and shows you the RGB color of a pixel when you mouse over it

## Compilers

1. Parse and evaluate arithmetic expressions like `(1 + 2) * 3` using [Dijkstra's shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)
1. String interning dictionary
1. Recursive-descent parser that builds an AST for a simple language, with good error messages
1. Interpreter for a simple language

## Metaprogramming

1. Allocator that infers the correct size and alignment from the type to allocate
1. Programmatically generate a compile-time-constant integer value with every _n_​th bit set, parameterized by _n_.
1. Programatically unroll a loop, given a compile-time-constant number of iterations
1. Create a text formatting function that recognizes argument types, e.g. `print("Foo: {0}", foo)` does the right thing whether `foo` is an int, float, string, etc.
1. Map strings to types, i.e. user inputs "Foo" and you create a Foo object
1. Given a regular expression, programmatically generate (at compile time) code that searches that regular expression efficiently
1. Given a set of command line parameters, programmatically generate (at compile time) code that parses the parameters into variables
1. Programatically generate bindings for a scripting language (e.g. Python or Lua) for a given set of functions or methods
