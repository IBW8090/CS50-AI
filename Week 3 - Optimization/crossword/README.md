# SDLC For Crossword Problem
## Planning:
### Goal:
Have the following 8 functions:
1. Enforce Node Consistency
   - This should update the word list so that only words which are the correct length remain.
2. Revise
   - If a word in the first given list does not have matching overlap with a word in the second list, then it should be removed from the first list.
3. AC3
   - It removes item from the word list until every choice for X has a possible choice for Y.
4. Assignment Complete
   - It will check if a given crossword is completely filled out.
5. Consistent
   - It will check to see if a given crossword is consistent. It is consistent if all values are distinct, every value is the correct length, and there are no conflicts between neighbouring variables.
6. Order Domain Values
   - This will return a list of all words with the first item being the one that rules out the fewest other words amongst the neighbours of that word.
7. Selected Unassigned Variable
   - This will return a single unassigned variable based on which one has the minimum number of remaining values in the domain. In the event of a tie, you chose the one with the highest degree.
8. Backtrack
   - This will take in a partially completed crossword and complete the crossword through a recursive selection process.

### Success Criteria:
Success is identified when the code is able to take input of a crossword puzzle and fill it in using the given dictionaries.

### Project Requirements:
- crossword.py must remain unchanged.
- The only modifications to generate.py should be the functions listed above.
  - You may also make extra functions if needed.
- Only Python standard library modules, numpy and pandas are imported.

## Analysis:
### Tools:
- Assets were given
- Data was given
- crossword.py was given
- Portions of generate.py was given

### Timeline & Steps:
- Create the enforce_node_consistency function
  - It removes all words from the word list which are not the correct length for a spot on the crossword.
- Create the revise function
  - Remove all the items in the word list which don't share the correct overlapping letters with other possibilities. 
  - Return True if a change was made
  - Return False if no changes were made
- Create the ac3 function
  - Every item in x, referred to as an arc, should have a possible option in y.
  - If the original set of arcs is empty, then make the arcs be every item in the current list of variables.
- Create the assignment_complete function
  - Return true if the crossword is complete and false otherwise.
- Create the consistent function
  - Return true if the entire assignment is consistent with all rules, and false otherwise.
    - Ensure that all the words are the correct length.
    - Ensure that no word repeats within the assignment.
    - Ensure that all overlapping characters are the same.
- Create the order_domain_values function
  - Return a list of the possible words ordered by how many words they rule out.
  - Look at the overlapping letters, with the word removing the least number of other possibilities being first in the list.
- Create the select_unassigned_variable function
  - Return a variable that is not already assigned a position within the assignment.
  - The chosen variable should be the one with the lowest number of remaining values in its domain.
    - In the event of a tie, it will use the degree of the variable as a tiebreaker, with higher degrees being better.
- Create the backtrack function
  - It can take an assignment which is partially complete and complete it.
  - Recursively select a new word which is consistent with all other words until either a solution is found or all possibilities are exhausted, showing that it is impossible.
  - Return the completed assignment if it is possible to complete or None if it is impossible.

### Troubleshooting Techniques:
- Use print statements to identify the current progress as the code runs.
- Go step by step through the code to identify which portion breaks it as you add new lines.
- Check the list of words to be removed, to see if any of them have a pattern to the incorrect selection.

### Flowchart
![Crossword Flowchart.png](Crossword%20Flowchart.png)