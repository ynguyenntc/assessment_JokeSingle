# Challenge: Mini - Max Sum

## **Table of Content**

- [Challenge: Mini - Max Sum](#challenge-mini---max-sum)
  - [**Table of Content**](#table-of-content)
  - [**Problem**](#problem)
    - [**Input**](#input)
    - [**Output**](#output)
    - [**Explanation**](#explanation)
    - [**Evaluation Criterion**](#evaluation-criterion)
  - [**Solution**](#solution)

## **Problem**
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

**Ex:**

**arr = [1, 3, 5, 7, 9]**

Our minimum sum is 1 + 3 + 5 + 7 = 16

and

Our maximum sum is 3 + 5 + 7 + 9 = 24

We would print: **16 24** 

### **Input**
A single line of five space-separated intergers

Sample input: **1 2 3 4 5**

### **Output**
Print two space-separated long integers denoting the respective minimum and maximum values that can
be calculated by summing exactly four of the five integers.

(The output can be greater than a 32 bit
integer.)

Sample output:  **10 14**

### **Explanation**

Our initial numbers are 1, 2, 3, 4 and 5. We can calculate the following sums using four of the five
integers:

* If we sum everything except 1, our sum is: 2 + 3 + 4 + 5 = 14

* If we sum everything except 2, our sum is: 1 + 3 + 4 + 5 = 13

* If we sum everything except 3, our sum is: 1 + 2 + 4 + 5 = 12

* If we sum everything except 4, our sum is: 1 + 2 + 3 + 5 = 11

* If we sum everything except 5, our sum is: 1 + 2 + 3 + 4 = 10

### **Evaluation Criterion**

Coder must finished at least 50% of the requirements to be given a pass. Evaluation will be based on speed, code quality and critical thinking. Grading is pessimistic - You will not get an A unless you clearly show you are an A. Some signs of an A is not enough.

The general grading is such that

| Grade | What it means|
| :---: | :---: |
|A| Above our standard|
|B| Met our standard|
|C| Not good Enough|
|D| This is seriously not good|
|E| Why should we hire you?|

The evaluation form for a coder is as below:

*Name:*

*Date of Evaluation:*

*Completeness of project (%):*

*Bonus completeness (%):*

**Overall Grade:**

 * **Git Commits**
  
    + A – Great commit messages and structure
    + B – Good commit messages and structure
    + C – Okay commit messages and structure
    + D – Poor commit messages and strucuture
    + E – No use of git

* **Test Coverage**

  + A – Critical paths are covered
  + B – Some critical paths are covered
  + C – Few critical paths are covered
  + D – Little or no test cases
  + E – No test cases!!!

* **Bouns*
  + Count total of array
  + Find min in array
  + Find max in array
  + Find even elements in array
  + Find odd elements in array

## **Solution**

Language Programming: Python [*link*](#algorithm\Python\code.py)






