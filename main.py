                                                                                    #""" Algorithms """#
""" The most important term of algorithm is while you making a program you can have thousand ways to solve it but if you want to use the shortest and the correct path or the most convenient path you have to use algorithm. Algorithm has two qualities: 1) Correctness 2) Efficiency """
""" Correctness: When you are making a program you use the shortest path but the program does not run because it was the shortest path not the correct path. So you have to make sure that you are using the correct path to solve the code or make the program. """
""" Efficiency: You have chosen the correct path but you didn't choose the efficient path the code will run or the program will work but the program or the code didn't meet the rules of algorithm. So you have to select the faster and the efficient path to solve the code or make the program. """
""" Remember that a good Algorithm gives a correct and efficient solution. """



                                                                                    #""" Pseudocode """#
""" Before writing the actual code with a programming language, a lot of people write the steps in English (natural language). This lines/steps are called Pseudocode. it's a concept about code to help a programmer think about steps. Pseudocode is an easier way to solve the problem. """



                                                                                   #""" Linear Search """#
""" Search algorithm is used to find elements. There might be a better way to search based on the condition of the list or the elements inside the list. Searching is as simple as finding a number in a list. If you are searching an element in a tree data structure or a dictionary the process of searching will be different. So, Algorithm to find an element is called Search Algorithm """

""" THis search algorithm progress one step forward at a time. And will always take the same amount of time to move forward while searching for an element. This means it will take a linear amount of time if you change the number of elements of the list. That's why it is called the Linear Search. """

nums = [10, 20, 90, 34, 88, 234, 235, 99, 100]
for i in nums:
      if i == 99:
            print('I have got the number', i)
print('\n\n')



                                                                                   #""" Binary Search """#
""" Divide & Conquer: One day you went to a house and there were 11 doors to get outside. Suddenly you had to go out and the owner of the house said that only the 10th door is open to get out. So you went to the place where the doors were at. As you were in a rush you couldn't think where the 10th door will be. So you went to the middle door means the 6th door. Though you were in a rush still you knew that the 10th door will be after the 6th door so you didn't go left. You went to the right and again hitted on the middle door means the 9th door which was closed. You again thought about it as you are in the 9th door the 10th door will be after it. And you went to the middle of the right side and hitted the opened door means the 10th door. You have used the Divide & Conquer rule here. You divided the left side and never visited the left side and only went to the right side. Divide & Conquer makes a solution better. """

""" Binary Search: The reason it called the Binary Search because it divides the search space into two equal parts. And choose one to continue to search and ignore the other part. Binary means two and here you are breaking down the list in two parts and choosing one part. To find the middle of two positions, you just find the average of the 'min' and the 'max'. Then you retrive the element in mid position. """
""" Right Side: If the element you are looking for is bigger than the mid element, you know the element you are looking for will be on the higher side.  """
""" Left Side: If the element you are looking for is smaller than the mid element, you know the element you are looking for will be on the lower side. """

""" Floor Division: Python has a special operator called floor division (//). 5 // 2 = 2 (It is flooring the number) """

""" Binary search only works in a sorted list. """

def binary_search(list, find_value):
      low = 0
      high = len(list)
      print(low, high)

      while low <= high:
            mid = (low + high) // 2
            if list[mid] < find_value:
                  low = mid
            elif list[mid] > find_value:
                  high = mid
            else:
                  return mid

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
searching = binary_search(nums, 60)
print(searching)
print('\n\n')



                                                                                       #""" Recursion """#
""" If a function calls itself it is called a recursive function. It is called recursive because it recursively calls itself. Recursion could make a complex problem simple. Recursion have two parts: 1) A stopping condition or base condition 2) Call the function itself. """

""" Iterative Factorial """
""" Explanation of below code:  """

def factorial(n):
      fact = 1 
      for i in range(1, n+1):
            fact = fact * i
      return fact
print(factorial(10))

""" Recursive Factorial """
""" Explanation of below code: You can see that we have passed a parameter which is 4 and it is bigger than 1 so if condition won't work after than it goes to else and the value of n is 4 as we are seeing the factorial(n-1) part the function will work again here and the value of n will be 3 there 3 * 2 is 6 and 4 * 6 is 24.. So the factorial of 4 is 24 """

def factorial(n):
      if n <= 1:
            return 'Siam'
      else:
            return n * factorial(n - 1)

print(factorial(1))
print('\n\n')



                                                                                    #""" Time Complexity """#
""" Two pieces of code might do the same thing. However, one could be faster and another could be slower. The efficiency is the measure of the time taken by an algorithm while running. The comparison of time to measure the efficiency of an algorithm is called Time Complexity. """

""" To measure the time complexity you need two things: 1) The input size 2) The growth rate. """

""" When the time complexity changes linearly with the change of the number of input elements, the algorithm complexity is called O(n). It is read as 'Ohh an'. The time complexity O(n) has two parts: 1) Input size 'n' 2) Growth rate 'O'. A for loop has O(n) time complexity. """

""" The time complexity of a nested loop is 'O(n^2)'. It is read as ohh an square. If you increase one element in the input list, the time will increase by a square of elements. This is called Quadratic Time Complexity """



                                                                                     #""" Swap Variable """#
""" This swap variable concept is easy. Just think that you want mango juice and your brother wants orange juice. Forgetfully your mom gave you orange juice in your glass and mango juice in your brothers' glass. now if she wants to give you mango juice in your glass she have to take another glass (a temporary glass) so that she can put that orange juice in that temporary glass and then that mango juice in your glass. after that she will put back that orange juice in your brothers' glass. That's how she swapped the juices. Like the example below, """

yourJuice = 'Orange'
brotherJuice = 'Mango'
print('You got:', yourJuice, '\nBrother got:', brotherJuice)
print('\n')
tempGlass = yourJuice
yourJuice = brotherJuice
brotherJuice = tempGlass
print('You got:', yourJuice, '\nBrother got:', brotherJuice)
print('\n\n')



                                                                                   #""" Range of Numbers """#
""" If you write range(8). This range of numbers will stop at 8. You will see numbers from 0 - 7. If you write range(n). You will see numbers from 0 to n-1. Because it will stop at n. By default the range will start from 0. If you want the range start from another number other than 0, you will pass two parameters to the range function. """    

for i in range(1, 20):
      print('i =', i)
print('\n\n')



                                                                                     #""" Bubble Sort """#
""" Bubble sort is the simplest sorting algorithm. The main concept is: 1) Compare two adjacent elements, 2) If the first item is bigger than the second item swap it, 3) Run the loop for n-1 items, 4) Keep doing it for all the elements.  """

def bubbleSort(list):
      n = len(list)
      for i in range(n):
            for j in range(n - 1):
                  if list[j] > list[j + 1]:
                        temp = list[j]
                        list[j] = list[j + 1]
                        list[j + 1] = temp
      return list

""" Testing """
nums = [35, 8, 23, 14, 65, 20, 11, 99, 69]
sortedNums = bubbleSort(nums)
print(sortedNums)
print('\n\n')



                                                                                   #""" Selection Sort """#
""" The selection sort workflow is like this, 1) For each position, loop the elements on the right, 2) Find the minimum numbers on the right, 3) Swap this two elements (Bring the minimum element to the current position and send the current element to the min element position), 4) Repeat steps from 1 to 3. """                                                                                   
""" The outer loop is very simple. You run a simple for loop for all elements. Hence you will run it for range. """
""" Inside the for loop, you will write another for loop to find out the minimum m=number. In simple cases, you will start with the first index and keep comparing all the way towards the end. """
""" Put the inner loop inside the outer loop. The inner loop will start from the index (i + 1). Then check on the right side to find out the minimum element. That minimum will be swapped with the element at the position i. """
""" Now swap the minimum item under the below nested loop. It's below not inside the loop """

def selectionSort(arr):
      for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                  if arr[min_index] > arr[j]:
                        min_index = j

#Swap the current with the min element
                  temp = arr[i]
                  arr[i] = arr[min_index]
                  arr[min_index] = temp
      return arr
#testing
nums = [60, 34, 234, 654, 1234, 765, 123, 89]
sortedNums2 = selectionSort(nums)
print(sortedNums2)