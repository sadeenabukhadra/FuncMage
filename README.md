# FuncMage
 This project takes us to discover and learn a bout the techniques of functional programming in python!

CONTENTS :
- [EX0](#EX0) : Lambda Sanctum - Master anonymous functions and lambda expressions
- [EX1](#EX1) : Higher Realm - Discover the power of higher-order functions
- [EX2](#EX2) : Memory Depths - Understand lexical scoping and closures
- [EX3](#EX3) : Ancient Library - Explore the functools module’s treasures
- [EX4](#EX4): Master’s Tower - Create powerful decorators and class methods

# EX0 
The idea of this exercise we learn a bout anonymous functions ( lambda ,filter, map) 

anonymous functions : a simple function without name(without def decleration).   

1) lambda : its anonymous function( a function that doesnt have a name ) that can take any number of arguments , but can only have one expression.
   
2) filter : a function that is used to extract elements from an iterable ( like a list ,tuple or set) that satisfy a given condition . it works by applying a function to each element and keeping only of those for which function returns True.
 - syntacs : filter( condition/function ,iterable/ input)
    - function -> test each element and if return ,True keep the element , if False discard the element.
    - iterable -> Any iterable (list,tuple set, etc).
    - Return Value: A filter object (an iterator), which can be converted into a list, tuple, set, etc.
      --- It returns a new iterable without modifying the original ---
     - when we use a lambda with a filter we write a lambda function directly without key. 

3) map : a function that applies a given function to each element of an iterable (list,tuple,set,etc)
and returns a map object (iterator). it sa higher-order function used for uniform element-wise transformation , anabling concise and effcient code.
 - syntacs :  map(function,iterable,...)
  - function :  the function to apply to every element of the iterable
  - iterable : one or more iterable objects (list, tuple) whose elements will be processed
  - ... : we can pass a multiple iterables objects if the function accepts multiple arguments.
  - for making it esier :map() with lambda -> We can use a lambda function instead of a custom function with map() to make code shorter and easier .

# EX1 
The idea of this exercise we learn a bout FIRST-CLASS CITIZENS , functions can behave like values (objects)

- FIRST-CLASS CITIZENS : these are  entities that support all operations availble to other entities in the programming language( in python First-Class Citizens (or First-Class Objects) means that functions are treated like any other object (such as integers, strings, or lists)) . it pased as arguments , returned from functions , asssigned to variables and sorted in data structures such as list in the last function of this exercise.
     1)Assigning Functions to Variables 
     2)Passing Functions as Arguments
     3)Returning Functions from Functions

- Key Properties of First-Class Citizens:
  -  Assignment ? Can be assigned to variables
  - Argument passing ? Can be passed as function arguments
  - Return values ? Can be returned from functions
  - Storage ? Can be stored in data structures like lists or dictionaries
  - Runtime creation ? Can be created at runtime 
- Callable : its a type hint of function that imports from collictions.abc lib

1) How do higher-order functions enable code reuse and composition?

Higher-order functions improve code reuse by allowing functions to be passed as arguments or returned as results. This means the same function can be reused with different behaviors without rewriting code.

They also enable function composition, where multiple small functions are combined to build more complex behavior. Instead of writing large blocks of code, we can build systems by connecting simple, reusable functions.

-In this project:
   - spell_combiner reuses two spells together
   - power_amplifier reuses a spell but modifies its input
   - conditional_caster reuses a spell only when a condition is met
   - spell_sequence reuses multiple spells in order
 2) What makes functions “first-class citizens” in Python?
Functions are called first-class citizens because they can be treated like any other object in Python. This means they can:

Be assigned to variables
Be passed as arguments to other functions
Be returned from functions
Be stored in data structures like lists or dictionaries

 Example from the project:
We pass functions like flower and tree into other functions such as spell_combiner and spell_sequence.

 3) From which package is Callable recommended? 
   Callable is imported from the typing module:
     from typing import Callable
    It is used for type hinting to specify that a variable or argument is a function.

 5) What is the purpose of callable()?
   - callable() is a built-in Python function that checks whether an object can be called like a function.

Example:
callable(flower)   # True
callable(10)       # False

👉 It is used to verify if an object behaves like a function.

- callable : it ckecks if an object is callable (return True or False )
     


 
