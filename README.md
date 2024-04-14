# Conversational apps with LangChain and Python for beginners

These notebooks were created as part of a workshop for the [Minds Mastering Machines](https://www.m3-konferenz.de/lecture.php?id=21478&source=0) on April 23rd in Cologne.

## Overview and requirements

The following examples were tested using Ollama on-premises and Azure OpenAI. Where the use of Ollama was not possible, only Azure OpenAI was used.

## What are LLMs, tokens, context window, embeddings, vector databases

## What is LangChain?

LangChain is a framework for developing applications powered by large language models.

## Overview of LangChain components

![](https://python.langchain.com/svg/langchain_stack_dark.svg)

## Langchain repository

[Here](https://github.com/langchain-ai/langchain) is the LangChain repository for Python.

## Project setup

* Bring your own large language model. LangChain supports the [followings](https://python.langchain.com/docs/integrations/llms/)
* [Install LangChain](https://python.langchain.com/docs/get_started/installation/)
* Test the installation and run [this](notebooks/func-test.ipynb) notebook. 

## First LangChain application

[hello_langchain.ipynb](notebooks/hello_langchain.ipynb)

## Use different LLMs

[llms.ipynb](notebooks/llms.ipynb)

## Caching and debugging

* [caching.ipynb](notebooks/caching.ipynb)
* [debugging.ipynb](notebooks/debugging.ipynb)

## Prompting

[prompting.ipynb](notebooks/prompting.ipynb)

## Application types

### RAG - Retrieval-Augmented Generation

* [rag.ipynb](notebooks/rag.ipynb)
* [rag2.ipynb](notebooks/rag2.ipynb)

### RAG Evaluation

[rag-eval.ipynb](notebooks/rag-eval.ipynb)

### Talk-with-your-database

[sql_db_qa.ipynb](notebooks/sql_db_qa.ipynb)

### Agents

* Research Agents
* Generative Agents

## UIs for Langchain

* [gradio-ollama-chat.py](gradio-ollama-chat.py)
* [chainlit-app.py](chainlit-app.py)
* [streamlit-ollama-chat.py](streamlit-ollama-chat.py)

## Low-code development with Langchain

Here are [examples](https://github.com/rawar/conversational-apps-with-langchain/tree/main/flows) of Langflow and Flowise.

## Example applications

t.b.d.

## Binging Langchain applications into production

t.b.d.

## Sources

[https://www.udemy.com/course/langchain/learn/lecture/37507516#overview](https://www.udemy.com/course/langchain/learn/lecture/37507516#overview)
[https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/1/introduction](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/lesson/1/introduction)
[https://github.com/CoderPush/chatlit](https://github.com/CoderPush/chatlit)
[https://www.gradio.app/](https://github.com/CoderPush/chatlit)
[https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
[https://flowiseai.com/](https://flowiseai.com/)
[https://langchaindart.com/#/](https://langchaindart.com/#/)
[https://python.langchain.com/cookbook/](https://python.langchain.com/cookbook/)
[https://www.langflow.org/](https://python.langchain.com/cookbook/)
[https://docs.smith.langchain.com](https://docs.smith.langchain.com)
[https://api.python.langchain.com/en/latest/vectorstores/langchain_community.vectorstores.sqlitevss.SQLiteVSS.html](https://api.python.langchain.com/en/latest/vectorstores/langchain_community.vectorstores.sqlitevss.SQLiteVSS.html)
