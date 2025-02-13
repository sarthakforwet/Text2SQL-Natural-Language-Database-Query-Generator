print('Building an NLP-SQL Pipeline.....')

import os
from transformers import pipeline
from transformers import BitsAndBytesConfig, AutoModelForCausalLM, AutoTokenizer
import torch


# bnb_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_compute_dtype=torch.float16
# )

# device = "cuda" if torch.cuda.is_available() else "cpu"

model_id = "delayedkarma/mistral-7b-text-to-sql_full-model"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_size = "right"

# pipe = pipeline("text2text-generation", model="delayedkarma/mistral-7b-text-to-sql_full-model", device_map='auto')

def text_to_sql(nl_query):
    """
    Convert natural language query to SQL using GPT-4.
    """
    prompt = f"""
    Convert the following natural language query into a SQL query that runs on the database with tables:
    Sales(order_id, product_id, quantity, price, date, department_id),
    Products(product_id, name, category),
    Customers(customer_id, name, age, region),
    Departments(department_id, name).

    Query: "{nl_query}"
    
    SQL Query:
    """

    # response = client.chat.completions.create(model="gpt-4",
    # messages=[{"role": "system", "content": "You are an expert SQL assistant."},
    #           {"role": "user", "content": prompt}])

    # sql_query = response.choices[0].message.content.strip()

    # sql_query = pipe(prompt)
    inputs = tokenizer(prompt, return_tensors='pt', padding=True)
    # inputs = inputs.to(model.device)
    outputs = model.generate(input_ids = inputs['input_ids'],
                             attention_mask = inputs['attention_mask'],
                             max_new_tokens = 256,
                             pad_token_id = tokenizer.eos_token_id)

    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Ensure the query does NOT contain triple backticks
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    return sql_query.strip()