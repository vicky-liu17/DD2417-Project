def clean_csv(input_path, output_path):
    cleaned_lines = []

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().rstrip(';')
            if line.startswith('"') and line.endswith('"'):
                line = line[1:-1]

            line = line.replace('""', '"')
            cleaned_lines.append(line + '\n')

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)


def main():
    input_path = "question_pairs.csv"
    output_path = "question_pairs_cleaned.csv"
    clean_csv(input_path, output_path)


if __name__ == "__main__":
    main()
