
import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()

from src.mcqgenerator.chains import generate_quiz_and_review_sequence_chain
from src.logger import logging
from src.mcqgenerator.streamlit_app import load_stream_lit_app 

def main():
    logging.log(logging.INFO, "generate sequence chain")
    generate_quiz_seq_chain=generate_quiz_and_review_sequence_chain()
    if not generate_quiz_seq_chain:
        logging.log(logging.ERROR,"Failed to generate sequence chain")
        raise Exception("Failed to generate sequence chain")
    
    logging.log(logging.INFO, "execute streamlit")
    load_stream_lit_app(generate_quiz_seq_chain)
    




if __name__=="__main__":
    logging.log(logging.INFO,"starting app execution...")
    main()