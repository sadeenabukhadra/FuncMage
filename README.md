# FuncMage
 This project takes us to discover and learn a bout the techniques of functional programming in python!

CONTENTS :
- [ex0](#EX0) : Lambda Sanctum - Master anonymous functions and lambda expressions
- ex1 : Higher Realm - Discover the power of higher-order functions
- ex2 : Memory Depths - Understand lexical scoping and closures
- ex3 : Ancient Library - Explore the functools module’s treasures
- ex4 : Master’s Tower - Create powerful decorators and class methods

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
