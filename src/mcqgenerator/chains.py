import os
from src.logger import logging

# langchain packages
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

apiKey=os.getenv("OPENAI_API_KEY")

TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}
"""

TEMPLATE2="""
You are an expert in english gramary and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}
"""

input_variables=["text","number","subject","tone","response_json"]
def __generate_quiz_chain(chat_client):
    quiz_prompt_template=PromptTemplate(
        input_variables=input_variables,
        template=TEMPLATE
    )
    quiz_chain=LLMChain(llm=chat_client,prompt=quiz_prompt_template,verbose=True,output_key="quiz")
    
    return quiz_chain

def __generate_review_chain(chat_client):
    review_prompt_template=PromptTemplate(input_variables=["subject","quiz"],template=TEMPLATE2)
    review_chain=LLMChain(llm=chat_client,prompt=review_prompt_template,verbose=True,output_key="review")

    return review_chain

def generate_quiz_and_review_sequence_chain():
    # load environment variables from .env file
    if not apiKey:
        logging.log(logging.ERROR,"apiKey is missing") 
        return False


    # temperature stands for creativeness 
    # 0 means straightforward not creativeness
    chat_client=ChatOpenAI(
        openai_api_key=apiKey,
        model="gpt-3.5-turbo",
        temperature=0.5,
        max_tokens=1000,
        n=1,
    )

    quiz_chain=__generate_quiz_chain(chat_client)

    review_chain=__generate_review_chain(chat_client)

    # combine single chain into one big chain
    generate_quiz_seq_chain=SequentialChain(chains=[quiz_chain,review_chain],input_variables=input_variables,output_variables=["quiz","review"],verbose=True)
    
    logging.log(logging.INFO, "sequece chain generated")
    return generate_quiz_seq_chain