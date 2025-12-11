# Tandemloop Screening Test - Piyush Jain

This repository contains the solutions for the Stage-1 Screening Test.

## Language Used
**Python 3**

## File Descriptions
* **Problem-1.py**: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
    * **Goal:** To create a calculator which performs basic operations based on user inputs.
    * **Logic:** Created a `Calculator` function that takes two numbers and an operation string as input. It supports addition, subtraction, multiplication, and division with basic error handling (e.g., division by zero).

* **Problem-2.py**: Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]

  Output: (examples)
    1) input a = 1, then output : 1
    2) input a = 2, then output : 1, 3
    3) input a = 3, then output : 1, 3, 5
    4) input a = 4, then output : 1, 3, 5, 7
    .
    .
    5) input a = x, then output : 1, 3, 5, 7, .......
    * **Goal:** Generate the first `a` odd numbers.
    * **Logic:** Used the formula `i*2 +1` inside a loop to generate the sequence `1, 3, 5, 7...` up to the requested count.

* **Problem-3.py**: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
  Output: (examples)
    1) input a = 1, then output : 1
    2) input a = 2, then output : 1
    3) input a = 3, then output : 1, 3, 5
    4) input a = 4, then output : 1, 3, 5
    5) input a = 5, then output : 1, 3, 5, 7, 9
    6) input a = 6, then output : 1, 3, 5, 7, 9
    .
    .
    7) input a = x, then output : 1, 3, 5, 7, ........
    * **Goal:** Generate a series based on whether the input `a` is odd or even.
    * **Logic:** * If `a` is **odd**, it generates `a` terms.
        * If `a` is **even**, it reduces the count by 1 (`a-1`) and generates that many terms.
        * The series format remains the same as Problem 2 (odd numbers).
* **Problem-4.py**: Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
  (examples)
  input: [1,2,8,9,12,46,76,82,15,20,30]
  Output: 
    {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}.
    * **Goal:** Count how many numbers in a list are multiples of 1 through 9.
    * **Logic:** Used a nested loop approach. It iterates through numbers 1-9, and for each number, it scans the entire input list to count divisible matches, storing the result in a dictionary.

## 🚀 How to Run
1. Ensure Python 3 is installed.
2. Run any file using the command:
   ```bash
   python Problem-1.py