import streamlit as st
import pandas as pd
import requests

st.title("Conversational Text-to-SQL Agent")

nl_query = st.text_input("Enter your query in natural language:")
if st.button("Generate SQL & Fetch Data") and nl_query:
    response = requests.post("http://127.0.0.1:8000/query", json={"x": nl_query}) #, json={'nl_query': nl_query})
    print(response.request.body)
    if response.status_code == 200:
        data = response.json()
        st.subheader("Generated SQL Query:")
        st.code(data["query"], language="sql")

        df = pd.DataFrame(data["result"])
        if not df.empty:
            st.subheader("Query Results:")
            st.dataframe(df)

            # Visualizing the results dynamically
            if len(df.columns) == 2:
                st.bar_chart(df.set_index(df.columns[0]))
            elif len(df.columns) > 2:
                st.line_chart(df.set_index(df.columns[0]))
    else:
        st.error("Error: " + str(response.json()["detail"]))
