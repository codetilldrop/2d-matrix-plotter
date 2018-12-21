# 2d-matrix-plotter

## Matrices

Matrices (plural for matrix) is a mathematical property/structure where lists of numbers are stored. They are used to perform a variety of important tasks in maths. 

A matrix will have a set number of complete rows and columns with numbers in it. 
(https://cdn.kastatic.org/googleusercontent/9XeqQ2stwpGbXuli1TWSbnHQwITfrYV_AtmjMFEtQZbAo9VvWQ0KYNBnyRx5x9Ekpwh_Pdwzu4dC6b3Y0Wb0Qsu5)

## Valid Matrices

A user of the program can enter a matrix into matrix.txt. To enter a matrix, it's form can look like the following

```
[
  1 0 1
  1 0 1
  1 1 1
]
```

As you can see, to write a valid matrix which can be parsed by the program, two corresponding square brackets need to be open with values which are spaced inside. 

## Representation of 2D shapes in a Matrix

To explain this concept, the following matrix will serve as
an example

```
[
  0 1
  1 1
]
```

### Referencing Matrix Indexes

Matrix indexes are referenced like the following.

aᵢⱼ where i is a row index and j is a column index.

Example: a₍₁,₁₎ = 0

### How the Plotting Works

Now that we know how Matrix indexes are referenced and how to represent one, it is time to get into the computer-side of matters


