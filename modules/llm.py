# from langchain.chains.llm import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# import re
# import json 

# load_dotenv()



# template = f"""
# **Task:** You are a highly skilled reader. Your goal is to analyze the text extracted from a several sources, which is /enclosed within #### and answer the question delimited by &&&&.


# **Sample Input:**
#   "Sample text here..."
#   "Sample Question..."

# **Expected Output:**
#   Please provide your answer to the question based on the provided text. 


#   **Points to consider**
#   1. Ensure that the output is only generated from the knowledge of provided text.
#   2. Avoid adding anything from your knowledge just use the input text to answer the question.
#   3. Double-check that all instructions are followed closely.
#   4. Please do not make anything up. If the answer to the question is not found in the input text, then respond with 'Data not available'.
#   5. Please do not provide explaination to your response. Either provide the answer to the question or 'Data not available'. 

#   ####
#   {{extracted_text}}
#   ####

#   &&&&
#   {{question}}
#   &&&&
#   """

# llm = ChatGroq(temperature=0.0, model_name="Llama3-8b-8192")
# prompt = PromptTemplate(template=template, input_variables=["extracted_text", "question"])

# chain = LLMChain(prompt=prompt, llm=llm)

# def get_answer(extracted_text, question): 
  
#   response = chain.invoke({"extracted_text": extracted_text, "question" : question})
#   print('\n\n\n', response['text'], '\n\n\n')
#   return response['text']

# # s = time.time()


# # input = """
# # AJAY KUCHHADIYA\n+91-7457878864 | Agra, Uttar Pradesh, India\nkuchhadiyaajay86kn@gmail.com | LinkedIn | GitHub\nPROFESSIONAL SUMMARY\nPassionate software engineer specializing in building advanced AI solutions. Skilled in Generative AI, NLP, and\nmachine learning using TensorFlow, Flask, and Python.\nAdept at creating cost-efficient systems and intelligent\nagents with a focus on developing impactful AI applications and deriving data-driven insights.\nEDUCATION\nB.Tech, Computer Science, 7.07 CGPA\n2020 - 2024\nHindustan College of Science and Technology\nFarah, Uttar Pradesh\n12th Grade, CBSE, 83%\n2019 - 2020\nRadhaballabh Public School\nAgra, Uttar Pradesh\nSKILLS\nProgramming Languages\nPython, C/C++\nMachine Learning/Deep Learning\nScikit-learn, TensorFlow\nData Analysis and Visualization\nPandas, SQL, NoSQL, Matplotlib, Seaborn\nGenerative AI\nLLM, RAG, Autogen, Vector Store, Hugging Face\nAPI Development\nFlask, FastAPI, RestfulAPI\nDatabases\nPostgreSQL, MongoDB\nEXPERIENCE\nTrainee Associate Software Engineer\nFeb 2024 – Aug 2024\nWalking Tree Technologies\nAgra, Uttar Pradesh\n• Developed AI-based solutions using LLM, Langchain, RAG, Vector Store databases, Autogen, and Flask.\n• Led the creation of a cost-efficient Retrieval-Augmented Generation (RAG) system, reducing API expenses.\n• Built a POC using Autogen for intelligent bug fixing and test case generation.\n• Contributed to AI-driven projects by utilizing Computer Vision techniques, PDF text extraction, Speech-to-\nText, Generative AI, and NLP.\nData Science Intern\nJun 2022 – Aug 2022\nFoxmula\nRemote\n• Analyzed datasets using Excel and Python, visualized with Matplotlib and Seaborn, leading to data-driven\ndecisions and revenue growth.\n• Produced reports on key performance indicators (KPIs), boosting efficiency by 15% and aiding strategic planning.\nPERSONAL PROJECTS\nCrewAI Health Advisor\n(GitHub)\n• Overview: Developed an AI system to assist in healthcare tasks, including summarizing medical reports, finding\nrelevant health articles, and providing health recommendations.\n• Technologies: LLM, CrewAI, Python, NLP, OCR, AI Agents.\nFashionAI: An AI-based Fashion Platform\n(GitHub)\n• Overview: Developed a fashion platform using Generative AI, Collaborative Filtering, and Visual Search.\n• Technologies: LLM (OpenAI, Groq), Computer Vision, Image Generation, Python, Flask, NLP.
# # """

# # question = "What is the educational background of the person?"
# # x = extract_entities(input, question)

# # print('\n\n Answer : ', x)