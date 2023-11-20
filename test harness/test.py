
# import os
# import subprocess

# def run_test(prog_name, test_name):
#     input_file = f'test/{prog_name}.{test_name}.in'
#     expected_stdout_file = f'test/{prog_name}.{test_name}.out'
#     expected_arg_stdout_file = f'test/{prog_name}.{test_name}.arg.out'

#     additional_args = ['data.csv','Age', 'Salary'] if prog_name == 'sumup' else []

    

#     # Run the program on STDIN
#     with open(input_file, 'rb') as f:
#         command = ['python', f'prog/{prog_name}.py'] + additional_args
#         result = subprocess.run(command, input=f.read(), capture_output=True)

#     expected_stdout = open(expected_stdout_file, 'r').read().strip()
#     actual_stdout = result.stdout.decode().strip()

#     if result.returncode != 0 or actual_stdout != expected_stdout:
#         print(f'FAIL: {prog_name} {test_name} failed (TestResult.OutputMismatch)')
#         print(f'      expected:\n{expected_stdout}')
#         print(f'           got:\n{actual_stdout}')
#     else:
#         print(f'PASS: {prog_name} {test_name} succeeded')

#     # Run the program with command-line argument
#     additional_args = ['Age', 'Salary']
#     result_arg = subprocess.run(['python', f'prog/{prog_name}.py', input_file] + additional_args, capture_output=True)

#     expected_arg_stdout = open(expected_arg_stdout_file, 'r').read().strip()
#     actual_arg_stdout = result_arg.stdout.decode().strip()

#     if result_arg.returncode != 0 or actual_arg_stdout != expected_arg_stdout:
#         print(f'FAIL: {prog_name} {test_name} failed in argument mode (TestResult.OutputMismatch)')
#         print(f'      expected:\n{expected_arg_stdout}')
#         print(f'          got:\n{actual_arg_stdout}')
#     else:
#         print(f'PASS: {prog_name} {test_name} succeeded in argument mode')


# if __name__ == "__main__":
#     # List of programs to test
#     programs = ["wc", "gron", "sumup"]

#     for prog in programs:
#         for test_file in os.listdir('test'):
#             if test_file.startswith(f'{prog}.') and test_file.endswith('.in'):
#                 test_name = test_file[len(prog) + 1: -3]
#                 run_test(prog, test_name)

import os
import subprocess

def run_test(prog_name, test_name):
    input_file = f'test/{prog_name}.{test_name}.in'
    expected_stdout_file = f'test/{prog_name}.{test_name}.out'
    expected_arg_stdout_file = f'test/{prog_name}.{test_name}.arg.out'
    expected_status_file = f'test/{prog_name}.{test_name}.status'

    additional_args = ['data.csv', 'Age', 'Salary'] if prog_name == 'sumup' else []

    # Check for expected status file
    if os.path.exists(expected_status_file):
        with open(expected_status_file, 'r') as f:
            expected_status = int(f.read().strip())
    else:
        expected_status = 0

    # Run the program on STDIN
    with open(input_file, 'rb') as f:
        command = ['python', f'prog/{prog_name}.py'] + additional_args
        result = subprocess.run(command, input=f.read(), capture_output=True)

    actual_stdout = result.stdout.decode().strip()
    expected_stdout = open(expected_stdout_file, 'r').read().strip()

    # Check for output and exit status
    if result.returncode != expected_status or actual_stdout != expected_stdout:
        print(f'FAIL: {prog_name} {test_name} failed')
        print(f'      expected status: {expected_status}, got status: {result.returncode}')
        print(f'      expected output:\n{expected_stdout}')
        print(f'           got output:\n{actual_stdout}')
    else:
        print(f'PASS: {prog_name} {test_name} succeeded')

    # Run the program with command-line argument
    additional_args = ['Age', 'Salary']
    result_arg = subprocess.run(['python', f'prog/{prog_name}.py', input_file] + additional_args, capture_output=True)

    actual_arg_stdout = result_arg.stdout.decode().strip()
    expected_arg_stdout = open(expected_arg_stdout_file, 'r').read().strip()

    # Check for output and exit status for argument mode
    if result_arg.returncode != expected_status or actual_arg_stdout != expected_arg_stdout:
        print(f'FAIL: {prog_name} {test_name} failed in argument mode')
        print(f'      expected status: {expected_status}, got status: {result_arg.returncode}')
        print(f'      expected output:\n{expected_arg_stdout}')
        print(f'           got output:\n{actual_arg_stdout}')
    else:
        print(f'PASS: {prog_name} {test_name} succeeded in argument mode')


if __name__ == "__main__":
    programs = ["wc", "gron", "sumup"]
    for prog in programs:
        for test_file in os.listdir('test'):
            if test_file.startswith(f'{prog}.') and test_file.endswith('.in'):
                test_name = test_file[len(prog) + 1: -3]
                run_test(prog, test_name)

