import json

def process_answers(file_prefix):
    # Load JSON data with all questions and possible answers
    with open('data/all_questions.json', 'r', encoding='utf-8') as json_file:
        questions_data = json.load(json_file)

    # Load answers from the answer_1.txt file
    answer_file_path = f'data/{file_prefix}.txt'
    with open(answer_file_path, 'r', encoding='utf-8') as answer_file:
        answer_lines = answer_file.readlines()

    # Prepare a dictionary to store the client's answers
    client_answers = {}
    line_index = 0

    # Iterate through the questions data to match it with answers
    for main_category, subcategories in questions_data.items():
        client_answers[main_category] = {}
        # Skip the main category header in answer file
        line_index += 1
        for subcategory, questions in subcategories.items():
            client_answers[main_category][subcategory] = {}
            # Skip the subcategory header in the answer file
            line_index += 1
            # Get the answers line and split by commas
            answers_line = answer_lines[line_index].strip().split(",")
            question_index = 0
            for question, options in questions.items():
                selected_option = answers_line[question_index]
                # Assign the selected answer to the dictionary
                client_answers[main_category][subcategory][question] = options[selected_option]
                question_index += 1
            # Move to the next line in the answers file
            line_index += 1

    # Save the client's answers into a new JSON file
    output_file = f'data/{file_prefix}.json'
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(client_answers, out_file, ensure_ascii=False, indent=4)

    print(f'Client answers saved to {output_file}')