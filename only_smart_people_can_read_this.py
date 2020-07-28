#!/bin/python3
#author: hydr10n@github

import sys
import random


def start_and_end_of_first_word(text: str) -> tuple:
    found_word = False
    start = -1
    end = 0
    text_len = len(text)
    for i in range(text_len):
        if text[i].isalpha():
            if start == -1:
                start = i
            end = i
            if i == text_len - 1:
                found_word = True
        elif start != -1:
            found_word = True
        if found_word:
            return (start, end)
    return (-1, -1)


def randomize_text(text: str, group_length: int) -> str:
    i = 0
    while i < len(text):
        start, end = start_and_end_of_first_word(text[i:])
        if start == -1:
            i += 1
        else:
            start += i + 1
            end += i
            i = end + 1
            length = end - start
            if length > 1:
                arr = [None] * length
                prev_k = -1
                randomized = False
                for j in range(length):
                    k = j // group_length * group_length
                    if k != prev_k:
                        randomized = False
                        prev_k = k
                    while True:
                        rand_i = random.randint(
                            k, min(length, k + group_length) - 1)
                        if arr[rand_i] == None and (text[start + rand_i] != text[start + j] or randomized or start + j + 1 == end):
                            randomized = True
                            break
                    arr[rand_i] = text[start + j]
                text = text[:start] + ''.join(arr) + text[end:]
    return text


def main():
    print("say something, and you will see something incredible...")
    print("(remember [Ctrl + D] on Linux or [Ctrl + Z] on Windows to confirm input)")
    print("---")
    text = ''.join(sys.stdin.readlines())
    print("\n-->\n")
    print(randomize_text(text, 5))
    print("---\nif you can read this, you must be smart! pretty cool huh?")


if __name__ == "__main__":
    main()
