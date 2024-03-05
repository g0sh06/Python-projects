import json
from difflib import get_close_matches


def load_question_base(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_question(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def best_match(user_question, questions):
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question, response):
    for q in response['questions']:
        if q['question'] == question:
            return q['answer']

def chat_bot():
    response = load_question_base('chatbot/response.json')

    while True:
        user_input = input('You:')

        if user_input.lower() == 'quit':
            break
        best_matched_question = best_match(user_input, [q['question'] for q in response['questions']])

        if best_matched_question:
            answer = get_answer(best_matched_question, response)
            print(f'Bot: {answer}')
        else:
            print('I dont know the answer can you teach me')
            new_answer = input('Type the answer or "skip"')

            if new_answer.lower() != "skip":
                response['questions'].append({'question': user_input, "answer": new_answer})
                save_question('response.json', response)
                try:
                    save_question('chatbot/response.json', response)
                    print('Data saved successfully')
                except Exception as e:
                    print(f'Error saving data: {e}')
                print('Bot: Thank you for teaching me')



if __name__ == '__main__':
    chat_bot()