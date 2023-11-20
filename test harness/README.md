# Project Name

## Author Information
- Name: [Abhishek Shankar]
- Stevens Login: [ashankar1@stevens.edu]

## Repository Information
- GitHub Repository URL: [https://github.com/AbhishekShankar17/TestHarness]

## Project Overview

### Time Spent
- Estimated Hours Spent: [10 - 15 hrs]

### Code Testing
- Description of Testing Methodology:
  I thoroughly tested my code by working on three files wc.py, gron.py and sumup.py
  Additionally, I tested by giving different inputs

### Known Bugs and Issues
- I resolved errors in standard input test failure and arguement mode test failure

### Resolved Difficult Issues
- Example of a Difficult Issue:
  in wc.py i encountered a arguement mode test failure where Expected output: 11 10 54 test/wc.basic.in
  Actual output: 11 10 54 test/wc.basic.in
The output matches, but the test fails with exit status 1. This suggests that there might be an issue with how the exit status is handled in your script or a problem in the test setup.

### Implemented Extensions
1. **More Advanced wc: Multiple Files**
   - Description: [To support multiple files in wc.py, you need to modify the script to handle multiple file paths as input arguments and provide a total count at the end.]
   

2. **More Advanced wc: Flags to Control Output**
   - Description: [wc.py to support flags like -l, -w, and -c for controlling the output.]
   - How to Test: [This would require a more complex parsing of command-line arguments. You can use argparse for this, but for simplicity, I'll demonstrate a basic version without it.]

3. **Expected Exit Status**
   - Description: [Modified the run_test function to include checking for expected exit status. This involves reading the expected status from a file and comparing it with the actual exit status.]




