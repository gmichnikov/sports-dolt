def extract_text_between_occurrences(file_path, start_str, end_str):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        start_index = content.find(start_str)
        end_index = content.find(end_str, start_index + len(start_str))
        return content[start_index + len(start_str):end_index].strip()

def save_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    file_path = "fullmlb.html"
    start_str = "HeaderSportsEventSchema"
    end_str = "HeaderSportsEventSchema"

    extracted_text = extract_text_between_occurrences(file_path, start_str, end_str)
    save_to_file("reducedmlb.html", extracted_text)

    print("Extraction and saving complete.")
