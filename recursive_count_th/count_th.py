'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word="thesis"):
    if len(word) < 2:
        return 0

    count = 0
    if word[0:2] == "th":
        count += 1

    count += count_th(word[1:])
    return count


if __name__ == "__main__":
    word = "The thirty-three thieves thought that they thrilled the throne throughout Thursday"
    print(f"{count_th(word)} cases of 'th' in '{word}'.")
