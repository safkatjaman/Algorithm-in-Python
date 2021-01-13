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