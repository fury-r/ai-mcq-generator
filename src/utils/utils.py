import os
import PyPDF2
import json
import traceback
from src.logger import logging


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfReader(file)
            text="".join([page.extract_text() for page in pdf_reader.pages])
            return text
        except Exception as e:
            logging.log(logging.ERROR,f"error reading PDF file {e}")
            raise Exception(f"error reading PDF file {e}")
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else: 
        logging.log(logging.ERROR,f"Unsupported file extension, file: {file.name}")
        raise Exception(f"Unsupported file extension, file: {file.name}")
    

def get_table_data(quiz_str):
    try:
        quiz=json.loads(quiz_str)

        quiz_table_data=[ 
        {
            "question":value["mcq"],
            "options":" || ".join([ f"{option_key}-> {option_value}" for option_key,option_value in value["options"].items() ]),
            "correct":value["correct"],
        }   
        for _,value in quiz.items()
        ]
        return quiz_table_data
    except Exception as e:
        logging.log(logging.ERROR,f"error occurred{e}")
        traceback.print_exception(type(e),e,e.__traceback__)
        return False