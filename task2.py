from itertools import combinations
import argparse


def create_list_comb(N):
    comb_list = list(combinations([0, 0, 0, 0, 0, 1, 2, 3, 4, 5], N))
    for i in comb_list:
        print(i)
    return comb_list


def create_text_file(comb_list):
    with open("task2_output.txt", "a") as file:
        for i in comb_list:
            file.write(f"{i}\n")


if __name__ == '__main__':
    parse_my = argparse.ArgumentParser(description='some tips')
    parse_my.add_argument('-number', '--number')
    args = parse_my.parse_args()
    number = args.number
    if number:
        comb_list = create_list_comb(int(number))
        create_text_file(comb_list)
    else:
        print("need args -inputFile:\n Example -number 5")