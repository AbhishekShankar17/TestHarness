# import sys

# def count_words(text):
#     lines = text.split('\n')
#     line_count = len(lines)
    
#     words = [word.strip(".,!?()[]{}") for line in lines for word in line.split()]
#     word_count = len(words)
    
#     char_count = sum(len(word) for word in words)
    
#     return line_count, word_count, char_count

# def main():
#     try:
#         if len(sys.argv) == 1:
#             # Read from stdin
#             input_text = sys.stdin.read()
#         else:
#             # Read from file
#             with open(sys.argv[1], 'r') as file:
#                 input_text = file.read()

#         line_count, word_count, char_count = count_words(input_text)
        
#         print(f"{line_count:8}{word_count:8}{char_count:8}", end='')
        
#         if len(sys.argv) > 1:
#             print(f" {sys.argv[1]}")
        
#         # Exit with status 0 (success)
#         sys.exit(0)
    
#     except FileNotFoundError:
#         print(f"Error: File '{sys.argv[1]}' not found.")
#         # Exit with a non-zero status to indicate an error
#         sys.exit(1)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         # Exit with a non-zero status to indicate an error
#         sys.exit(1)

# if __name__ == "__main__":
#     main()


import sys

def count_words(text):
    lines = text.split('\n')
    line_count = len(lines)
    if text and not text.endswith('\n'):  # Check if the text does not end with a newline
        line_count -= 1

    words = [word.strip(".,!?()[]{}") for line in lines for word in line.split()]
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    return line_count, word_count, char_count

def main():
    total_lines, total_words, total_chars = 0, 0, 0
    files = sys.argv[1:] if len(sys.argv) > 1 else ['-']
    try:

        for file in files:
            if file == '-':
                input_text = sys.stdin.read()
                line_count, word_count, char_count = count_words(input_text)
                print(f"{line_count:8}{word_count:8}{char_count:8}")  # Print without filename for STDIN
            else:
                try:
                    with open(file, 'r') as f:
                        input_text = f.read()
                        line_count, word_count, char_count = count_words(input_text)
                except FileNotFoundError:
                    print(f"Error: File '{file}' not found.", file=sys.stderr)
                    sys.exit(1)

                total_lines += line_count
                total_words += word_count
                total_chars += char_count
                print(f"{line_count:8}{word_count:8}{char_count:8} {file}")  # Print with filename for file input

        if len(files) > 1:
            print(f"{total_lines:8}{total_words:8}{total_chars:8} total")


    except FileNotFoundError:
        print(f"Error: File '{file}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
        
    sys.exit(0)

if __name__ == "__main__":
    main()
