# 📖 Lesson 1 <br> An Introduction to Generative AI

In this lesson, we'll cover the fundamentals of the exciting field of generative AI and large language models.

## Table of Contents
1. [What is Generative AI?](#1-what-is-generative-ai)
2. [Rise of Generative AI](#2-rise-of-generative-ai)
3. [Benefits of Generative AI?](#3-benefits-of-generative-ai)
4. [Building Generative AI apps](#4-building-generative-ai-apps)
5. [Generative AI app ideas](#5-generative-ai-app-ideas)

## 1. What is Generative AI?

Generative artificial intelligence (also known as Generative AI or Gen AI) has in recent months emerged as a powerful and robust tool that can use prompt inputs to generate new content where both of which can exist in various formats including text, image, audio and video.

In this course, our focus is on text generation and the underlying method for producing such text is made possible by large language models (LLMs). Briefly, as the name imply, LLM is a language model that has been trained on a large data set as well as large number of parameters. Such LLM models can be used for text generation that can be applied on a wide range of use cases:
- Brainstorm ideas
- Generate blog drafts
- Generate social posts
- Copy writing
- Text summarization
- Text paraphrasing
- Language translation
- Sentiment analysis

Often times, you might notice that the generative AI term may be used interchangeably with LLMs or GPT (acronym for generative pre-trained transformer) and you'll also notice that this is the case in this lesson as well as others you may find on the internet.

## 2. Rise of Generative AI

Probably the most popular and well-known LLM is ChatGPT, which in a matter of days had reached 1 million users and is approximately supporting over 100 million users. Not only is ChatGPT used by the general public, developers and indie hackers are building some interesting and innovative tools for tackling various use cases.

Technically, the underlying LLM model powering ChatGPT is GPT 3.5 and it has established itself as a gold standard model from which other emerging models are compared against owing to its presence as the first model to market along with its reasonably good performance and low cost.

## 3. Benefits of Generative AI?

Generative AI has pioneered a new era of possibilities where an area that has received a remarkable boost is content creation. 

Gone are the days where we would stare at a blank document with a blinking cursor that is infamously known as the Writer's block.

With a well crafted prompt, one could brainstorm and generate hundreds of possible ideas; then subsequently turn those idea seeds into an article outline and even a longer form draft. Aside from the content itself, LLM models can also be used to generate complementary contents such as social promotion posts (_e.g._ Twitter posts or threads) and TL;DR summaries, from amongst the plethora of content possibilities. 

## 4. Building Generative AI apps

The motivation for building generative AI apps can stem from various compelling factors, whether it be to solve work-related real-world problems or to build up an impressive portfolio of projects. In either case, a common goal of such effort is to solve real-world problems through the use of AI.

A generic workflow for building an app involves:
- Identify a problem to solve,
- Figure out a solution to the problem through the use of AI and
- Package this into an app that consists of a frontend for accepting user input, a backend that takes and processes (_i.e._ it is here that generative AI comes into play) the input and finally relaying the final output back to the frontend.

As mentioned above, we can use generative AI in the data processing phase where essentially the prompt input is used for generating the LLM response output. In the next section, we'll take a look at some example generative AI apps that we can build.

## 5. Generative AI app ideas

Let's now think about some of the generative AI apps that we can build.


| App ideas | Description | Tech stack | Example |
|---|---|---|---|
| Chatbot | Build a generic chatbot or chatbot with a personality | `LLM`, `Streamlit` | [App](https://llama2.streamlit.app/), [Blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/) |
| YouTube summarization | Summarize a Youtube video (load video using LangChain's data loader) | `LLM`, `LangChain`, `Streamlit` |  |
| Research paper summarization | Summarize a research article (TXT, HTML or PDF) | `LLM`, `Streamlit` | [App](https://langchain-text-summarization.streamlit.app/), [Blog](https://blog.streamlit.io/langchain-tutorial-3-build-a-text-summarization-app/) |
| Questions & Answer over articles |  Ask questions about an article (TXT, HTML or PDF) | `LLM`, `LangChain`, `Streamlit` | [App](https://langchain-ask-the-doc.streamlit.app/), [Blog](https://blog.streamlit.io/langchain-tutorial-4-build-an-ask-the-doc-app/) |
| Questions & Answer over Docs | Ask questions on contents from an open source Documentation website | `LLM`, `LlamaIndex`, `Streamlit` | [App](https://llamaindex-chat-with-docs.streamlit.app/), [Blog](https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/) |
| Questions & Answer over Data | Ask questions about a CSV data | `LLM`, `LangChain`, `Streamlit` | [App](https://langchain-ask-the-data.streamlit.app/), [Blog](https://blog.streamlit.io/langchain-tutorial-5-build-an-ask-the-data-app/) |

Here are only a few ideas to get you started and there are many more that you can build. Proceed to the next lesson to get started!
