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

1) How do higher-order functions enable code reuse and composition?
   - Higher-order functions improve code reuse by allowing functions to be passed as arguments or returned as results. This means the same function can be reused
     with different behaviors without rewriting code.
     They also enable function composition, where multiple small functions are combined to build more complex behavior. Instead of writing large blocks of code,
     we can build systems by connecting simple, reusable functions.

     -In this project:
     
        - spell_combiner reuses two spells together
     
        - power_amplifier reuses a spell but modifies its input
   
        - conditional_caster reuses a spell only when a condition is met
        
        - spell_sequence reuses multiple spells in order
          
2) What makes functions “first-class citizens” in Python?
   - Functions are called first-class citizens because they can be treated like any other object in Python. This means they can:
      - Be assigned to variables
      - Be passed as arguments to other functions
      - Be returned from functions
      - Be stored in data structures like lists or dictionaries
     
     Example from the project: -> We pass functions like flower and tree into other functions such as spell_combiner and spell_sequence.

3) From which package is Callable recommended? 
    - Callable is imported from the typing module or  from collictions.abc module:
          from typing import Callable ,it is used for type hinting to specify that a variable or argument is a function.
      

 4) What is the purpose of callable()?
    - callable() is a built-in Python function that checks whether an object can be called like a function (it ckecks if an object is callable (return True or False ).
    - Example:
         callable(flower)   # True
         callable(10)       # False

# EX2
The idea of this exercise is learning about Lexical Scoping and Closures in python.
- Lexical scoping (static scoping ) : detemine the scope of variable based on the structure of the  program code .
     - lexical : based on the position of writing code .
     - scope : it is where the variable can be accessed (the position of variable that can function access).
thae python has four scope levels so the tracking follows LEGB rule.
    - NOTE:The tracking ends when the variable is found at its corresponding level.
1) Local : This scope contains the names that you define inside the function .These names are only visible from within the function.

2) Enclosing (nonlocal scope) : This a scope that exists only for nested functions and is defined by the outer or enclosing function.The names in the enclosing scope are visible from the code of the inner and outer functions.
    - nonlocal name: its mean the name is neither local nor global that means its visible from both the outer and inner functions.

3) Global(module scope): This scope contains all of the names that you define at the top level of a script or module. Names in this scope are visible from everywhere in your code.

4) Built-in : This scope contains names such as built-in functions, exceptions, and other attributes that are built into Python. Names in this scope are also available from everywhere in your code.

- Clouser : function + remmebered variables

# EX3
This exercise we learn a bout functiontools module

Functiontools module : it offers a collecyion of tools that simplify working with functions and callable objects . 
- WHY we use it ?
     
     - simplifies functional programming
            - by using reduce() and decoratores functions.

        - reduce() : a functon from functiontools that applies a function cumulatively to the elements of an iterable and returns a single final value.
  
        - Syntax  -> reduce (finction, itrable)
         
        - Parameters:

           - function: A function that takes two arguments and returns a single value.
       
            
            
            
            - iterable: The sequence to be reduced (list, tuple, etc.).
                  
           
            
            -  initializer (optional): A starting value that is placed before first element.
     
     
     
     - improve performance through memoization
    
         
         
         - by using lura_cache() -> stores the results of excpensive calling functions and reuses them when the same result accure again.
   
     
     
     
     - create specialized functions


        - by using partial() : its class that
     
     
     
     - reduces boilerplate code with decoratore
     

          - by decotratore
     

     - enhances code readability and reuseability
     

          - by enabling clearner , more modular and maintainable solutions.


     - preserve function metedata
       

         - by using wrap() : it means write functions that take function as arguments then define an return new functions. its a decorator used when creating costume decoratores.
        
           
               - Syntacs -> @wrap(func).


               - note : its epuivelience -> wrapper.__name__ = func .__name__
 # EX4
This exercise demonstrates advanced usage of python decorators, higher-order functions and class static methods
-a decotator : is a function that 
1) take another function as input
2) add extra behavior
3) returns a new modified function
          
           
               @decoratot
               def func():
                   pass
Its equivelce to :

                     func= decrator(func)

- Function wrapping means: Taking an original function and placing it inside another function (called a wrapper) to add extra behavior without changing the original function.
 
   - Wrapping = putting a function inside another function to control how it runs

- original function


          def say_hi():
              print("hi")

- wrapped function

         def wrapped():
             print("smile")
             say_hi()
             print("wave hand")
         #run
         wrapper()
  
  
   
|decrator | decrator factory |
|---------|-----------------|
|no argument|takes arguments|


#  Decorators in Python – Clear Breakdown

## 1. Normal Decorator (No Arguments)

A normal decorator wraps a function directly without taking any extra parameters.

### Example:

         def decorator(func):
           def wrapper():
             print("Before")
             func()
             print("After")
           return wrapper
### Usage:
       ```python
          @decorator
          def hello():
              print("Hi")
### Key Points:
- No parameters


- Directly wraps the function

- Simple use case

 2) Decorator Factory (Parameterized Decorator)

    A decorator factory is a function that takes arguments and returns a decorator.


 - What is parameterized decrator ?

  A parameterized decorator is a decorator that accepts arguments and uses them to customize how the wrapper behaves.
   
      def decorator_factory(x):
          def decorator(func):
             def wrapper():
                 print(x)
                 func()
              return wrapper
          return decorator
usage:
                
               @decorator_factory(10)
               def hello():
                 print("Hi")

- Summury :


Decorator = function wrapper


Decorator factory = creates decorators
#
         

            
