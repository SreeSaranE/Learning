# https://drive.google.com/file/d/14HQIdZrOhE7SlW8gzQceN0Tf2dekp7n0/view?usp=drive_link
def solve(s):
    words: list = s.split(" ")
    new_words: list = []
    for i in words:
        new_words.append(i.capitalize())
    return " ".join(new_words)

solve("Hello there")