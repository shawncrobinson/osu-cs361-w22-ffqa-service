import json
import random
from time import sleep
from pathlib import Path


def create_questions_list():
    with open('./questions.jsonl', 'r') as questions:
        output = []
        for line in questions:
            output.append(json.loads(line))
        return output


def sample_questions(questions, amount):
    return random.sample(questions, amount)


def send_questions(questions):
    with open('./io.json', 'w') as io_file:
        io_file.write(json.dumps(questions))


def get_input():
    with open('./io.json', "r") as io_file:
        return io_file.read()


def main():
    questions_list = create_questions_list()
    Path('./io.json').touch(exist_ok=True)

    while True:
        io_input = get_input()

        try:
            io_input = int(io_input)
            send_questions(sample_questions(questions_list, io_input))
            # print(f"{io_input} question request processed")
        except ValueError:
            pass

        # print("waiting for request...")
        sleep(5)


if __name__ == '__main__':
    main()
