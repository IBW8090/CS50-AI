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

