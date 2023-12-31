import argparse
import os
import PyPDF2
import re
import sys


def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def printGreen(text):
    print_colored(text, '32')

def printRed(text):
    print_colored(text, '31')

# Function to search for keywords in text
def search_keywords(text, keywords):
    match_keys = []
    for keyword in keywords:
        pattern = r'\b{}(?:,)?\b'.format(keyword.lower())
        matches = re.findall(pattern, text.lower(), re.IGNORECASE)
        if len(matches) > 0:
            match_keys.append(f'{keyword} ({len(matches)})')

    return match_keys


def main():
    parser =argparse.ArgumentParser()
    parser.add_argument(
        '-k', '--keywords', required=True, help='Please enter at least one keyword. e.x. python, js'
    )
    parser.add_argument(
        '-p', '--files_path', default='demo_resumes', help='Add files location to be extracted'
    )
    args = parser.parse_args()

    if args.files_path is None or not os.path.exists(args.files_path):
        parser.print_help()
        raise ValueError('Please provide a valid path..')

    if args.keywords is None:
        parser.print_help()
        raise ValueError('Please Enter a valid keyword with the comma..')

    keyword_list = [keyword.strip() for keyword in args.keywords.split(',')]
    print('----------keyword_list-{}------'.format(keyword_list))
    shortlisted_resumes = []
    no_match_resumes = []
    invalid_pdfs = []
    # Iterate through PDF files in the directory
    for filename in os.listdir(args.files_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(args.files_path, filename)

            # Read the PDF content
            with open(pdf_path, 'rb') as pdf_file:
                try:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    resume_text = ""
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        resume_text += page.extract_text()

                    matched_keywords = search_keywords(resume_text, keywords=keyword_list)
                    if len(matched_keywords):
                        shortlisted_resumes.append({
                            'FileName': filename,
                            'MatchKeywords': ', '.join(matched_keywords)
                        })
                    else:
                        no_match_resumes.append({
                            'FileName': filename,
                            'MatchKeywords': 'No match found'
                        })
                except Exception as e:
                    invalid_pdfs.append(filename)
                    continue

    if len(shortlisted_resumes) > 0:
        print("\n***Following are shortlisted resumes.***\n")
        shortlisted_resumes = sorted(shortlisted_resumes, key=lambda x: len(x['MatchKeywords']), reverse=True)
        for index, resume in enumerate(shortlisted_resumes, start=1):
            printGreen(
                f'{index}. Filename: {resume["FileName"]}, \nMatching keywords: {resume["MatchKeywords"]}\n'
            )

    if len(no_match_resumes) > 0:
        print("\n***Following are resumes with not match keywords found.***\n")
        for index, resume in enumerate(no_match_resumes, start=1):
            printRed(
                f'{index}. Filename: {resume["FileName"]}, \nMatching keywords: {resume["MatchKeywords"]}\n'
            )

    if len(invalid_pdfs) > 0:
        print("\n***Following are invalid pdf's.***\n")
        for item in invalid_pdfs:
            printRed(f'Filename: {item}\n')


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as ex:
        printRed(f'Exception: {ex}')
        sys.exit(1)
