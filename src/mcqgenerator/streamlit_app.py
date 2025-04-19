import os
import json
import traceback
import pandas as pd


import streamlit as st
from langchain.callbacks import get_openai_callback
from src.utils.utils import read_file,get_table_data
from src.logger import logging


with open("./src/data/response.json","r") as file:
    RESPONSE_JSON=file.read()
    logging.log(logging.INFO,f"response structure loaded {json.loads(RESPONSE_JSON)}")


def load_stream_lit_app(generate_evaluate_quiz_review):
    df,table_data=pd.DataFrame(),None
    logging.log(logging.INFO,"starting streamlit app")
    
    # title for app
    st.title("MCQs Creator App with Langchain")

    with st.form("user_inputs"):
        
        # file upload
        uploaded_file=st.file_uploader("Upload a PDF or TXT file")
        # number of questions
        mcq_count=st.number_input("Number of Questions",min_value=3,max_value=50)
        # subject name
        subject=st.text_input("Name of the Subject",max_chars=50)
        # quiz tone: complexity level
        tone=st.text_input("Complexity Level of the questions",max_chars=20,placeholder="Simple",)
        # Add Button
        button=st.form_submit_button("Create MCQs")

        if button and uploaded_file  and  mcq_count and subject and tone:
            logging.log(logging.INFO,f"processing user input uploaded_file:{uploaded_file}, mcq_count:{mcq_count}, subject:{subject}, tone:{tone}.")
            with st.spinner("Processing..."):
                
                logging.log(logging.INFO, "Displaying loader")
                try:
                    text=read_file(uploaded_file)
                    with get_openai_callback() as cb:
                        response=generate_evaluate_quiz_review({
                            "text":text,
                            "number":mcq_count,
                            "subject":subject,
                            "tone":tone,
                            "response_json":RESPONSE_JSON
                        })
                except Exception as e:
                    traceback.print_exception(type(e),e,e.__traceback__)
                    st.error("Error")
                else:
                    
                    logging.log(logging.INFO,f"Total Tokens:{cb.total_tokens}")
                    logging.log(logging.INFO,f"Prompt Tokens:{cb.prompt_tokens}")
                    logging.log(logging.INFO,f"Completion Tokens:{cb.completion_tokens}")
                    logging.log(logging.INFO,f"Total Cost:{cb.total_cost}")

                    if isinstance(response,dict):
                        quiz_str=response.get("quiz")
                        if quiz_str:
                            table_data=get_table_data(quiz_str)
                            if table_data:
                                df=pd.DataFrame(table_data)
                                df.index=df.index+1
                                # display the quiz in the table
                                st.table(df)
                                # display the review
                                st.text_area(label="Review",value=response.get("review","Not found"))



                            else:
                                logging.log(logging.ERROR,f"Error in table data {table_data}")
                                st.error("Error in table data")
                    else:
                        st.write(response)
    if not df.empty and table_data:
        print(df,table_data)
        st.download_button("Download CSV",data=df.to_csv(index=False),file_name="mcq.csv",mime="text/csv")
        st.download_button("Download JSON",data=json.dumps(table_data),file_name="mcq.json",mime="application/json")