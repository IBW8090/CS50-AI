# SDLC For Knights and Knaves Problem


## Planning:
### Goal: 
Have a knowledge base for each problem which allows the code to identify which character is a knight and which is a knave.
### Success Criteria:
Success will be identified when the code is able to evaluate the knowledge base to obtain the correct answers to each of the given problems.
### Project Requirements:
- All logic occurs in logic.py and logic.py is unmodified.
- No extra libraries are imported.
- The code successfully evaluates the problems.

## Analysis:
### Tools:
- logic.py was given
  - Symbols
  - Evaluate
  - Not
  - And
  - Or
  - Implication
  - Biconditional
  - Model Check
- Premade symbols for saying that a character is either a knight or a knave.

### Timeline & Steps:
- Identify the rules:
  - A knight will always tell the truth.
  - A knave will always lie.
  - A single character can not be both a knight and a knave.
  - Each character will always be either a knight or a knave.
- Identify the given knowledge from the problems
  - P0:
    - If A is a knight, it is both a knight and a knave.
    - If A is a knave, then it is not both a knight and a knave.
  - P1:
    - If A is a knight, then both A and B are knaves.
    - If A is a knave, then A and B are not both knaves.
  - P2:
    - If A is a knight, then either both A and B are knights or both A and B are knaves.
    - If A is a knave, then either A and B are not both knights, or A and B are not both knaves.
    - If B is a knight, then either A is a knight and B is a knave, or A is a knave and B is a knight.
    - If B is a knave, then either A is not a knight while B is not a knave or A is not a knave while B is not a knight.
  - P3:
    - If A says "I am a knight" then:
      - If A is a knight, then they are a knight.
      - If A is a knave, then they are not a knight.
    - If A says "I am a knave" then:
      - If A is a knight, then they are a knave.
      - If A is a knave, then they are not a knave.
    - If A is a knight, then A could be either a knight or a knave.
    - If A is a knave, then A is either not a knight or not a knave.
    - If B is a knight, then A said that they were a knave and C is a knave.
    - If B is a knave, then A did not say that they were a knave, and C is not a knave.
    - If C is a knight, then A is a knight.
    - If C is a knave, then A is not a knight.
- Create logic statements for the knowledge base to allow the algorithm to identify which characters are which pieces in each problem.

### Troubleshooting Techniques:
- Use print statements to identify what the code considers the logic as in each step.
- Go step by step through the logic adding more each time to identify where it breaks.


### Flowchart:
Refer to the Flowchart PDF.