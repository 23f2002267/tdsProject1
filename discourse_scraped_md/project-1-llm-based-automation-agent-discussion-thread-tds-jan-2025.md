# Thread Markdown: 164277

---

    ### 💬 Post 1 by @s.anand  
    **Posted on:** 2025-01-19 08:17 UTC  

    Please post any questions related to Project 1 - LLM-based Automation Agent.
Deadline: Sunday, February 16, 2025 6:29 PM
Update on 27 Jan 2025:
A sample evaluation script for Project 1 tasks A1-A10 is available at tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub
You can use this to validate your code for Project 1.
Please note:

This is a sample. It WILL change.
Don’t rely on the dataset being the same. It WILL change.
LLMs give different results each time they are called. Make sure:

Your code gives correct results reliably (i.e. try a few times)
Change the task in the evaluation script slightly to test variations


Your AI Proxy usage resets on 1 Feb. You have a limited budget. Utilize what you can this month.
For those who submit their code by Friday 31 Jan, I will run a sample evaluation and share the results.

    ---

    ### 💬 Post 2 by @s.anand  
    **Posted on:** 2025-01-19 08:20 UTC  

    

    ---

    ### 💬 Post 3 by @roy2003  
    **Posted on:** 2025-01-19 13:44 UTC  

    sir show us all the way to do project

    ---

    ### 💬 Post 4 by @Jivraj  
    **Posted on:** 2025-01-19 13:45 UTC  

    Hi Shouvik,
We will have live sessions to guide on how to do project.
Kind regards
Jivraj

    ---

    ### 💬 Post 5 by @23f2000237  
    **Posted on:** 2025-01-20 10:44 UTC  

    Will those session be on youtube too?

    ---

    ### 💬 Post 6 by @carlton  
    **Posted on:** 2025-01-20 10:48 UTC  

    Hi Sakthivel,
Yes all sessions are being recorded and are available on youtube within a day.
Jan 25 TDS Playlist
Kind regards

    ---

    ### 💬 Post 7 by @22f3001315  
    **Posted on:** 2025-01-23 09:57 UTC  

    *🖼️ Image description: The image shows instructions for a step labeled A1.  It involves installing a package named 'uv' (if needed), then running a python script from a GitHub URL, using a user's email address as input. The script generates data files for subsequent steps.*Screenshot 2025-01-23 1516141281×125 18.1 KB
sir @Jivraj after editing line 127 in datagen.py i got those  required data files. is it allowed ? also i had to run datagen.py MANUALLY(is this process also should be automatic)?

    ---

    ### 💬 Post 8 by @Jivraj  
    **Posted on:** 2025-01-23 11:30 UTC  

    Hi Guddu ,
I didn’t make any changes to file and it worked for me. Can you mention what is need of making changes ?
command that I used :
uv run datagen.py 22f3002542@ds.study.iitm.ac.in --root ./data
here --root option defines the folder where you want to store generated data. by default it would try to create a folder in root directory of operating system.
Kind regards
Jivraj

    ---

    ### 💬 Post 10 by @23f2005325  
    **Posted on:** 2025-01-23 13:05 UTC  

    getting this issue :
openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_issuer'}}

    ---

    ### 💬 Post 11 by @Jivraj  
    **Posted on:** 2025-01-23 13:22 UTC  

    Hi Aishik,
Pls add context to your query, without that we won’t be able to understand, where exactly you are facing problem.



*🖼️ Image description: That's a solid green square with a white uppercase letter "A" in the center.* 23f2005325:

openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid_request_error', 'param': None, 'code': 'invalid_issuer'}}



Possible reasons for this issue:

Not using anand sir’s proxy url for sending requests.
Token not being correct.

    ---

    ### 💬 Post 12 by @23f2005325  
    **Posted on:** 2025-01-25 16:20 UTC  

    yes I was not setting the base url to the proxy. I have fixed it thank you .

    ---

    ### 💬 Post 13 by @23f2005325  
    **Posted on:** 2025-01-25 18:12 UTC  

    While implementing task A5, I am confused about what recent actually means in the phrase “recent log file”, mentioned under task A5, in the problem statement. This confusion arises because there are no dates corresponding to the log files. Should I consider log-0 as the most recent one? or the log-<largest_number> file? Please clarify.

    ---

    ### 💬 Post 15 by @23f2005325  
    **Posted on:** 2025-01-26 10:30 UTC  

    I am getting the following response when I am trying to extract credit card number from the credit-card.png :
{'id': 'chatcmpl-<redacted>', 'object': 'chat.completion', 'created': 1737872397, 'model': 'gpt-4o-mini-2024-07-18', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': "I'm sorry, but I can't assist with that.", 'refusal': None}, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 946, 'completion_tokens': 11, 'total_tokens': 957, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'service_tier': 'default', 'system_fingerprint': '<redacted>', 'monthlyCost': 0.07715699999999998, 'cost': 0.0029040000000000003, 'monthlyRequests': 31, 'costError': 'crypto.createHash is not a function'}

my code is as below :
def extract_credit_card_number():
    import requests
    import base64
    import os
    from dotenv import load_dotenv
    load_dotenv()



    BASE_URL = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ["AIPROXY_TOKEN"]}"
    }

    image_path = "../data/credit_card.png"

    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",  
                "content": "You are a helpful assistant that provides detailed and accurate descriptions of images. Focus on describing the objects, colors, textures, the overall scene, and most importantly, the text and numbers in the image. Be concise but thorough."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "You are given an image containing a credit card number. Extract the credit card number from the image"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
    }

    
    response = requests.post(BASE_URL, headers=headers, json=payload)

    
    if response.status_code == 200:
        result = response.json()
        print("RESULT:", result)
        cno = result["choices"][0]["message"]["content"]
        print("CREDIT CARD NUMBER:", cno)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

please guide @Jivraj @Saransh_Saini

    ---

    ### 💬 Post 16 by @23f1000299  
    **Posted on:** 2025-01-26 17:16 UTC  

    do we have to do these tasks in the linux? As in some of the GA1, the linux answers only accepted. Please tell me that, do we can do it in the desktop or we have to use linux?
@Jivraj @carlton

    ---

    ### 💬 Post 17 by @Saransh_Saini  
    **Posted on:** 2025-01-26 18:10 UTC  

    The bash commands are usually run in a linux machine, but you can easily run those commands in VSCode without installing any virtual machines. Download the WSL extension in VSCode and you will get a WSL terminal to work with.
For more information watch this video https://youtu.be/q74CP4fB7cY?si=M_zw8WzpmMCyVQat or watch TDS Live Sessions.
Regards,
TDS TA

    ---

    ### 💬 Post 18 by @23f1002382  
    **Posted on:** 2025-01-27 01:27 UTC  

    what frameworks can we use? hopefully anything?
or what frameworks can’t we use?
@carlton @Jivraj

    ---

    ### 💬 Post 19 by @carlton  
    **Posted on:** 2025-01-27 03:04 UTC  

    Project 1 deliverables are all that matter. How you accomplish them is not very relevant. The keys to a successful Project 1 are:
Deliverables,
and an example of the Evaluation has been provided.
If your project runs in accordance with the Evaluation methodology then it is considered.
*🖼️ Image description: The image shows instructions for a coding project.  It details the deliverables, including creating a GitHub repository, writing and testing code, creating a Docker image, and publishing it to Docker Hub.  It also includes notes on using an environment variable for an API token and limitations on token usage and model selection.  Finally, it mentions an evaluation section.*Screenshot 2025-01-27 at 8.35.23 am1764×1764 374 KB
Please read the documentation carefully from top to bottom.
So the main question is how do you test if the script will run according to the evaluation? The whole point is for it to run not just on your system. It should be deployable anywhere on any machine. Your solution should work anywhere we test it. Thats why you package it in a docker container. How you achieve that is up to you. But if we cannot run your docker container according to the specification we have provided then it has failed this crucial test.
Kind regards

    ---

    ### 💬 Post 20 by @carlton  
    **Posted on:** 2025-01-27 03:09 UTC  

    @23f1002382
You can use any library as long as your Project 1 meets the deliverable requirements and does all the (20+) API tasks.
Kind regards

    ---

    ### 💬 Post 21 by @s.anand  
    **Posted on:** 2025-01-27 13:32 UTC  

    A sample evaluation script for Project 1 tasks A1-A10 is available at tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub
You can use this to validate your code for Project 1.
Please note:

This is a sample. It WILL change.
Don’t rely on the dataset being the same. It WILL change.
LLMs give different results each time they are called. Make sure:

Your code gives correct results reliably (i.e. try a few times)
Change the task in the evaluation script slightly to test variations


Your AI Proxy usage resets on 1 Feb. You have a limited budget. Utilize what you can this month.
For those who submit their code by Friday, I will run a sample evaluation and share the results.

@carlton @Jivraj @Saransh_Saini - please socialize this during the live sessions.

    ---

    ### 💬 Post 22 by @Divya1  
    **Posted on:** 2025-01-27 14:00 UTC  

    By clicking the project link ,I am getting the notes…but no project is available in my project 1

    ---

    ### 💬 Post 23 by @Divya1  
    **Posted on:** 2025-01-27 14:02 UTC  

    by clicking the link
*🖼️ Image description: The image shows a screen capture of a form asking if a user has seen and attempted Project 1,  with a link provided.  The form has a yes/no option to answer.  There is also a side panel listing "Project 1".*image1198×136 9.49 KB
*🖼️ Image description: A webpage displays details for Project 1: an LLM-based automation agent.  The project description, due date (February 15th, 2025), and a link to a discussion forum are included.  A sidebar lists various tools and projects in data science.*image1750×581 70.9 KB
I am getting this opened.

    ---

    ### 💬 Post 24 by @Jivraj  
    **Posted on:** 2025-01-27 21:30 UTC  

    Hi @Divya1 ,
There won’t be any project1 page such as GA1s, there is a google form(which can be found in same page) which needs to be filled after you do project1.

    ---

    ### 💬 Post 25 by @Jivraj  
    **Posted on:** 2025-01-27 21:57 UTC  

    Hi @23f2005325 ,
Extracting details from credit cards is sensitive, try using strong prompts or take code from LLM and execute it in script.
kind regards

    ---

    ### 💬 Post 26 by @23f1002382  
    **Posted on:** 2025-01-28 08:28 UTC  

    Regarding Wednenday 9-10 pm live session, maybe the instructors could also discuss how to use docker as a virtual environment using maybe ollama(local llm as now there is deepseek opensource, i doubt we would need to use openai for testing, just for production(test submission)  would be enough) and also some agent(langchain, autogen, crewai) just a quick how-to on setting up and problems while setting up if possible
More resources on docker. Using docker as a virtual environment. Editing and executing code in Dockerfiles (like when you change code in src a web framework automatically reloads page(hot reload)), something along the lines of this .
@carlton @Jivraj

    ---

    ### 💬 Post 27 by @Jivraj  
    **Posted on:** 2025-01-28 11:55 UTC  

    *🖼️ Image description: That's a stylized illustration of Monkey D. Luffy from the anime *One Piece*.  He's wearing his iconic straw hat and raising one hand in a celebratory or waving gesture.  The background is a simple, light orange.* 23f1002382:

Regarding Wednenday 9-10 pm live session, maybe the instructors could also discuss how to use docker as a virtual environmen


In Tuesday’s(21 January) session we had discussed docker towards ending of session.
What was discussed in that live session regarding docker:

Search for existing containers on repositories such as dockerhub.
Pull an existing docker image.
Run that image inside a container.
Enter to that container and modify something(such as installing python inside a ubuntu container, for customization or create some file)
Once done you can commit it.
And push customized container’s image to docker hub.

Regarding local models running for project1, it’s a good idea, we will see if it’s possible to discuss in session.

    ---

    ### 💬 Post 29 by @Divya1  
    **Posted on:** 2025-01-28 18:07 UTC  

    In the google forms , I have 2 questions in one form now to submit should it is compulsory that to answer the both the questions?

    ---

    ### 💬 Post 30 by @carlton  
    **Posted on:** 2025-01-29 02:57 UTC  

    Hi @Divya1
*🖼️ Image description: This image shows a list of deliverables for a programming assignment.  The tasks involve creating a public GitHub repository, writing and testing code with POST and GET requests, creating a Dockerfile and publishing the resulting image to Docker Hub, and finally submitting the GitHub repository URL and Docker image name via a Google Form.*Screenshot 2025-01-29 at 8.19.05 am1738×982 122 KB
Please do very carefully all things mentioned in the Deliverables as well as look at the Evaluation Section.
*🖼️ Image description: This image shows the prerequisites for evaluating a repository.  The repository must be publicly accessible on GitHub, contain a LICENSE file with the MIT license, and a valid Dockerfile.  Additionally, the corresponding Docker image must be publicly accessible and runnable via a specified `podman run` command, using the same Dockerfile as the GitHub repository.*Screenshot 2025-01-29 at 8.26.08 am1460×496 45.5 KB
We had a session on 28th Jan introducing all the important aspects of Project.
If you do not do everything exactly as mentioned especially the pre - requisites mentioned in the Evaluation section you will get 0 in the project and there will be no appeal for failing to meet the pre - requisites of the evaluation criteria.
In order for us to evaluate the project you have to provide the deliverables mentioned above.
Kind regards

    ---

    ### 💬 Post 31 by @23f1002382  
    **Posted on:** 2025-01-29 06:32 UTC  

    Subject: Request to Add Instructors to Private GitHub Repo
Message:
"Dear [Instructors’ Names],
I’ve set up the environment and dependencies for the project and was wondering if it would be appropriate to add you to my private GitHub repository. I’d appreciate any guidance on improving performance, scalability, and design principles. Please let me know if this is feasible or if there’s a more suitable way to seek feedback. Apologies if this request is out of scope.
Thank you for your time!
Best,
[Your Name]"*
ChatGPT can make mistakes. Check important info.

    ---

    ### 💬 Post 32 by @s.anand  
    **Posted on:** 2025-01-29 10:41 UTC  

    @23f1002382 - You’re welcome to use the evaluation script in this post for private repos.



*🖼️ Image description: That's a close-up portrait photograph of a man.  He appears middle-aged, with short brown hair and is wearing glasses. The lighting is dramatic, creating shadows on his face.*
Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025] Tools in Data Science


    A sample evaluation script for Project 1 tasks A1-A10 is available at tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub 
You can use this to validate your code for Project 1. 
Please note: 

This is a sample. It WILL change.
Don’t rely on the dataset being the same. It WILL change.
LLMs give different results each time they are called. Make sure:

Your code gives correct results reliably (i.e. try a few times)
Change the task in t…
  

For public repos submitted in the form, I’ll run this script over the weekend and share preliminary results.

    ---

    ### 💬 Post 33 by @23f1002382  
    **Posted on:** 2025-01-29 11:29 UTC  

    T  h  a  n  k      y  o  u         sir.

    ---

    ### 💬 Post 34 by @JoelJeffrey  
    **Posted on:** 2025-01-30 06:20 UTC  

    For A6, /data/docs/ has subfolders with .md files from which we have to extract the heading level 1’s (#) right? Apparently there are few files with different content but the same name. Can someone confirm the same? If yes how to address these files @Jivraj @carlton

    ---

    ### 💬 Post 35 by @23f1002382  
    **Posted on:** 2025-01-30 06:26 UTC  

    I had set up the environment and dependencies and everything was working fine. When i tried to recreate it from scratch in a new codespace it broke. I fixed almost everything except this error
@ANdIeCOOl ➜ /workspaces/TDS-Project-1 (main) $ crewai create crew b2b
Traceback (most recent call last):
  File "/home/codespace/.python/current/bin/crewai", line 5, in <module>
    from crewai.cli.cli import crewai
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/__init__.py", line 3, in <module>
    from crewai.agent import Agent
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agent.py", line 7, in <module>
    from crewai.agents import CacheHandler
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/__init__.py", line 2, in <module>
    from .parser import CrewAgentParser
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/agents/parser.py", line 6, in <module>
    from crewai.utilities import I18N
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/__init__.py", line 13, in <module>
    from .embedding_configurator import EmbeddingConfigurator
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/crewai/utilities/embedding_configurator.py", line 4, in <module>
    from chromadb import Documents, EmbeddingFunction, Embeddings
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/__init__.py", line 6, in <module>
    from chromadb.auth.token_authn import TokenTransportHeader
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/auth/token_authn/__init__.py", line 24, in <module>
    from chromadb.telemetry.opentelemetry import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/chromadb/telemetry/opentelemetry/__init__.py", line 13, in <module>
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/trace_exporter/__init__.py", line 25, in <module>
    from opentelemetry.exporter.otlp.proto.grpc.exporter import (  # noqa: F401
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/exporter/otlp/proto/grpc/exporter.py", line 72, in <module>
    from opentelemetry.sdk.metrics.export import MetricsData
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/__init__.py", line 16, in <module>
    from opentelemetry.sdk.metrics._internal import Meter, MeterProvider
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/__init__.py", line 56, in <module>
    from opentelemetry.sdk.metrics._internal.measurement_consumer import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/measurement_consumer.py", line 29, in <module>
    from opentelemetry.sdk.metrics._internal.metric_reader_storage import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/metric_reader_storage.py", line 26, in <module>
    from opentelemetry.sdk.metrics._internal._view_instrument_match import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/_view_instrument_match.py", line 22, in <module>
    from opentelemetry.sdk.metrics._internal.aggregation import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/aggregation.py", line 48, in <module>
    from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.exponent_mapping import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/exponent_mapping.py", line 25, in <module>
    from opentelemetry.sdk.metrics._internal.exponential_histogram.mapping.ieee_754 import (
  File "/usr/local/python/3.12.1/lib/python3.12/site-packages/opentelemetry/sdk/metrics/_internal/exponential_histogram/mapping/ieee_754.py", line 15, in <module>
    from ctypes import c_double, c_uint64
  File "/usr/local/python/3.12.1/lib/python3.12/ctypes/__init__.py", line 8, in <module>
    from _ctypes import Union, Structure, Array
ImportError: /usr/local/python/3.12.1/lib/python3.12/lib-dynload/_ctypes.cpython-312-x86_64-linux-gnu.so: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0

i updated the libffi package using sudo but while breaking something else can someone pls help me? @carlton @Jivraj @s.anand



history of commands in new codespace
    1  crewai --version
    2  pip install crewai crewai-tools
    3  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    4  export PATH=/opt/conda/bin:$PATH
    5  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    6  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    7  crewai create crew <project_name>
    8  crewai create crew b2b
    9  history



UPDATE: IT’s WORKING if you do this in order
    1  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    2  export PATH=/opt/conda/bin:$PATH
    3  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    4  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    5  pip install --no-cache-dir --force-reinstall typing_extensions pydantic crewai crewai-tools
    6  conda install -c conda-forge typing_extensions
    7  exec bash
    8  crewai create crew "Project 1 - LLM-based Automation Agent"

Something about different environment conda and python can the instructors please help me understand it(resources ), so i can trouble shoot this later with better accuracy come precision

    ---

    ### 💬 Post 36 by @23f1002382  
    **Posted on:** 2025-01-30 12:51 UTC  

    evaluate.py
TDS course repo

*🖼️ Image description: Failed to load image: cannot identify image file <_io.BytesIO object at 0x772a47454db0>*
github.com


tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip ·...
Contribute to sanand0/tools-in-data-science-public development by creating an account on GitHub.





line 20
from datagen import (
    get_markdown,
    get_dates,
    get_contacts,
    get_logs,
    get_docs,
    get_email,
    get_credit_card,
    get_comments,
    get_tickets,
)

but we get datagen.py only in a1 task
line 69
async def a1(email: str, **kwargs):
    await run(
        f"""
Install `uv` (if required) and run the script `https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py`
with `{email}` as the only argument
"""
    )
    return email in await read("/data/format.md")

The issue is importing datagen before ensuring it exists
just checking
@carlton @Jivraj

    ---

    ### 💬 Post 37 by @Jivraj  
    **Posted on:** 2025-01-30 21:37 UTC  

    Hi @23f1002382,
Yes datagen.py must be present in same directory from where you  are executing evaluate.py.
Oh, You trying to use crewai locally for Project1
kind regards

    ---

    ### 💬 Post 38 by @Jivraj  
    **Posted on:** 2025-01-30 21:56 UTC  

    Hi @JoelJeffrey ,
Filepath is unique for every file, which needs to be inserted to json file.

    ---

    ### 💬 Post 39 by @JoelJeffrey  
    **Posted on:** 2025-01-31 06:55 UTC  

    Ok. So just to confirm, since there are files with the same name, the json file should map the filepath and not the filename to the title right?
*🖼️ Image description: The image shows a programming task (A6).  It describes finding all `.md` files in a directory, extracting the first header line from each, and creating a JSON index file mapping filenames to their header titles.  An example of the JSON output is provided.*Screenshot from 2025-01-31 12-25-29790×117 19.9 KB

    ---

    ### 💬 Post 40 by @23f1002382  
    **Posted on:** 2025-01-31 08:40 UTC  

    no crewai, it takes really long i put time out for 300 secs(in run(task:str) in evaluate.py) still sometimes its not enough. I’ll try with autogen next and then langchain

    ---

    ### 💬 Post 41 by @22f3001315  
    **Posted on:** 2025-01-31 08:41 UTC  

    INFO:     127.0.0.1:65085 - "GET /read?path=/data/format.md HTTP/1.1" 200 OK
data/format.md 81ms
INFO:     127.0.0.1:65149 - "POST /run?task=%0AFormat+the+contents+of+%60%2Fdata%2Fformat.md%60+using+%60prettier%403.4.2%60%2C+updating+the+file+in-place%0A HTTP/1.1" 200 OK
INFO:     127.0.0.1:65251 - "GET /read?path=/data/format.md HTTP/1.1" 200 OK
INFO:     127.0.0.1:65263 - "POST /run?task=The+file+%60%2Fdata%2Fdates.txt%60+contains+a+list+of+dates%2C+one+per+line.+Count+the+number+of+Wednesdays+in+the+list%2C+and+write+just+the+number+to+%60%2Fdata%2Fdates-wednesdays.txt%60 HTTP/1.1" 200 OK
INFO:     127.0.0.1:65298 - "GET /read?path=/data/dates-wednesdays.txt HTTP/1.1" 200 OK
INFO:     127.0.0.1:65312 - "POST /run?task=Sort+the+array+of+contacts+in+%60%2Fdata%2Fcontacts.json%60+by+%60last_name%60%2C+then+%60first_name%60%2C+and+write+the+result+to+%60%2Fdata%2Fcontacts-sorted.json%60 HTTP/1.1" 200 OK
INFO:     127.0.0.1:65350 - "GET /read?path=/data/contacts-sorted.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:65361 - "POST /run?task=Write+the+first+line+of+the+10+most+recent+%60.log%60+file+in+%60%2Fdata%2Flogs%2F%60+to+%60%2Fdata%2Flogs-recent.txt%60%2C+most+recent+first HTTP/1.1" 200 OK
INFO:     127.0.0.1:65390 - "GET /read?path=/data/logs-recent.txt HTTP/1.1" 200 OK
INFO:     127.0.0.1:65402 - "POST /run?task=Find+all+Markdown+%28%60.md%60%29+files+in+%60%2Fdata%2Fdocs%2F%60.%0AFor+each+file%2C+extract+the+first+occurrance+of+each+H1+%28i.e.+a+line+starting+with+%60%23+%60%29.%0ACreate+an+index+file+%60%2Fdata%2Fdocs%2Findex.json%60+that+maps+each+filename+%28without+the+%60%2Fdata%2Fdocs%2F%60+prefix%29+to+its+title%0A%28e.g.+%60%7B%22README.md%22%3A+%22Home%22%2C+%22path%2Fto%2Flarge-language-models.md%22%3A+%22Large+Language+Models%22%2C+...%7D%60%29 HTTP/1.1" 200 OK
INFO:     127.0.0.1:65436 - "GET /read?path=/data/docs/index.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:65452 - "POST /run?task=%60%2Fdata%2Fcredit_card.png%60+contains+a+credit+card+number.+Pass+the+image+to+an+LLM%2C+have+it+extract+the+card+number%2C+and+write+it+without+spaces+to+%60%2Fdata%2Fcredit-card.txt%60 HTTP/1.1" 500 Internal Server Error
INFO:     127.0.0.1:65482 - "GET /read?path=/data/credit-card.txt HTTP/1.1" 500 Internal Server Error
INFO:     127.0.0.1:65503 - "POST /run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 HTTP/1.1" 200 OK
INFO:     127.0.0.1:49154 - "GET /read?path=/data/ticket-sales-gold.txt HTTP/1.1" 200 OK

result after running evaluate.py:
*🖼️ Image description: That's a dartboard with a blue dart hitting the bullseye.* Score: 0 / 10
why sir @Jivraj @Saransh_Saini  what is the problem here??
please do a live session of complete project process with one or two tasks if possible

    ---

    ### 💬 Post 42 by @carlton  
    **Posted on:** 2025-01-31 09:04 UTC  

    Hi Guddu,
We are planning several project sessions in order to show the workflow of creating a successful project.
Although you are returning a 200 ok, the get request file must match the expectation. In other words after running the first task for example, has the new format.md been formatted correctly and matches the expected output.
In this case you would write out the the expected variable in the evaluate.py and see if result variable matches the expected. Then you can figure out what went wrong.
Kind regards

    ---

    ### 💬 Post 43 by @22f3001315  
    **Posted on:** 2025-01-31 09:32 UTC  

    Ok sir
But please try to take those sessions sooner
Because it’s taking too much time for me to do any problem(plus two more courses and one oppe you know) .so I just want to build the project before deadline.

    ---

    ### 💬 Post 44 by @23f1002382  
    **Posted on:** 2025-01-31 11:10 UTC  

    Please give the date, time and agenda also please.

    ---

    ### 💬 Post 45 by @carlton  
    **Posted on:** 2025-01-31 11:38 UTC  

    Yes sir ,*🖼️ Image description: That's a stylized yellow emoticon with a hand saluting above it.  The emoticon has a neutral or slightly pleased expression.*
As soon as we know we will send an announcement.
Kind regards.

    ---

    ### 💬 Post 46 by @23f1002382  
    **Posted on:** 2025-02-01 06:48 UTC  

    the model keeps wrong answer, it says uvicorn for uv and has no info on how to run uv even after explicitly giving instructions(basically an older model) , basic “ls” command is also wrong, among other things. You can check your logs with respect to my api key.
Do you think we could access a better model?
Maybe Download Deepseek 70b or even 671b and create an api while y’all run the model locally, in the long it would be cheaper for the course?
because the model doesn’t know basic commands after telling how to do it.
So if the model gives us wrong commands 2/3 times then how would we even solve the question.
I spent a week on this just saying
@s.anand @carlton @Jivraj

    ---

    ### 💬 Post 47 by @23f1002382  
    **Posted on:** 2025-02-01 07:03 UTC  

    sent pull request maybe accept it then please *🖼️ Image description: That's a yellow emoticon with a downturned mouth and neutral eyes.  It expresses mild displeasure or sarcasm.*

    ---

    ### 💬 Post 48 by @23f1002382  
    **Posted on:** 2025-02-01 07:50 UTC  

    *🖼️ Image description: A stylized image depicting various tools used in data science.  The central text reads "TOOLS IN DATA SCIENCE," surrounded by colorful icons representing charts, graphs, and other data-related imagery.*


can we have the code for this session please?
@Jivraj @carlton

    ---

    ### 💬 Post 51 by @23f1002382  
    **Posted on:** 2025-02-02 08:46 UTC  

    i need some help can you send me your repo?

    ---

    ### 💬 Post 52 by @23f3001745  
    **Posted on:** 2025-02-02 19:19 UTC  

    Hello, I recently started working on the project. I understood how to do all the phase A tasks on a high level but I’m struggling to start the implementation of the first task in phase A. I’m confused mainly about how the /data directory is supposed to be created, I don’t know how to generate the data and a little confused about the output formats. I would appreciate if I could get in contact with anyone who could guide me in the right direction.

    ---

    ### 💬 Post 53 by @21f3002390  
    **Posted on:** 2025-02-03 06:42 UTC  

    Hello everyone, @s.anand @carlton
I had a few queries regarding the project;

I am preloading my docker image with uv and generating the /data files when the container is ran. For task A1, I am automating my server to remove the /data directory that’s already present and run datagen.py again. Is this fine?
For /read endpoint, is there a standard for parameters like “path=/data/format.md” or the parameter could be a plain english sentence like “path=show the data in format.md”?
Are we concerned about what’s shown on the console if I run a /run command as long as it gets the job done?
For tasks A1-10, are the file paths provided in the project doc standard or even they’re flexible? Ex. “Count the number of Wednesdays in file /data/format.md, and write just the number to /data/out.txt”

    ---

    ### 💬 Post 54 by @23f1002382  
    **Posted on:** 2025-02-03 08:00 UTC  

    +1

    ---

    ### 💬 Post 55 by @24DS1000121_ULAGAOOZ  
    **Posted on:** 2025-02-03 08:54 UTC  

    Dear Sir,
Can we have a mentorship program for TDS for those who have no experience in programming like me ?
thanks & regards.
ULAGAOOZHIAN

    ---

    ### 💬 Post 56 by @23f2004781  
    **Posted on:** 2025-02-02 10:36 UTC  

    For Project-1 to complete, it requires:
"You MUST complete ALL these 3 steps to get a score. Failure to do so will result in getting 0 in the project. If you do not do ALL these 3 steps before the deadline, there will be no appeal available.
• Fill the form that is on the Project Page
But I did not get the form; where is it? While I checked inside the project pages also.

    ---

    ### 💬 Post 57 by @carlton  
    **Posted on:** 2025-02-03 13:02 UTC  

    Hi Dewang,
*🖼️ Image description: A screenshot shows a project's deliverables and instructions.  The project involves creating a public GitHub repository, writing and testing code (using POST and GET requests), building and publishing a Docker image, and submitting the GitHub repository URL and Docker image name via a Google Form.  Instructions also cover using environment variables for API tokens and specify constraints on prompt length and API call response times.*Screenshot 2025-02-03 at 6.27.39 pm 12268×1766 491 KB
Please read the Project page Deliverables carefully as well as the Evaluation Pre - Requisites.
Kind regards

    ---

    ### 💬 Post 58 by @23f1002382  
    **Posted on:** 2025-02-04 09:04 UTC  

    github.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-


README.md

main

# TDS-Project1-Ollama_FastAPI-
## Info
- Create codespaces on main or evalution script branch
Use history.txt to get sqlite to version 3.45.3 into bash session 
   - 64  export PATH=/opt/conda/bin:$PATH
   - 65  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
   - 66  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"

- cd to latest_ai_development and run cmd [ crewai run] which set up server 
- Then in a separate bash terminal run "python evaluate.py" 
- also make sure to enter openai or sanand api key in crew.py

# Simple history of commands
1. Terminal 1 
    - 1  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    - 2  export PATH=/opt/conda/bin:$PATH
    - 3  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
    - 4  python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
    - 5  cd latest_ai_development/
    - 7  pip install crewai crewai-tools




  This file has been truncated. show original





My take on autonomous agents. Limited by model capabilities to some extent. Will use function calling hence forth but here is a quick look at using crewai for agent tasks.

    ---

    ### 💬 Post 59 by @22f3001315  
    **Posted on:** 2025-02-04 09:55 UTC  

    Sir   @carlton @Jivraj just saying,
If possible Please do 40-50% of project in upcoming live sessions so that we all have atleast something to submit.

    ---

    ### 💬 Post 60 by @Arjun7  
    **Posted on:** 2025-02-05 16:32 UTC  

    I am using ubuntu. How do I use python 3.13. It says my python version is 3.12 even after installing python 3.13
Someone please help

    ---

    ### 💬 Post 61 by @22f3000819  
    **Posted on:** 2025-02-05 18:38 UTC  

    @s.anand sir, I see that the project 1 timeline was changed from February 7 - 17, 2025 to January 17 - February 15 which undoubtedly is a good increase in duration. However, I have my GATE DA exam on Feb 15 and the exam center is unexpectedly far. So, I request you to consider pushing the deadline to at least Feb 16. If not, I’ll still do my best.

    ---

    ### 💬 Post 63 by @21f3002390  
    **Posted on:** 2025-02-06 07:04 UTC  

    Hello! @carlton @s.anand
Is the proxy server down right now?
I am getting this error when I am accessing the endpoint:
{‘id’: ‘chatcmpl-Axq55TzulOVjHYuXYIhkRQzCC3PNl’, ‘object’: ‘chat.completion’, ‘created’: 1738824915, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: …, ‘costError’: ‘crypto.createHash is not a function’}
Or, do I have to install crypto module?

    ---

    ### 💬 Post 64 by @s.anand  
    **Posted on:** 2025-02-06 07:29 UTC  

    @21f3002390 - AI Proxy is working and you did get the result. You can ignore any costError. It won’t happen in the future anyway.
What’s happening? I was trying to generate a unique hash for each request, as a precursor to caching requests. But I made a mistake in the code. Specifically, crypto.createHash is not supported in CloudFlare. I fixed that by removing this. I’ll introduce caching later if required.

    ---

    ### 💬 Post 65 by @23f2005138  
    **Posted on:** 2025-02-06 09:28 UTC  

    For the question #A8 on recognizing the credit card number in the image, Open AI doesn’t seem to be recognizing the number correctly and as a result the evaluation is failing. What should be the solution?
*🖼️ Image description: The image shows a log of a task that extracts a credit card number from an image.  The task uses an LLM, makes POST and GET HTTP requests, and successfully extracts the number, though there's a slight discrepancy between the expected and actual result.*image913×498 13.6 KB

    ---

    ### 💬 Post 66 by @23f2004097  
    **Posted on:** 2025-02-06 12:31 UTC  

    When will live sessions for demo project start? If started please provide link for that as I am unable to get what the project is about and what are the initial steps to start project.

    ---

    ### 💬 Post 67 by @23f2005325  
    **Posted on:** 2025-02-06 20:18 UTC  

    Getting the following error :
127.0.0.1 - - [07/Feb/2025 01:44:54] "GET /run?task=generate%20data%20for%20ujanaishik109@gmail.com HTTP/1.1" 200 -
  File "/tmp/datagenyhqKlO.py", line 1
    404: Not Found
    ^^^
SyntaxError: illegal target for annotation


when executing the following code :
Main.py
@routes.route("/run", methods=["GET", "POST"])
def run():
    task = request.args.get("task")
    try:
        res = get_func_name(task)
        func_name = res["func_name"]
        args = res.get("arguments", [])
        print("ARGUMENTS : ", args)
        if args:
            generated_func = globals()[func_name](*args)
            print("GENERATED FUNC :",generated_func)
            res = f"{func_name} executed successfully"
        else:
            generated_func = globals()[func_name]()
            print(generated_func)
            res = f"{func_name} executed successfully"
    except Exception as e:
        res = None
        print("error : ", e)
    return jsonify(res)


Tasks.py
def generate_data_files(user_email: str):
    subprocess.Popen(
        [
            "uv",
            "run",
            "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py",
            f"{user_email}",
            "--root",
            "../data",
        ]
    )
    print("data generated successfully")

Please Guide @s.anand @carlton @Jivraj

    ---

    ### 💬 Post 68 by @JoelJeffrey  
    **Posted on:** 2025-02-07 07:29 UTC  

    A query regarding the task description in the query given to LLM for phase A.
For task A3, we have been asked to count wednesdays and the python file corresponding to A3 does count for wednesday alone. However the example says the LLM might be asked to count Sundays or other days. Should we be modifying task A3 code? Or was that just an example and only Wednesdays would need to be counted?

    ---

    ### 💬 Post 69 by @23f1002382  
    **Posted on:** 2025-02-07 10:11 UTC  

    @carlton @Jivraj  Please respond .

    ---

    ### 💬 Post 70 by @22f3001777  
    **Posted on:** 2025-02-07 13:37 UTC  

    When will the project session be held? If I have missed it, can I get the recording?
@carlton

    ---

    ### 💬 Post 71 by @carlton  
    **Posted on:** 2025-02-07 14:15 UTC  

    Tuesday is when we are currently planning a project session.
Kind regards

    ---

    ### 💬 Post 72 by @carlton  
    **Posted on:** 2025-02-07 14:21 UTC  

    Tasks in Phase A are defined but that does not mean it has to do one precise thing. If that was the case then there is no use for an LLM.
Your application should be able to take parse the input and be able to run commands that do similar things in parameterised fashion. It could be Wednesdays or Sundays or it might be in Arabic days or anything. So coding to precisely do something very specific is not the goal.
The program has to be intelligent to do a certain type or class of tasks.
We had a session introducing project. Week 3 session 1. But we will have a more hands on session on Tuesday.
Kind regards

    ---

    ### 💬 Post 73 by @23f2003751  
    **Posted on:** 2025-02-07 15:47 UTC  

    the last date of project submission is gonne get extended?

    ---

    ### 💬 Post 74 by @carlton  
    **Posted on:** 2025-02-07 16:03 UTC  

    Project 1 was released over a month ago. So there will be no extension for Project 1

    ---

    ### 💬 Post 75 by @21f3002277  
    **Posted on:** 2025-02-07 16:06 UTC  

    how to handle this error
*🖼️ Image description: A terminal window displays a Python traceback error indicating a `ModuleNotFoundError` for the module 'datagen'.  The error occurred in the file `/tmp/evaluatewEpC39.py` on line 20. The top line shows a user running a script related to OpenAI API and a GitHub repository.*image1425×490 11.1 KB
@carlton @s.anand

    ---

    ### 💬 Post 76 by @22f3001315  
    **Posted on:** 2025-02-07 19:50 UTC  

    expected = sum(1 for date in dates if parse(date).weekday() == 2)
    if result.strip() != str(expected):
        return mismatch("/data/dates-wednesdays.txt", expected, result)
    return True```



*🖼️ Image description: That's a digital image of a shiny, red sphere.  It appears to be a simple, cartoonish rendering.* /data/dates-wednesdays.txt
*🖼️ Image description: That's a yellow triangle with a black exclamation mark inside.  It's a common warning symbol.* EXPECTED:
129
*🖼️ Image description: That's a yellow triangle with a black exclamation mark inside.  It's a common warning symbol.* RESULT:
“129”
If it is expecting str then why throw error sir  ? @carlton @Jivraj
or just tell me how to pass count as an int here
with open(output_file, "w") as f:
        f.write(str(count))

    ---

    ### 💬 Post 77 by @22f2001640  
    **Posted on:** 2025-02-08 08:33 UTC  

    @s.anand @carlton @Jivraj
I am getting below error message from LLM end points https://api.openai.com/v1/chat/completions or https://aiproxy.sanand.workers.dev/openai/v1/embeddings , while running my project .
*🖼️ Image description: That's a JSON representation of an API error message.  The error code is 429, indicating a rate limit was exceeded. The message specifies that on February 2025, a limit of $2 was exceeded by using $2.002295600000011.*
Kindly help me to resolve this issue. *🖼️ Image description: That's a yellow emoticon with a single tear rolling down its cheek.  It has a downturned mouth and arched eyebrows, conveying sadness.*

    ---

    ### 💬 Post 78 by @23f2005138  
    **Posted on:** 2025-02-08 10:13 UTC  

    @carlton Will there be evaluation script for tasks in group B also?
Some questions about ‘B’ group tasks:
Q1: For the following tasks (B5, B7, B9, and B10) tasks, how will input files be provided? Will it be URL or will datagen.py also generate files for these?
Q2: For the above tasks as well as for B6 ( Extract data from (i.e. scrape) a website), how should output be returned?
Q3: In task B8, for transcribing audio file, which Python package is recommended or do we need to use OpenAI API?
B5. Run a SQL query on a SQLite or DuckDB database
B7. Compress or resize an image
B8. Transcribe audio from an MP3 file
B9. Convert Markdown to HTML
B10. Write an API endpoint that filters a CSV file and returns JSON data

    ---

    ### 💬 Post 79 by @22f3001315  
    **Posted on:** 2025-02-08 10:14 UTC  

    its expecting to  match every single detail in that even " and ’ .
in that case changing evaluate.py will result in zero or less marks.
llm will only handle  -calling function based on query and parameter   . What is it going to do about the logic of functions.
If i still focus on passing evaluate.py will it be any good sir @carlton @s.anand
🔴 /data/contacts-sorted.json
⚠️ EXPECTED:
[{'first_name': 'Kevin', 'last_name': 'Aguirre', 'email': 'ricardocarlson@example.net'}, {'first_name': 'Andrew', 'last_name': 'Anderson', 'email': 'kimberly08@example.com'}, {'first_name': 'Robert', 'last_name': 'Arnold', 'email': 'hunterpamela@example.com'}, {'first_name': 'Isaac', 'last_name': 'Barker', 'email': 'jessicabriggs@example.net'}, {'first_name': 

My output was in good looking structured form but I had to make it look like this just to pass the evaluation.
⚠️ RESULT:
[{"first_name": "Kevin", "last_name": "Aguirre", "email": "ricardocarlson@example.net"}, {"first_name": "Andrew", "last_name": "Anderson", "email": "kimberly08@example.com"}, {"first_name": "Robert", "last_name": "Arnold", "email": "hunterpamela@example.com"}, {"first_name": "Isaac", "last_name": "Barker", "email": "jessicabriggs@example.net"}, {"first_name": "Anthony", "last_name": "Barrett", "email": "kevinknox@example.org"}, {"first_name": "Monique", "last_name": "Bass", "email": "lindsaymcgrath@example.net"}, {"first_name": "Michael", "last_name": "Berry", "email": "an

    ---

    ### 💬 Post 81 by @23f2003751  
    **Posted on:** 2025-02-09 06:06 UTC  

    Sorry, sir, not trying to be rude, but there isn’t a single full-fledged project session. It’s a bit difficult to dive into the project without guidance on how to do it. It would be nice to have a full project session where we can start a project from the beginning and follow it to completion.
@carlton @Jivraj @s.anand

    ---

    ### 💬 Post 82 by @Yogesh1  
    **Posted on:** 2025-02-09 06:33 UTC  

    Yes. I am very worried about this project. I have been trying to do this. But have gotten nowhere until now.

    ---

    ### 💬 Post 83 by @22f2001590  
    **Posted on:** 2025-02-09 08:10 UTC  

    @carlton sir I request you demonstrate atleast few tasks, I spent last 2 days trying to implement but din’t reach anywhere, its really demotivating sir.

    ---

    ### 💬 Post 84 by @akashkunwar  
    **Posted on:** 2025-02-09 09:38 UTC  

    Can you please demonstrate it by just doing One task or provide sample example code of 1 similar task in the way you explained here. It will be very helpful right now it is very confusing.

    ---

    ### 💬 Post 85 by @carlton  
    **Posted on:** 2025-02-09 10:30 UTC  

    We will be doing project session on Tuesday 9 Feb [correction] Tuesday 11th of Feb (thanks @23f1002382 @23f2000237) . Project 1 uses the things you learnt in week 1-3. But mostly week 2 & 3.
We dont do it in the beginning, (but introduced it 2 weeks ago in a live session), to give students chance to practise the new learnings from week 2 & 3.
The plan has always been to demonstrate a few tasks and have you try doing the rest.
Kind regards

    ---

    ### 💬 Post 86 by @22f2001640  
    **Posted on:** 2025-02-09 10:41 UTC  

    @s.anand @carlton @Jivraj
I am getting below error message from LLM end points https://api.openai.com/v1/chat/completions or https://aiproxy.sanand.workers.dev/openai/v1/embeddings , while running my project .
*🖼️ Image description: The image shows an API error message.  The error code is 429, indicating a rate limit has been exceeded. The message explains that on 2025-02, $2.002295600000011 was used, exceeding a limit of $2.*
Kindly help me to resolve this issue. I am unable to proceed with my project.

    ---

    ### 💬 Post 88 by @23f2000237  
    **Posted on:** 2025-02-09 11:07 UTC  

    Today’s 9th Feb and it’s a Sunday.

    ---

    ### 💬 Post 89 by @23f2000983  
    **Posted on:** 2025-02-09 15:27 UTC  

    *🖼️ Image description: That's a close-up portrait of a man with short, light brown hair. He appears to be middle-aged, and is wearing glasses.  The lighting is somewhat dramatic, casting shadows on his face.* s.anand:

Update: 27 Feb 2025:


Sir, does this mean 27th is submission deadline?

    ---

    ### 💬 Post 90 by @carlton  
    **Posted on:** 2025-02-10 02:01 UTC  

    Hi Aindree,
No its a typo (and will be corrected soon). In the context of what was written it clearly means it was updated on 27th January. The update being that the evaluation.py file was provided so that you could test your code against it.
Thanks for bringing it to our attention.
Kind regards

    ---

    ### 💬 Post 91 by @JoelJeffrey  
    **Posted on:** 2025-02-10 05:47 UTC  

    Hi
This would be only for a selected few questions right because say for the credit card question, where the LLM is involved, to get the card number itself, we have to give a fine-tuned and strong query.

    ---

    ### 💬 Post 92 by @23f2000237  
    **Posted on:** 2025-02-10 09:14 UTC  

    Try using the eval() function, that seemed to work for me

    ---

    ### 💬 Post 93 by @23f2005138  
    **Posted on:** 2025-02-10 10:38 UTC  

    @carlton @s.anand @Jivraj  Sir, could you please share some guidance on the above?

    ---

    ### 💬 Post 94 by @23ds1000022  
    **Posted on:** 2025-02-10 11:26 UTC  

    @jivraj,@carlton
I have done the a1 to a10 task and tried querying through localhost and its working fine basically all these ten steps but dont know whether its enough or not. also steps in phase B i am confused that should we create separate endpoints for these tasks or should it be with same /run endpoint and query. then will the input be random by any user. what about the output . where should it be given. phase b needs more explanation.

    ---

    ### 💬 Post 95 by @23f2001305  
    **Posted on:** 2025-02-10 11:35 UTC  

    At what time will the session be happening tomorrow sir can you please give the details?

    ---

    ### 💬 Post 96 by @apanjwani  
    **Posted on:** 2025-02-10 14:27 UTC  

    Hi @carlton @Jivraj
Facing some issues in running my project. Taking an example of the Phase A - A3 task.
I am able to read my files through the GET/read/data/dates.txt query.
I am also able to use the count_wednesdays function through the POST/run task/count_wednesdays.
But when I am entering a query such as “count_wednesdays in data/dates.txt” I am unable to get a response.
*🖼️ Image description: The image shows a code response with a status code of 200 and an error message indicating that the task could not be understood.*image618×246 6.28 KB
Please advice. Thank you.

    ---

    ### 💬 Post 97 by @23f1000299  
    **Posted on:** 2025-02-10 17:09 UTC  

    *🖼️ Image description: The image shows instructions for two tasks:  extracting an email address from a file and writing it to another file, and extracting a credit card number from an image using an LLM and saving it to a file without spaces.*image1215×112 19 KB
On task A8, credit-card.png is given, but it is in credit_card.
it makes the errors. I checked that 2 to 3 tasks depend on these, and we create the ouput file with ‘-’ this only. please clarify that output and input files name ‘-’ or ‘_’   @carlton @Jivraj

    ---

    ### 💬 Post 98 by @23f1000299  
    **Posted on:** 2025-02-10 17:13 UTC  

    On tomorrow live sessions, kindly explain how to use docker, evaluations, github, what generally we have to do submit, please get some tuturials for us to submit those answers. Thankyou Sir  @Jivraj @carlton

    ---

    ### 💬 Post 99 by @23f1002382  
    **Posted on:** 2025-02-10 18:51 UTC  

    (post deleted by author)

    ---

    ### 💬 Post 100 by @23f1002382  
    **Posted on:** 2025-02-10 21:15 UTC  

    (post deleted by author)

    ---

    ### 💬 Post 101 by @23f1002382  
    **Posted on:** 2025-02-10 21:25 UTC  

    (post deleted by author)

    ---

    ### 💬 Post 102 by @23f1002382  
    **Posted on:** 2025-02-10 21:59 UTC  

    *🖼️ Image description: That's a simple image of a dartboard with a dart in the bullseye.  The dartboard is red and white, and the dart is blue.* Score: 9 / 10
Almost done with A tasks. Please use this for local llm to verify output
Also Ollama doesn’t require Schemas
CHECK OUT THE REPO AND ANY INPUTS ARE WELCOME
Link to ReadMe and also repo

    ---

    ### 💬 Post 103 by @carlton  
    **Posted on:** 2025-02-11 03:51 UTC  

    Hi Andrew,
You have done a great job with the Phase A tasks. Very methodical, well structured, logical and even incorporates (unnecessarily) two different ways of evaluating its performance via local llm or the project proxy.
I just want to forewarn you (and others who are tempted to just blindly copy and paste) that evaluate.py is not meant to give you an exact expectation of what prompts will be sent to your application.
In other words getting 10/10 in evaluate.py does NOT guarantee 10/10 or even 5/10  or 1/10 in the real evaluation.
So do not write your code so rigidly that it will only work in the very strict interpretation of evaluate.py. It has always been meant to give you a feel for what to aim for. Your code should be flexible enough to deal with the general idea of the task.
That said, evaluate.py is a good way to know what to expect. Some of Phase A tasks although given a detailed specification in the project description, will still be given challenging prompts (i.e. hard difficulty, and requires some clever self correcting mechanism). Some of the tasks will be given straight forward prompt (i.e. easy for your application).  Some of the tasks will be given with some level of parameterisation that deviates from the strict interpretation (i.e. medium difficulty).
Hope that helps with how you deal with Phase B tasks (and making your Phase A more robust to a stronger evaluation.)
A word of caution: (i.e. this is just some advice, not a set in stone recommendation) Your requirements.txt is massive. If your code does not execute a task (possibly your first task) within 20 seconds (on our server) then it will fail that task. You might want to consider a dynamic, flexible way of installing only required libraries when necessary and keeping the image footprint small and efficient, as we will necessarily have limits on how big we allow images to grow since we have to run and evaluate hundreds of images automatically.
Kind regards

    ---

    ### 💬 Post 105 by @22f2001640  
    **Posted on:** 2025-02-11 07:01 UTC  

    Respected @s.anand @carlton and @Jivraj ,
Is anyone actively monitoring the Discourse page? I have been raising this issue for the past few days, but there has been no response. Does this mean the TAs are not addressing students’ concerns?
I am encountering the following error while running my project with these LLM endpoints:

https://api.openai.com/v1/chat/completions
https://aiproxy.sanand.workers.dev/openai/v1/embeddings
*🖼️ Image description: The image shows a JSON object representing an API error.  The error code is 429, indicating a rate limit has been exceeded.  The message explains that on 2025-02, $2.002295600000011 was used, exceeding a limit of $2.*
This issue is blocking my progress, and I urgently need assistance to resolve it. Kindly provide guidance or suggest a solution at the earliest.

Looking forward to your response.
Thanks,
Telvin Varghese

    ---

    ### 💬 Post 106 by @Kratikajain  
    **Posted on:** 2025-02-11 07:17 UTC  

    Hi,
I am not able to understand how to do the Project 1. The date is also very near.
The problem I am facing is, When I did the Modules the page was different, but now in the Project 1 I am not getting any section to submit the project.
Please let me know where are the questions and how tot submit that.
The deadline is near.

    ---

    ### 💬 Post 107 by @23f1002382  
    **Posted on:** 2025-02-11 07:18 UTC  

    *🖼️ Image description: That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow or beige.* carlton:

o do not write your code so rigidly that it will only work in the very strict interpretation of evaluate.py. It has always been meant to give you a feel for what to aim for. Your code should be flexible enough to deal with the general idea of the task.


This where I need help, i tried doing with agentic framework but i failed with the model in llm proxy, which was highly suspect because, that model should have known what the uv framework but it seemed to me to be outdated. Hence executing code Interpreter tools failed as the model gave outdated code. I have raised this issue before
Hence i moved to function calling, using local llms as cost-effective solution and it was quite robust.
I just need to understand how the function should be general, maybe 2-3 tasks you could provide the general description along with all the ways one would query the agent llm(ie our project). This general function is what i need help with. Please kindly do the needful.

    ---

    ### 💬 Post 108 by @21f2000709  
    **Posted on:** 2025-02-11 07:54 UTC  

    *🖼️ Image description: That's a headshot of a man with short dark hair and glasses. He's wearing a purple collared shirt and has a slight smile.  The background is a plain, light yellow or beige.* carlton:

keeping the image footprint small and efficient, as we will necessarily have limits on how big we allow images to grow since we have to run and evaluate hundreds of images automatically.


Any tentative size cutoff for the docker image?

    ---

    ### 💬 Post 109 by @carlton  
    **Posted on:** 2025-02-11 10:14 UTC  

    Hi Telvin
You have run out of tokens. Thats what the message is saying. You ran out 3 days ago. It was clearly mentioned that the limit is $1. You have exceeded $2.
*🖼️ Image description: This is a webpage section about Large Language Models (LLMs).  It explains that using LLMs incurs a cost, but API keys are provided with a usage limit of $1 per calendar month.  Instructions are given on how to use an AI proxy instead of OpenAI, requiring a replacement of API and key information.  The page includes navigation links (Previous, Next) and a sidebar with related tools and resources.*Screenshot 2025-02-11 at 3.36.50 pm2078×1276 305 KB
In our current internal build of project 1, we have yet to exceed $0.50
As to whether it can be renewed is something we have still not yet decided, because the question you have raised equally would apply to everyone. Raising it for you means raising it for everyone. $1 for everyone equals raising it by $1600+ (i.e Rs 1.39 Lakhs) for us!
The budget question then involves more than one person. It also involves the BS Team Operations and not just the TDS team and therefore instead of responding with a response that is not useful, we typically try to solve the problem first and then respond.
In short we are working on it. But as we have mentioned repeatedly in our sessions, use APIs efficiently, thats part of the skill. As soon as we have a resolution we will inform everyone via an announcement and an email.
Kind regards

    ---

    ### 💬 Post 110 by @22f2001640  
    **Posted on:** 2025-02-11 10:34 UTC  

    Thanks for your response, @Carlton. It seems I won’t be able to proceed with the project until this issue is resolved. Also, I haven’t used LLM so much until February 7th to cost $2.

    ---

    ### 💬 Post 111 by @carlton  
    **Posted on:** 2025-02-11 10:43 UTC  

    Every request you send, gives you a response back with exactly how much that request cost. So you can track your usage.

    ---

    ### 💬 Post 112 by @22f2001640  
    **Posted on:** 2025-02-11 11:08 UTC  

    I’m aware of that. I’ve mostly noticed a cost of $0.0003 per request, so I haven’t been tracking my total monthly expenses. Moving forward, I’ll keep a record of the cost for each request. Also, do strong prompts impact the overall cost?

    ---

    ### 💬 Post 113 by @21f2000709  
    **Posted on:** 2025-02-11 11:32 UTC  

    @carlton Is the project session happening today? I don’t have the link. Can you please send it if it’s happening?

    ---

    ### 💬 Post 114 by @apanjwani  
    **Posted on:** 2025-02-11 11:34 UTC  

    Hi, where is the link for todays Project 1 demo session? @carlton @Jivraj

    ---

    ### 💬 Post 115 by @23f2000573  
    **Posted on:** 2025-02-11 11:37 UTC  

    https://meet.google.com/odh-ycbm-ahj?authuser=0

    ---

    ### 💬 Post 116 by @22f3002786  
    **Posted on:** 2025-02-11 11:46 UTC  

    request
http://localhost:8000/run?task=Extract the sender's email from /data/email.txt and write to /data/email-sender.txt](http://localhost:8000/run?task=Extract the sender's email from /data/email.txt and write to /data/email-sender.txt)

output
{    "detail": "Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid\_request\_error', 'param': None, 'code': 'invalid\_issuer'}}"}

@carlton sir I am getting this issue while running my script. Please help!

    ---

    ### 💬 Post 117 by @23f2000983  
    **Posted on:** 2025-02-11 12:19 UTC  

    I’m getting an error in task a2, def do_a2():
“”“Format markdown using prettier”“”
format_md_path = DATA_ROOT / “format.md”
subprocess.Popen([“prettier”, str(format_md_path), “–write”, “–parser”, “markdown”])
print(“data formatted successfully”)
any idea how to fix this? Also in A8, a 5 and a 3 is getting interchanged. Can someone help why that is hapening, I changed the prompt to include caution about not switching 3 and 5 as well, that didn’t help either

    ---

    ### 💬 Post 118 by @22f2000113  
    **Posted on:** 2025-02-11 12:35 UTC  

    what is  the session time?

    ---

    ### 💬 Post 119 by @23f1002104  
    **Posted on:** 2025-02-11 12:45 UTC  

    *🖼️ Image description: The image shows a terminal displaying a Python traceback error.  The error, a `PermissionError`, indicates a lack of permission to create the directory '/data'.  The traceback shows the error originated in the `makedirs` function within a script downloaded from a GitHub URL.*Screenshot 2025-02-11 1814531459×207 15.3 KB
Could you kindly help me with this

    ---

    ### 💬 Post 120 by @23f1001524  
    **Posted on:** 2025-02-11 15:23 UTC  

    in checking for the task of json my code is outputting json with double quotes (valid json) and evaluate.py has exact same json but with single quotes , what should I do?

    ---

    ### 💬 Post 121 by @23f1002382  
    **Posted on:** 2025-02-11 15:26 UTC  

    check out my repo and download the datagen and evaluate file for testing

    ---

    ### 💬 Post 122 by @23f1002382  
    **Posted on:** 2025-02-11 15:27 UTC  

    it should work, use fastapi text response when /read api

    ---

    ### 💬 Post 123 by @22f2000113  
    **Posted on:** 2025-02-11 16:22 UTC  

    Has anyone used a local LLM for testing? If so, could you please share the request URL and the request body format? I attempted to use a local LLM, but I was unable to succeed

    ---

    ### 💬 Post 124 by @23f1002382  
    **Posted on:** 2025-02-11 17:07 UTC  

    use ollama it is openai api compatible, supports function calling without json schema for tool usage. Check it out

    ---

    ### 💬 Post 125 by @23f1002382  
    **Posted on:** 2025-02-11 18:04 UTC  

    NEED HELP. CAN SOMEONE CONTACT OLLAMA AND ASK THEM TO CHECK THEIR CODE ITS HAS SOME SILLY MISTAKES IN CODE EXAMPLES. I DONT KNOW HOW TO DO IT.
LINK TO PAGE WITH CODE EXAMPLE
*🖼️ Image description: The image shows Python code for storing documents in a vector embedding database using the `ollama` library and then retrieving the most relevant document based on an example prompt.  The code first generates embeddings for each document and then uses those embeddings to search the database for the closest match to a given query.*Screenshot 2025-02-11 232608919×714 22.4 KB

correct code in step 2 collection query step
response = ollama.embed(
  model="nomic-embed-text:latest",
  input=task
)
results = collection.query(
  query_embeddings=response["embeddings"], #here embeddings and also not list of list as response embeddings already gives correct format
  n_results=1
)
data = results['documents'][0][0]

@s.anand @Jivraj @carlton

    ---

    ### 💬 Post 126 by @23f2005325  
    **Posted on:** 2025-02-11 19:51 UTC  

    @s.anand @carlton @Jivraj
While implementing the Phase B tasks, can I take the data (csv file, git repo, audio, sqlite/duckdb database, website, image and markdown file) of my choice and perform any operation on them as long as they meet the critetia mentioned in the Phase B task list? Please guide.

    ---

    ### 💬 Post 127 by @23f2005325  
    **Posted on:** 2025-02-11 20:29 UTC  

    @s.anand @carlton @Jivraj
In the Task B5, where we have to run an SQL query on a sqlite or duckdb database, should I create a database on my own and then take the query to be ran on it as an argument? Or should I take the query as an argument and run it on the ticker_sales.db in ./data folder? Please guide

    ---

    ### 💬 Post 128 by @23f2001978  
    **Posted on:** 2025-02-11 21:56 UTC  

    same issue on my side as well

    ---

    ### 💬 Post 129 by @23f2001978  
    **Posted on:** 2025-02-11 22:23 UTC  

    on using the AIPROXY_TOKEN from here https://aiproxy.sanand.workers.dev/
getting this error :
Error: Your authentication token is not from a valid issuer.
@carlton @Jivraj  please help!

    ---

    ### 💬 Post 130 by @Yogesh1  
    **Posted on:** 2025-02-12 00:20 UTC  

    @carlton @Jivraj Can the link to the live session (for project) be provided?

    ---

    ### 💬 Post 131 by @23f2004752  
    **Posted on:** 2025-02-12 00:57 UTC  

    As in the previous session for task a1 we use llm just to get the url and email , so after retriving the both arguments can i use them in a function and got the work given in work done in function.
Also, am i correct that we use llm only to retrive url or location ??
@carlton @Jivraj

    ---

    ### 💬 Post 132 by @23f2004752  
    **Posted on:** 2025-02-12 01:27 UTC  

    Anyone whom have done have done any one task of phase a and one task of phase b, please help…

    ---

    ### 💬 Post 133 by @23f2004752  
    **Posted on:** 2025-02-12 01:47 UTC  

    Can you do one task from each phase in today’s session. Please @carlton @Jivraj

    ---

    ### 💬 Post 134 by @22f2000113  
    **Posted on:** 2025-02-12 02:13 UTC  

    thanks for the reply I will check

    ---

    ### 💬 Post 135 by @thinkmachine  
    **Posted on:** 2025-02-12 03:29 UTC  

    TDS project *🖼️ Image description: That's a red "X" symbol on a black background.  The X is slightly rounded and has a three-dimensional appearance.* Tedious project *🖼️ Image description: That's a light green square button with a large white checkmark in the center.  It's a common symbol indicating completion, confirmation, or approval.*

    ---

    ### 💬 Post 136 by @AnvithaV  
    **Posted on:** 2025-02-12 05:12 UTC  

    can anyone share the link of yesterdays live session if there in youtube

    ---

    ### 💬 Post 137 by @23f2004042  
    **Posted on:** 2025-02-12 05:16 UTC  

    Its updated in the TDS live sessions playlist


*🖼️ Image description: The image shows a graphic announcing "Week 5 Session 1".  The announcement is overlaid on a background of colorful, stylized icons related to data, technology, and design.*

    ---

    ### 💬 Post 138 by @Adithya  
    **Posted on:** 2025-02-12 06:27 UTC  

    For task A2:

A2. Format the contents of /data/format.md using prettier@3.4.2, updating the file in-place

I am getting the following error:
🔴 A2 failed: Command '['npx', 'prettier@3.4.2', '--stdin-filepath', '/data/format.md']' returned non-zero exit status 1.
However, running a POST request to https://localhost:8000/run?task=Format+/data/format.md+with+prettier+3.4.2 gives successful output.
{"success":true,"message":"Formatted and verified successfully!"}% 
Here is my code snippet:
def format_file(filepath):
    while True:  # Loop until formatting and verification pass
        try:
            result = subprocess.run(
                ["npx", "prettier@3.4.2", "--write", filepath],
                check=False,  # Don't raise exception automatically
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                return {"success": False, "message": f"Prettier write failed: {result.stderr}"}

            if verify_prettier_formatting(filepath):
                return {"success": True, "message": "Formatted and verified successfully!"}
            else:
                logging.info("Verification failed. Retrying formatting...") #Log the retry
                # If verification fails, the loop continues and prettier --write is executed again.

        except Exception as e:
            return {"success": False, "message": str(e)}

def verify_prettier_formatting(filepath):
    try:
        subprocess.run(["npx", "prettier@3.4.2", "--check", filepath], check=True, capture_output=True, text=True) #Capture output
        return True  # File is formatted correctly
    except subprocess.CalledProcessError as e:
        logging.error(f"Prettier check failed: {e.stderr}") # Log the error from prettier check
        return False  # File is not formatted correctly

What am I missing here?

    ---

    ### 💬 Post 139 by @22f3001307  
    **Posted on:** 2025-02-12 07:05 UTC  

    I am getting the same error. Did you find any solution?

    ---

    ### 💬 Post 140 by @21f2000709  
    **Posted on:** 2025-02-12 07:08 UTC  

    Has anyone succeeded in the extraction of credit cards details task? The LLM seems to consider it as illegal task and if I use pytessaract the docker image size will become really large. What to do in this case?
@carlton @Jivraj

    ---

    ### 💬 Post 141 by @22f3001307  
    **Posted on:** 2025-02-12 07:12 UTC  

    Hi @carlton @Jivraj,
I followed what you taught in Feb 11 session and tried implementing task A1. My understanding is once i run the subprocess, datagen.py file should be run and /data folder should be created in the project folder. But it is not happening to me. I am getting the following error
Traceback (most recent call last):
  File "/var/folders/rj/z_3b8hl51558519w90k5hp600000gn/T/datagen4COEF3.py", line 284, in <module>
    os.makedirs(config["root"], exist_ok=True)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen os>", line 227, in makedirs
OSError: [Errno 30] Read-only file system: '/data'

If i can’t automate this process, i don’t see the point writing code for other tasks. Can anyone help me solving this error?

    ---

    ### 💬 Post 142 by @23f1002382  
    **Posted on:** 2025-02-12 07:22 UTC  

    shell = true in evaluate.py, remove it meaning comment it out, task a2 thats causing the error

    ---

    ### 💬 Post 143 by @23f1002382  
    **Posted on:** 2025-02-12 07:25 UTC  

    the admin banned me from using laughing emoji  @jkmadathil

    ---

    ### 💬 Post 144 by @JoelJeffrey  
    **Posted on:** 2025-02-12 08:44 UTC  

    For task A6,

HTTP Request: GET http://localhost:8000/read?path=/data/docs/index.json “HTTP/1.1 200 OK”

⚠️ EXPECTED:
{'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/culture.md': 'Prevent north only miss cold.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/family.md': 'Debate at office traditional stop great.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/bar.md': 'Among ago cover good.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/story.md': 'Anything song key first.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'drop/former.md': 'Brother college detail.', 'drop/add.md': 'Fish work to individual.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/else.md': 'Fly candidate may so college.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/ready.md': 'Central about ready information.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/question.md': 'Family evening its degree.', 'civil/argue.md': 'Line culture seven six.', 'civil/gas.md': 'Talk why around necessary.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/central.md': 'Believe region their our whatever.', 'standard/easy.md': 'Myself must detail win.', 'standard/sound.md': 'Night national film next.', 'standard/five.md': 'Lay would green generation season.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/late.md': 'Scientist people may story.', 'standard/level.md': 'Work around ask to.', 'standard/analysis.md': 'While natural from staff option artist can.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/sometimes.md': 'Big order defense field represent.', 'few/weight.md': 'Man mission American.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/my.md': 'Open line address contain whole impact into front.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/southern.md': 'Meet prove admit.', 'few/theory.md': 'Security effort protect future task long close.', 'few/information.md': 'Really morning yeah.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/save.md': 'Thought hear home set employee early purpose.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/book.md': 'Mr oil difficult dog.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/cold.md': 'Election buy member alone school audience.', 'community/else.md': 'Actually service thank state.', 'community/left.md': 'Picture let tell never.', 'community/soldier.md': 'It lawyer cover job.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'Congress/remember.md': 'Purpose good policy line trade.', 'ten/rock.md': 'Method wall when book agency.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/nature.md': 'Eight own hot first success.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/serve.md': 'Want exist bank book.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/white.md': 'Whatever significant capital air about.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/own.md': 'Say small finish sing raise.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/discuss.md': 'Hit result find miss culture heart clear task.'}

⚠️ RESULT:
{'suddenly/mouth.md': 'Outside food subject positive human.', 'suddenly/add.md': 'Window word during born do finally.', 'suddenly/free.md': 'Them ball significant different which traditional.', 'suddenly/management.md': 'Man fire long hour modern.', 'suddenly/leave.md': 'Season people Democrat hand among too.', 'suddenly/low.md': 'Front actually decision security fast song believe leg.', 'suddenly/why.md': 'Account listen such day method sing.', 'suddenly/miss.md': 'Rather although team thank.', 'suddenly/base.md': 'Total low room structure staff.', 'suddenly/strategy.md': 'Never understand less operation onto still trade environment.', 'ground/girl.md': 'Civil speech back sell.', 'ground/game.md': 'Fill whose card or daughter old meet.', 'ground/term.md': 'Pick return put set.', 'ground/every.md': 'Free service trouble effort somebody blood modern.', 'ground/along.md': 'Important plant increase door much.', 'ground/call.md': 'Article agent three scientist.', 'ground/do.md': 'Memory food strategy meeting.', 'ground/end.md': 'Large player discussion similar prove part.', 'ground/full.md': 'Actually start commercial.', 'ground/ever.md': 'Human example gun now my just Republican.', 'way/not.md': 'Decision together land chair.', 'way/morning.md': 'Information later service raise after trial base.', 'way/responsibility.md': 'Our child why environment care goal.', 'way/increase.md': 'Return say response political.', 'way/relationship.md': 'General view thing poor machine market peace.', 'way/soldier.md': 'Produce table should will school produce player wall.', 'way/act.md': 'Smile guess simple read style its international.', 'way/sound.md': 'Conference first finally recognize as.', 'way/reach.md': 'Exactly size discuss management miss article.', 'way/hotel.md': 'From become actually.', 'hit/run.md': 'Stock several region put thought decade evening.', 'hit/free.md': 'Crime usually produce.', 'hit/foot.md': 'Ball specific trip state.', 'hit/ball.md': 'Condition color focus traditional.', 'hit/song.md': 'Section environmental final light word in yes operation.', 'hit/since.md': 'Shoulder wrong matter seek cultural vote themselves.', 'hit/safe.md': 'Hear try spend item can along light.', 'hit/much.md': 'Guess great dream through concern feel.', 'hit/prove.md': 'Her base cup forward.', 'hit/stop.md': 'Nation this avoid herself deal place memory.', 'few/sometimes.md': 'Big order defense field represent.', 'few/southern.md': 'Meet prove admit.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/weight.md': 'Man mission American.', 'few/information.md': 'Really morning yeah.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/theory.md': 'Security effort protect future task long close.', 'few/my.md': 'Open line address contain whole impact into front.', 'resource/rest.md': 'Ok tough talk.', 'resource/move.md': 'Law write democratic drug itself house accept through.', 'resource/particularly.md': 'Affect woman nice.', 'resource/entire.md': 'Focus to once sea friend group.', 'resource/painting.md': 'Customer environment none trade.', 'resource/structure.md': 'Stuff return protect our bit reality.', 'resource/until.md': 'Growth industry region receive.', 'resource/significant.md': 'Long million fall throughout government tend.', 'resource/hospital.md': 'Quality certain fight want much body between.', 'resource/marriage.md': 'Foot specific mission.', 'for/hope.md': 'Whatever report wife fly close lot student.', 'for/poor.md': 'Explain claim police eye paper much when.', 'for/assume.md': 'Control yeah effect local economy worry.', 'for/couple.md': 'Floor both take indeed audience.', 'for/money.md': 'Join live next care material.', 'for/never.md': 'Me natural full.', 'for/situation.md': 'Show book instead hope lawyer.', 'for/north.md': 'Card level kind send loss growth.', 'for/hit.md': 'Minute wish above pass just later watch.', 'for/perhaps.md': 'Every professor sport unit rock bed.', 'project/individual.md': 'Tough safe machine small outside mention could must.', 'project/change.md': 'Century drug value.', 'project/home.md': 'Big decade edge feeling surface matter force student.', 'project/want.md': 'Region catch nation civil one Mr specific.', 'project/something.md': 'Major control three.', 'project/reality.md': 'Mouth including fine.', 'project/my.md': 'Fire point or success marriage write example.', 'project/issue.md': 'Former true career similar use visit machine.', 'project/surface.md': 'Cold reduce task life American act stage.', 'project/drug.md': 'Reason still field animal.', 'effort/morning.md': 'Policy quickly get capital smile.', 'effort/he.md': 'Thought view product interview explain.', 'effort/house.md': 'High hear thought according.', 'effort/church.md': 'Culture ask change focus.', 'effort/effect.md': 'Before suddenly who student could boy serve.', 'effort/price.md': 'Shoulder financial public reason home explain safe.', 'effort/company.md': 'Exactly treatment concern fly factor care drive.', 'effort/international.md': 'Rich take hear open.', 'effort/federal.md': 'Difference rate character by his blood this.', 'effort/computer.md': 'Lay financial article exactly.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/culture.md': 'Prevent north only miss cold.', 'by/family.md': 'Debate at office traditional stop great.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'bill/appear.md': 'Whole senior next stop yard national section.', 'bill/room.md': 'Able improve anything teacher media writer employee.', 'bill/citizen.md': 'Safe anyone major reach mother ground over leave.', 'bill/for.md': 'A several low detail.', 'bill/role.md': 'More light anything study hand power.', 'bill/set.md': 'Necessary century drive attack capital.', 'bill/generation.md': 'Stay could quality shake.', 'bill/drive.md': 'Situation we his.', 'bill/computer.md': 'Culture ahead change perhaps however audience.', 'bill/gas.md': 'Reveal attack and church.', 'color/sell.md': 'Mention although while boy turn.', 'color/throughout.md': 'She actually gun start.', 'color/management.md': 'Short serve beat increase than visit.', 'color/smile.md': 'His season employee husband.', 'color/wear.md': 'Share green measure sometimes.', 'color/official.md': 'Suddenly seat tend thus office action move.', 'color/admit.md': 'Each important clear.', 'color/treat.md': 'Tv outside attorney rich say same environment.', 'color/turn.md': 'Try drop old along.', 'color/sit.md': 'Including turn seem none computer.', 'build/together.md': 'Finally point only police artist.', 'build/rest.md': 'Author run let.', 'build/wall.md': 'Administration a week form side feeling.', 'build/none.md': 'Commercial stop page else.', 'build/explain.md': 'Join tend idea stand not option woman.', 'build/decision.md': 'Poor fund interesting bring.', 'build/beyond.md': 'Artist billion begin record anything none management practice.', 'build/dream.md': 'Decision suddenly prevent speak old power herself.', 'build/each.md': 'Able out key.', 'build/street.md': 'Knowledge specific technology before leave.', 'wrong/market.md': 'Realize key point whatever Democrat or say.', 'wrong/free.md': 'Deal even from mouth source.', 'wrong/sure.md': 'Similar him believe actually.', 'wrong/apply.md': 'Everybody office list service stock significant.', 'wrong/share.md': 'Painting every apply.', 'wrong/standard.md': 'Already place fund really.', 'wrong/might.md': 'Possible during claim view.', 'wrong/nation.md': 'About prove cold question race.', 'wrong/be.md': 'Land debate natural American.', 'wrong/suggest.md': 'Could environmental rather can us night.', 'Congress/remember.md': 'Purpose good policy line trade.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'industry/wrong.md': 'Floor race land those hard actually avoid property.', 'industry/book.md': 'Together state billion race beautiful how.', 'industry/car.md': 'Heart central eye thought painting government appear.', 'industry/cause.md': 'Time religious describe oil heart.', 'industry/feeling.md': 'Include memory strategy other statement imagine teach.', 'industry/small.md': 'Little third your season kind.', 'industry/heavy.md': 'Quality international window probably adult attention.', 'industry/election.md': 'Democrat often turn.', 'industry/possible.md': 'Structure high discover half dog half forward.', 'industry/fish.md': 'Much without in fight miss.', 'live/white.md': 'Whatever significant capital air about.', 'live/discuss.md': 'Hit result find miss culture heart clear task.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/own.md': 'Say small finish sing raise.', 'lot/seat.md': 'Method institution third political.', 'lot/wall.md': 'Each feel program size different kid.', 'lot/worry.md': 'Support moment maintain majority American rule rock.', 'lot/improve.md': 'Reason better difficult take.', 'lot/heart.md': 'Make let way.', 'lot/modern.md': 'Example first recently let.', 'lot/make.md': 'First eat data executive.', 'lot/check.md': 'Wall artist recent side approach.', 'lot/hotel.md': 'Technology town film nothing writer head from.', 'lot/perhaps.md': 'Main manage authority serious short.', 'drop/add.md': 'Fish work to individual.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/else.md': 'Fly candidate may so college.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/former.md': 'Brother college detail.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'central/several.md': 'Appear talk administration sort.', 'central/them.md': 'Unit huge call.', 'central/often.md': 'For nice after analysis series.', 'central/before.md': 'Account vote off police since.', 'central/commercial.md': 'Address country last teacher game compare.', 'central/these.md': 'Feeling rate first national.', 'central/tough.md': 'Party single media process statement forget.', 'central/crime.md': 'Hotel we five blue lawyer argue.', 'central/less.md': 'Guess environmental cover three late.', 'central/nice.md': 'Those religious audience case those.', 'civil/argue.md': 'Line culture seven six.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/ready.md': 'Central about ready information.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/question.md': 'Family evening its degree.', 'civil/gas.md': 'Talk why around necessary.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/central.md': 'Believe region their our whatever.', 'friend/oil.md': 'Little someone story put hundred able.', 'friend/discover.md': 'Someone city idea.', 'friend/month.md': 'Race walk people its Democrat sound.', 'friend/alone.md': 'Suffer concern choose participant work.', 'friend/myself.md': 'Truth simply memory alone plant large.', 'friend/note.md': 'Word end size enough.', 'friend/large.md': 'Tough glass per.', 'friend/wife.md': 'Sea investment many difference keep like improve.', 'friend/allow.md': 'Become personal own behavior sport.', 'friend/hand.md': 'Nation yourself final ground thus follow.', 'standard/late.md': 'Scientist people may story.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/level.md': 'Work around ask to.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/sound.md': 'Night national film next.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/easy.md': 'Myself must detail win.', 'standard/five.md': 'Lay would green generation season.', 'standard/analysis.md': 'While natural from staff option artist can.', 'community/book.md': 'Mr oil difficult dog.', 'community/else.md': 'Actually service thank state.', 'community/soldier.md': 'It lawyer cover job.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/cold.md': 'Election buy member alone school audience.', 'community/left.md': 'Picture let tell never.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/save.md': 'Thought hear home set employee early purpose.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/story.md': 'Anything song key first.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/bar.md': 'Among ago cover good.', 'education/evening.md': 'Give tonight sell over whole word care.', 'education/body.md': 'Note start bad part positive during.', 'education/total.md': 'Contain hit individual college month.', 'education/nature.md': 'Skin look fine policy special part.', 'education/really.md': 'Difference beyond cost but.', 'education/reason.md': 'Wrong increase investment deep near simply spring.', 'education/blood.md': 'North smile know.', 'education/imagine.md': 'Summer keep conference.', 'education/fish.md': 'Answer impact sense professor gun fast me.', 'education/article.md': 'Usually could bad attack customer couple represent.', 'lead/rest.md': 'Address half hit.', 'lead/speech.md': 'Maintain prepare indicate production surface.', 'lead/become.md': 'Building plant air something direction fall provide.', 'lead/stage.md': 'View main when Republican father plant.', 'lead/under.md': 'Test next education series.', 'lead/adult.md': 'Rule others especially institution total what law.', 'lead/which.md': 'Far task service radio reach morning accept.', 'lead/phone.md': 'Unit good including show stand.', 'lead/would.md': 'President still follow race analysis opportunity.', 'lead/trade.md': 'Success whatever environmental avoid father how although may.', 'why/show.md': 'Decade station development character movement.', 'why/data.md': 'Itself feeling fund mean.', 'why/more.md': 'Address music fish team national tough.', 'why/debate.md': 'Meeting wind medical can city face cost.', 'why/something.md': 'Everybody bed economic own least peace executive.', 'why/most.md': 'Agreement station room name.', 'why/spring.md': 'Fine according mission against.', 'why/phone.md': 'By near next teacher be degree although.', 'why/full.md': 'Yard like phone catch on attention your.', 'why/stuff.md': 'Cup everybody open book he decade.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/serve.md': 'Want exist bank book.', 'ten/nature.md': 'Eight own hot first success.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/rock.md': 'Method wall when book agency.', 'rule/hear.md': 'History event character everybody paper machine little billion.', 'rule/thing.md': 'Trial produce despite water range television.', 'rule/feel.md': 'Soon give never future difference.', 'rule/system.md': 'Bill article station despite.', 'rule/produce.md': 'Yes method sense.', 'rule/eye.md': 'Finally this team yet throughout.', 'rule/nation.md': 'Radio entire ago behavior prevent response ten according.', 'rule/thousand.md': 'Anything help military with run.', 'rule/goal.md': 'Inside firm without.', 'rule/perhaps.md': 'Back election leave.'}

If I am not wrong, both the expected and actual result contain the same entries. It is just that the ordering is different. The expected result also doesnt follow any particular format (so does the actual result).
Kindly advise on this @carlton
EDIT : Resolved on a later evaluation

    ---

    ### 💬 Post 145 by @21f2000709  
    **Posted on:** 2025-02-12 08:55 UTC  

    For the task - * B10. Write an API endpoint that filters a CSV file and returns JSON data
Do we have to handle prompts for converting CSV to JSON or for writing an endpoint for doing so?
@carlton @Jivraj

    ---

    ### 💬 Post 146 by @22f3001315  
    **Posted on:** 2025-02-12 09:04 UTC  

    yeah i am also facing the same doubt

    ---

    ### 💬 Post 147 by @23f1002382  
    **Posted on:** 2025-02-12 09:04 UTC  

    +1…
@Jivraj @s.anand

    ---

    ### 💬 Post 148 by @23f2003413  
    **Posted on:** 2025-02-12 09:36 UTC  

    could someone please share their repo for reference. it would be very much helpful

    ---

    ### 💬 Post 149 by @TRIGON  
    **Posted on:** 2025-02-12 09:38 UTC  

    Dear Instructors (@carlton, @iamprasna):
Confirming, just to be needfully pedantic:
It will solely be the responsibility of the Project Evaluator (human or machine) to parse the correct AIPROXY_TOKEN generated against my IITM email ID (presumably, per some database which holds all such generated AIPROXY_TOKENs of the students who have generated one); and the correct $IMAGE_NAME (to-be-submitted by myself in the Project Submission Google Form) in podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000, correct?
Asking this seemingly obvious question, as (apparently) the actual AIPROXY_TOKEN is not to be included anywhere in the code, or the repository, or the dockerfile.

    ---

    ### 💬 Post 150 by @Adithya  
    **Posted on:** 2025-02-12 09:51 UTC  

    I am also facing the same issue, just that the ordering is different.
Sorting by keys also didn’t help.
Please help on this @carlton @Jivraj

    ---

    ### 💬 Post 151 by @Haricharan  
    **Posted on:** 2025-02-12 10:36 UTC  

    sir will the tasks of Phase A and Phase B change? like currently do we need to make llm write the code for all tasks dynamically or can we write a pre defined python code to execute tasks after the llm parses the task and runs python code

    ---

    ### 💬 Post 152 by @23f1002382  
    **Posted on:** 2025-02-12 10:42 UTC  

    Check length of result and length of expected, one is 98 and other is 298
expected = {'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/culture.md': 'Prevent north only miss cold.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/family.md': 'Debate at office traditional stop great.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/bar.md': 'Among ago cover good.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/story.md': 'Anything song key first.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'drop/former.md': 'Brother college detail.', 'drop/add.md': 'Fish work to individual.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/else.md': 'Fly candidate may so college.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/ready.md': 'Central about ready information.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/question.md': 'Family evening its degree.', 'civil/argue.md': 'Line culture seven six.', 'civil/gas.md': 'Talk why around necessary.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/central.md': 'Believe region their our whatever.', 'standard/easy.md': 'Myself must detail win.', 'standard/sound.md': 'Night national film next.', 'standard/five.md': 'Lay would green generation season.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/late.md': 'Scientist people may story.', 'standard/level.md': 'Work around ask to.', 'standard/analysis.md': 'While natural from staff option artist can.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/sometimes.md': 'Big order defense field represent.', 'few/weight.md': 'Man mission American.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/my.md': 'Open line address contain whole impact into front.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/southern.md': 'Meet prove admit.', 'few/theory.md': 'Security effort protect future task long close.', 'few/information.md': 'Really morning yeah.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/save.md': 'Thought hear home set employee early purpose.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/book.md': 'Mr oil difficult dog.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/cold.md': 'Election buy member alone school audience.', 'community/else.md': 'Actually service thank state.', 'community/left.md': 'Picture let tell never.', 'community/soldier.md': 'It lawyer cover job.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'Congress/remember.md': 'Purpose good policy line trade.', 'ten/rock.md': 'Method wall when book agency.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/nature.md': 'Eight own hot first success.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/serve.md': 'Want exist bank book.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/white.md': 'Whatever significant capital air about.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/own.md': 'Say small finish sing raise.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/discuss.md': 'Hit result find miss culture heart clear task.'}
result  = {'suddenly/mouth.md': 'Outside food subject positive human.', 'suddenly/add.md': 'Window word during born do finally.', 'suddenly/free.md': 'Them ball significant different which traditional.', 'suddenly/management.md': 'Man fire long hour modern.', 'suddenly/leave.md': 'Season people Democrat hand among too.', 'suddenly/low.md': 'Front actually decision security fast song believe leg.', 'suddenly/why.md': 'Account listen such day method sing.', 'suddenly/miss.md': 'Rather although team thank.', 'suddenly/base.md': 'Total low room structure staff.', 'suddenly/strategy.md': 'Never understand less operation onto still trade environment.', 'ground/girl.md': 'Civil speech back sell.', 'ground/game.md': 'Fill whose card or daughter old meet.', 'ground/term.md': 'Pick return put set.', 'ground/every.md': 'Free service trouble effort somebody blood modern.', 'ground/along.md': 'Important plant increase door much.', 'ground/call.md': 'Article agent three scientist.', 'ground/do.md': 'Memory food strategy meeting.', 'ground/end.md': 'Large player discussion similar prove part.', 'ground/full.md': 'Actually start commercial.', 'ground/ever.md': 'Human example gun now my just Republican.', 'way/not.md': 'Decision together land chair.', 'way/morning.md': 'Information later service raise after trial base.', 'way/responsibility.md': 'Our child why environment care goal.', 'way/increase.md': 'Return say response political.', 'way/relationship.md': 'General view thing poor machine market peace.', 'way/soldier.md': 'Produce table should will school produce player wall.', 'way/act.md': 'Smile guess simple read style its international.', 'way/sound.md': 'Conference first finally recognize as.', 'way/reach.md': 'Exactly size discuss management miss article.', 'way/hotel.md': 'From become actually.', 'hit/run.md': 'Stock several region put thought decade evening.', 'hit/free.md': 'Crime usually produce.', 'hit/foot.md': 'Ball specific trip state.', 'hit/ball.md': 'Condition color focus traditional.', 'hit/song.md': 'Section environmental final light word in yes operation.', 'hit/since.md': 'Shoulder wrong matter seek cultural vote themselves.', 'hit/safe.md': 'Hear try spend item can along light.', 'hit/much.md': 'Guess great dream through concern feel.', 'hit/prove.md': 'Her base cup forward.', 'hit/stop.md': 'Nation this avoid herself deal place memory.', 'few/sometimes.md': 'Big order defense field represent.', 'few/southern.md': 'Meet prove admit.', 'few/choose.md': 'Official travel although price message example indeed.', 'few/store.md': 'Hand thought example exist record practice though.', 'few/weight.md': 'Man mission American.', 'few/information.md': 'Really morning yeah.', 'few/prove.md': 'Opportunity foot agent herself save other become study.', 'few/expect.md': 'Bill well artist night rule bag.', 'few/theory.md': 'Security effort protect future task long close.', 'few/my.md': 'Open line address contain whole impact into front.', 'resource/rest.md': 'Ok tough talk.', 'resource/move.md': 'Law write democratic drug itself house accept through.', 'resource/particularly.md': 'Affect woman nice.', 'resource/entire.md': 'Focus to once sea friend group.', 'resource/painting.md': 'Customer environment none trade.', 'resource/structure.md': 'Stuff return protect our bit reality.', 'resource/until.md': 'Growth industry region receive.', 'resource/significant.md': 'Long million fall throughout government tend.', 'resource/hospital.md': 'Quality certain fight want much body between.', 'resource/marriage.md': 'Foot specific mission.', 'for/hope.md': 'Whatever report wife fly close lot student.', 'for/poor.md': 'Explain claim police eye paper much when.', 'for/assume.md': 'Control yeah effect local economy worry.', 'for/couple.md': 'Floor both take indeed audience.', 'for/money.md': 'Join live next care material.', 'for/never.md': 'Me natural full.', 'for/situation.md': 'Show book instead hope lawyer.', 'for/north.md': 'Card level kind send loss growth.', 'for/hit.md': 'Minute wish above pass just later watch.', 'for/perhaps.md': 'Every professor sport unit rock bed.', 'project/individual.md': 'Tough safe machine small outside mention could must.', 'project/change.md': 'Century drug value.', 'project/home.md': 'Big decade edge feeling surface matter force student.', 'project/want.md': 'Region catch nation civil one Mr specific.', 'project/something.md': 'Major control three.', 'project/reality.md': 'Mouth including fine.', 'project/my.md': 'Fire point or success marriage write example.', 'project/issue.md': 'Former true career similar use visit machine.', 'project/surface.md': 'Cold reduce task life American act stage.', 'project/drug.md': 'Reason still field animal.', 'effort/morning.md': 'Policy quickly get capital smile.', 'effort/he.md': 'Thought view product interview explain.', 'effort/house.md': 'High hear thought according.', 'effort/church.md': 'Culture ask change focus.', 'effort/effect.md': 'Before suddenly who student could boy serve.', 'effort/price.md': 'Shoulder financial public reason home explain safe.', 'effort/company.md': 'Exactly treatment concern fly factor care drive.', 'effort/international.md': 'Rich take hear open.', 'effort/federal.md': 'Difference rate character by his blood this.', 'effort/computer.md': 'Lay financial article exactly.', 'by/region.md': 'Claim card from receive alone you capital book.', 'by/they.md': 'Unit its thank half morning determine development place.', 'by/defense.md': 'Marriage million crime organization give over.', 'by/draw.md': 'Shoulder class six finally build call note bring.', 'by/culture.md': 'Prevent north only miss cold.', 'by/family.md': 'Debate at office traditional stop great.', 'by/treat.md': 'Themselves young course feel.', 'by/little.md': 'Break somebody whose set else history.', 'by/color.md': 'Soon address everyone computer against.', 'by/perhaps.md': 'Base relationship identify mean happy Mrs whatever.', 'bill/appear.md': 'Whole senior next stop yard national section.', 'bill/room.md': 'Able improve anything teacher media writer employee.', 'bill/citizen.md': 'Safe anyone major reach mother ground over leave.', 'bill/for.md': 'A several low detail.', 'bill/role.md': 'More light anything study hand power.', 'bill/set.md': 'Necessary century drive attack capital.', 'bill/generation.md': 'Stay could quality shake.', 'bill/drive.md': 'Situation we his.', 'bill/computer.md': 'Culture ahead change perhaps however audience.', 'bill/gas.md': 'Reveal attack and church.', 'color/sell.md': 'Mention although while boy turn.', 'color/throughout.md': 'She actually gun start.', 'color/management.md': 'Short serve beat increase than visit.', 'color/smile.md': 'His season employee husband.', 'color/wear.md': 'Share green measure sometimes.', 'color/official.md': 'Suddenly seat tend thus office action move.', 'color/admit.md': 'Each important clear.', 'color/treat.md': 'Tv outside attorney rich say same environment.', 'color/turn.md': 'Try drop old along.', 'color/sit.md': 'Including turn seem none computer.', 'build/together.md': 'Finally point only police artist.', 'build/rest.md': 'Author run let.', 'build/wall.md': 'Administration a week form side feeling.', 'build/none.md': 'Commercial stop page else.', 'build/explain.md': 'Join tend idea stand not option woman.', 'build/decision.md': 'Poor fund interesting bring.', 'build/beyond.md': 'Artist billion begin record anything none management practice.', 'build/dream.md': 'Decision suddenly prevent speak old power herself.', 'build/each.md': 'Able out key.', 'build/street.md': 'Knowledge specific technology before leave.', 'wrong/market.md': 'Realize key point whatever Democrat or say.', 'wrong/free.md': 'Deal even from mouth source.', 'wrong/sure.md': 'Similar him believe actually.', 'wrong/apply.md': 'Everybody office list service stock significant.', 'wrong/share.md': 'Painting every apply.', 'wrong/standard.md': 'Already place fund really.', 'wrong/might.md': 'Possible during claim view.', 'wrong/nation.md': 'About prove cold question race.', 'wrong/be.md': 'Land debate natural American.', 'wrong/suggest.md': 'Could environmental rather can us night.', 'Congress/remember.md': 'Purpose good policy line trade.', 'Congress/let.md': 'Bank ability actually outside.', 'Congress/produce.md': 'Land do heart watch which many.', 'Congress/task.md': 'Book help represent now.', 'Congress/which.md': 'Partner score fast herself character minute.', 'Congress/democratic.md': 'Research knowledge owner Mr whole money cup.', 'Congress/accept.md': 'Expert plant institution relate old research position I.', 'Congress/remain.md': 'But natural film discussion among whole.', 'Congress/whatever.md': 'Today catch analysis.', 'Congress/fish.md': 'Herself share yourself movie behind whom check.', 'industry/wrong.md': 'Floor race land those hard actually avoid property.', 'industry/book.md': 'Together state billion race beautiful how.', 'industry/car.md': 'Heart central eye thought painting government appear.', 'industry/cause.md': 'Time religious describe oil heart.', 'industry/feeling.md': 'Include memory strategy other statement imagine teach.', 'industry/small.md': 'Little third your season kind.', 'industry/heavy.md': 'Quality international window probably adult attention.', 'industry/election.md': 'Democrat often turn.', 'industry/possible.md': 'Structure high discover half dog half forward.', 'industry/fish.md': 'Much without in fight miss.', 'live/white.md': 'Whatever significant capital air about.', 'live/discuss.md': 'Hit result find miss culture heart clear task.', 'live/traditional.md': 'If participant be year how may.', 'live/focus.md': 'Western win tree kid radio however value.', 'live/democratic.md': 'Reach rate none thank key after.', 'live/so.md': 'Type look identify spend drop sit skin heart.', 'live/possible.md': 'Window help reflect when consider science.', 'live/leader.md': 'Hold garden imagine style water ready several.', 'live/own.md': 'Say small finish sing raise.', 'lot/seat.md': 'Method institution third political.', 'lot/wall.md': 'Each feel program size different kid.', 'lot/worry.md': 'Support moment maintain majority American rule rock.', 'lot/improve.md': 'Reason better difficult take.', 'lot/heart.md': 'Make let way.', 'lot/modern.md': 'Example first recently let.', 'lot/make.md': 'First eat data executive.', 'lot/check.md': 'Wall artist recent side approach.', 'lot/hotel.md': 'Technology town film nothing writer head from.', 'lot/perhaps.md': 'Main manage authority serious short.', 'drop/add.md': 'Fish work to individual.', 'drop/mission.md': 'Ready kind only meeting.', 'drop/main.md': 'Education left somebody.', 'drop/of.md': 'Write room national change.', 'drop/else.md': 'Fly candidate may so college.', 'drop/manage.md': 'Allow expect heavy quality.', 'drop/arrive.md': 'Education science car common husband economy.', 'drop/former.md': 'Brother college detail.', 'drop/from.md': 'Though important executive Democrat smile.', 'drop/through.md': 'Adult large protect agency whom magazine behind.', 'central/several.md': 'Appear talk administration sort.', 'central/them.md': 'Unit huge call.', 'central/often.md': 'For nice after analysis series.', 'central/before.md': 'Account vote off police since.', 'central/commercial.md': 'Address country last teacher game compare.', 'central/these.md': 'Feeling rate first national.', 'central/tough.md': 'Party single media process statement forget.', 'central/crime.md': 'Hotel we five blue lawyer argue.', 'central/less.md': 'Guess environmental cover three late.', 'central/nice.md': 'Those religious audience case those.', 'civil/argue.md': 'Line culture seven six.', 'civil/life.md': 'Concern decide better whom.', 'civil/culture.md': 'National could exactly well discuss candidate especially sport.', 'civil/ready.md': 'Central about ready information.', 'civil/door.md': 'Can choice spring alone ball spend half.', 'civil/deep.md': 'Thought charge team type tonight maybe.', 'civil/question.md': 'Family evening its degree.', 'civil/gas.md': 'Talk why around necessary.', 'civil/hand.md': 'Discussion itself in far station head phone.', 'civil/central.md': 'Believe region their our whatever.', 'friend/oil.md': 'Little someone story put hundred able.', 'friend/discover.md': 'Someone city idea.', 'friend/month.md': 'Race walk people its Democrat sound.', 'friend/alone.md': 'Suffer concern choose participant work.', 'friend/myself.md': 'Truth simply memory alone plant large.', 'friend/note.md': 'Word end size enough.', 'friend/large.md': 'Tough glass per.', 'friend/wife.md': 'Sea investment many difference keep like improve.', 'friend/allow.md': 'Become personal own behavior sport.', 'friend/hand.md': 'Nation yourself final ground thus follow.', 'standard/late.md': 'Scientist people may story.', 'standard/audience.md': 'Finally remain actually toward purpose bad.', 'standard/level.md': 'Work around ask to.', 'standard/hear.md': 'Poor budget agent artist.', 'standard/sound.md': 'Night national film next.', 'standard/with.md': 'Former writer cause pattern school answer.', 'standard/standard.md': 'Do number shoulder animal yourself.', 'standard/easy.md': 'Myself must detail win.', 'standard/five.md': 'Lay would green generation season.', 'standard/analysis.md': 'While natural from staff option artist can.', 'community/book.md': 'Mr oil difficult dog.', 'community/else.md': 'Actually service thank state.', 'community/soldier.md': 'It lawyer cover job.', 'community/stay.md': 'Military teach subject cold affect shake.', 'community/cold.md': 'Election buy member alone school audience.', 'community/left.md': 'Picture let tell never.', 'community/up.md': 'Final all commercial anything term begin cultural.', 'community/woman.md': 'Big might attorney organization less drop.', 'community/save.md': 'Thought hear home set employee early purpose.', 'daughter/whose.md': 'Program writer interesting prepare authority skill.', 'daughter/seek.md': 'Throughout growth history save.', 'daughter/poor.md': 'Possible leave him up bag will.', 'daughter/product.md': 'Social stand administration challenge personal.', 'daughter/story.md': 'Anything song key first.', 'daughter/professor.md': 'Effect ahead eye serve single.', 'daughter/check.md': 'Young prevent play follow.', 'daughter/business.md': 'Alone idea security behavior.', 'daughter/put.md': 'Doctor eat should add pull customer might.', 'daughter/bar.md': 'Among ago cover good.', 'education/evening.md': 'Give tonight sell over whole word care.', 'education/body.md': 'Note start bad part positive during.', 'education/total.md': 'Contain hit individual college month.', 'education/nature.md': 'Skin look fine policy special part.', 'education/really.md': 'Difference beyond cost but.', 'education/reason.md': 'Wrong increase investment deep near simply spring.', 'education/blood.md': 'North smile know.', 'education/imagine.md': 'Summer keep conference.', 'education/fish.md': 'Answer impact sense professor gun fast me.', 'education/article.md': 'Usually could bad attack customer couple represent.', 'lead/rest.md': 'Address half hit.', 'lead/speech.md': 'Maintain prepare indicate production surface.', 'lead/become.md': 'Building plant air something direction fall provide.', 'lead/stage.md': 'View main when Republican father plant.', 'lead/under.md': 'Test next education series.', 'lead/adult.md': 'Rule others especially institution total what law.', 'lead/which.md': 'Far task service radio reach morning accept.', 'lead/phone.md': 'Unit good including show stand.', 'lead/would.md': 'President still follow race analysis opportunity.', 'lead/trade.md': 'Success whatever environmental avoid father how although may.', 'why/show.md': 'Decade station development character movement.', 'why/data.md': 'Itself feeling fund mean.', 'why/more.md': 'Address music fish team national tough.', 'why/debate.md': 'Meeting wind medical can city face cost.', 'why/something.md': 'Everybody bed economic own least peace executive.', 'why/most.md': 'Agreement station room name.', 'why/spring.md': 'Fine according mission against.', 'why/phone.md': 'By near next teacher be degree although.', 'why/full.md': 'Yard like phone catch on attention your.', 'why/stuff.md': 'Cup everybody open book he decade.', 'ten/pull.md': 'Factor list try able pattern.', 'ten/serve.md': 'Want exist bank book.', 'ten/nature.md': 'Eight own hot first success.', 'ten/sea.md': 'Trial heart office dark fine everything suggest.', 'ten/page.md': 'Edge to window size stand sea.', 'ten/someone.md': 'Themselves hair together maybe yes never.', 'ten/international.md': 'Food style wait tend improve.', 'ten/time.md': 'Note center brother process big.', 'ten/simply.md': 'Congress way enjoy hand first.', 'ten/rock.md': 'Method wall when book agency.', 'rule/hear.md': 'History event character everybody paper machine little billion.', 'rule/thing.md': 'Trial produce despite water range television.', 'rule/feel.md': 'Soon give never future difference.', 'rule/system.md': 'Bill article station despite.', 'rule/produce.md': 'Yes method sense.', 'rule/eye.md': 'Finally this team yet throughout.', 'rule/nation.md': 'Radio entire ago behavior prevent response ten according.', 'rule/thousand.md': 'Anything help military with run.', 'rule/goal.md': 'Inside firm without.', 'rule/perhaps.md': 'Back election leave.'}
print(len(set(result)), len(set(expected)))
count = 0
print("length of result", len(result))
print("length of expected", len(expected))
for y in result:
    if y not in expected:
        count += 1
        print(f"{y}:{result[y]} IS EXTRA FILE")
        print(count)

    ---

    ### 💬 Post 153 by @21f2000709  
    **Posted on:** 2025-02-12 11:18 UTC  

    *🖼️ Image description: That's a close-up headshot of a man with short, light brown hair. He appears to be middle-aged, and he's wearing glasses. The lighting is dramatic, with shadows on his face.  The background is a muted brownish-red.* s.anand:

A sample evaluation script for Project 1 tasks A1-A10 is available at tools-in-data-science-public/project-1 at tds-2025-01-project-1-wip · sanand0/tools-in-data-science-public · GitHub


Sir there is an error in the evaluation script for task A1, url - https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py doesn’t exist,
instead this should - https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py

    ---

    ### 💬 Post 155 by @carlton  
    **Posted on:** 2025-02-12 12:54 UTC  

    @23f2001978
That error is usually if you are using the wrong endpoint (ie. using open ai libraries instead of sending requests to aiproxy).
Without seeing the request its hard to tell you what the cause of the error is.
Kind regards

    ---

    ### 💬 Post 156 by @carlton  
    **Posted on:** 2025-02-12 13:20 UTC  

    @21f2000709 @23f1002382
B10 → Create a service that creates a specified endpoint that receives a CSV and returns a JSON data . Where the JSON is expected, whether in the response body of the endpoint , or in a file will be specified by the task master *🖼️ Image description: That's a simple, round yellow emoticon with two small black dots for eyes and a small, slightly upturned black line for a mouth, expressing a happy or pleasant emotion.*
Kind regards

    ---

    ### 💬 Post 157 by @22f3002771  
    **Posted on:** 2025-02-12 14:02 UTC  

    hi @carlton @Jivraj
for A2 i am getting this particular error and i don’t know what i am doing wrong in this
*🖼️ Image description: The image shows a terminal window displaying the results of a task that formats a Markdown file.  A POST request formats the file using Prettier, and a GET request then shows the formatted file. The before and after are shown, highlighting the removal of extra spaces and inconsistent formatting.*Screenshot from 2025-02-12 19-31-471501×564 44.7 KB

    ---

    ### 💬 Post 159 by @23f1002382  
    **Posted on:** 2025-02-12 14:07 UTC  

    issue with evaluate.py , post the code snippet in task a2, where it calculates the result and checks with expected.

    ---

    ### 💬 Post 160 by @22f3002771  
    **Posted on:** 2025-02-12 14:16 UTC  

    you mean screenshot of evaluate.py file?
*🖼️ Image description: The image shows a snippet of Python code within a code editor.  The code appears to be a function that uses the `prettier` tool to format a markdown file and then compares the formatted output to an expected output.  The bottom shows tabs for Problems, Output, Debug Console, Terminal, and Ports.*Screenshot from 2025-02-12 20-21-561501×564 61.8 KB

    ---

    ### 💬 Post 161 by @23f1002382  
    **Posted on:** 2025-02-12 14:55 UTC  

    running in docker?
////////////////////////////

    ---

    ### 💬 Post 162 by @22f3002771  
    **Posted on:** 2025-02-12 15:01 UTC  

    Yes, I commented out check=True to see the error

    ---

    ### 💬 Post 163 by @23f2003413  
    **Posted on:** 2025-02-12 15:56 UTC  

    @carlton @Jivraj
could you please help me out on how to start with TDS Project-1, as I am stuck at the moment and don’t know where to start from. This project is very much unfamiliar for me and I need some guidance on how to start with it. It would be really great if you could provide some help through resources/materials/videos and help me complete the project. Thanks in advance!

    ---

    ### 💬 Post 165 by @23f1002382  
    **Posted on:** 2025-02-12 16:46 UTC  

    then im not sure exactly wait lemme check

    ---

    ### 💬 Post 166 by @23f1002382  
    **Posted on:** 2025-02-12 16:49 UTC  

    issue with evaluate py, specifically , how it formats the file, maybe shell=True should be uncommented if commented out. then im not sure. Im not in composing docker files yet

    ---

    ### 💬 Post 167 by @AnvithaV  
    **Posted on:** 2025-02-12 17:08 UTC  

    Could anyone please help me with the project… I am trying to do it but I’m always getting errors even while starting.

    ---

    ### 💬 Post 168 by @21f2000709  
    **Posted on:** 2025-02-12 17:16 UTC  

    My final docker image size is coming 1.25 gb, I am using the ubuntu base image as I thought it would be appropriate given the tasks. Is it ok with that size?
PS - Also I would be running out of token if I need to test again with some other base image now.
@carlton

    ---

    ### 💬 Post 169 by @21f2000709  
    **Posted on:** 2025-02-12 17:21 UTC  

    Go through the week 1-3 assignments once, you would be good to go with Phase A tasks.
@23f2003413 @AnvithaV

    ---

    ### 💬 Post 170 by @carlton  
    **Posted on:** 2025-02-12 17:29 UTC  

    You do not need the whole of ubuntu!
Just python and uv
More like 128mb image.
Please watch Tues week 5 session 1
Kind regards

    ---

    ### 💬 Post 171 by @22f3001777  
    **Posted on:** 2025-02-12 17:38 UTC  

    Will there be more live sessions on project ?
@carlton

    ---

    ### 💬 Post 172 by @21f2000709  
    **Posted on:** 2025-02-12 17:53 UTC  

    I could pull it down to 610 mb, using python:3.9-slim now, but there are some essential libraries that is needed which is taking up the space…will it be ok? I mean installing on the go with uv might lead to timeout during evaluation…

    ---

    ### 💬 Post 173 by @ShahbaazSingh  
    **Posted on:** 2025-02-12 18:30 UTC  

    How did you corrected it ?

    ---

    ### 💬 Post 174 by @21f2000709  
    **Posted on:** 2025-02-12 19:09 UTC  

    I tried cutting it down further but it is affecting the functionality, this is the best I can do, i.e., 610 mb

    ---

    ### 💬 Post 175 by @23f1002382  
    **Posted on:** 2025-02-12 19:33 UTC  

    could you help later, when i need to construct docker image, via gmeet? PLEASE

    ---

    ### 💬 Post 176 by @22f3001315  
    **Posted on:** 2025-02-12 20:00 UTC  

    ANY SUGGESTIONS (just one digit away) ::
import easyocr
from pathlib import Path
import re

def extract_credit_card_number(input_image: str, output_file: str):
    
    input_path = Path(f".{input_image}")
    output_path = Path(f".{output_file}")

    if not input_path.exists():
        raise ValueError(f"Image file {input_path} does not exist.")

    # Step 1: Use OCR to extract text from the image
    reader = easyocr.Reader(['en'])
    try:
        result = reader.readtext(str(input_path))
    except Exception as e:
        raise ValueError(f"OCR processing failed: {str(e)}")

    # Combine all extracted text into a single string
    extracted_text = " ".join([text for (_, text, _) in result])

    # Step 2: Use the LLM to refine the extracted text and extract the credit card number
    prompt = f"""
    The following text was extracted from an image. It may contain a credit card number. 
    Extract the credit card number and return only the number without spaces or dashes. 
    If no credit card number is found, return "None".

    Extracted text: {extracted_text}
    """
    try:
        response = chat_completion(prompt)
        card_number = response.get("choices", [])[0].get("message", {}).get("content", "").strip()

        # Validate the card number (basic check for 16 digits)
        if card_number.lower() == "none" or not card_number.isdigit() or len(card_number) != 16:
            raise ValueError("No valid credit card number found in the image.")

        # Write the card number to the output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(card_number)

        return f"A8 Completed: Credit card number extracted and written to {output_file}"
    except Exception as e:
        raise ValueError(f"Failed to process text with LLM: {str(e)}")

 /data/credit-card.txt
⚠️ EXPECTED:
4026399336539356
⚠️ RESULT:
4026399338539356

    ---

    ### 💬 Post 177 by @23f1002382  
    **Posted on:** 2025-02-12 20:31 UTC  

    <Response [200]>
{‘id’: ‘chatcmpl-B0De8V66WZAucAweJe6e32BWSLnpT’, ‘object’: ‘chat.completion’, ‘created’: 1739392156, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: “I’m sorry, but I can’t assist with that.”, ‘refusal’: None}, ‘logprobs’: None, ‘finish_reason’: ‘stop’}], ‘usage’: {‘prompt_tokens’: 874, ‘completion_tokens’: 11, ‘total_tokens’: 885, ‘prompt_tokens_details’: {‘cached_tokens’: 0, ‘audio_tokens’: 0}, ‘completion_tokens_details’: {‘reasoning_tokens’: 0, ‘audio_tokens’: 0, ‘accepted_prediction_tokens’: 0, ‘rejected_prediction_tokens’: 0}}, ‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_bd83329f63’, ‘monthlyCost’: 0.048128640000000014, ‘cost’: 0.0026880000000000003, ‘monthlyRequests’: 51}
def query_gpt_image(image_path: str, task: str):
    print("🔍 Image Path:", image_path)
    image_format = image_path.split(".")[-1]
    with open(image_path, "rb") as file:
        image_data = base64.b64encode(file.read()).decode("utf-8")
    response = requests.post(
        "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {"APIKEY"}",
                "Content-Type": "application/json"},
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                "role": "user",
                "content": [
                    {"type": "text", "text": task},
                    {
                    "type": "image_url",
                    "image_url": { "url": f"data:image/{image_format};base64,{image_data}" }
                    }
                ]
                }
            ]
            }
                     )
    response.raise_for_status()
    print(response)
    print(response.json())
    result = response.json() 
response = query_gpt_image("data/credit_card.png","Extract the credit card number from image")

Why is this not working?
EDIT: Requires prompt engineering as “credit card” is sensitive information *🖼️ Image description: That's a yellow emoticon with its eyes rolled upwards and a straight mouth, suggesting boredom, apathy, or disinterest.**🖼️ Image description: That's a yellow emoticon with its eyes rolled upwards and a straight mouth, conveying boredom, disinterest, or skepticism.*
<Response [200]>
{‘id’: ‘chatcmpl-B0Dlie1ZIS68PZBCT0XJKhLKbyPAC’, ‘object’: ‘chat.completion’, ‘created’: 1739392626, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: ‘The numbers extracted from the image are:\n\n- 3009 1429 5211 59\n- 09/29\n- 113’, ‘refusal’: None}, ‘logprobs’: None, ‘finish_reason’: ‘stop’}], ‘usage’: {‘prompt_tokens’: 871, ‘completion_tokens’: 31, ‘total_tokens’: 902, ‘prompt_tokens_details’: {‘cached_tokens’: 0, ‘audio_tokens’: 0}, ‘completion_tokens_details’: {‘reasoning_tokens’: 0, ‘audio_tokens’: 0, ‘accepted_prediction_tokens’: 0, ‘rejected_prediction_tokens’: 0}}, ‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_bd83329f63’, ‘monthlyCost’: 0.05092764000000002, ‘cost’: 0.002799, ‘monthlyRequests’: 52}
response = query_gpt_image("data/credit_card.png","Extract number from image")

    ---

    ### 💬 Post 179 by @Rishabh2  
    **Posted on:** 2025-02-13 02:36 UTC  

    Sir in main.py file I’m defining task with different variables . But in evaluate.py tasks are defined by different variables to test and when I’m testing it using python evaluate.py it returns unsuccessful . I’m testing all my tasks of main.py with Postman it returns successful.
My query is that how the tasks get evaluated and do i need to change my variables in main.py ? And what are the other things i have to change.
Also plss update evaluate.py fie with phase B tasks
@s.anand @carlton @Saransh_Saini

    ---

    ### 💬 Post 180 by @carlton  
    **Posted on:** 2025-02-13 03:29 UTC  

    @22f3001777
Yes there will be one more session today (13th Feb) at usual time 8pm to 10pm
Kind regards

    ---

    ### 💬 Post 181 by @trebhuvansb  
    **Posted on:** 2025-02-13 04:09 UTC  

    Hi instructors and TAs,
For the different tasks in Phase B, I don’t have a clear idea of what type of a response you expect.
eg.

Run a SQL query on a SQLite or DuckDB database & Extract data from (i.e. scrape) a website & Transcribe audio from an MP3 file - Do you want the query’s response on an output file like A10? or as a response?

I understand that these are broad problems you except us to solve, but it would be helpful to know what type of response you would require.
Thanks,
Trebhuvan

    ---

    ### 💬 Post 182 by @22f3001307  
    **Posted on:** 2025-02-13 04:45 UTC  

    Hi,
Pls tell us how to use evaluate.py script to check our codes

    ---

    ### 💬 Post 183 by @carlton  
    **Posted on:** 2025-02-13 04:49 UTC  

    Output specifications will be detailed in the “task” sent to the endpoint.
Phase B is meant to be vague because if you can solve it, without an elaborate and gratuitous use of gpt function calling, then you can actually solve all tasks using the same function !
Kind regards

    ---

    ### 💬 Post 184 by @21f2000709  
    **Posted on:** 2025-02-13 04:54 UTC  

    Okay sure!! Ping me when you require to generate…

    ---

    ### 💬 Post 185 by @22f3002248  
    **Posted on:** 2025-02-13 05:05 UTC  

    Hello sir,
Is yesterday’s session not uploaded to YouTube yet ?
I couldn’t find it in calendar either… It will be very helpful if you (or anyone else) could provide yesterday session’s recording’s link…

    ---

    ### 💬 Post 186 by @21f2000709  
    **Posted on:** 2025-02-13 05:14 UTC  

    *🖼️ Image description: That's a headshot of a man with short brown hair. He's wearing a plaid shirt and appears to be sitting indoors, possibly in a cafe or restaurant setting, with some greenery visible in the background.* 21f2000709:

I tried cutting it down further but it is affecting the functionality, this is the best I can do, i.e., 610 mb


@carlton @Jivraj
will it be ok? Actually I developed it in a way that require some of the essential dependencies and at this point of time it would be dangerous to alter the way of handling it as I am running short of AIProxy Token credits.
Earlier when I asked this:



*🖼️ Image description: That's a headshot of a man with short brown hair. He's wearing a plaid shirt and appears to be seated indoors, possibly in a cafe or restaurant setting, with some greenery visible in the background.* 21f2000709:

Any tentative size cutoff for the docker image?


I could have altered my way of handling dependencies but at that point of time there was no clear numbers.
I request you to please allow this time around with this size…

    ---

    ### 💬 Post 187 by @Yogesh1  
    **Posted on:** 2025-02-13 05:45 UTC  

    @carlton Could you please consider extending the submission date of Assignment 5 (it is 16th Feb right now). We are very busy with the project.
And assignment 6 submission date is much later: 9th of March.

    ---

    ### 💬 Post 188 by @thinkmachine  
    **Posted on:** 2025-02-13 06:01 UTC  

    @carlton +1 Agreed, a relaxation in deadline will be a boon for students who’ve taken up other projects this term.

    ---

    ### 💬 Post 189 by @trebhuvansb  
    **Posted on:** 2025-02-13 06:08 UTC  

    usage of langchain is allowed?

    ---

    ### 💬 Post 190 by @21f2000709  
    **Posted on:** 2025-02-13 06:26 UTC  

    It will be extended, @carlton mentioned it in a TA session already.

    ---

    ### 💬 Post 191 by @Jivraj  
    **Posted on:** 2025-02-13 06:53 UTC  

    Hi @Rishabh2
What exactly you mean by variables?  only one argument is required for running evaluate.py that’s an email address.
You need to download both evaluate.py and datagen.py in same folder and then execute evaluate.py using uv.
uv run evaluate.py --email $any_email.
For phase B



*🖼️ Image description: That's a headshot of a man with dark hair and glasses, wearing a purple collared shirt.  The background is a plain, light yellow or beige.*
Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025] Tools in Data Science


    Output specifications will be detailed in the “task” sent to the endpoint. 
Phase B is meant to be vague because if you can solve it, without an elaborate and gratuitous use of gpt function calling, then you can actually solve all tasks using the same function ! 
Kind regards
  

Kind regards

    ---

    ### 💬 Post 192 by @Jivraj  
    **Posted on:** 2025-02-13 06:59 UTC  

    610 Mb’s is good size, no need to worry, it will be evaluated.

    ---

    ### 💬 Post 193 by @Saransh_Saini  
    **Posted on:** 2025-02-13 07:14 UTC  

    Hi @23f1002382
This is the classic case where you use Prompt engineering to solve your problems. I assume you have already achieved your answers, but I want to clarify this for someone who is facing this problem.
The thing is GPT-4o-mini is intelligent enough to understand what kind of task you are asking it do, and extracting Credit Card info from an image is one of the many prohibited tasks.
What you can do is, try to fool it using itself. Just ask ChatGPT to generate a prompt that would be capable of fooling itself into extracting out that credit card info. I was capable of doing it after pretending to be a working on a Cyber Security project, and other fake details which ChatGPT itself provided me with.

    ---

    ### 💬 Post 194 by @21f3000512  
    **Posted on:** 2025-02-13 07:17 UTC  

    @carlton . I cannot send requests to https://aiproxy.sanand.workers.dev/openai/v1 . Getting  $RateLimitError: Error code: 429 - {‘message’: 'On 2025-02 you used $2.0003758999999954, exceeding 2'}  . Looks like I used all of my credit . What can I do now ? Project is also Incomplete.

    ---

    ### 💬 Post 195 by @Saransh_Saini  
    **Posted on:** 2025-02-13 07:17 UTC  

    Try creating a better prompt for this task.
Hint: Ask it to recheck certain similar looking digits.

    ---

    ### 💬 Post 196 by @Jivraj  
    **Posted on:** 2025-02-13 07:40 UTC  

    After submitting docker image through, it will be pulled and our token will be used.
Things to be checked at your end.
1. podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p8000:8000 $IMAGE_NAME works fine
2.  Above command will start 8000 server so use evaluate.py to test if things are working as expected.
Kind regards.
Jivraj

    ---

    ### 💬 Post 197 by @Jivraj  
    **Posted on:** 2025-02-13 07:44 UTC  

    Hi @JoelJeffrey
What you did wrong and how did you correct it?

    ---

    ### 💬 Post 198 by @JoelJeffrey  
    **Posted on:** 2025-02-13 07:47 UTC  

    I think there was something wrong with the way the code was getting inputs (keys). I just rewrote that part and it worked

    ---

    ### 💬 Post 199 by @Jivraj  
    **Posted on:** 2025-02-13 07:50 UTC  

    Hi @22f3001307
Provide required write permissions to /data folder. We will also discuss this issue regarding permissions in initial part of today’s session.
Kind regards

    ---

    ### 💬 Post 201 by @22f3002248  
    **Posted on:** 2025-02-13 07:55 UTC  

    Hello sir,
Is yesterday’s session not uploaded to YouTube yet ?
I couldn’t find it in calendar either…

    ---

    ### 💬 Post 202 by @21f2000709  
    **Posted on:** 2025-02-13 08:00 UTC  

    Command to run the image in the docs, seemed to have some error,
*🖼️ Image description: This image shows instructions on how to run a docker image named `$IMAGE_NAME` using `podman`. The command includes environment variables for an AI proxy token, and maps port 8000 to the container.  The resulting API is accessible at `http://localhost:8000/run?task=...`.*
The command:
podman run $IMAGE_NAME -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000
gives the error:
crun: executable file `-e` not found in $PATH: No such file or directory: OCI runtime attempted to invoke a command that was not found
However the correct command seems to be:
podman run -e AIPROXY_TOKEN="$AIPROXY_TOKEN" -p 8000:8000 $IMAGE_NAME
This works totally fine.
*🖼️ Image description: The image shows a terminal output indicating the successful startup of a Uvicorn server at http://0.0.0.0:8000.  The server was started using podman.  The application startup is complete and the server is ready.*
@Jivraj

    ---

    ### 💬 Post 203 by @23f1002382  
    **Posted on:** 2025-02-13 08:10 UTC  

    nvm i can laugh nw xD

    ---

    ### 💬 Post 204 by @21f2000709  
    **Posted on:** 2025-02-13 08:25 UTC  

    One final question @Jivraj @carlton , will our projects be evaluated with our AIPROXY_TOKEN or a different one.
Because my project is done but for evaluation if my AIPROXY_TOKEN is used, it might be out of credits.

    ---

    ### 💬 Post 205 by @Yogesh1  
    **Posted on:** 2025-02-13 08:36 UTC  

    Thanks. Do you know the new date?

    ---

    ### 💬 Post 206 by @21f2000709  
    **Posted on:** 2025-02-13 08:57 UTC  

    That wasn’t said, but it was not this weekend for sure.

    ---

    ### 💬 Post 207 by @23f2001975  
    **Posted on:** 2025-02-13 09:14 UTC  

    my automation is happening and prompt distribution too but it just isnt able to pass any test after 1st in evaluation.py did someone else face same problem if yes then how to solve it please help

    ---

    ### 💬 Post 208 by @22f3001315  
    **Posted on:** 2025-02-13 09:24 UTC  

    actually that easyocr is directly sending the clear text(no confusion) to llm and llm is just extracting the  exact numbers from it .

    ---

    ### 💬 Post 212 by @23f2001975  
    **Posted on:** 2025-02-13 10:04 UTC  

    [quote=“23f2001975, post:211, topic:164277, full:true”]
@s.anand @carlton
While running the evaluation.py i am facing several issues because my output isnt strictly adhering sometimes to it will the checking be on such a basis only
for example in A3
*🖼️ Image description: That's a yellow triangle with a black exclamation mark inside.  It's a common warning symbol.* EXPECTED:
129
*🖼️ Image description: That's a yellow triangle with a black exclamation mark in the center.  It's a common warning symbol.* RESULT:
“129”
this is the error i get while it is the function in eval.py checking problem as it gets response as text and doesnt strip (“”)
Please guide what should i do

    ---

    ### 💬 Post 213 by @Jivraj  
    **Posted on:** 2025-02-13 10:18 UTC  

    *🖼️ Image description: That's a headshot of a man with short brown hair. He's wearing a plaid shirt and appears to be sitting indoors.  The background is slightly blurry but shows some greenery and what looks like a window.* 21f2000709:

podman run -e AIPROXY_TOKEN=“$AIPROXY_TOKEN” -p 8000:8000 $IMAGE_NAME


Yes this is correct command, we will update in project page.

    ---

    ### 💬 Post 215 by @Jivraj  
    **Posted on:** 2025-02-13 10:22 UTC  

    *🖼️ Image description: Failed to load image: 451 Client Error:  for url: https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png*
Project 1 - LLM-based Automation Agent - Discussion Thread [TDS Jan 2025] Tools in Data Science


    After submitting docker image through, it will be pulled and our token will be used. 
Things to be checked at your end. 
1. podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p8000:8000 $IMAGE_NAME works fine 
2.  Above command will start 8000 server so use evaluate.py to test if things are working as expected. 
Kind regards. 
Jivraj

    ---

    ### 💬 Post 216 by @vikramjncasr  
    **Posted on:** 2025-02-13 10:25 UTC  

    @Jivraj sir I get this error
but my app.py is able to get the server running on localhost and not on 0.0.0.
*🖼️ Image description: The image shows a terminal displaying a Python `ModuleNotFoundError`.  The error indicates that the `fastapi` module could not be found when running a Python script (`/app/app.py`).  The user is working in a directory related to an IIT Madras project.*image1014×190 18.2 KB
could you please help ?

    ---

    ### 💬 Post 217 by @22f3001307  
    **Posted on:** 2025-02-13 10:27 UTC  

    When i am trying evaluate the code, I am getting the following error
Traceback (most recent call last):
  File "/var/folders/rj/z_3b8hl51558519w90k5hp600000gn/T/evaluateyea70I.py", line 20, in <module>
    from datagen import (
    ...<9 lines>...
    )
ModuleNotFoundError: No module named 'datagen'

can someone tell me what i should do?
@carlton @Jivraj @Saransh_Saini

    ---

    ### 💬 Post 218 by @Jivraj  
    **Posted on:** 2025-02-13 10:28 UTC  

    @22f3001307
Install datagen.py in the same folder from where you are executing evaluate.py.
@vikramjncasr Check how you are executing, use uv or else install required modules globally
Kind regards

    ---

    ### 💬 Post 219 by @22f3001307  
    **Posted on:** 2025-02-13 10:33 UTC  

    Sir,
the folder already exists in that folder
besides, I am using OPENAI_API_KEY=$AIPROXY_TOKEN uv run https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/evaluate.py from Anand sir’s page to run the code in my system

    ---

    ### 💬 Post 220 by @vikramjncasr  
    **Posted on:** 2025-02-13 10:39 UTC  

    Sir would the belowformat be ok when you evaluate ?
*🖼️ Image description: The image shows a console log of a Uvicorn server starting up, listening on port 8000 of the local machine (127.0.0.1), and successfully handling a GET request.*image985×211 24.1 KB

    ---

    ### 💬 Post 221 by @vikramjncasr  
    **Posted on:** 2025-02-13 10:40 UTC  

    But when I use podman i keep getting errror.

    ---

    ### 💬 Post 222 by @24f2006061  
    **Posted on:** 2025-02-13 10:58 UTC  

    Hello,
Can anyone please reset my AIProxy limit. I am getting this error, {“detail”:“Agent error: 429 Client Error: Too Many Requests for url: https://aiproxy.sanand.workers.dev/openai/v1/chat/completions”}
Thank you.

    ---

    ### 💬 Post 223 by @22f3002771  
    **Posted on:** 2025-02-13 11:09 UTC  

    i am getting unauthorized error in A9 again and again, i have pasted my code if someone can help please look into this.
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "numpy",
#   "httpx",
#   "fastapi",
# ]
# ///


import httpx
import numpy as np
import datetime
import os

from fastapi import HTTPException


now = datetime.datetime.now()

OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"


# async def get_similarity_from_embeddings(emb1: list[float], emb2: list[float]) -> float:
def get_similarity_from_embeddings(emb1: list[float], emb2: list[float]) -> float:
    # """Calculate cosine similarity between two texts."""
    # emb1 = await embed(text1)
    # emb2 = await embed(text2)
    return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))


# async def embed_list(text_list: list[str]) -> list[float]:
async def embed_list(text_list: list[str]) -> list[float]:
    OPENAI_API_KEY = os.environ["AIPROXY_TOKEN"]
    OPENAI_API_URL = "http://aiproxy.sanand.workers.dev/openai/v1/embeddings"
    """Get embedding vector for text using OpenAI's API."""
    try:
        async with httpx.AsyncClient() as client:
            # with httpx.AsyncClient() as client:
            response = await client.post(
                # response = httpx.post(
                OPENAI_API_URL,
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
                
                json={"model": "text-embedding-3-small", "input": text_list},
            )
        # print(f'{response.json()["data"][0]["embedding"]}')
        emb_list = [emb["embedding"] for emb in response.json()["data"]]
        print(f"Number of embeddings returned = {len(emb_list)}")
        return emb_list

    except KeyError as e:
        print(f"INSIDE EMBED_LIST IN A9. KeyError occurred while querying GPT: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        print(f"INSIDE EMBED_LIST IN A9. General Error while querying gpt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


def most_similar(embeddings):
    # Extract the phrases and their corresponding embeddings
    phrases = list(embeddings.keys())
    emb_values = list(embeddings.values())

    # Initialize variables to track the maximum similarity
    max_similarity = -1  # Start with the smallest possible similarity value
    most_similar_pair = None

    # Compute cosine similarity between each pair of embeddings
    for i in range(len(emb_values)):
        for j in range(i + 1, len(emb_values)):  # Avoid repeating pairs
            similarity = get_similarity_from_embeddings(emb_values[i], emb_values[j])
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_pair = (phrases[i], phrases[j])

    return most_similar_pair


# async def get_similar_comments(input_file_path: str, output_file_path: str):
async def get_similar_comments(input_file_path: str, output_file_path: str):
    print(f"Reading the input file: {input_file_path}")
    with open(input_file_path, "r") as file:
        comments = file.readlines()

    print(f"Embedding the comments")
    # embeddings = await embed_list(comments)
    embeddings = await embed_list(comments)
    embed_dict = dict(zip(comments, embeddings))
    most_similar_pair = most_similar(embed_dict)
    print(f"Most similar comments: {most_similar_pair}")

    with open(output_file_path, "w") as file:
        for comment in most_similar_pair:
            file.write(f"{comment.strip()}\n")
        # file.write(f"Most similar comments: {most_similar_pair}")


if __name__ == "__main__":
    # import asyncio

    input_file_path = "/data/comments.txt"
    output_file_path = "/data/similar_comments.txt"
    # asyncio.run(get_similar_comments(input_file_path, output_file_path))
    get_similar_comments(input_file_path, output_file_path)

    ---

    ### 💬 Post 224 by @23f2004752  
    **Posted on:** 2025-02-13 11:30 UTC  

    @Jivraj @carlton sir can you take my doubt in today’s session please , i have successfully run docker server but endpoints are not working…
*🖼️ Image description: The image shows a split screen.  One side displays a web browser showing a "Not Found" error message. The other side shows a code editor with Python code, a terminal window displaying git push output, and other IDE elements.  The code appears to be a FastAPI application.*Screenshot 2025-02-13 1659121917×1024 124 KB
If anyone have knowledge about this , please help

    ---

    ### 💬 Post 225 by @Adithya  
    **Posted on:** 2025-02-13 11:32 UTC  

    How did u resolve the issue?  @JoelJeffrey

    ---

    ### 💬 Post 226 by @Adithya  
    **Posted on:** 2025-02-13 11:38 UTC  

    I am also facing the same issue.
Evaluation Output:
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"

🔴 A9 failed: 'data'

❌ A9 FAILED

I sense ‘Authentication Problem’ happens only with the evaluation script, as the curl requests seems to work fine.
INFO:httpx:HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
INFO:     127.0.0.1:60849 - "POST /run?task=%60%2Fdata%2Fcomments.txt%20contains%20a%20list%20of%20comments,%20one%20per%20line.%20Using%20embeddings,%20find%20the%20most%20similar%20pair%20of%20comments%20and%20write%20them%20to%20%2Fdata%2Fcomments-similar.txt,%20one%20per%20line HTTP/1.1" 200 OK

Any views? @carlton @Jivraj

    ---

    ### 💬 Post 227 by @vidushi  
    **Posted on:** 2025-02-13 12:36 UTC  

    @Jivraj @carlton Sir i keep getting this error
*🖼️ Image description: The image shows a Python traceback error.  The error is a `ModuleNotFoundError`, indicating that the program can't find the `fastapi` module, which is likely a dependency not installed in the current environment.  The traceback shows the error occurred on line 9 of `app.py` within the `tds-project-1` directory.*image671×109 8.64 KB
even though i have downloaded the packages globally and tried installing them by making a venv but nothing seems to work please help

    ---

    ### 💬 Post 228 by @Udipth  
    **Posted on:** 2025-02-13 12:56 UTC  

    what is the base url?

    ---

    ### 💬 Post 229 by @23f1002382  
    **Posted on:** 2025-02-13 13:16 UTC  

    use your api key guys

    ---

    ### 💬 Post 230 by @22f3002771  
    **Posted on:** 2025-02-13 13:17 UTC  

    we are using that only bro, only for A9 it says unauthorized

    ---

    ### 💬 Post 231 by @23f1002382  
    **Posted on:** 2025-02-13 13:18 UTC  

    network mapping or something, even im working that out

    ---

    ### 💬 Post 232 by @AnvithaV  
    **Posted on:** 2025-02-13 13:18 UTC  

    Even i am facing the same problem. I am unable to resolve it ,i tried many ways.
could anyone please help

    ---

    ### 💬 Post 233 by @23f1002382  
    **Posted on:** 2025-02-13 13:20 UTC  

    2 ways, try command line package installing, or inside venv, try which python,etc and make paths reconcile, or inside venv, uv pip install , if that doesn’t work, inside venv pip install

    ---

    ### 💬 Post 234 by @23f2004752  
    **Posted on:** 2025-02-13 13:37 UTC  

    thanks , already it work out

    ---

    ### 💬 Post 236 by @vikramjncasr  
    **Posted on:** 2025-02-13 15:44 UTC  

    @Jivraj @carlton sir please help
When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?
needs sudo permission all the time…
*🖼️ Image description: The image shows a terminal window displaying a directory listing.  The listing shows many common Linux directories, including `bin`, `boot`, `etc`, `home`, `lib`, `mnt`, `proc`, `root`, and others.  The `tmp` directory is highlighted in a different color.  Several lines at the top and bottom appear to be path information.*image1368×124 19.9 KB

    ---

    ### 💬 Post 237 by @huzaifa  
    **Posted on:** 2025-02-13 15:58 UTC  

    Hello Sir @carlton @Jivraj
What are implications on missing the project 1.
Due to some personal reasons I wasn’t able to start any work on my project 1. It seems difficult for me to complete it.
Could you please tell what will be the implications of missing it. Will I in anyway be able to cover up and pass in the subject doing future assignments and projects?
Thank you
PS: This isn’t any request to extend dates. I accept my fault and respect the dates provided by the team.

    ---

    ### 💬 Post 238 by @23f2001286  
    **Posted on:** 2025-02-13 16:55 UTC  

    Sir I haven’t initaiated the podman earlier.
Now when i try to use podman using the wsl via the code “sudo apt install -y podman” it is asking for the password…
The problem is:

I haven’t set any password for podman earlier.
Though it is asking for password but it is not taking any input.(ie I am unable type anything there).
what should I am supposed to do…
*🖼️ Image description: A terminal window shows multiple attempts to enter a password for the user "ayushcodes2611", resulting in error messages indicating incorrect password entries and ultimately a lockout after three failed attempts.  Commands involving `sudo apt update` and `sudo apt install` are also visible, suggesting system package management operations.*image1612×359 21.3 KB

    ---

    ### 💬 Post 239 by @Vihaanv07  
    **Posted on:** 2025-02-13 17:52 UTC  

    @s.anand @Jivraj I think the evaluation.py test case is broken for A8 because I can manually see more folders and markdown files than the expected case output of A8 evaluation. And also is there any evaluation file for Part B

    ---

    ### 💬 Post 240 by @23f2004094  
    **Posted on:** 2025-02-13 18:04 UTC  

    password are not visible in wsl when typed, just type and enter if it matches, the process will continue

    ---

    ### 💬 Post 241 by @22f1000376  
    **Posted on:** 2025-02-13 18:22 UTC  

    Sir If possible please extend the Project deadline.

    ---

    ### 💬 Post 242 by @23f3004024  
    **Posted on:** 2025-02-13 19:01 UTC  

    same error the execution is correct but format.md file is not modified with correct markdown format

    ---

    ### 💬 Post 243 by @23f2003413  
    **Posted on:** 2025-02-13 19:53 UTC  

    @carlton @Jivraj
can u please upload the video that was recorded on 12th Feb, as I am able to view only the video that was last recorded on 11th Feb (3 hrs 57 mins video). As I am doing the project completely from the recorded videos, please post those videos in youtube at the earliest.

    ---

    ### 💬 Post 244 by @Jivraj  
    **Posted on:** 2025-02-13 20:43 UTC  

    Hi @23f2003413
Because of some technical issues we could not record 12 Feb session. That was doubt clearing session regrading project1.
Kind regards

    ---

    ### 💬 Post 245 by @23f2004752  
    **Posted on:** 2025-02-14 00:36 UTC  

    Can we submit project number of times before deadline…

    ---

    ### 💬 Post 246 by @23f2001286  
    **Posted on:** 2025-02-14 02:49 UTC  

    thanks for you feedbacak I have figured it out! Thanks it means a lot…

    ---

    ### 💬 Post 247 by @23f2001286  
    **Posted on:** 2025-02-14 03:05 UTC  

    A silly Doubt though but still a doubt!
Could we create an image first of our project in initial stage(ie the my “app.py” is not completely ready) but I have build an docker image including the app.py and other dependencies.
Should I give the same url now and then carry on updating the app.py
Or, Should first complete and then upload in the form!
plz reply!!

    ---

    ### 💬 Post 248 by @23f2001305  
    **Posted on:** 2025-02-14 05:30 UTC  

    Can you send the link for the video on 11th Feb?

    ---

    ### 💬 Post 249 by @24f2003130  
    **Posted on:** 2025-02-14 05:49 UTC  

    How did you resolve the file cannot be found error?

    ---

    ### 💬 Post 250 by @23f1002279  
    **Posted on:** 2025-02-14 06:55 UTC  

    *🖼️ Image description: The image shows a log of failed attempts to extract a credit card number from an image.  The first attempt fails because the image file is not found.  A subsequent attempt to read the output file also fails because the file doesn't exist.  A final attempt to use an embeddings API fails due to unauthorized access.*image872×550 16.5 KB
pls help with this error

    ---

    ### 💬 Post 251 by @sharma_abhay  
    **Posted on:** 2025-02-14 07:01 UTC  

    Sir, could you please mention the title of youtube videos in which the project session are covered?

    ---

    ### 💬 Post 252 by @23f2005419  
    **Posted on:** 2025-02-14 07:18 UTC  

    Hi,
When yesterday’s recorded video will be uploaded in youtube?

    ---

    ### 💬 Post 253 by @23f2003413  
    **Posted on:** 2025-02-14 07:34 UTC  

    Thanks for the prompt reply @Jivraj . I have done the project setup till whatever was covered on the 11th Feb session. I am not able to proceed further as I have no clue on how to work on this. Can you please help me out as it would mean a lot.

    ---

    ### 💬 Post 254 by @23f1002279  
    **Posted on:** 2025-02-14 07:39 UTC  

    @carlton @23f1002382

    ---

    ### 💬 Post 255 by @23f2003413  
    **Posted on:** 2025-02-14 07:40 UTC  

    *🖼️ Image description: The image shows a graphic for "Week 5, Session 1".  The background is a peach color and features various colorful icons related to data, technology, and design, including charts, graphs, and mobile devices.  A dark blue banner across the center displays the week and session number in large white font.*

    ---

    ### 💬 Post 256 by @carlton  
    **Posted on:** 2025-02-14 07:40 UTC  

    Are you subscribed to the TDS channel? If you were it would notify you immediately when it was uploaded. (10am this morning).
Please subscribe to the channel. It was also on the main page for TDS.
https://tds.s-anand.net/#/README

*🖼️ Image description: That's a blurry image of the YouTube play button.  The button is white on a red background.*
YouTube


*🖼️ Image description: The image shows a graphic design with the text "TOOLS IN DATA SCIENCE" displayed prominently over a background of various colorful icons representing data science concepts and tools.  The style is flat and illustrative.*
Tools in Data Science
Share your videos with friends, family, and the world





Kind regards

    ---

    ### 💬 Post 257 by @23f2005419  
    **Posted on:** 2025-02-14 07:42 UTC  

    Thanks sir, Now I subscribed to the channel.

    ---

    ### 💬 Post 258 by @23f2003413  
    **Posted on:** 2025-02-14 07:45 UTC  

    Hi @carlton sir! Is this video (Week-5 Session-3) the continuation video from the previous session (Week-5 Session-1), since the Session-2 video has not been recorded and uploaded. I am totally relying on these videos to complete the project sir. Please help me out!

    ---

    ### 💬 Post 259 by @23f1002382  
    **Posted on:** 2025-02-14 08:04 UTC  

    offical answer is you dont, you let run it in docker and it would apparently work , im not there yet, bus as of of now , create your docker image and start testing there

    ---

    ### 💬 Post 260 by @23f1002382  
    **Posted on:** 2025-02-14 08:08 UTC  

    The deadline is at 11:59 pm right Saturday? Feb 15th? Google Standard Time?

    ---

    ### 💬 Post 261 by @Jivraj  
    **Posted on:** 2025-02-14 08:17 UTC  

    Yes feb 15 11:59 PM indian standard time.

    ---

    ### 💬 Post 262 by @Jivraj  
    **Posted on:** 2025-02-14 08:21 UTC  

    Hi @23f2003413
Session 3 was continuation of session1.
Session 2 was DCS(doubts clearing session)
Kind regards

    ---

    ### 💬 Post 263 by @23f2003413  
    **Posted on:** 2025-02-14 08:25 UTC  

    Got it. Thank you sir!

    ---

    ### 💬 Post 264 by @23f2005419  
    **Posted on:** 2025-02-14 08:33 UTC  

    Hi @Jivraj, @carlton, @Saransh_Saini sir,
I’m getting the following error while post mapping, I couldn’t able to fix it.
I’m getting status code as 400 from the llm api response. How to fix it sir?
   "json": {
        "message": "Invalid JSON body: SyntaxError: Unexpected token 'm', \"model=gpt-\"... is not valid JSON"
    }

    ---

    ### 💬 Post 265 by @Jivraj  
    **Posted on:** 2025-02-14 08:35 UTC  

    There is some problem with the json that you are using.
Try to debug it with GPT.

    ---

    ### 💬 Post 266 by @Jivraj  
    **Posted on:** 2025-02-14 08:36 UTC  

    week5 session 1 and session3

    ---

    ### 💬 Post 267 by @23f2001286  
    **Posted on:** 2025-02-14 08:38 UTC  

    *🖼️ Image description: A Visual Studio Code window is frozen and displays a "The window is not responding" error message.  Options to reopen, close, or keep waiting are available.  Some code is visible in the background.*image929×427 11.7 KB
Is someone else are also getting this kind of error messages…
I have a low end system, then shifted to high one then again this popped up…
Does anyone know how to come over this…

    ---

    ### 💬 Post 268 by @21f2000588  
    **Posted on:** 2025-02-14 09:23 UTC  

    Hello @carlton @Jivraj @Saransh_Saini sir, I have implemented the code for B3 & B6 but unfortunately as per the instructions given in project for B3 & B6 —


B6. Extract data from (i.e. scrape) a website


B3. Fetch data from an API and save it


They are almost similar and it’s getting confusing in both cases, it’s given output based on B3 and not reading the input for B6, so could you please help me out with this?
Is anyone else facing this or a similar issue?

    ---

    ### 💬 Post 269 by @Jivraj  
    **Posted on:** 2025-02-14 09:27 UTC  

    Two solutions

give proper permissions.
use docker containers this is what we will test on.

I would prefer 2nd approach

    ---

    ### 💬 Post 271 by @Jivraj  
    **Posted on:** 2025-02-14 09:31 UTC  

    For B tasks use LLM to write code on the fly and execute it, use better prompts. In evaluation script detailed task will be provided with what data needs to be scraped, endpoints, parameters, etc.

    ---

    ### 💬 Post 272 by @23f1002382  
    **Posted on:** 2025-02-14 09:45 UTC  

    {‘error’: {‘message’: “Invalid ‘tools[6].function.description’: string too long. Expected a string with maximum length 1024, but got a string with length 4384 instead.”, ‘type’: ‘invalid_request_error’, ‘param’: ‘tools[6].function.description’, ‘code’: ‘string_above_max_length’}, ‘monthlyCost’: 0.08569882000000002, ‘cost’: 0, ‘monthlyRequests’: 82}
i cant send long prompts then what is the point?

    ---

    ### 💬 Post 273 by @23f1002382  
    **Posted on:** 2025-02-14 09:45 UTC  

    local llm also we cant use you because you have some limit on file size, we send long prompt also it doesn’t work xD . What do we do?
@s.anand @carlton @Jivraj @anybodywhowouldatleastreplyONCE

    ---

    ### 💬 Post 274 by @Saransh_Saini  
    **Posted on:** 2025-02-14 10:04 UTC  

    Hi,
If you read these questions carefully then they are not similar, one is asking you to extract data from a webpage, meaning you have to do something related to the HTML code. And the other is simply sending a request to a given endpoint.

    ---

    ### 💬 Post 275 by @22f2001640  
    **Posted on:** 2025-02-14 11:13 UTC  

    Hi @carlton @Saransh_Saini @Jivraj ,
In task A6
Find all Markdown (.md ) files in /data/docs/ . For each file, extract the first occurrance of each H1 (i.e. a line starting with #  ). Create an index file /data/docs/index.json that maps each filename (without the /data/docs/ prefix) to its title (e.g. {"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...} ).
Here expected output JSON “key” is file name or file path without prefix /data/docs/ as prompt is bit confusing . when “path/to/large-language-models.md” is given in example is actually referring to file path or filename itself is “path/to/large-language-models.md”.

    ---

    ### 💬 Post 276 by @Saransh_Saini  
    **Posted on:** 2025-02-14 11:44 UTC  

    This can easily be checked by runing the evaluate.py file.
Anyways, a file present in data/docs/folder_a/folder_b/md_file should be folder_a/folder_b/md_file as key.

    ---

    ### 💬 Post 277 by @22f3002248  
    **Posted on:** 2025-02-14 11:48 UTC  

    hey @23f2001975 did you find the solution to this problem ?
i am facing the exact same issue

    ---

    ### 💬 Post 278 by @22f3001777  
    **Posted on:** 2025-02-14 12:44 UTC  

    @carlton
Sir, my token limit has crossed the $1 limit. Will I receive new limit or a fresh token ? I still need to complete my project.
Thank you

    ---

    ### 💬 Post 279 by @23f1002382  
    **Posted on:** 2025-02-14 12:50 UTC  

    *🖼️ Image description: That's a picture of a shiny, red circle.  It looks like a cartoonish depiction of a ball or bubble.* /data/credit-card.txt
*🖼️ Image description: That's a yellow triangle with a black exclamation mark inside.  It's a warning symbol.* EXPECTED:
30091429521159
*🖼️ Image description: That's a yellow triangle with a black exclamation mark inside.  It's a warning symbol.* RESULT:
3009142952159
{‘role’: ‘assistant’, ‘content’: ‘3009142952159’, ‘refusal’: None} if LLM is giving wrong output. I hope y’all look into edge cases. Some people tried really hard. to prompt it xD *🖼️ Image description: That's an upside-down smiley face emoji.  The mouth is an inverted arc, and the eyes are simple dots.* *🖼️ Image description: That's a yellow emoticon with a downturned, upside-down smile.  The eyes are simple black dots.* *🖼️ Image description: That's an upside-down smiley face emoji.  The mouth is an inverted arc, and the eyes are in their usual position.*.
You can check the logs

(venv) @ANDIECOOLER2 ➜ /workspaces/TDS-Project-1/app (checking-with-open-ai) $ uv run evaluate.py 
🟡 Running task: Install `uv` (if required) and run the script `https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/refs/heads/main/datagen.py`
with `23f1002382@ds.study.iitm.ac.in` as the only argument
HTTP Request: POST http://localhost:8000/run?task=
Install+`uv`+(if+required)+and+run+the+script+`https%3A%2F%2Fraw.githubusercontent.com%2FANdIeCOOl%2FTDS-Project1-Ollama_FastAPI-%2Frefs%2Fheads%2Fmain%2Fdatagen.py`
with+`23f1002382%40ds.study.iitm.ac.in`+as+the+only+argument
 “HTTP/1.1 200 OK”
*🖼️ Image description: That's a pixelated image of a light green, shiny sphere or bubble.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/format.md “HTTP/1.1 200 OK”
*🖼️ Image description: That's a light green square with a large white checkmark in the center.  It's a common symbol indicating completion, approval, or correctness.* A1 PASSED
10.8.2
*🖼️ Image description: That's a digital image of a shiny, golden, circular object resembling a bubble or a coin.* Running task: Format the contents of /data/format.md using prettier@3.4.2, updating the file in-place
HTTP Request: POST http://localhost:8000/run?task=
Format+the+contents+of+`%2Fdata%2Fformat.md`+using+`prettier%403.4.2`%2C+updating+the+file+in-place
 “HTTP/1.1 200 OK”
*🖼️ Image description: That's a digital illustration of a single, round, light green bubble.  It has a slight highlight at the top, suggesting shine or reflectivity.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/format.md “HTTP/1.1 200 OK”
*🖼️ Image description: That's a green square with a large white checkmark in the center.  It's a common symbol indicating completion, confirmation, or correctness.* A2 PASSED
*🖼️ Image description: That's a digital image of a large, shiny, golden circle or sphere.  It appears to be a simple, cartoonish rendering.* Running task: The file /data/dates.txt contains a list of dates, one per line. Count the number of Wednesdays in the list, and write just the number to /data/dates-wednesdays.txt
HTTP Request: POST http://localhost:8000/run?task=The+file+`%2Fdata%2Fdates.txt`+contains+a+list+of+dates%2C+one+per+line.+Count+the+number+of+Wednesdays+in+the+list%2C+and+write+just+the+number+to+`%2Fdata%2Fdates-wednesdays.txt` “HTTP/1.1 200 OK”
*🖼️ Image description: That's a pixelated image of a light green sphere or bubble.  It has a slightly lighter, almost translucent highlight at the top.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/dates-wednesdays.txt “HTTP/1.1 200 OK”
*🖼️ Image description: That's a light green square with a large white checkmark in the center.  It's a simple checkmark icon, often used to indicate completion, agreement, or correctness.* A3 PASSED
*🖼️ Image description: That's a digital illustration of a shiny, golden sphere or orb.  It has a highlighted area suggesting a light source.* Running task: Sort the array of contacts in /data/contacts.json by last_name, then first_name, and write the result to /data/contacts-sorted.json
HTTP Request: POST http://localhost:8000/run?task=Sort+the+array+of+contacts+in+`%2Fdata%2Fcontacts.json`+by+`last_name`%2C+then+`first_name`%2C+and+write+the+result+to+`%2Fdata%2Fcontacts-sorted.json` “HTTP/1.1 200 OK”
*🖼️ Image description: That's a drawing of a light green sphere or bubble.  It has a slightly lighter, almost translucent highlight at the top.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/contacts-sorted.json “HTTP/1.1 200 OK”
*🖼️ Image description: That's a green square button with a large white checkmark in the center.  It's a common symbol indicating completion, confirmation, or approval.* A4 PASSED
*🖼️ Image description: That's a digital illustration of a shiny, golden sphere or bubble.  It's a simple, round shape with a highlight suggesting a glossy texture.* Running task: Write the first line of the 10 most recent .log file in /data/logs/ to /data/logs-recent.txt, most recent first
HTTP Request: POST http://localhost:8000/run?task=Write+the+first+line+of+the+10+most+recent+`.log`+file+in+`%2Fdata%2Flogs%2F`+to+`%2Fdata%2Flogs-recent.txt`%2C+most+recent+first “HTTP/1.1 200 OK”
*🖼️ Image description: That's a digital drawing of a light green circle, resembling a bubble or orb.  It has a slight highlight at the top.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/logs-recent.txt “HTTP/1.1 200 OK”
*🖼️ Image description: That's a green square button with a large white checkmark in the center.  It signifies completion, confirmation, or approval.* A5 PASSED
*🖼️ Image description: That's a digital image of a shiny, golden sphere or orb.  It's circular with a subtle highlight suggesting a glossy texture.* Running task: Find all Markdown (.md) files in /data/docs/.
For each file, extract the first occurrance of each H1 (i.e. a line starting with # ).
Create an index file /data/docs/index.json that maps each filename (without the /data/docs/ prefix) to its title
(e.g. {"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...})
HTTP Request: POST http://localhost:8000/run?task=Find+all+Markdown+(`.md`)+files+in+`%2Fdata%2Fdocs%2F`.
For+each+file%2C+extract+the+first+occurrance+of+each+H1+(i.e.+a+line+starting+with+`%23+`).
Create+an+index+file+`%2Fdata%2Fdocs%2Findex.json`+that+maps+each+filename+(without+the+`%2Fdata%2Fdocs%2F`+prefix)+to+its+title
(e.g.+`{“README.md”%3A+“Home”%2C+“path%2Fto%2Flarge-language-models.md”%3A+“Large+Language+Models”%2C+...}`) “HTTP/1.1 200 OK”
*🖼️ Image description: That's a simple illustration of a light green sphere or bubble.  It has a slightly lighter highlight at the top.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/docs/index.json “HTTP/1.1 200 OK”
*🖼️ Image description: That's a green square with a large white checkmark in the center.  It's a common symbol indicating completion, agreement, or correctness.* A6 PASSED
*🖼️ Image description: That's a digital illustration of a shiny, golden sphere or bubble.  It's circular with a highlight suggesting a glossy texture.* Running task: /data/email.txt contains an email message. Pass the content to an LLM with instructions to extract the sender’s email address, and write just the email address to /data/email-sender.txt
HTTP Request: POST http://localhost:8000/run?task=`%2Fdata%2Femail.txt`+contains+an+email+message.+Pass+the+content+to+an+LLM+with+instructions+to+extract+the+sender’s+email+address%2C+and+write+just+the+email+address+to+`%2Fdata%2Femail-sender.txt` “HTTP/1.1 200 OK”
*🖼️ Image description: That's a pixelated image of a light green sphere or bubble.  It has a slight highlight at the top.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/email-sender.txt “HTTP/1.1 200 OK”
*🖼️ Image description: That's a green square button with a large white checkmark in the center.  It's a common symbol indicating completion, confirmation, or agreement.* A7 PASSED
*🖼️ Image description: That's a digital image of a shiny, golden, circular object.  It resembles a bubble or a coin.* Running task: /data/credit_card.png contains a credit card number. Pass the image to an LLM, have it extract the card number, and write it without spaces to /data/credit-card.txt
HTTP Request: POST http://localhost:8000/run?task=`%2Fdata%2Fcredit_card.png`+contains+a+credit+card+number.+Pass+the+image+to+an+LLM%2C+have+it+extract+the+card+number%2C+and+write+it+without+spaces+to+`%2Fdata%2Fcredit-card.txt` “HTTP/1.1 200 OK”
*🖼️ Image description: That's a simple drawing of a light green sphere or bubble.  It has a slight highlight near the top.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/credit-card.txt “HTTP/1.1 200 OK”
*🖼️ Image description: That's a picture of a shiny, red circle or sphere.  It appears to be a simple, cartoonish rendering.* /data/credit-card.txt
*🖼️ Image description: That's a yellow triangle with a black exclamation mark in the center.  It's a common warning symbol.* EXPECTED:
30091429521159
*🖼️ Image description: That's a yellow triangle with a black exclamation mark inside.  It's a common warning symbol indicating caution or danger.* RESULT:
3009142952159
*🖼️ Image description: That's a red "X" symbol on a black background.  It's a simple, slightly rounded, and somewhat glossy-looking X.* A8 FAILED
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings “HTTP/1.1 200 OK”
*🖼️ Image description: That's a simple image of a shiny, golden sphere or orb.  It appears to be a digital drawing or graphic.* Running task: /data/comments.txt contains a list of comments, one per line. Using embeddings, find the most similar pair of comments and write them to /data/comments-similar.txt, one per line
HTTP Request: POST http://localhost:8000/run?task=`%2Fdata%2Fcomments.txt`+contains+a+list+of+comments%2C+one+per+line.+Using+embeddings%2C+find+the+most+similar+pair+of+comments+and+write+them+to+`%2Fdata%2Fcomments-similar.txt`%2C+one+per+line “HTTP/1.1 200 OK”
*🖼️ Image description: That's a drawing of a light green, shiny sphere or bubble.  It has a slightly darker green highlight at the top.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/comments-similar.txt “HTTP/1.1 200 OK”
*🖼️ Image description: That's a green square button with a large white checkmark in the center.  It's a common visual representation of confirmation, completion, or agreement.* A9 PASSED
*🖼️ Image description: That's a digital illustration of a shiny, golden sphere or bubble.  It's a simple, circular shape with a highlight suggesting a glossy texture.* Running task: The SQLite database file /data/ticket-sales.db has a tickets with columns type, units, and price. Each row is a customer bid for a concert ticket. What is the total sales of all the items in the “Gold” ticket type? Write the number in /data/ticket-sales-gold.txt
HTTP Request: POST http://localhost:8000/run?task=The+SQLite+database+file+`%2Fdata%2Fticket-sales.db`+has+a+`tickets`+with+columns+`type`%2C+`units`%2C+and+`price`.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+“Gold”+ticket+type%3F+Write+the+number+in+`%2Fdata%2Fticket-sales-gold.txt` “HTTP/1.1 200 OK”
*🖼️ Image description: That's a drawing of a light green, glossy sphere or bubble.  It appears to be a simple, cartoonish depiction.* HTTP 200 {
“status”: “success”,
“message”: “Task executed successfully”
}
HTTP Request: GET http://localhost:8000/read?path=/data/ticket-sales-gold.txt “HTTP/1.1 200 OK”
*🖼️ Image description: That's a green square button with a large white checkmark in the center.  It's a common symbol indicating completion, confirmation, or agreement.* A10 PASSED
*🖼️ Image description: That's a bullseye dartboard with a blue dart hitting the center.* Score: 9 / 10 proof
EDIT CREDIT CARD NUMBERS are 16 digits, so even there is discrepancy

    ---

    ### 💬 Post 280 by @23f1002382  
    **Posted on:** 2025-02-14 12:51 UTC  

    usage’: {‘prompt_tokens’: 1384,
‘completion_tokens’: 67,
‘total_tokens’: 1451,
‘prompt_tokens_details’: {‘cached_tokens’: 0, ‘audio_tokens’: 0},
‘completion_tokens_details’: {‘reasoning_tokens’: 0, ‘audio_tokens’: 0, ‘accepted_prediction_tokens’: 0, ‘rejected_prediction_tokens’: 0}},
‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_13eed4fce1’,
‘monthlyCost’: 0.5243745800000005,
‘cost’: 0.004554000000000001
GPT-4o mini
Fine-tuning price
Input:--------------------------> CALCUATION: (1384/10^6)*$0.30 = 0.0004152
$0.30 / 1M tokens
Cached input:
$0.15 / 1M tokens
Output:------------------------->  CALCUATION: (67/10^6)$1.20 = 0.0000804
$1.20 / 1M tokens
Training:
$3.00 / 1M tokens
TOTAL = 0.0004152 + 0.0000804 = 0.0004956
‘cost’: 0.004554000000000001 MAKE IT MAKE SENSE?
‘total_tokens’: 1451, so only input and completion tokens used?




INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:root:10
INFO:root:Inside run_task with task:
Install uv (if required) and run the script https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/refs/heads/main/datagen.py
with 23f1002382@ds.study.iitm.ac.in as the only argument
INFO:root:PRINTING RESPONSE:::PRINTING RESPONSE:::PRINTING RESPONSE:::
{‘id’: ‘chatcmpl-B0pChhrBiCN8x8ueL2u57rwQiucl7’, ‘object’: ‘chat.completion’, ‘created’: 1739536527, ‘model’: ‘gpt-4o-mini-2024-07-18’, ‘choices’: [{‘index’: 0, ‘message’: {‘role’: ‘assistant’, ‘content’: None, ‘tool_calls’: [{‘id’: ‘call_ULCgfFzpEcnGNditwVwGwRIS’, ‘type’: ‘function’, ‘function’: {‘name’: ‘install_and_run_script’, ‘arguments’: ‘{“package”:“uv”,“args”:[“23f1002382@ds.study.iitm.ac.in”],“script_url”:“https://raw.githubusercontent.com/ANdIeCOOl/TDS-Project1-Ollama_FastAPI-/refs/heads/main/datagen.py”}’}}], ‘refusal’: None}, ‘logprobs’: None, ‘finish_reason’: ‘tool_calls’}], ‘usage’: {‘prompt_tokens’: 1384, ‘completion_tokens’: 67, ‘total_tokens’: 1451, ‘prompt_tokens_details’: {‘cached_tokens’: 0, ‘audio_tokens’: 0}, ‘completion_tokens_details’: {‘reasoning_tokens’: 0, ‘audio_tokens’: 0, ‘accepted_prediction_tokens’: 0, ‘rejected_prediction_tokens’: 0}}, ‘service_tier’: ‘default’, ‘system_fingerprint’: ‘fp_13eed4fce1’, ‘monthlyCost’: 0.5243745800000005, ‘cost’: 0.004554000000000001, ‘monthlyRequests’: 217}
@s.anand  How is the usage calculated? Just asking not implying
UPDATE:  ITS EVEN MORE CHEAPER, I gave benefir of doubt better its much cheaper? ???
*🖼️ Image description: A screenshot of OpenAI's API pricing page shows pricing information for two models: GPT-40 and GPT-40 mini.  Both models have 128k context length.  The GPT-40 model is described as high-intelligence for complex tasks, while the GPT-40 mini is described as affordable for everyday tasks.  Pricing is displayed in USD per million tokens for input, cached input, and output.*Screenshot 2025-02-14 1838441695×879 52 KB

    ---

    ### 💬 Post 281 by @carlton  
    **Posted on:** 2025-02-14 13:02 UTC  

    You can continue to $2. Then you would need to ask for a new token.

    ---

    ### 💬 Post 282 by @24ds3000061  
    **Posted on:** 2025-02-14 13:07 UTC  

    @carlton @Jivraj please upload recording of TDS Week 5 - Session 2. Only recordings of session 1 & 3 have been uploaded.

    ---

    ### 💬 Post 283 by @23f1002382  
    **Posted on:** 2025-02-14 13:28 UTC  

    github.com



*🖼️ Image description: This is a GitHub project page for `ANdleCOO1/TDS-Project-1`.  It shows 2 contributors, 0 issues, 1 star, and 0 forks.*
GitHub - ANdIeCOOl/TDS-Project-1
Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.






DONE WITH A TASK , you have to create DOCKER IMAGE THOUGH < HAVE ENV file with keys , check the key value pair names, an cheers guy , we all get 9 marks hopefully

    ---

    ### 💬 Post 284 by @23f2002592  
    **Posted on:** 2025-02-14 13:29 UTC  

    For as task description like this

Write the # of Thursdays in /data/extracts.txt into /data/extracts-count.txt

I have given the prompt in such detail to the LLM but it is still not able to understand the task because of the “#” symbol. The task is getting truncated even before it reaches to the LLM.
Can anyone help me on this because I have tried so many things to fix this but nothing seems to help.

    ---

    ### 💬 Post 285 by @23f2005419  
    **Posted on:** 2025-02-14 13:39 UTC  

    Hi @Jivraj, @carlton sir,
I have created a docker file and run the application but it’s throwing error for
A2 task
No such file or directory: ‘npx’
Do i need give the node install in docker file?

    ---

    ### 💬 Post 286 by @carlton  
    **Posted on:** 2025-02-14 13:41 UTC  

    Hash is just another way of writing “number”

    ---

    ### 💬 Post 287 by @23f2001286  
    **Posted on:** 2025-02-14 13:51 UTC  

    @carlton @Jivraj
sir i have tried to solve the A1. when I want to check the solution we are asked for the datagen module as the evaluate.py have
’
''from datagen import (
    get_markdown,
    get_dates,
    get_contacts,
    get_logs,
    get_docs,
    get_email,
    get_credit_card,
    get_comments,
    get_tickets,
)
'''

so do we need to download the datagen.py in the local system first…
Or it should be the part of the automation only…

    ---

    ### 💬 Post 288 by @sharma_abhay  
    **Posted on:** 2025-02-14 13:53 UTC  

    I am getting internal server error for task A1, I have been trying for a long time. It may be possible that i have issues with my ai_proxy token thus tell how to properly set the taken.

    ---

    ### 💬 Post 289 by @23f2002592  
    **Posted on:** 2025-02-14 14:05 UTC  

    Yes I know that but LLM does not know that # indicates number. And no prompt is fixing this issue because the task has to be passed as query parameter and by the time LLM reads the task, it is already half gone due to #.

    ---

    ### 💬 Post 290 by @23f2001305  
    **Posted on:** 2025-02-14 14:13 UTC  

    Where to find AIProxy token from?

    ---

    ### 💬 Post 291 by @daksh76  
    **Posted on:** 2025-02-14 14:16 UTC  

    what if we are out of token sir how do we complete our project then?

    ---

    ### 💬 Post 292 by @daksh76  
    **Posted on:** 2025-02-14 14:17 UTC  

    could u share your code once i think you should explicitly try to install npx in your code

    ---

    ### 💬 Post 293 by @daksh76  
    **Posted on:** 2025-02-14 14:19 UTC  

    *🖼️ Image description: That's a stylized image of Monkey D. Luffy from the anime *One Piece*.  He's wearing his iconic straw hat and raising one arm in a celebratory or waving gesture.  The background is a simple light orange.* 23f1002382:

ANDIECOOLER2


could you help me out with q2?

    ---

    ### 💬 Post 294 by @23f2001305  
    **Posted on:** 2025-02-14 14:19 UTC  

    Can you tell me where to get the AIPROXY Token from and also are u able to execute docker image push command it keeps showing as an error to me

    ---

    ### 💬 Post 295 by @23f2005419  
    **Posted on:** 2025-02-14 14:19 UTC  

    def format_with_prettier(file_path:str, prettier_version:str):
    if file_path and os.path.exists(file_path):
        print('Path exisit - will perform prettier')
        subprocess.run(["npx", f"prettier@{prettier_version}", "--write", file_path])
    else:
        raise FileNotFoundError()

This is my code

    ---

    ### 💬 Post 296 by @daksh76  
    **Posted on:** 2025-02-14 14:21 UTC  

    this isnt also working are you sure its right?

    ---

    ### 💬 Post 297 by @daksh76  
    **Posted on:** 2025-02-14 14:22 UTC  

    *🖼️ Image description: The image shows a code snippet in Python that checks for a file's existence and then uses the `subprocess` module to run the `prettier` command-line tool on it.  Below the code, there's an example of unformatted Markdown text, showing the input and output of the prettier process; both are identical.*image1027×917 28.1 KB

    ---

    ### 💬 Post 298 by @23f2005419  
    **Posted on:** 2025-02-14 14:24 UTC  

    okay but in my docker image when i tried to run that in local, its asking for npx and it doesnt work

    ---

    ### 💬 Post 299 by @daksh76  
    **Posted on:** 2025-02-14 14:25 UTC  

    @carlton could you please give a hint as to why this isnt working

    ---

    ### 💬 Post 300 by @daksh76  
    **Posted on:** 2025-02-14 14:25 UTC  

    im running locally first and then will use docker when i get a 10/10 score

    ---

    ### 💬 Post 301 by @23f2005419  
    **Posted on:** 2025-02-14 14:27 UTC  

    Okay, actually when i tried with local, i’m facing path error
./data/format.md
[WinError 2] The system cannot find the file specified

So that’s why i moved to docker but there also i’m getting error for A2.

    ---

    ### 💬 Post 302 by @daksh76  
    **Posted on:** 2025-02-14 14:28 UTC  

    you should manually check if the file really exists or not because i think the code and the folder where datagen.py is downloading files(data folder) are different

    ---

    ### 💬 Post 303 by @23f2005419  
    **Posted on:** 2025-02-14 14:30 UTC  

    yes yes i moved the folder to current working directory

    ---

    ### 💬 Post 304 by @carlton  
    **Posted on:** 2025-02-14 14:42 UTC  

    If you are using the function calling approach, you could just parse the ‘#’ and change it to ‘number’ and then send the prompt to the llm for that particular task.
Or another approach is tell the llm,
If you ever see the phrase ‘count the # of’ in a task, please interpret it as ‘count the number of’. For example
Count the # of Fridays means
Count the number of Fridays

    ---

    ### 💬 Post 305 by @21f3002277  
    **Posted on:** 2025-02-14 14:51 UTC  

    *🖼️ Image description: The image shows a VS Code window displaying Python code that uses the `subprocess` module to download and execute a Python script from a GitHub URL, passing an argument to it.  The code includes error handling and output from the subprocess calls.  The terminal shows successful HTTP requests and a traceback from a `NameError` exception, indicating a missing `import subprocess` statement.*Screenshot 2025-02-14 2018541919×1015 81.4 KB
@carlton @Jivraj this is showing while docker image is running

    ---

    ### 💬 Post 306 by @23f1002382  
    **Posted on:** 2025-02-14 15:06 UTC  

    in project page, ctrl+F and search ai proxy, one link s.anandProxy or something, there it will validate you email and get you your token.

    ---

    ### 💬 Post 307 by @23f1002382  
    **Posted on:** 2025-02-14 15:08 UTC  

    can you share your code for dynamic code generation, i dont have the base to start with , can you send me the code?
whatever this image is , llm_code,oy and etc

    ---

    ### 💬 Post 308 by @23f2005702  
    **Posted on:** 2025-02-14 15:20 UTC  

    What file should we have while pushing it to git and making image
should datagen file and data be there or not?

    ---

    ### 💬 Post 309 by @carlton  
    **Posted on:** 2025-02-14 15:24 UTC  

    Please read the deliverables and evalute section.
datagen.py and evaluate.py were for only for your testing purposes so that you have an idea of the workflow and how the evaluation works. They are NOT part of your project submission.
Only DO what the project page tells you in the deliverables and evalute sections.
Kind regards

    ---

    ### 💬 Post 310 by @Sourabhraj  
    **Posted on:** 2025-02-14 16:01 UTC  

    sir i am getting this error by running the docker image
*🖼️ Image description: A Python traceback showing a `ModuleNotFoundError` because the `fastapi` module couldn't be found in `/app/app.py` at line 11.*image656×116 3.28 KB
i tried troubleshooting this for hours but no luck could you please tell me what i did wrong here

    ---

    ### 💬 Post 311 by @23ds1000005  
    **Posted on:** 2025-02-14 16:05 UTC  

    i can help you up, if you need my help you can email me

    ---

    ### 💬 Post 312 by @ShahbaazSingh  
    **Posted on:** 2025-02-14 16:34 UTC  

    @s.anand Sir please tell me this I am not using podman i am using docker for building and hosting is it fine sir ?

    ---

    ### 💬 Post 313 by @21f2000709  
    **Posted on:** 2025-02-14 16:56 UTC  

    Hey @carlton @Jivraj , I actually submitted the project already in the morning,
I included all the deliverables and things mentioned in the evaluation section.
But since I was actively testing with the - datagen.py and evaluate.py, I forgot to remove them before submission.
However these files do not play a role in my project execution in any way, they just sit idle. Will there be any issue?

    ---

    ### 💬 Post 314 by @22f3002723  
    **Posted on:** 2025-02-14 16:57 UTC  

    when trying to use function call way of open api
tools = [
    {
        "type": "function",
        "function": {
            "name": "extract_email_sender",
            "description": "Extract sender email from a specific file in directory",
            "parameters": {},
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "count_day_of_week",
            "description": "To count the occurances of a specific day of a week in a file with various dates",
            "parameters": {
                "type": "object",
                "properties": {
                    "day_of_week": {
                        "type": "string",
                        "description": "day of week"
                    }
                },
                "required": ["day_of_week"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": user_input},
                
        ],      
	"tools": tools,
    "tool_choice": "auto",
    "max_tokens": 500,
    "temperature": 0.7
    }

facing the below issue
ror’: {‘message’: “Invalid type for ‘tools[0]’: expected an object, but got an array instead.”

    ---

    ### 💬 Post 315 by @AnvithaV  
    **Posted on:** 2025-02-14 17:04 UTC  

    when i run POST request t is showing output “HTTP/1.1 200 OK” but when i give GET request it is showing HTTP/1.1" 404 Not Found. Can you please say how can it be solved

    ---

    ### 💬 Post 316 by @21f2000709  
    **Posted on:** 2025-02-14 17:06 UTC  

    These files are inside a separate folder - evaluation in my project root directory. Since I already submitted please do consider.
Thanks & Regards
Pradeep

    ---

    ### 💬 Post 317 by @21f2000709  
    **Posted on:** 2025-02-14 17:09 UTC  

    This indicates your task execution returns  “HTTP/1.1 200 OK” but the execution doesn’t creates the required file in the given location that the evaluation script is requesting.

    ---

    ### 💬 Post 318 by @23f1002382  
    **Posted on:** 2025-02-14 17:09 UTC  

    If have doubts in building DOCKER stuff can you help me debug
PLEASE SENPAI
*🖼️ Image description: That's a depiction of a kamaboko, a Japanese fish cake.  Specifically, it shows a single, pink, spiraled slice.**🖼️ Image description: That's an image of a kamaboko, a Japanese fish cake.  Specifically, it shows a stylized depiction of a single, pink swirl-patterned kamaboko slice.**🖼️ Image description: That's a simple illustration of a kamaboko, a Japanese fish cake.  It shows the characteristic pink swirl pattern.**🖼️ Image description: That's a depiction of a kamaboko, a Japanese fish cake.  Specifically, it shows a pink swirl design commonly found on them.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  It shows a pink spiral design on a white, scalloped disc.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  It shows a pink spiral design on a white, scalloped-edge disc.**🖼️ Image description: That's a depiction of a kamaboko, a Japanese fish cake.  Specifically, it shows a pink swirl design common on these cakes.**🖼️ Image description: That's an image of a kamaboko, a Japanese fish cake.  Specifically, it shows a single, pink, spiraled slice.**🖼️ Image description: That's a simplified illustration of a kamaboko, a Japanese fish cake.  It shows the characteristic swirl pattern.**🖼️ Image description: That's a stylized image of a kamaboko, a Japanese fish cake.  It shows the characteristic pink spiral design on a white, scalloped-edge disc.**🖼️ Image description: That's a simplified illustration of a kamaboko fish cake.  It shows the characteristic pink swirl design on a white, scalloped-edged background.**🖼️ Image description: That's a stylized image of a kamaboko, a Japanese fish cake.  It shows the typical pink swirl design on a white, scalloped background.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  It shows the typical pink spiral design on a white, scalloped-edge disc.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  It shows a pink spiral design on a white, scalloped-edge disc.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  Specifically, it shows a pink swirl design common on kamaboko slices.**🖼️ Image description: That's an illustration of a kamaboko fish cake, specifically showing a pink swirl design within a white, scalloped-edged circle.**🖼️ Image description: That's a simple, stylized image of a kamaboko fish cake.  It shows a pink spiral design within a white, scalloped-edge circle.**🖼️ Image description: That's an image of a kamaboko, a Japanese fish cake.  Specifically, it depicts a slice with the characteristic pink swirl design.**🖼️ Image description: That's a stylized image of a kamaboko, a Japanese fish cake.  It shows a pink spiral design on a white, scalloped background.**🖼️ Image description: That's a stylized image of a kamaboko fish cake.  It shows a pink spiral design within a white, scalloped-edged circle.**🖼️ Image description: That's a picture of a kamaboko, a Japanese fish cake.  Specifically, it shows a pink, swirled kamaboko slice with a scalloped edge.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  It shows a pink spiral design on a white, scalloped background.**🖼️ Image description: That's a stylized image of a kamaboko fish cake.  It shows the characteristic pink spiral design on a white, scalloped background.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  It shows the characteristic pink swirl design.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  Specifically, it shows a pink, spiraled design common to many kamaboko.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  Specifically, it shows a pink swirl design common on the type served as a garnish.**🖼️ Image description: That's a simplified illustration of a kamaboko, a Japanese fish cake.  It shows the characteristic pink swirl pattern on a white, scalloped disc.**🖼️ Image description: That's an illustration of a kamaboko, a Japanese fish cake.  Specifically, it shows a slice with the characteristic swirl pattern.**🖼️ Image description: That's an image of two stylized hina dolls,  traditional Japanese figures representing the Emperor and Empress.  They are depicted in a simplified, almost pixelated style.**🖼️ Image description: That's a picture of two kokeshi dolls, traditional Japanese wooden dolls.  The dolls are stylized figures, one in a blue robe and the other in an orange robe, each with dark hair and painted features.**🖼️ Image description: That's a digital illustration of a pair of Hina dolls, traditional Japanese figurines representing the Emperor and Empress, used in the Hinamatsuri festival.  They are depicted in a simplified, almost pixelated style.**🖼️ Image description: That's a digital image of two hina dolls, traditionally Japanese figures used in the Hina Matsuri (Doll's Festival) celebration.  The dolls are stylized and appear to be pixel art or a similar low-resolution graphic style.**🖼️ Image description: That's a depiction of a pair of hina dolls, traditional Japanese dolls representing the Emperor and Empress, often displayed during the Hinamatsuri (Doll's Festival).  They are stylized and appear to be in a pixel art or low-resolution graphic style.**🖼️ Image description: That's a picture of two hina dolls,  traditional Japanese figurines representing the Emperor and Empress, typically displayed during the Hinamatsuri (Doll's Festival).  They are depicted in simplified, almost pixelated style.**🖼️ Image description: That's a pixel art depiction of a pair of hina dolls, traditional Japanese dolls displayed during the Hinamatsuri (Doll's Festival).  The male doll is in blue and the female doll is in orange/red.**🖼️ Image description: That's an image of two hina dolls, traditional Japanese figurines representing the Emperor and Empress, dressed in ornate clothing.  They are presented in a stylized, possibly pixel-art, format.**🖼️ Image description: That's a depiction of a pair of hina dolls, traditional Japanese figures used in the Hina Matsuri (Doll's Festival) celebration.  The image shows a male and female doll, dressed in elaborate, stylized clothing.**🖼️ Image description: That's a picture of two hina dolls, traditional Japanese figures representing the Emperor and Empress, displayed for the Hinamatsuri festival.  They are stylized and appear to be pixel art or a similar digital rendering.**🖼️ Image description: That's a digital image of two hina dolls,  traditional Japanese figurines representing the Emperor and Empress,  dressed in colorful, stylized clothing.**🖼️ Image description: That's a pixel art depiction of a pair of hina dolls, traditional Japanese dolls displayed during the Hinamatsuri (Doll's Festival).  The male doll is in blue, and the female doll is in orange/red.**🖼️ Image description: That's a depiction of a pair of hina dolls, traditional Japanese figures representing the Emperor and Empress, used in the Hinamatsuri festival.  They are stylized and appear to be pixel art or a similar simplified style.**🖼️ Image description: That's a digital image of two hina dolls,  traditional Japanese figurines representing the Emperor and Empress, typically displayed during the Hinamatsuri festival.  They are depicted in a simplified, almost pixelated style.**🖼️ Image description: That's a depiction of a pair of hina dolls,  traditional Japanese dolls representing the Emperor and Empress, often displayed during the Hinamatsuri (Doll's Festival).  The image shows them in a simplified, possibly pixel art style.**🖼️ Image description: That's a digital image depicting a pair of hina dolls, traditional Japanese figurines representing the Emperor and Empress.  They are stylized and appear to be pixel art or a similar low-resolution graphic style.**🖼️ Image description: That's a depiction of a pair of hina dolls, traditional Japanese figures used in the Hinamatsuri (Doll's Festival) celebration.  The image shows a male and female doll in stylized, pixelated art.**🖼️ Image description: That's an image of two hina dolls, traditionally used in the Japanese Hina Matsuri (Doll's Festival).  They are stylized, possibly pixel art, representations of the Emperor and Empress.**🖼️ Image description: That's an image of two hina dolls, traditional Japanese figurines representing the Emperor and Empress.  They are depicted in simplified, almost pixelated style.**🖼️ Image description: That's a depiction of a pair of hina dolls, traditional Japanese figures representing the Emperor and Empress, used in the Hinamatsuri (Doll's Festival) celebration.  They are styled in a simplified, almost pixelated manner.**🖼️ Image description: That's a digital image of two hina dolls,  traditional Japanese figurines representing the Emperor and Empress, used in the Hinamatsuri festival.  They are stylized and pixelated in appearance.**🖼️ Image description: That's a digital image of two hina dolls,  traditional Japanese dolls representing the Emperor and Empress, typically displayed during the Hinamatsuri (Doll's Festival).  They are depicted in a simplified, almost pixelated style.**🖼️ Image description: That's a digital illustration of a pair of hina dolls, traditional Japanese figures associated with the Hinamatsuri (Doll's Festival).  They are depicted in a simplified, almost pixelated style.**🖼️ Image description: That's a depiction of a pair of hina dolls, traditional Japanese figurines used in the Hinamatsuri (Doll's Festival) celebration.  The image shows a male and female doll in simplified, possibly pixel art, style.**🖼️ Image description: That's a depiction of a pair of hina dolls,  traditional Japanese dolls associated with the Hinamatsuri (Doll's Festival).  They're stylized and appear to be pixel art or a similar digital representation.**🖼️ Image description: That's a digital image of two hina dolls,  traditional Japanese figures representing the Emperor and Empress,  dressed in colorful, stylized clothing.*

    ---

    ### 💬 Post 319 by @21f2000709  
    **Posted on:** 2025-02-14 17:10 UTC  

    sure!! how can I help?

    ---

    ### 💬 Post 320 by @23f1002382  
    **Posted on:** 2025-02-14 17:10 UTC  

    +1
SENPAI is right *🖼️ Image description: That's a smiling yellow emoticon with a light blue halo.  It appears to be a stylized depiction of a happy angel.*

    ---

    ### 💬 Post 321 by @23f1002382  
    **Posted on:** 2025-02-14 17:12 UTC  

    not yet maybe in an hour, im building, but after that running in docker is different ball game, thats why , i need quick debugs in a meeting, other people also can join, maybe tomorrow, i have an exam tomorrow, so preferably , collectively before project submission . IF YOU HAVE TIME

    ---

    ### 💬 Post 322 by @21f2000709  
    **Posted on:** 2025-02-14 17:14 UTC  

    *🖼️ Image description: That's a drawing of Monkey D. Luffy from the anime *One Piece*.  He's wearing his signature straw hat and appears to be waving or reaching upwards.* 23f1002382:


Sure tell me I would try, if I am online then otherwise tomorrow if it’s late

    ---

    ### 💬 Post 323 by @23f2004752  
    **Posted on:** 2025-02-14 17:30 UTC  

    I am getting this error while pulling docker image
ansh@Lenovo:~/llm_project$ podman pull docker.io/ansh205/llm_project:final
Trying to pull docker.io/ansh205/llm_project:final…
Error: parsing image configuration: Get “https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/07/079f65bc553514a8f38a08fd959e932ca984894a64eed71fca406f3353b71d3b/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250214%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250214T172706Z&X-Amz-Expires=1200&X-Amz-SignedHeaders=host&X-Amz-Signature=073575bf08338fcdda378b997ebe749b15a6b676ed7b80fbf4c3f8080a791152”: dial tcp: lookup docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com on 10.255.255.254:53: server misbehavingPreformatted text

    ---

    ### 💬 Post 324 by @23f2004752  
    **Posted on:** 2025-02-14 17:50 UTC  

    @carlton @Jivraj @s.anand @Saransh_Saini
sir please provide me other api key. My current request cost is full.
Full LLM Response: {‘message’: ‘On 2025-02 you used $2.000143640000001, exceeding $2’}

    ---

    ### 💬 Post 325 by @22f3002723  
    **Posted on:** 2025-02-14 17:54 UTC  

    curl -X POST http://localhost:8001/run?task=Extract%20sender%20email
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    36  100    36    0     0      9      0  0:00:04  0:00:03  0:00:01     9{"results":"wrighttara@example.net"}

is this expectation of having %20 for blanks in query string fine ?

    ---

    ### 💬 Post 326 by @23f1002382  
    **Posted on:** 2025-02-14 18:00 UTC  

    docker run -e OPEN_AI_PROXY_TOKEN=your_token_value 
-e OPEN_AI_PROXY_URL=your_proxy_url 
-e OPEN_AI_EMBEDDING_URL=your_embedding_url 
-p 8000:8000
how do we get out urls inside, hardcode?

    ---

    ### 💬 Post 327 by @23f1002382  
    **Posted on:** 2025-02-14 18:44 UTC  

    Can you help with docker size image?
is it 2 GB?

    ---

    ### 💬 Post 328 by @23f2001975  
    **Posted on:** 2025-02-14 19:25 UTC  

    I want to reset my aiproxys i have used them all if i could even buy some would work i need it to test my app or could iitm help in resetting it please tell

    ---

    ### 💬 Post 329 by @daksh76  
    **Posted on:** 2025-02-14 19:33 UTC  

    could u help me in q9 thats the one left

    ---

    ### 💬 Post 330 by @daksh76  
    **Posted on:** 2025-02-14 19:34 UTC  

    @carlton my aiproxy is also exhausted please help me out

    ---

    ### 💬 Post 331 by @Namannn28  
    **Posted on:** 2025-02-14 19:35 UTC  

    sir my api tokens limit reached to one dollar , hiw to reset it

    ---

    ### 💬 Post 332 by @23f2001975  
    **Posted on:** 2025-02-14 19:39 UTC  

    bro can you help me with q2

    ---

    ### 💬 Post 334 by @21f3000512  
    **Posted on:** 2025-02-14 20:00 UTC  

    How to handle task a8 ? I tried pytesseract but gave wrong results.EasyOCR is giving the exact answer so tried in docker but some Model download is interrupting the flow of evaluate.py resulting in error .
I appreciate any help/procedure or code to handle taska8.
Thanks in advance.

    ---

    ### 💬 Post 335 by @23f2001975  
    **Posted on:** 2025-02-14 20:10 UTC  

    Did you get any solution to this

    ---

    ### 💬 Post 336 by @TheVishal  
    **Posted on:** 2025-02-14 20:14 UTC  

    u can use groq api groq api is compatible with openai

    ---

    ### 💬 Post 337 by @23f1002382  
    **Posted on:** 2025-02-14 20:19 UTC  

    whats up?
/////////////////////

    ---

    ### 💬 Post 339 by @TheVishal  
    **Posted on:** 2025-02-14 20:22 UTC  

    bro can please check my repo i am only able to do 7 tasks.
repo url: GitHub - 23f2005593/tds-project-1: TDS Project 1

    ---

    ### 💬 Post 340 by @23f1002382  
    **Posted on:** 2025-02-14 20:34 UTC  

    got the docker working?

    ---

    ### 💬 Post 341 by @22f3001011  
    **Posted on:** 2025-02-14 21:26 UTC  

    @carlton @Jeeveash.k
sir i submitted the wrong docker image file while submitted the form. Can you please let me change it, or make it such that we can reupload it
thank you.

    ---

    ### 💬 Post 343 by @s.anand  
    **Posted on:** 2025-02-14 21:43 UTC  

    22f3001011 I’ve enabled “Allow response editing” on the form. I think that means you can edit your response… but since you had submitted it before it was enabled, I’m not sure what the procedure is. Worst case, please submit again.

    ---

    ### 💬 Post 344 by @22f3000079  
    **Posted on:** 2025-02-14 21:53 UTC  

    Please make this change in evaluation.py
In evaluation script url of datagen.py is different than actual one please change it
evaluation.py line 72
Install uv (if required) and run the script https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py
change this to
Install uv (if required) and run the script https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py

    ---

    ### 💬 Post 345 by @23f2001975  
    **Posted on:** 2025-02-14 22:56 UTC  

    very true there is too much confusion Id like to ask if you know that evaluate.py is mean to run only for user@example.com or our own mail too  because there was written You MUST use your Student Id (eg. 22f3xxxxxx@ds.study.iitm.ac.in) to do the Project, otherwise your score will not be considered for evaluation.

    ---

    ### 💬 Post 346 by @23f2005419  
    **Posted on:** 2025-02-14 23:29 UTC  

    Hi any one have any idea on the below,
SyntaxError: illegal target for annotation

I’m getting this error only when i run the evaluate.py but in with postman it works as expected.
Anyone please help on this

    ---

    ### 💬 Post 348 by @21f3002277  
    **Posted on:** 2025-02-15 01:57 UTC  

    *🖼️ Image description: The image shows a screenshot of a VS Code IDE with a Python script that downloads and runs another Python script (`datagen.py`) using the `subprocess` module.  The script also includes handling of command-line arguments, specifically a URL and an email address. The terminal output shows the script successfully running and making a POST request to a GitHub URL.*Screenshot 2025-02-15 0719101919×1021 71.3 KB
sir why the datagen.py in not created in the tree and the data folder please help me @s.anand @Jivraj @carlton

    ---

    ### 💬 Post 349 by @23f1002382  
    **Posted on:** 2025-02-15 02:08 UTC  

    created in toot, cd /data in docker will take you there.

    ---

    ### 💬 Post 350 by @21f3002277  
    **Posted on:** 2025-02-15 02:42 UTC  

    *🖼️ Image description: A screenshot shows a VS Code terminal running a Python application.  The terminal output indicates a successful application startup and a successful POST request.  A Dockerfile is also open in the editor, showing instructions for building a Docker image for the application.*Screenshot 2025-02-15 0758431919×1017 70.9 KB
is changes is required in Dockerfile

    ---

    ### 💬 Post 351 by @23f2002205  
    **Posted on:** 2025-02-15 03:36 UTC  

    i too got the same error you can change the the tools part in your payload to
"tools": [{"type": "function", "function": schema} for schema in function_schema]

    ---

    ### 💬 Post 352 by @23f2002205  
    **Posted on:** 2025-02-15 03:42 UTC  

    i think you have to run the following command
uv run datagen.py <your_email> --root ./data

try to include --root ./data in your code

    ---

    ### 💬 Post 353 by @23f2002205  
    **Posted on:** 2025-02-15 03:47 UTC  

    sorry i forgot the change the name of function_schema to tools please you do that

    ---

    ### 💬 Post 354 by @22f3002248  
    **Posted on:** 2025-02-15 04:05 UTC  

    @carlton @Jivraj
Hello,
just a silly question, if my code runs well in docker environment with /data in root directory, will it be fine ?
or should i keep the relative ./data directory like in the lecture ?
Thanks

    ---

    ### 💬 Post 355 by @carlton  
    **Posted on:** 2025-02-15 04:22 UTC  

    The reason in the lecture they were using ./data was because they were debugging in their local machine not in the docker.
For the docker image (the official submission) you must use /data.
It is a clear requirement mentioned in the project page.
Thats why it works fine when you use it in the docker image.
Kind regards

    ---

    ### 💬 Post 356 by @Atimanas  
    **Posted on:** 2025-02-15 04:52 UTC  

    *🖼️ Image description: The image shows a form with two sections.  The first asks for a GitHub repository link for Project 1, providing an example format and a correctly filled-in response. The second asks for the name of a DockerHub image, providing an example format and a partially filled-in response with a "Must match pattern" warning.*Screenshot 2025-02-15 101818858×521 24.4 KB
@Jivraj @carlton
hello sir i need help here. I have pushed my image into a docker repo and trying to submit it on ht google form. but it is not accepting it and asking to remove the tag .
What do i do ?

    ---

    ### 💬 Post 357 by @22f3001011  
    **Posted on:** 2025-02-15 05:05 UTC  

    Alright sir.  Thank you very much for your help.

    ---

    ### 💬 Post 358 by @22f3002034  
    **Posted on:** 2025-02-15 06:03 UTC  

    Are multiple submissions allowed for project?

    ---

    ### 💬 Post 359 by @23f2004912  
    **Posted on:** 2025-02-15 06:20 UTC  

    *🖼️ Image description: The image shows a computer screen displaying code execution results.  There are errors indicated, specifically regarding an HTTP POST request and a mismatch between expected and actual results for a file named "credit-card.txt".  The code appears to be part of a larger program with various files and tasks involved.  A file named "credit-card.png" is also listed.*A8720×1280 85.1 KB
@carlton @Jivraj
please check this one…

    ---

    ### 💬 Post 360 by @23f2005419  
    **Posted on:** 2025-02-15 06:23 UTC  

    Hi @carlton @Jivraj  sir,
For A2 do i need to install node in the docker? I’m getting error with npx.
please suggest some way sir?

    ---

    ### 💬 Post 361 by @23f2004752  
    **Posted on:** 2025-02-15 06:23 UTC  

    if i have two repo on docker , is there any problem in that

    ---

    ### 💬 Post 362 by @23f2003413  
    **Posted on:** 2025-02-15 07:15 UTC  

    *🖼️ Image description: The image shows a debugging window displaying a 500 Internal Server Error. The error message indicates that the authentication token is invalid because it's not from a valid issuer (401 error).  The response size is 184 bytes and the response time was 792 milliseconds.*image684×316 12.7 KB
why do i get this error? can someone please help me out @Jivraj @carlton…Anyone pls help

    ---

    ### 💬 Post 363 by @23f2003413  
    **Posted on:** 2025-02-15 07:20 UTC  

    can u please share the base proxy url

    ---

    ### 💬 Post 364 by @Samra  
    **Posted on:** 2025-02-15 07:47 UTC  

    I’m also getting the same error. I have used a proxy URL and token. Before, it was working, but now it’s not.

    ---

    ### 💬 Post 365 by @23f2005702  
    **Posted on:** 2025-02-15 07:59 UTC  

    sir or anyone can you please provide what should be the content inside the docker file … i am getting confuse like /data or python-slim etc
… i am done with locally testing and only this thing left.

    ---

    ### 💬 Post 366 by @23f2002592  
    **Posted on:** 2025-02-15 08:02 UTC  

    yes please explain somebody. What should be inside the dockerfile

    ---

    ### 💬 Post 367 by @23f2005419  
    **Posted on:** 2025-02-15 08:08 UTC  

    Hi ,
Anyone completed Task B, I don’t know how to combine task A (function calling) and task B (self creating python code)
can anyone suggest how to do that? It will be really helpful

    ---

    ### 💬 Post 368 by @23f2003413  
    **Posted on:** 2025-02-15 08:20 UTC  

    “http://aiproxy.sanand.workers.dev/openai/v1” use this as proxy URL. its working for me now!

    ---

    ### 💬 Post 369 by @sarvan108  
    **Posted on:** 2025-02-15 08:24 UTC  

    How to resolve this?
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro$ uv run app.py
Traceback (most recent call last):
File “/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro/app.py”, line 10, in 
from fastapi import FastAPI
ModuleNotFoundError: No module named ‘fastapi’
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro$ pip show fastapi
WARNING: Package(s) not found: fastapi
sarvan108@SURIYA:/mnt/c/Users/sarva/OneDrive/Documents/Knowledge/IIT Madras Datascience/tds_pro$ pip install fastapi
error: externally-managed-environment
× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
python3-xyz, where xyz is the package you are trying to
install.
If you wish to install a non-Debian-packaged Python package,
create a virtual environment using python3 -m venv path/to/venv.
Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
sure you have python3-full installed.

If you wish to install a non-Debian packaged Python application,
it may be easiest to use pipx install xyz, which will manage a
virtual environment for you. Make sure you have pipx installed.

See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

    ---

    ### 💬 Post 370 by @23f2001286  
    **Posted on:** 2025-02-15 08:35 UTC  

    sir,
It is a humble requests from my side, to plz extend the deadline.
Because student like who come from non technical background, are unable to come up with this project…
though we have somehow comeup with the GAs taking the helps of groups, seniors and sessions.
Moreover I am Dual Degree student. It is very hectic for me.
Sir you won’t believe but I am continuously trying since last week. Specially after the release of the sessions… Whole day and night have gone like nothing, infront of the computer…
Plz sir understand the situation and extend the deadline…

    ---

    ### 💬 Post 371 by @Samra  
    **Posted on:** 2025-02-15 08:39 UTC  

    *🖼️ Image description: That's a teal-colored square with a white capital letter "S" in the center.* 23f2003413:

http://aiproxy.sanand.workers.dev/openai/v1


For me it says invalid path

    ---

    ### 💬 Post 372 by @21f3002277  
    **Posted on:** 2025-02-15 08:39 UTC  

    *🖼️ Image description: A JSON-formatted message stating that on 2025-02, $2.0037491399999996 was used, exceeding a $2 limit.*
@carlton @Jivraj

    ---

    ### 💬 Post 373 by @22f3002319  
    **Posted on:** 2025-02-15 08:43 UTC  

    same issue happening with me even though working for last whole week only got 4 correct . please extend some time so we can complete the project as weekends are the time when we get a day off from our primary college and can work with full attention on this project.

    ---

    ### 💬 Post 374 by @Jaideep  
    **Posted on:** 2025-02-15 08:59 UTC  

    it usually happens in some GNU/Linux OS. since you are using some distribution based on Debian namely Ubuntu or whatever try doing sudo apt install python-packagename (replace package name with fastapi for fastapi)
then it works. It usually happens due to manual intervention with pip3 the user might break some system dependencies which require some python3 package. No need to worry about it.
Another Fix: try using a virtual environment which is highly suggested since there is no chance for you to interfere with the system packages.
create a venv using python3 -m venv name_of_venv
add this line to your .bashrc in ~ folder as source /path/to/your/venv/location
and run source .bashrc. This time no error occurs as you do everything in your virtual environment you can install anything python3 package using pip3 install package name.
It even happened for me
*🖼️ Image description: A terminal window shows an error message ("externally-managed-environment") while attempting to install the NumPy Python package.  The message explains that the system is preventing the installation because it's externally managed and suggests creating a virtual environment or using `pipx` as alternatives.  The error is successfully resolved by activating a virtual environment.*Screenshot_20250215_1433573841×1009 237 KB

    ---

    ### 💬 Post 375 by @carlton  
    **Posted on:** 2025-02-15 09:03 UTC  

    Most of your questions and doubts will be solved in todays sessions. First 20 mins will be a clear overview of the logic and workflow and how evaluation actually works.
Rest of the session will be bug fixing and doubts.
Kind regards

    ---

    ### 💬 Post 376 by @Jayeshbansal  
    **Posted on:** 2025-02-15 09:10 UTC  

    *🖼️ Image description: That's a yellow triangle with a black exclamation mark in the center.  It's a common warning symbol.* EXPECTED:
Everybody significant bank herself them process build body. Price live size. Assume begin better language east like machine.
New customer green strategy.
Feeling stock experience certainly history talk buy. Quality perform appear human general religious feeling. Kid indicate fear word win carry.
During professional sport growth citizen glass great student. Exactly receive cause. Couple off current between role natural.
Wind develop world next. Impact appear capital cold stock we. Quality get run case huge that.
Use century general above more region. Radio him quality stage. Truth least military dinner growth.
Study maybe source. For expect imagine.
Analysis remain voice dog sit part. Safe them store spring life girl.
House bring challenge. Tell but rock able great.
Mouth president worker common Mr billion.
*🖼️ Image description: That's a yellow triangle with a black exclamation point in the center.  It's a warning symbol.* RESULT:
“Everybody significant bank herself them process build body. Price live size. Assume begin better language east like machine.\nNew customer green strategy.\nFeeling stock experience certainly history talk buy. Quality perform appear human general religious feeling. Kid indicate fear word win carry.\nDuring professional sport growth citizen glass great student. Exactly receive cause. Couple off current between role natural.\nWind develop world next. Impact appear capital cold stock we. Quality get run case huge that.\nUse century general above more region. Radio him quality stage. Truth least military dinner growth.\nStudy maybe source. For expect imagine.\nAnalysis remain voice dog sit part. Safe them store spring life girl.\nHouse bring challenge. Tell but rock able great.\nMouth president worker common Mr billion.”
it is the error i am facing but when i am opening manually, i am not getting any error, what should I do?
this same issue is with 3-4 questions

    ---

    ### 💬 Post 377 by @23f2003413  
    **Posted on:** 2025-02-15 10:02 UTC  

    when will the session be conducted and how can we join it sir?

    ---

    ### 💬 Post 378 by @sarvan108  
    **Posted on:** 2025-02-15 10:03 UTC  

    Hi Thanks.
Yes. it works when venv is created. But I see that it was working find in Week 5-Session 1 video without creating virtual environment.

    ---

    ### 💬 Post 379 by @21f1003816  
    **Posted on:** 2025-02-15 10:12 UTC  

    I will not submit project.

    ---

    ### 💬 Post 380 by @Jivraj  
    **Posted on:** 2025-02-15 10:27 UTC  

    Get authentication token from this AI Proxy and usage and follow documentation for sending requests.
sanand0/aiproxy: Authorizing proxy for LLMs

    ---

    ### 💬 Post 381 by @Jivraj  
    **Posted on:** 2025-02-15 10:28 UTC  

    No Problems, just fill form with correct image name in google forms.

    ---

    ### 💬 Post 382 by @Jivraj  
    **Posted on:** 2025-02-15 10:28 UTC  

    yes npx will require node to be installed.

    ---

    ### 💬 Post 383 by @23f2003413  
    **Posted on:** 2025-02-15 10:31 UTC  

    @Jivraj when would today’s live session be conducted and how can we attend it sir

    ---

    ### 💬 Post 384 by @Rrishit  
    **Posted on:** 2025-02-15 10:45 UTC  

    evaluate.py is not working sir.

    ---

    ### 💬 Post 385 by @24f2000074  
    **Posted on:** 2025-02-15 10:53 UTC  

    What if you run out of credits during or just before final evaluation?

    ---

    ### 💬 Post 386 by @Jivraj  
    **Posted on:** 2025-02-15 11:07 UTC  

    This is only for testing on local machine.
In docker image keep /data.

    ---

    ### 💬 Post 387 by @Jivraj  
    **Posted on:** 2025-02-15 11:09 UTC  

    One session is going live right now (from 3 to 5 pm).
It will be visible from calendra.

    ---

    ### 💬 Post 388 by @Vedant22  
    **Posted on:** 2025-02-15 11:15 UTC  

    sir,
It is a humble requests from my side, to plz extend the deadline.
Because student like who come from non technical background, are unable to come up with this project…
though we have somehow comeup with the GAs taking the helps of groups, seniors and sessions.
Moreover I am Dual Degree student. It is very hectic for me.
Sir you won’t believe but I am continuously trying since last week. Specially after the release of the sessions… Whole day and night have gone like nothing, infront of the computer…
Plz sir understand the situation and extend the deadline…

    ---

    ### 💬 Post 389 by @sharma_abhay  
    **Posted on:** 2025-02-15 11:15 UTC  

    Sir, I have put my AIPROXY_TOKEN in .env file should I need to push the .env file also in the github

    ---

    ### 💬 Post 391 by @Namannn28  
    **Posted on:** 2025-02-15 11:21 UTC  

    yes sir do we have to put env file also @carlton sir @Jivraj sir

    ---

    ### 💬 Post 392 by @23f2001286  
    **Posted on:** 2025-02-15 11:31 UTC  

    In the evaluation.py there is an import require named from datagen import some stuff.
which means inorder to run the evaluation.py we need to manually bring the datagen.py in the working directory…
Because in order to run the evaluation.py we need the datagen. plz help…

    ---

    ### 💬 Post 393 by @23f2003413  
    **Posted on:** 2025-02-15 11:32 UTC  

    can someone send the meet link for the live session happening now

    ---

    ### 💬 Post 394 by @Kabir1203  
    **Posted on:** 2025-02-15 11:38 UTC  

    Everytime I run datagen.py for the A1 task, the data file gets downloaded in the C drive instead of the current project folder. I even tried to set the current project folder as the root directory but it still downloads the files in C drive and I cant seem to find a workaround this. Can someone please help with this issue. Thanks!

    ---

    ### 💬 Post 395 by @Kabir1203  
    **Posted on:** 2025-02-15 11:42 UTC  

    Can you please make the changes in the datagen.py file
config = {“root”: “/data”}
This is where I have been facing the issue.
The only solution I can think of is moving the /data folder from the root to the project directory. which I am not sure is a good way to solve this issue.

    ---

    ### 💬 Post 396 by @gouthamnischay  
    **Posted on:** 2025-02-15 12:03 UTC  

    *🖼️ Image description: A black screen displays a large orange circle containing a white capital T in the center.  In the upper right corner, a small Google Meet logo is visible.  The name "TELVIN VARGHESE" is at the bottom left.*

    ---

    ### 💬 Post 397 by @23f2001978  
    **Posted on:** 2025-02-15 12:04 UTC  

    @carlton
please tell do we have to put this url in a variable for A1 task ?
https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py

    ---

    ### 💬 Post 398 by @Nelson  
    **Posted on:** 2025-02-15 12:06 UTC  

    Task A9 fails.

HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings “HTTP/1.1 401 Unauthorized”
*🖼️ Image description: That's a digital image of a shiny, red sphere or circle.  It appears smooth and has a slight highlight at the top.* A9 failed: ‘data’
*🖼️ Image description: That's a red "X" on a black background.  It's a simple, slightly rounded, and somewhat glossy-looking graphic.* A9 FAILED

If I run
curl -X POST http://aiproxy.sanand.workers.dev/openai/v1/embeddings -H "Content-Type: application/json" -H "Authorization: Bearer $AIPROXY_TOKEN" -d '{"model": "text-embedding-3-small", "input": ["king", "queen"]}'

I get
{
  "message": "Missing Authorization: Bearer header. See https://github.com/sanand0/aiproxy"
}

@carlton @Jivraj @s.anand

    ---

    ### 💬 Post 399 by @23f1002279  
    **Posted on:** 2025-02-15 12:08 UTC  

    @carlton sir @Jivraj sir  do i have to put env file in docker

    ---

    ### 💬 Post 400 by @22f3002248  
    **Posted on:** 2025-02-15 12:23 UTC  

    you have to give the AIPROXY_TOKEN to the evaluate.py by either
bash - export AIPROXY_TOKEN="your token"
or
powershell - $env:AIPROXY_TOKEN="your token"
the evaluate.py file takes the token to send request to embedding end point for processing.
so you have to set AIPROXY_TOKEN in both terminals
i.e. app.py and evaluate.py teminals

    ---

    ### 💬 Post 401 by @Kabir1203  
    **Posted on:** 2025-02-15 12:29 UTC  

    when I run the evaluation file, i get the following error - *🖼️ Image description: That's a digital illustration of a shiny, golden sphere or bubble.  It's round and has a slight highlight at the top, suggesting a reflective surface.* Running task: Install uv (if required) and run the script https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py with user@example.com as the only argument *🖼️ Image description: That's a simple image of a shiny, red circle.  It looks like a cartoonish depiction of a ball or bubble.* A1 failed: All connection attempts failed *🖼️ Image description: That's a red "X" symbol on a black background.  The X is slightly rounded and has a three-dimensional appearance.* A1 FAILED
I am getting the following error when running the evaluation scripts, can someone help me understand what this error is?

    ---

    ### 💬 Post 402 by @koustubhr  
    **Posted on:** 2025-02-15 12:34 UTC  

    Humble request to extend the deadline please. Finding it extremely difficult and having time atleast till Sunday will be really helpful for working professionals like me

    ---

    ### 💬 Post 403 by @Nelson  
    **Posted on:** 2025-02-15 12:58 UTC  

    All my tasks are running except A9. I have created a .env file and added my token. Despite that I ran commands in both the terminals. A9 still fails.

    ---

    ### 💬 Post 404 by @Kabir1203  
    **Posted on:** 2025-02-15 12:59 UTC  

    I second this, have been trying to debug the project for the past 1 week, spending over 4 hours daily and yet facing issues everytime I reopen. An extension of even 24 hours would be extremely appreciated. Please consider this. Thanks.

    ---

    ### 💬 Post 405 by @23f2001978  
    **Posted on:** 2025-02-15 13:09 UTC  

    same issue on my side as well

    ---

    ### 💬 Post 406 by @23f2001978  
    **Posted on:** 2025-02-15 13:10 UTC  

    how u did A2
could u please share ?

    ---

    ### 💬 Post 408 by @23f1002382  
    **Posted on:** 2025-02-15 13:21 UTC  

    @s.anand @jivraj @carlton
AIPROXY_TOKEN=$AIPROXY_TOKEN
what abt m url stuff?

    ---

    ### 💬 Post 409 by @NarendraAbhiyantrik  
    **Posted on:** 2025-02-15 13:24 UTC  

    Sir, I request you to Please  extend the deadline, Because it is time consuming  and regular Students and Working professionals  have only saturday and sunday to complete this project.
Thanks

    ---

    ### 💬 Post 410 by @22f3002248  
    **Posted on:** 2025-02-15 13:32 UTC  

    also, in evaluate.py file, the embedding url is wrong and the AIPROXY_TOKEN is changed to OPENAI_API_TOKEN or something. i could send you edited evaluate.py… check your messages on discourse

    ---

    ### 💬 Post 411 by @Nelson  
    **Posted on:** 2025-02-15 13:40 UTC  

    On bash it gives below output. On PowerShell it says missing authorization. A9 is failed.
*🖼️ Image description: The image shows a terminal window displaying a curl command that sends a request to an OpenAI embeddings API endpoint. The response includes a list of embeddings for the words "king" and "queen".  The terminal also shows the progress of the request, including download speed and time.*image907×661 26.5 KB
In PowerShell
*🖼️ Image description: A PowerShell terminal displays a curl command that attempts to send a POST request to an OpenAI embedding endpoint.  The request returns an error indicating a missing authorization header.*image967×292 16.5 KB

    ---

    ### 💬 Post 412 by @Kabir1203  
    **Posted on:** 2025-02-15 13:45 UTC  

    My data is getting generated -
*🖼️ Image description: A browser window displays a JSON response indicating that data generation is complete, listing several files created:  comments.txt, contacts.json, credit_card.png, dates.txt, docs, email.txt, format.md, logs, ticket-sales-gold.txt, and ticket-sales.db.  The URL shows a task labeled "Install".*image459×454 12.7 KB
despite this I am getting an error when evaluating the file with no explanation of the error. Can someone please help with this.
*🖼️ Image description: That's a digital image of a shiny, golden sphere or orb.  It appears to be a simple, cartoon-like rendering.* Running task: Install uv (if required) and run the script https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/datagen.py
with user@example.com as the only argument
*🖼️ Image description: That's a digital image of a shiny, red sphere or circle.  It appears smooth and has a slight highlight suggesting a glossy texture.* A1 failed:
*🖼️ Image description: That's a red "X" symbol on a black background.  It's a simple, slightly rounded design.* A1 FAILED

    ---

    ### 💬 Post 413 by @Kabir1203  
    **Posted on:** 2025-02-15 13:47 UTC  

    *🖼️ Image description: A code editor displays a markdown file (`format.md`) containing an unformatted sample paragraph with extra spaces and a bulleted list.  Below that is a Python snippet printing an email address.  Other files (.env, app.py, evaluate.py) are also listed in the editor tabs.*image820×404 12.3 KB
Even the markdown file shows the correct email. What are the possible issues that I could be facing with this one.

    ---

    ### 💬 Post 414 by @23f1002382  
    **Posted on:** 2025-02-15 13:57 UTC  

    *🖼️ Image description: Failed to load image: cannot identify image file <_io.BytesIO object at 0x772a44302930>*
github.com


GitHub - ANdIeCOOl/TDS-Project-1
main
Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.





ATLEAST 6 minimum score use at own risk(MIT LICENCE xD)

BUILD TIME TAKES 2 mins
WITH DOCKER FILE
@ANdIeCOOl ➜ /workspaces/TDS-Project-1/tds-project-1 (main) $ docker build -t tds-project-1 .
[+] Building 123.9s (13/13) FINISHED                                                                       docker:default
 => [internal] load build definition from Dockerfile                                                                 0.0s
 => => transferring dockerfile: 1.18kB                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                  2.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                        0.0s
 => [internal] load .dockerignore                                                                                    0.0s
 => => transferring context: 2B                                                                                      0.0s
 => [internal] load build context                                                                                    0.1s
 => => transferring context: 34.30kB                                                                                 0.0s
 => [1/7] FROM docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8  8.7s
 => => resolve docker.io/library/python:3.11-slim@sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8  0.0s
 => => sha256:2c2c44fb54acb184dbedee948d7ba6460b1075a60a014d66857ce46543d4d840 5.29kB / 5.29kB                       0.0s
 => => sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260 28.21MB / 28.21MB                     0.7s
 => => sha256:73c4bbda278d9a2b5133d6dabfac3eec43a92b8c8c15da914f298b4c966bea53 3.51MB / 3.51MB                       0.9s
 => => sha256:acc53c3e87ac87c98e44b79e0d2a6293146650f5cba576f424dab77f8c0a4335 16.20MB / 16.20MB                     1.6s
 => => sha256:42420f737ba91d509fc60d5ed65ed0492678a90c561e1fa08786ae8ba8b52eda 9.13kB / 9.13kB                       0.0s
 => => sha256:a66bd09b8d35bb52cd106a94c23a94ba22e6fde6bd13d6c5912ec4f5888a7f14 1.75kB / 1.75kB                       0.0s
 => => extracting sha256:c29f5b76f736a8b555fd191c48d6581bb918bcd605a7cbcc76205dd6acff3260                            2.2s
 => => sha256:ad3b14759e4f8c9a73d51c897a8b96f022ec96ffc237502ad3f1f12b0b0e361f 249B / 249B                           1.9s
 => => extracting sha256:73c4bbda278d9a2b5133d6dabfac3eec43a92b8c8c15da914f298b4c966bea53                            0.2s
 => => extracting sha256:acc53c3e87ac87c98e44b79e0d2a6293146650f5cba576f424dab77f8c0a4335                            1.4s
 => => extracting sha256:ad3b14759e4f8c9a73d51c897a8b96f022ec96ffc237502ad3f1f12b0b0e361f                            0.0s
 => [2/7] WORKDIR /app                                                                                               0.2s
 => [3/7] RUN pip install --upgrade pip setuptools wheel                                                             8.7s
 => [4/7] RUN apt-get update && apt-get install -y --no-install-recommends     gcc     g++     make     libffi-dev  84.5s
 => [5/7] RUN npm install -g prettier                                                                                1.5s
 => [6/7] COPY app /app                                                                                              0.1s
 => [7/7] RUN pip install uv                                                                                         4.5s
 => exporting to image                                                                                              13.4s
 => => exporting layers                                                                                             13.4s
 => => writing image sha256:39add91710bc7970d44dae04b3f4a0c4f227d1471fac4df7b01cec86ce7af3cf                         0.0s
 => => naming to docker.io/library/tds-project-1                                                                     0.0s

@ANdIeCOOl ➜ /workspaces/TDS-Project-1/tds-project-1 (main) $ docker images
REPOSITORY      TAG       IMAGE ID       CREATED          SIZE
tds-project-1   latest    39add91710bc   31 seconds ago   923MB
if this cause any issues please notify  @s.anand @carlton @Jivraj

    ---

    ### 💬 Post 415 by @23f3000709  
    **Posted on:** 2025-02-15 14:00 UTC  

    in phase B tasks are we supposed to create files to store the output or return it in the response ???
Please answer ASAP sir.

    ---

    ### 💬 Post 416 by @lakshaygarg654  
    **Posted on:** 2025-02-15 14:02 UTC  

    @s.anand
Respected Sir,
I sincerely request you to kindly consider granting a one-day extension for Project 1. Many key clarifications were provided in today’s session, and we need just one additional day to effectively implement them. This extension would be immensely helpful in ensuring a more refined submission.
I truly appreciate your time and consideration.
Thank you.

    ---

    ### 💬 Post 418 by @23f1002382  
    **Posted on:** 2025-02-15 14:07 UTC  

    @all can everyone please test my image and let me know PLEASE. THIS IS THE MOST YOU ALL CAN DO FOR ME. I WILL BE BERY GRATEFUL

*🖼️ Image description: Failed to load image: cannot identify image file <_io.BytesIO object at 0x772a4742ddf0>*
github.com


GitHub - ANdIeCOOl/TDS-Project-1
main
Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.

    ---

    ### 💬 Post 419 by @23f3000709  
    **Posted on:** 2025-02-15 14:08 UTC  

    hey I have a few doubts, if something was said about this please say so.

in Phase be tasks do we have to store the output in files or just return it in the response
When I call my some of my endpoints using post man or CURL they work but if I run the evaluate.py it throws an error, this I think is a bug in the eval.py file.

any idea about these ?

    ---

    ### 💬 Post 420 by @22f3002723  
    **Posted on:** 2025-02-15 14:22 UTC  

    facing the issue on submission
*🖼️ Image description: The image shows a form with two questions.  The first asks for a GitHub repository link, providing an example format. The second asks for the name of a DockerHub image, also providing an example format.  Both questions have input fields where the user should provide the requested information.  An error message indicates the second answer must match a specific pattern.*image942×521 28.7 KB

    ---

    ### 💬 Post 421 by @22f3002723  
    **Posted on:** 2025-02-15 14:25 UTC  

    please ignore the above… there was a upper case issue  in image name… now fine

    ---

    ### 💬 Post 422 by @Sagan  
    **Posted on:** 2025-02-15 14:35 UTC  

    Is it import to use python 3.13?
It is not stable yet

    ---

    ### 💬 Post 423 by @23f2003413  
    **Posted on:** 2025-02-15 14:38 UTC  

    *🖼️ Image description: The image shows a Python traceback, indicating an error occurred while initializing an OpenAI client.  The error message states that the API key must be provided either directly to the client or via an environment variable.*image1831×146 7.91 KB
can someone help me fix this error @Jivraj @carlton

    ---

    ### 💬 Post 424 by @abhigyandsa  
    **Posted on:** 2025-02-15 14:40 UTC  

    for the datagen script is it ok to hardcode the scripts url and my email id? I understand the script itself may change but can I count on the link remaining the same? Also is it necessary to pass the email as argument?

    ---

    ### 💬 Post 425 by @TheVishal  
    **Posted on:** 2025-02-15 14:41 UTC  

    from dotenv import load_dotenv
load_dotenv()

    ---

    ### 💬 Post 426 by @23f2003413  
    **Posted on:** 2025-02-15 14:45 UTC  

    yahh i have it in my code…still facing the issue

    ---

    ### 💬 Post 427 by @abhigyandsa  
    **Posted on:** 2025-02-15 14:55 UTC  

    @Jivraj @carlton [filler to extend length]

    ---

    ### 💬 Post 429 by @24ds3000061  
    **Posted on:** 2025-02-15 15:05 UTC  

    whats the image’s name on Docker?

    ---

    ### 💬 Post 430 by @23f2004936  
    **Posted on:** 2025-02-15 15:05 UTC  

    just completed my sem exams started worrking on the project from 2 days please give extension of deadline for the project sir

    ---

    ### 💬 Post 431 by @23f2003751  
    **Posted on:** 2025-02-15 15:32 UTC  

    dont we have to add the data folder or folder like datagen in the repo?

    ---

    ### 💬 Post 432 by @23f1002382  
    **Posted on:** 2025-02-15 15:33 UTC  

    thats confidential, im not an idiot xD, that will get me definitely  in trouble

    ---

    ### 💬 Post 433 by @23f1002382  
    **Posted on:** 2025-02-15 15:33 UTC  

    no, not really . Just your app

    ---

    ### 💬 Post 434 by @23f2003751  
    **Posted on:** 2025-02-15 15:42 UTC  

    in your project,in the app folder you have the data folder which is empty so should I keep that or remove it

    ---

    ### 💬 Post 435 by @23f2003751  
    **Posted on:** 2025-02-15 15:45 UTC  

    and also will u be making any chnages in the repo

    ---

    ### 💬 Post 436 by @23f2003413  
    **Posted on:** 2025-02-15 15:47 UTC  

    File “/app/app.py”, line 35, in 
client = OpenAI(
^^^^^^^
File “/usr/local/lib/python3.12/site-packages/openai/_client.py”, line 110, in init
raise OpenAIError(
openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable                                                                              some pls help me fix this error!!

    ---

    ### 💬 Post 437 by @Jivraj  
    **Posted on:** 2025-02-15 16:01 UTC  

    Blunder in your main.py.
You are using API_KEY = os.getenv(“AI_PROXY_TOKEN”) but it should be AIPROXY_TOKEN.
Btw what you using for phase B?

    ---

    ### 💬 Post 438 by @23f1002382  
    **Posted on:** 2025-02-15 16:03 UTC  

    yes i will change that

    ---

    ### 💬 Post 439 by @23f1002382  
    **Posted on:** 2025-02-15 16:03 UTC  

    nothing i think, i’ll import those generic functions and use tool usage only probably if can’t crack dynamic code generation

    ---

    ### 💬 Post 440 by @23f1002382  
    **Posted on:** 2025-02-15 16:04 UTC  

    i don’t have that

*🖼️ Image description: Failed to load image: cannot identify image file <_io.BytesIO object at 0x772a44302340>*
github.com


TDS-Project-1/tds-project-1/app at main · ANdIeCOOl/TDS-Project-1
Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.

    ---

    ### 💬 Post 441 by @Jivraj  
    **Posted on:** 2025-02-15 16:05 UTC  

    What we expect in project.

server running inside docker container at 8000.
And all files will be accessed from data folder in root directory.

Apart from these two you can have anything extra.

    ---

    ### 💬 Post 442 by @21f2000710  
    **Posted on:** 2025-02-15 16:05 UTC  

    *🖼️ Image description: A Docker build process failed because it could not resolve the source metadata for the `python:3.12-slim-bookworm` image.  The error message indicates a problem connecting to the Docker image repository due to a missing HTTPS proxy or a network connectivity issue.*Screenshot 2025-02-15 2128261903×492 32.1 KB
how to fix this error ?

    ---

    ### 💬 Post 443 by @Jivraj  
    **Posted on:** 2025-02-15 16:05 UTC  

    What problem you facing with that dynamic code generation part?

    ---

    ### 💬 Post 444 by @23f2001413  
    **Posted on:** 2025-02-15 16:06 UTC  

    I have exhausted my api limit of $2. I need to test my project. Can you please provide some more credits? @Jivraj @carlton @s.anand

    ---

    ### 💬 Post 445 by @23f1002382  
    **Posted on:** 2025-02-15 16:07 UTC  

    no problem but im losing steam slowly, i need to buckle up and PUSH @Jivraj

    ---

    ### 💬 Post 446 by @23f2004644  
    **Posted on:** 2025-02-15 16:08 UTC  

    Subject: Request for Project Deadline Extension
Dear Sir,
This project is highly complex, and we need additional time to ensure its successful completion. We kindly request an extension of the deadline to allow for thorough testing and proper implementation. An extension would greatly help us deliver the best results.
Thank you for your understanding  @Jivraj @carlton @s.anand

    ---

    ### 💬 Post 447 by @Jivraj  
    **Posted on:** 2025-02-15 16:13 UTC  

    This might be problem with network settings(unstable internet, firewall, VPN interference)
try to debug it with help of chatgpt.
You can also use codespaces for trying another network.
Streamlining setup with GitHub Codespaces

    ---

    ### 💬 Post 448 by @Jivraj  
    **Posted on:** 2025-02-15 16:13 UTC  

    Push push @23f1002382

    ---

    ### 💬 Post 449 by @23f2003413  
    **Posted on:** 2025-02-15 16:18 UTC  

    @Jivraj is it fine if i have my AIPROXY_TOKEN in my code instead of getting it as environment variable?

    ---

    ### 💬 Post 450 by @23f2001413  
    **Posted on:** 2025-02-15 16:20 UTC  

    if you do that then during evaluation, it would use your credit limit. if it gets exhausted, you may face problems. @23f2003413

    ---

    ### 💬 Post 451 by @23f2003751  
    **Posted on:** 2025-02-15 16:21 UTC  

    *🖼️ Image description: This is a file directory listing showing the contents of a Python project.  The project is organized into folders and contains several Python scripts, including `datagen.py` and `evaluate.py`.  There's also a Dockerfile, a `.gitignore` file, and README files.  The presence of `_pycache_` folders indicates that the project has been run previously.*image266×559 12.5 KB
this is what i am doing first using the podman given in the portal and then running the evaluate.py file

    ---

    ### 💬 Post 452 by @23f2003413  
    **Posted on:** 2025-02-15 16:21 UTC  

    ahhh okay, but i am getting an error while trying to fetch the token as an environment variable. any suggestions to fix this issue?

    ---

    ### 💬 Post 453 by @23f2001413  
    **Posted on:** 2025-02-15 16:22 UTC  

    you can use python-dotenv. check that out.

    ---

    ### 💬 Post 454 by @23f2003413  
    **Posted on:** 2025-02-15 16:23 UTC  

    tried that still not getting T_T anyways thanks mate!

    ---

    ### 💬 Post 455 by @Jivraj  
    **Posted on:** 2025-02-15 16:25 UTC  

    No don’t do that, just follow the procedure.
Two problems with keeping token in file.

It will become public after you push to github.
While running evaluation script after submission your token might run out of credits.

    ---

    ### 💬 Post 456 by @24ds3000061  
    **Posted on:** 2025-02-15 16:27 UTC  

    ohh yes, didn’t think it through xD

    ---

    ### 💬 Post 457 by @22f3000880  
    **Posted on:** 2025-02-15 16:29 UTC  

    I am facing the same error. and I have checked for solutions and found none. Did you resolve it? If yes can you please guide me through it?

    ---

    ### 💬 Post 458 by @23f2003413  
    **Posted on:** 2025-02-15 16:34 UTC  

    {
“detail”: “Error code: 401 - {‘error’: {‘message’: ‘Your authentication token is not from a valid issuer.’, ‘type’: ‘invalid_request_error’, ‘param’: None, ‘code’: ‘invalid_issuer’}}”
}          getting this error sir

    ---

    ### 💬 Post 459 by @23f1002382  
    **Posted on:** 2025-02-15 16:40 UTC  

    *🖼️ Image description: Failed to load image: cannot identify image file <_io.BytesIO object at 0x772a47438400>*
github.com


TDS-Project-1/tds-project-1/app at main · ANdIeCOOl/TDS-Project-1
Contribute to ANdIeCOOl/TDS-Project-1 development by creating an account on GitHub.






i keep updating, check this

    ---

    ### 💬 Post 460 by @AyushTiwari  
    **Posted on:** 2025-02-15 16:47 UTC  

    Please extend deadline by 1 day. i just got discharged from hospital today, was suffering from liver problem since some days and got high heart beat due to a medicine unrelated to liver and made me got admitted@Jivraj

    ---

    ### 💬 Post 461 by @23f1002382  
    **Posted on:** 2025-02-15 16:49 UTC  

    11:59 + 5 hours atthe most, @s.anand ? *🖼️ Image description: That's a large, round yellow emoticon with large, expressive eyes that are slightly teary, a small, happy smile, and curved eyebrows suggesting slight sadness or worry.  It conveys a feeling of bittersweet happiness, or happy crying.* *🖼️ Image description: That's a cartoon emoticon; a yellow circle face with large, expressive eyes that are tearing up, a small smile, and slightly arched eyebrows.  It conveys a feeling of happy crying or bittersweet joy.* *🖼️ Image description: That's a cartoon emoticon of a yellow face with large, expressive eyes that are tearing up, yet it also has a small, happy smile.  It conveys a feeling of bittersweet happiness or happy sadness.*

    ---

    ### 💬 Post 462 by @jkmadathil  
    **Posted on:** 2025-02-15 20:11 UTC  

    11 posts were split to a new topic: Project 1 - Casual banter

    ---

    ### 💬 Post 467 by @23f1002279  
    **Posted on:** 2025-02-15 16:59 UTC  

    @Jivraj sir   @carlton    sir do have to add datagen in the docker container?
As when I’m running it locally, it gives 9/10, but when I pull it from Hub and run eval, it says:detail": “[Errno 2] No such file or directory: ‘/data/datagen.py’”

    ---

    ### 💬 Post 469 by @23f2003413  
    **Posted on:** 2025-02-15 17:03 UTC  

    *🖼️ Image description: The image shows a JSON response code, indicating an error (401) because the authentication token is invalid.  A "Copy" button is also visible.*image706×193 6.15 KB
someone please help me fix this error

    ---

    ### 💬 Post 475 by @rohitgarg  
    **Posted on:** 2025-02-15 17:10 UTC  

    @carlton can you pl merge this

github.com/sanand0/tools-in-data-science-public








Update evaluate.py with correct link of datagen.py for task `A1`


tds-2025-01 ← rohitxiitm:patch-1



          opened 10:56AM - 15 Feb 25 UTC



*🖼️ Image description: A young man with short dark hair stands in front of a green wall. He is wearing a light beige, long-sleeved kurta.*
            rohitxiitm
          



+1
-1










ppl are facing issues in evaluate.py for task A2

    ---

    ### 💬 Post 476 by @rohitgarg  
    **Posted on:** 2025-02-15 17:15 UTC  

    folks, need a confirmation. i don’t know but i heard it from someone or somewhere.
we cannot send json in response, if it is success ? need to send text
is that really the case ?

    ---

    ### 💬 Post 477 by @s.anand  
    **Posted on:** 2025-02-15 17:21 UTC  

    @rohitgarg - thanks for this. Merged your PR pointing to the correct link for evaluate.py

    ---

    ### 💬 Post 478 by @23F3004407_RATANPRIY  
    **Posted on:** 2025-02-15 18:07 UTC  

    Sir from which session to which session is about tds project?

    ---

    ### 💬 Post 479 by @23f2003413  
    **Posted on:** 2025-02-15 18:22 UTC  

    week-5 session-1 & week-5 session-3

    ---

    ### 💬 Post 481 by @23f3004114  
    **Posted on:** 2025-02-15 18:38 UTC  

    Here is  a Bruno collection (open source alternate for postman) for API testing A1 to A6
bruno collection

    ---

    ### 💬 Post 484 by @abhigyandsa  
    **Posted on:** 2025-02-15 18:44 UTC  

    On my system evaulate.py is throwing an error on A2 trying to execute npx on format.md before the llm is even invoked. However running the command directly on the command line works.
evaluate.py:
*🖼️ Image description: That's a digital image of a shiny, red circle.  It resembles a ball or a bubble.* A2 failed: Command ‘[‘npx’, ‘prettier@3.4.2’, ‘–stdin-filepath’, ‘data/format.md’]’ returned non-zero exit status 2.
*🖼️ Image description: That's a red 'X' symbol on a black background.  It's a simple, somewhat rounded, graphic representation of the letter X.* A2 FAILED
bash:
npx prettier@3.4.2 --stdin-filepath data/format.md
bash works as expected. Can someone help?

    ---

    ### 💬 Post 485 by @22f3001777  
    **Posted on:** 2025-02-15 18:56 UTC  

    @carlton
Is there a maximum size limit for the Docker Image?
Thanking you

    ---

    ### 💬 Post 486 by @RoyalAagman  
    **Posted on:** 2025-02-15 19:34 UTC  

    @carlton @Jivraj
Hi ,
I am trying to build using both docker and podman but it failed on both. I have watched many videos trying to resolve this adn also chatgpt in order to resolve the issue but it seems to persist. I even uninstalled and reinstalled both podman and doceker multiple times but no help.
When i run command docker build -t ___________ .
the error that comes is :
Dockerfile:2
1 |     # Use a lightweight Python image
2 | >>> FROM python:3.12-slim
3 |
4 |     # Set the working directory in the container
ERROR: failed to solve: python:3.12-slim: failed to resolve source metadata for Docker Hub Container Image Library | App Containerization failed to copy: httpReadSeeker: failed open: failed to do request: Get “https://docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com/registry-v2/docker/registry/v2/blobs/sha256/6f/6f3c6367c5a38963f84310cbb24dfcfbddab1dad40cff18afb8fe89098891f08/data?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=f1baa2dd9b876aeb89efebbfc9e5d5f4%2F20250215%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250215T192245Z&X-Amz-Expires=1200&X-Amz-SignedHeaders=host&X-Amz-Signature=ed37cf0c346e2ed440f29638ec43ce66640bdc7d285e7be7bf25c308c46fd6b1”: dialing docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443 container via direct connection because static system has no HTTPS proxy: connecting to docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com:443: dial tcp: lookup docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.com: no such host
Even tried getting python:3.12-slim separatly and trying again but that also didn’t work.
I think there is some problem in getting python:3.12-slim as the build always stops at this.
on asking ChatGPT it shows that some DNS or network issue is there. I even tried all the remedy that was provided on creating custom network etc. but this was also of no use
Kindly help me finding solution to this and pls mention any other assistance I may require to get this running
Thank You.
Regards,
Aagman

    ---

    ### 💬 Post 487 by @22f3000639  
    **Posted on:** 2025-02-15 19:53 UTC  

    i am getting this error, I have tried many times but still the error persists:
“message”: “Bearer YOUR_AIPROXY_TOKEN is invalid: JWSInvalid: Invalid Compact JWS”

    ---

    ### 💬 Post 488 by @22f3000639  
    **Posted on:** 2025-02-15 19:56 UTC  

    someone please help!!!

    ---

    ### 💬 Post 490 by @rohitgarg  
    **Posted on:** 2025-02-15 19:59 UTC  

    @carlton needed a confirmation on this task
A8 * `/data/credit-card.png` contains a credit card number. Pass the image to an LLM, have it extract the card number, and write it without spaces to `/data/credit-card.txt - in this task i assume prompt can ask for credit card number or other details like cvv and name.
My question is, whether my system should allow prompt that CVV or or such info ? or should give it ?

    ---

    ### 💬 Post 491 by @23f2001413  
    **Posted on:** 2025-02-15 20:29 UTC  

    Previously I asked for some more credits to test my project. I got an email stating I have been provided with a new token but I think I got that same token again, not a new one. I still cant send request to the AIPROXY. Please help.


Do I need to submit the docker image name with the tag or without the tag? I submitted it before without the tag. Now i see that I have tagged the image with as v1 but I cant submit the form due to pattern matching problems. Should i submit again after tagging it with :latest ?


@s.anand @carlton @Jivraj

    ---

    ### 💬 Post 492 by @23f1002279  
    **Posted on:** 2025-02-15 21:20 UTC  

    @Jivraj @carlton  sir in the phase B will the input and output path will be given ?

    ---

    ### 💬 Post 493 by @22f3000819  
    **Posted on:** 2025-02-15 21:44 UTC  

    @carlton @Jivraj @Saransh_Saini
When I run my docker image using
podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME
Task A2 fails as the podman container is unable to find npx.
Running the same image using
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME
works fine and Task A2 passes. I can’t understand why this is happening.
I also ran the image in both docker and podman in interactive mode as show in the below snippet from terminal.
When run using docker, which node gives /usr/bin/node as output but when run using podman, nothing.
shiva@shiva:~/Desktop/tdsp1$ sudo podman run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo docker run --rm -it docker.io/myusername/myreponame /bin/sh
# echo $PATH
/root/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# which node
/usr/bin/node
# exit
shiva@shiva:~/Desktop/tdsp1$ sudo podman run --user=root --rm -it docker.io/myusername/myreponame /bin/sh
# which node
# which node
# exit

    ---

    ### 💬 Post 494 by @23f1003186  
    **Posted on:** 2025-02-15 22:00 UTC  

    Here’s how to prompt folks. Just do what @carlton mentioned in today’s live session (the 5 hour marathon) and you should be good for Project-1!


x.com


*🖼️ Image description: That's a close-up headshot of a smiling man with dark hair, glasses, and a short beard.  He's wearing a dark shirt, and a blurred cityscape is visible in the background.*
Aakash Gupta
@aakashg0

Most people are still prompting wrong.

I've found this framework, which was even shared by OpenAI President Greg Brockman.

Here’s how it works: pic.x.com/2MMcEqBeIJ*🖼️ Image description: This image shows a breakdown of an "o1 prompt," which is a type of prompt used in AI systems.  The prompt requests a list of three unique, medium-length hikes near San Francisco, with specific details about each hike. The image is broken down into sections for the goal, the desired return format, warnings for accuracy, and contextual information about the requester's preferences and circumstances.*


8:06 PM - 14 Feb 2025


      5.5K
    


      360

    ---

    ### 💬 Post 495 by @Yogesh1  
    **Posted on:** 2025-02-15 23:08 UTC  

    Same issue. Got the same token. Can’t use it since 2 dollar limit has been crossed. Please help. @carlton @Jivraj

    ---

    ### 💬 Post 496 by @23f2001286  
    **Posted on:** 2025-02-16 03:01 UTC  

    Yes I also need the answer of this.

    ---

    ### 💬 Post 497 by @23f2001286  
    **Posted on:** 2025-02-16 03:03 UTC  

    Is there any way of figuring what is the usage of my token and if yes then how…
Plz some peers help…

    ---

    ### 💬 Post 498 by @carlton  
    **Posted on:** 2025-02-16 03:06 UTC  

    It will be corrected soon by @jkmadathil
He is in charge of our budget for TDS and the tokens are being issued by him.
Please tag him for any token related issues.

    ---

    ### 💬 Post 499 by @jkmadathil  
    **Posted on:** 2025-02-16 03:34 UTC  

    New token assigned to the students.  Emails are also sent.

    ---

    ### 💬 Post 500 by @23f2001286  
    **Posted on:** 2025-02-16 04:34 UTC  

    sir I am noticing a pattern, that when I am running the datagen first. And then using the evaluate.py, then I am getting the A2 right.
But running the evaluation.py for the 2nd time cause the A2 to fail…
Probabbly Because the file in the data folder gets upated should I worry for that…

    ---

    ### 💬 Post 501 by @Jayeshbansal  
    **Posted on:** 2025-02-16 05:21 UTC  

    in the phase B, we have no idea about how many arguments are there, so should we make every function mapping with 2 arguments ( 1 containing the input location and other containing output location) or should we take the parameters in some other way

    ---

    ### 💬 Post 502 by @carlton  
    **Posted on:** 2025-02-16 06:21 UTC  

    There has been an outage in some parts of the country related to cloudflare servers. What helped some students (and us) is using a completely different network eg. instead of using your home wifi, use mobile internet, since they go through a different DNS and this sometimes works.
Kind regards

    ---

    ### 💬 Post 503 by @carlton  
    **Posted on:** 2025-02-16 06:22 UTC  

    We have not specified a size limit for the docker image, so in theory there is not a limit to the docker image size.
Kind regards

    ---

    ### 💬 Post 504 by @kushabarodekar  
    **Posted on:** 2025-02-16 06:26 UTC  

    Hello  @carlton Sir,
While running evaluate.py , I have observed that the expected  and actual output is having difference like “\n” then also it marks task as fail.
eg:
*🖼️ Image description: That's a yellow triangle with a black exclamation mark inside.  It's a common warning symbol.* EXPECTED:
Cover west give likely individual though question inside. System many human plant card among provide. Large former seek mouth there long.
Attention officer successful. Us population the true show.
Real cold if play side wind affect. Street cause investment receive have miss page station.
Cold rest term her conference. Animal sure campaign new.
Meeting back page exactly itself book forward. Decision western series under from shoulder. Pay during feeling newspaper human. Professional old recent beyond girl three human.
Difficult yourself build increase back put others.
Although artist operation thing skin lead. Billion deep measure down adult suggest. Anything action start artist when first.
Whole way know down. Music machine trip father rather.
Must medical bad law issue.
Someone explain seven maintain wrong day factor property.
*🖼️ Image description: That's a yellow triangle with a black exclamation mark in the center.  It's a warning symbol.* RESULT:
“Cover west give likely individual though question inside. System many human plant card among provide. Large former seek mouth there long.\nAttention officer successful. Us population the true show.\nReal cold if play side wind affect. Street cause investment receive have miss page station.\nCold rest term her conference. Animal sure campaign new.\nMeeting back page exactly itself book forward. Decision western series under from shoulder. Pay during feeling newspaper human. Professional old recent beyond girl three human.\nDifficult yourself build increase back put others.\nAlthough artist operation thing skin lead. Billion deep measure down adult suggest. Anything action start artist when first.\nWhole way know down. Music machine trip father rather.\nMust medical bad law issue.\nSomeone explain seven maintain wrong day factor property.\n”
*🖼️ Image description: That's a red "X" symbol on a black background.  It's a simple, somewhat rounded, graphic representation of the letter X.* A5 FAILED
Will this be considered as failure in actual evaluation as well or will this be taken care in actual evaluation?

    ---

    ### 💬 Post 505 by @Kabir1203  
    **Posted on:** 2025-02-16 06:34 UTC  

    *🖼️ Image description: A browser window displays a JSON response indicating the successful execution of a Python script (`datagen.py`) located on GitHub, using a specified email address.  The URL in the address bar shows a local server address and a request to install something.*image1412×248 16.3 KB
Im able to execute the query succesfully.
*🖼️ Image description: A Windows file explorer window shows the contents of a "data" folder, including several files and subfolders, with details such as date modified, type, and size.  The left pane displays standard folders like "Pictures," "Documents," etc.*image1109×570 40.3 KB
But the data gets downloaded to C drive instead of the project folder
The datagen.py file is in the project folder itself.
*🖼️ Image description: A code snippet in Python that sets the project root directory and creates a 'data' subdirectory within it if it doesn't already exist.  It uses `os.path` functions for path manipulation and `os.makedirs` to create directories.*image821×149 9.61 KB
am I making any error when setting the directories?
Please help, have been facing this issue since the beginning of this project, initially tried to move the files from C drive to project folder but that does not seem like a viable solution.

    ---

    ### 💬 Post 506 by @Kabir1203  
    **Posted on:** 2025-02-16 06:51 UTC  

    *🖼️ Image description: The image contains Python code that extracts a URL and email address from a task description, downloads a Python script from the URL, checks if a UV package is installed (installing it if necessary), and then runs the downloaded script with the extracted email address as a parameter.  The code uses regular expressions for extraction, the `requests` library for downloading, and the `subprocess` library for running the script.  Error handling is included.*image1123×760 42.8 KB
I am also running datagen.py in the project directory, yet data folder is created in C drive.

    ---

    ### 💬 Post 507 by @23f2001286  
    **Posted on:** 2025-02-16 06:54 UTC  

    @jkmadathil
sir plz renew my token…
Showing,
{‘message’: ‘On 2025-02 you used $2.0041067399999912, exceeding $2’}
Sorry sir!..

    ---

    ### 💬 Post 508 by @21f3002277  
    **Posted on:** 2025-02-16 06:57 UTC  

    use PlainTextResponse for /read

    ---

    ### 💬 Post 509 by @23f2001286  
    **Posted on:** 2025-02-16 06:59 UTC  

    Plz do someone reply.

    ---

    ### 💬 Post 510 by @Kabir1203  
    **Posted on:** 2025-02-16 07:04 UTC  

    @carlton @s.anand @Jivraj
Please review the code and help me fix the error in order to proceed further. Thanks.

    ---

    ### 💬 Post 511 by @23f1002382  
    **Posted on:** 2025-02-16 07:19 UTC  

    github.com/ANdIeCOOl/TDS_CLUTCH_PROJECT_1


README.md

main

# TDS_CLUTCH_AT_6AY







using code generation, getting 6/10 or * if lucky, similar comments needs a tool function call for sure, maybe someone can implement and create pull request, if you all can get 10/10 fine tuning with tool functions
@Jivraj @carlton Please help if it meets deliverables

    ---

    ### 💬 Post 512 by @23f2001286  
    **Posted on:** 2025-02-16 08:28 UTC  

    Sir I need a help, In hte B portion where no any destination and source files are given…
There we need to ask the user to povide the source and destination files or does we should store it in any default file locations…
As the statement is very vauge saying the “agent should handle this”…
Thanks Sir!!

    ---

    ### 💬 Post 513 by @23f2001286  
    **Posted on:** 2025-02-16 09:09 UTC  

    @jkmadathil @carlton @Jivraj
Sir earlier my code was running fine, but after the assigment of the new token,
it is now showing 400 bad request, which simply implies there is something wrong with the token…
plz do something sir…
*🖼️ Image description: The image shows a terminal output displaying two HTTP requests.  A POST request to `/run` received a 400 Bad Request response, and a GET request to `/read` received a 404 Not Found response.  The requests appear to be related to a SQLite database containing concert ticket sales data.*
I have do have cross verified the new token been correctly been assigned to the system variable…

    ---

    ### 💬 Post 514 by @23f2001286  
    **Posted on:** 2025-02-16 09:19 UTC  

    More Particularily the failure occurs in the response portion…
def get_completions(prompt: str):
    print("Inside get_completions")#Debug
    with httpx.Client(timeout=20) as client:
        response = client.post(
            f"{openai_api_chat}",
            headers=headers,
            json=
                {
                    "model": "gpt-4o-mini",
                    "messages": [
                                    {"role": "system", "content": "You are a function classifier that extracts structured parameters from queries."},
                                    {"role": "user", "content": prompt}
                                ],
                    "tools": [
                                {
                                    "type": "function",
                                    "function": function
                                } for function in function_definitions_llm
                            ],
                    "tool_choice": "auto"
                },
        )

    print("DId suceessful llm calll")#Debug

INFO:     127.0.0.1:52108 - "POST /run?task=The+SQLite+database+file+%60%2Fdata%2Fticket-sales.db%60+has+a+%60tickets%60+with+columns+%60type%60%2C+%60units%60%2C+and+%60price%60.+Each+row+is+a+customer+bid+for+a+concert+ticket.+What+is+the+total+sales+of+all+the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 HTTP/1.1" 400 Bad Request

    ---

    ### 💬 Post 515 by @23f2003413  
    **Posted on:** 2025-02-16 09:19 UTC  

    is there any limit on the size of the docker image @Jivraj @carlton ? because mine is about 5.6Gb

    ---

    ### 💬 Post 516 by @23f2001286  
    **Posted on:** 2025-02-16 09:20 UTC  

    bhai nhi hai…
koi size limit

    ---

    ### 💬 Post 517 by @23f3002091  
    **Posted on:** 2025-02-16 10:12 UTC  

    uv run https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/evaluate.py
Installed 13 packages in 543ms
Traceback (most recent call last):
File “/tmp/evaluateF6zgG9.py”, line 20, in 
from datagen import (
…<9 lines>…
)
ModuleNotFoundError: No module named ‘datagen’
I am getting this error when I try to run evaluate.py
when I run the evaluate.py by having datagen.py in same folder , it is running perfectly. But my doubt is only after task a1 runs the datagen.py will be downloaded into the /data folder right ?
@carlton @Saransh_Saini @Jivraj
Kindly help me with this issue

    ---

    ### 💬 Post 518 by @Aditya_Sahu  
    **Posted on:** 2025-02-16 10:15 UTC  

    Use following as first parameter of subprocess.run() to create data/ directory inside your project instead of C: drive
["uv", "run", script_url, user_email, "--root", "./data"]

Also, you don’t need to download to script, you can directly run it from the url.

    ---

    ### 💬 Post 519 by @Aditya_Sahu  
    **Posted on:** 2025-02-16 10:33 UTC  

    The reason for error is evaluate.py is trying to import datagen.py which doesn’t exist in your system. I’ll suggest download both the files, keep them in same folder and run evaluate.py from your computer

    ---

    ### 💬 Post 520 by @23f3002091  
    **Posted on:** 2025-02-16 10:35 UTC  

    Yes actually Thats my doubt , when I run both in same folder it is working , but only after task a1 runs datagen.py will be downloaded in /data folder  right ?,
or did I misunderstood something??

    ---

    ### 💬 Post 521 by @TheVishal  
    **Posted on:** 2025-02-16 10:38 UTC  

    Generation-Based Automation Agent (No Hard Coding)
Repository Link: GitHub - 23f2005593/tds
Currently, it can complete 7 out of 10 tasks. In reality, it can complete 9 out of 10 tasks, but the expected results are not flexible in evaluate.py file.
If we can extract credit card numbers, it will be able to complete 10 out of 10 tasks.
Please contribute to this repository. We will win together.

    ---

    ### 💬 Post 522 by @21F1005510  
    **Posted on:** 2025-02-16 10:42 UTC  

    {
“message”: “On 2025-02 you used $2.0041388599999848, exceeding $2”
}
What to do?

    ---

    ### 💬 Post 523 by @21F1005510  
    **Posted on:** 2025-02-16 10:43 UTC  

    facing same error, have you fouind any solution?

    ---

    ### 💬 Post 524 by @21f3000745  
    **Posted on:** 2025-02-16 11:07 UTC  

    sir for this task- A6 Find all Markdown (.md ) files in /data/docs/ . For each file, extract the first occurrance of each H1 (i.e. a line starting with #  ). Create an index file /data/docs/index.json that maps each filename (without the /data/docs/ prefix) to its title (e.g. {"README.md": "Home", "path/to/large-language-models.md": "Large Language Models", ...} )   …I am getting correct result for all files but for the very first file budget.md it shows wrong.
my result- { “budget.md”: “Success easy same main modern doctor.”,
“build.md”: “Shoulder follow own never above.”,
and in the data files there is different heading in budget.md.-  # Series dog who make specific agree between.
my question is this if it works for all the files then why not for this file budget.md    @Saransh_Saini @Jivraj @carlton

    ---

    ### 💬 Post 526 by @21f3000745  
    **Posted on:** 2025-02-16 11:14 UTC  

    do you able to do this task * A5. Write the first line of the 10 most recent .log file in /data/logs/ to /data/logs-recent.txt, most recent first …
i am also doing using prompt no hard-coded.

    ---

    ### 💬 Post 527 by @21f3000745  
    **Posted on:** 2025-02-16 11:15 UTC  

    yes doing this only but finding correct for most of the files.

    ---

    ### 💬 Post 528 by @TheVishal  
    **Posted on:** 2025-02-16 11:17 UTC  

    yes i am able to do task a5.

    ---

    ### 💬 Post 530 by @21f3000745  
    **Posted on:** 2025-02-16 11:19 UTC  

    so you directly using prompt for doing this task.

    ---

    ### 💬 Post 531 by @TheVishal  
    **Posted on:** 2025-02-16 11:20 UTC  

    yes i am only using prompt based method

    ---

    ### 💬 Post 532 by @21f3000745  
    **Posted on:** 2025-02-16 11:22 UTC  

    If filename has number in its name then extract the number from the filename and convert it to an integer before sorting .Ensure numbers inside filenames are compared as integers, not as strings, to maintain proper order. Sort filenames in said in task. Avoid any lexicographical sorting issues.    i am using this extra info for doing this but still it does not give accurate result. can you help me in this

    ---

    ### 💬 Post 533 by @TheVishal  
    **Posted on:** 2025-02-16 11:23 UTC  

    i already shared my repo u can check there.

    ---

    ### 💬 Post 534 by @23f2003751  
    **Posted on:** 2025-02-16 12:17 UTC  

    you have pushed data,datagen and evaluate files…do we have to submit them as well??
(also send the docker file)

    ---

    ### 💬 Post 535 by @Saransh_Saini  
    **Posted on:** 2025-02-16 12:24 UTC  

    Check the file once, there is a possibility that it’s either fetching a comment or the second heading. Refactor your prompt to search only for the First Heading, specify it explixitly.

    ---

    ### 💬 Post 536 by @21f3000745  
    **Posted on:** 2025-02-16 12:34 UTC  

    okay let me check once.
one more thing sir {“first_name”: “Crystal”, “last_name”: “Wilson”, “email”: “delgadorebecca@example.com”}   then what will be the sorted-contact for this as in email there is no first and lastname present. @Saransh_Saini

    ---

    ### 💬 Post 537 by @23f1000371  
    **Posted on:** 2025-02-16 12:58 UTC  

    Hey, I submitted the project links in the google form yesterday but, today in the portal it shows that I have not submitted the project.

    ---

    ### 💬 Post 538 by @23f2005325  
    **Posted on:** 2025-02-16 13:11 UTC  

    I am getting this error while running evaluate.py on task A9
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"

🔴 A9 failed: 'data'

There were no authentication issues till yesterday.
please guide @carlton @Jivraj @Saransh_Saini

    ---

    ### 💬 Post 540 by @Saransh_Saini  
    **Posted on:** 2025-02-16 13:20 UTC  

    This is happening because evaluate.py is unable to fetch your API Key from the environment variables. Create a new variable and set it’s value to your API Key then try.

    ---

    ### 💬 Post 541 by @Flibon  
    **Posted on:** 2025-02-16 13:22 UTC  

    Hi everyone,
I’m running into an issue with the AI Proxy embeddings endpoint while executing the A9 task. Every time I send a POST request to:
bash
Copy
https://aiproxy.sanand.workers.dev/openai/v1/embeddings

I receive a 401 Unauthorized response. This, in turn, causes my code to fail with a KeyError: 'data' because the expected JSON response doesn’t include the "data" key.
What I’ve Tried

Token Verification:


I’m using the AIPROXY_TOKEN obtained by logging in at aiproxy.sanand.workers.dev with my IITM email.
The token is passed in the header as follows:

python
Copy
"Authorization": f"Bearer {AIPROXY_TOKEN}"


I added debug prints to confirm that the token is being used correctly (printing the first few characters).


API Request Details:


The request includes the correct Content-Type: application/json header.
The payload is set as:

json
Copy
{"model": "text-embedding-3-small", "input": ["Test"]}


Despite this, the response status is consistently 401 Unauthorized.


Debug Output:
Here’s a snippet of the debug output:

bash
Copy
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 401 Unauthorized"
🔴 A9 failed: 'data'

This confirms that the issue is with the authentication rather than our processing logic.
What I Suspect

The token may be invalid, expired, or misconfigured.
There could be changes in the token permissions or endpoint requirements that I’m not aware of.
Alternatively, there might be an issue on the server side with token validation.

Request for Help
Has anyone else encountered this issue recently? Could someone verify if there are any changes to the authentication requirements for the embeddings endpoint? Any insights or updated instructions on how to ensure the token is valid and has the proper permissions would be greatly appreciated.
Thanks in advance for your assistance!

    ---

    ### 💬 Post 542 by @23f2001286  
    **Posted on:** 2025-02-16 13:26 UTC  

    B5. Run a SQL query on a SQLite or DuckDB database
Should I ask for the SQL data base. Or the agent should be smart enough to find the required database…
Moreover in the data folder there is only one database is it should be robust to handle multiple databases…

    ---

    ### 💬 Post 543 by @23f2004644  
    **Posted on:** 2025-02-16 13:31 UTC  

    same issue i also face                   pls sir help us fix this issue and provide us more  token
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings “HTTP/1.1 429 Too Many Requests”
*🖼️ Image description: That's a simple image of a shiny, red circle or sphere.  It appears to be a cartoonish or stylized rendering.* A9 failed: ‘data’
@Jivraj @carlton @Saransh_Saini

    ---

    ### 💬 Post 544 by @bhashwar_sengupta  
    **Posted on:** 2025-02-16 13:55 UTC  

    I had a question on evaluation by the course team. To test that my application would run everywhere, I first deleted all images from my local machine using podman rmi -a and then ran podman run --rm -p 8000:8000 -e AIPROXY_TOKEN=$AIPROXY_TOKEN $IMAGE_NAME with the appropriate variables set. This is as per the instructions provided here. But this gave me the following error:
Error: short-name "freshbash/dataworks-agent" did not resolve to an alias and no unqualified-search registries are defined in "/etc/containers/registries.conf

The above is the format in which we have to provide the image name in the Google form. So, I was confused whether this would succeed during actual evaluation.
The only way its working right now is when I specify the image name to be docker.io/freshbash/dataworks-agent
I’m not yet very good with how containers work so some insights would be very helpful. Thanks!

    ---

    ### 💬 Post 545 by @23f1002382  
    **Posted on:** 2025-02-16 14:06 UTC  

    Nice bro, if its getting 8 you are sorted, probably get more later. But Prompting seems a little less info
BUT





Structured Outputs
JSON Mode




Outputs valid JSON
Yes
Yes


Adheres to schema
Yes (see supported schemas)
No


Compatible models
gpt-4o-mini, gpt-4o-2024-08-06, and later
gpt-3.5-turbo, gpt-4-* and gpt-4o-* models


Enabling
response_format: { type: json_schema, json_schema: {strict: true, schema: …} }
response_format: { type: json_object }



    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"}
        )



github.com/23f2005593/tds


app.py

main


      
          prompt = (
              f"The Python code generated for the task '{task}' produced the following error when executed:\n"
              f"{error_message}\n\n"
              f"Here is the original code:\n{original_code_data['code']}\n\n"
              "Please provide a corrected version of the code that fixes the error. Return only a JSON object with:\n"
              "- code: the corrected Python code as a string\n"
              "- function_name: name of the main function\n"
              "- required_libraries: list of required pip packages\n\n"
              "Make sure the code is simple, direct, and error-free this time. And try not to mess it up like before."
          )
          try:
              response = client.chat.completions.create(
                  model="gpt-4o-mini",
                  messages=[{"role": "user", "content": prompt}],
                  temperature=0,
                  response_format={"type": "json_object"}
              )
          except Exception as exc:
              logger.error("Error connecting to OpenAI API for auto-fix: %s", exc)
              raise HTTPException(status_code=500, detail="Connection error during auto-fix. Maybe it's time to admit defeat?")
          
      
    





you are taking a chance on that format

    ---

    ### 💬 Post 546 by @23f1002382  
    **Posted on:** 2025-02-16 14:18 UTC  

    *🖼️ Image description: A Codespaces usage summary showing 172.37 of 180.00 core hours and 9.21 of 20.00 GB-months used.  No charges are shown.  Quotas reset in 10 days.  A spending limit can be set.*Screenshot 2025-02-16 0913411315×404 24.2 KB
*🖼️ Image description: A Codespaces usage summary shows 120 of 120 included core hours used and 1.46 of 15 GB-months used, both at $0.00 cost.  Quotas reset in 13 days.*Screenshot 2025-02-16 0911011351×292 13.3 KB
Hardest i ever worked in my life. Thank you @s.anand

    ---

    ### 💬 Post 547 by @23f1002382  
    **Posted on:** 2025-02-16 14:26 UTC  

    *🖼️ Image description: That's a circular image depicting a stylized owl's face.  The owl appears mechanical or robotic, with glowing blue eyes and intricate, dark metal-like detailing around its features.  It's set within an ornate, circular frame with dark, purplish-brown hues.* TheVishal:

If we can extract credit card numbers, it will be able to complete 10 out of 10 tasks.


have tried function calling? with open code generation ?

    ---

    ### 💬 Post 548 by @TheVishal  
    **Posted on:** 2025-02-16 14:32 UTC  

    not yet… but i have another problem when i am running this by using docker it is giving error “datagen module not found”

    ---

    ### 💬 Post 549 by @TheVishal  
    **Posted on:** 2025-02-16 14:32 UTC  

    bro please help by contribute please

    ---

    ### 💬 Post 550 by @23f1002382  
    **Posted on:** 2025-02-16 14:35 UTC  

    come off on one meet

    ---

    ### 💬 Post 551 by @23f2003413  
    **Posted on:** 2025-02-16 14:35 UTC  

    what should we push in the github repo @Jivraj @carlton ??
is it enough if we just push the Dockerfile, app.py, datagen.py and the LICENSE. Someone pls help!

    ---

    ### 💬 Post 552 by @23f1002382  
    **Posted on:** 2025-02-16 14:35 UTC  

    bro i used all my codespaces credits xD
i am nitpicking and editing from website and running not exceed limit XD

    ---

    ### 💬 Post 553 by @23f2003413  
    **Posted on:** 2025-02-16 14:36 UTC  

    someone pls help T_T

    ---

    ### 💬 Post 554 by @23f1002382  
    **Posted on:** 2025-02-16 14:37 UTC  

    submit image and github  repo link, evalhaters will handle the rest im assuming

    ---

    ### 💬 Post 555 by @23f2003413  
    **Posted on:** 2025-02-16 14:38 UTC  

    yeaa i got that but what should we add in the github repo…like should we add the generated data folder?
or is it enough if we just add the code and the Dockerfile to the repo

    ---

    ### 💬 Post 556 by @23f1002382  
    **Posted on:** 2025-02-16 14:38 UTC  

    doesn’t matter they use only image

    ---

    ### 💬 Post 557 by @TheVishal  
    **Posted on:** 2025-02-16 14:38 UTC  

    use local editor naa bro

    ---

    ### 💬 Post 558 by @23f1002382  
    **Posted on:** 2025-02-16 14:39 UTC  

    and run my code xD i have one crazy setup XD give me some time, at 9:30 we’ll hop on eachother

    ---

    ### 💬 Post 559 by @23f2003751  
    **Posted on:** 2025-02-16 14:39 UTC  

    which repo u submitting yesterday one or todays.
i am unable to run the yesterday one

    ---

    ### 💬 Post 560 by @23f1002382  
    **Posted on:** 2025-02-16 14:40 UTC  

    this one new one only xD

    ---

    ### 💬 Post 561 by @23f2003413  
    **Posted on:** 2025-02-16 14:40 UTC  

    and what do they mean by image-name in the gform…is it the repo name in dockerhub?

    ---

    ### 💬 Post 562 by @23f2003751  
    **Posted on:** 2025-02-16 14:40 UTC  

    what evil have u done xd

    ---

    ### 💬 Post 563 by @23f1002382  
    **Posted on:** 2025-02-16 14:41 UTC  

    why? ///////////// O—O

    ---

    ### 💬 Post 564 by @23f2003751  
    **Posted on:** 2025-02-16 14:41 UTC  

    dockerhub image name

    ---

    ### 💬 Post 565 by @23f2003751  
    **Posted on:** 2025-02-16 14:42 UTC  

    ur words are saying something else *🖼️ Image description: That's a simple, yellow smiley face emoticon with small, black eyes and a small, curved smile.*

    ---

    ### 💬 Post 566 by @23f2003413  
    **Posted on:** 2025-02-16 14:42 UTC  

    image name as in i dont get it lol.

    ---

    ### 💬 Post 567 by @shubhamatkal  
    **Posted on:** 2025-02-16 14:43 UTC  

    (general) [shubham@laptop data]$ curl https://api.openai.com/v1/models -H "Authorization: Bearer $AIPROXY_TOKEN"
{
  "error": {
    "message": "Your authentication token is not from a valid issuer.",
    "type": "invalid_request_error",
    "param": null,
    "code": "invalid_issuer"
  }

pls help

    ---

    ### 💬 Post 568 by @23f2003751  
    **Posted on:** 2025-02-16 14:43 UTC  

    push ur image to docker hub that it will be available for them to use
(use chatgpt on how to push to docker hub 2 3 steps to flw)

    ---

    ### 💬 Post 569 by @23f2003413  
    **Posted on:** 2025-02-16 14:45 UTC  

    yeah i hv pushed the image to dockerhub but i exactly dont get what image name is
like is it the name of my repo

    ---

    ### 💬 Post 570 by @23f2003751  
    **Posted on:** 2025-02-16 14:46 UTC  

    ur docker-username/image-name

    ---

    ### 💬 Post 571 by @23f2003413  
    **Posted on:** 2025-02-16 14:46 UTC  

    check if u have exported the AIPROXY_TOKEN properly in your environment

    ---

    ### 💬 Post 572 by @23f2003751  
    **Posted on:** 2025-02-16 14:47 UTC  

    anyone check my repo

github.com



*🖼️ Image description: This is a GitHub project page for "Tusharisme/TDS_Project_1".  The project has one contributor, zero issues, zero stars, and zero forks.  A small, blue, pixelated icon is displayed.*
GitHub - Tusharisme/TDS_Project_1
Contribute to Tusharisme/TDS_Project_1 development by creating an account on GitHub.

    ---

    ### 💬 Post 573 by @shubhamatkal  
    **Posted on:** 2025-02-16 14:48 UTC  

    yes i have the same key which is provided on ai proxy website for my login
and yes i have that key properly exported

    ---

    ### 💬 Post 574 by @23f2003413  
    **Posted on:** 2025-02-16 14:55 UTC  

    check if u have used the correct ai proxy url then

    ---

    ### 💬 Post 575 by @Yogesh1  
    **Posted on:** 2025-02-16 14:58 UTC  

    An email I just received says my license doesn’t have “MIT” in it. Although it does have it. I don’t know what I am missing. Someone help (if you didn’t get this mail). @carlton @Jivraj

    ---

    ### 💬 Post 576 by @22f3001307  
    **Posted on:** 2025-02-16 14:59 UTC  

    @carlton @Jivraj @Saransh_Saini
Hi,
I received a mail saying that my submission has no Dockerfile. But git repo has a dockerfile.
even if i am to submit again, i have submit the same repo.
what should i do?

    ---

    ### 💬 Post 577 by @21f2001550  
    **Posted on:** 2025-02-16 15:00 UTC  

    Hey I just got a mail saying that my github repo has no Dockerfile present. and im confused .
It doesnt mention anywhere that the dockerfile must be present in the root directory as a requirement/prerequisite of the project.
In my case its present inside the app directory. Could the team help clarify on this issue.
@Jivraj @carlton

    ---

    ### 💬 Post 578 by @23f2004636  
    **Posted on:** 2025-02-16 15:01 UTC  

    What is expected repo structure ?
I have a folder in my repo and dockerfile and license are present in that folder but I still received a mail regarding missing License and Dockerfile.

    ---

    ### 💬 Post 579 by @shubhamatkal  
    **Posted on:** 2025-02-16 15:08 UTC  

    do we need to have data folder in repo no right?

    ---

    ### 💬 Post 580 by @22f3001307  
    **Posted on:** 2025-02-16 15:11 UTC  

    No, it is not needed

    ---

    ### 💬 Post 581 by @22f3001011  
    **Posted on:** 2025-02-16 15:14 UTC  

    We see that your submission GitHub - 22f3001011/project-1  has a result of FAIL due to the below reasons:
No “MIT” in LICENSE
Hello sir, i got this mail despite having added the mit license as stated in the project problem statement. I cant figure out what the issue is, and help me out here.
@carlton @Jeeveash.k

*🖼️ Image description: Failed to load image: cannot identify image file <_io.BytesIO object at 0x772a474389a0>*
github.com


GitHub - 22f3001011/project-1
main
Contribute to 22f3001011/project-1 development by creating an account on GitHub.






Thank you
Regards
Shashank J Shetth
22f3001011

    ---

    ### 💬 Post 582 by @Yogesh1  
    **Posted on:** 2025-02-16 15:22 UTC  

    Yeah. Same issue. Someone who didn’t get this error, please share the MIT license.

    ---

    ### 💬 Post 584 by @23f2002592  
    **Posted on:** 2025-02-16 15:31 UTC  

    https://github.com/saniyanz/tds-p1new
check my repo. whats wrong. Ive also got the mail but I`ve included the MIT License and the Dockerfile

    ---

    ### 💬 Post 585 by @23f1001231  
    **Posted on:** 2025-02-16 15:32 UTC  

    Rename LICENSE.txt to LICENSE

    ---

    ### 💬 Post 586 by @nayonika  
    **Posted on:** 2025-02-16 15:41 UTC  

    I got a mail saying my Dockerfile is missing. However I have a dockerfile already in my github repository. Is it an issue with the spelling of dockerfile since I have submitted it in all small case as ‘dockerfile’. It was showing the score when I checked with the evaluate.py that was provided by iitm.
Shall I just change the name of the file from ‘dockerfile’ to ‘Dockerfile’ in github repository of mine or is there anything else that is needed to detect the Dockerfile?

    ---

    ### 💬 Post 587 by @21f2001550  
    **Posted on:** 2025-02-16 15:42 UTC  

    Hey team, I just moved my Dockerfile to the root level on my Github repo. Hope this solves the issue.
Small doubt: Do i need to submit the google form again?

    ---

    ### 💬 Post 589 by @23f1002909  
    **Posted on:** 2025-02-16 15:53 UTC  

    I ran out of tokens. Please help me. Please its urgent.

    ---

    ### 💬 Post 590 by @ShahbaazSingh  
    **Posted on:** 2025-02-16 15:57 UTC  

    @carlton sir @s.anand sir please provide me more tokens, I am out of tokens i don’t knwo what happened i hade 151 requests use and 0.09 usd and suddenly i check it was 300 requests and 2 usd i don’t knwo what happened can you provide me more tokens.

    ---

    ### 💬 Post 591 by @lakshaygarg654  
    **Posted on:** 2025-02-16 16:00 UTC  

    Dear @s.anand , @carlton , @Jivraj , and @Saransh_Saini
Thank you all for this wonderful project. Coming from a non-coding background, I have learned a lot new things throughout this project building process.
@carlton Sir, yesterday’s session provided valuable insights into Method 1 (prompt engineering) for dynamically handling tasks. I was able to develop an application using this approach; however, due to submission time constraints, I could not verify all tasks (my bad). While I tested some tasks and found the results to be highly accurate, I was unable to validate everything thoroughly.
Therefore, I submitted the function-calling approach (Method 2) instead.
I sincerely appreciate everyone’s guidance and support.

    ---

    ### 💬 Post 592 by @ShahbaazSingh  
    **Posted on:** 2025-02-16 16:09 UTC  

    Did you ran out of tokens suddenly like me ?
How many requests have you sent in total ?

    ---

    ### 💬 Post 593 by @23f2003751  
    **Posted on:** 2025-02-16 16:17 UTC  

    can u share ur repo
i really need it

    ---

    ### 💬 Post 594 by @Saransh_Saini  
    **Posted on:** 2025-02-16 16:24 UTC  

    Thanks @lakshaygarg654 for this feedback. Glad to know you learned from our efforts, it means a lot. This proves that even a person from non-tech background with determination can achieve it.

    ---

    ### 💬 Post 595 by @23f2004644  
    **Posted on:** 2025-02-16 16:26 UTC  

    sir pls provide more token   @Saransh_Saini @Jivraj @s.anand                              sir pls , give any reply we have only 2 hr left

    ---

    ### 💬 Post 596 by @Saransh_Saini  
    **Posted on:** 2025-02-16 16:29 UTC  

    Change the name of your dockerfile to “Dockerfile”

    ---

    ### 💬 Post 597 by @ShahbaazSingh  
    **Posted on:** 2025-02-16 16:29 UTC  

    yes sir please provide more tokens to me also @s.anand @Jivraj @carlton @Saransh_Saini

    ---

    ### 💬 Post 598 by @23f1002382  
    **Posted on:** 2025-02-16 16:38 UTC  

    i hope i get 1 mark xD
im getting tasks only maybe 3 / 10

    ---

    ### 💬 Post 599 by @Algsoch  
    **Posted on:** 2025-02-16 16:55 UTC  

    i have done many attempt but it is not working please show  my environment saying fastapi is not installed but i have installed and it is showing on checking but no running file it is saying no module i have installed in both virtual and system
please help

    ---

    ### 💬 Post 600 by @Algsoch  
    **Posted on:** 2025-02-16 17:01 UTC  

    *🖼️ Image description: A screenshot shows a VS Code window displaying Python code and terminal output.  The code appears to be a FastAPI application. The terminal shows errors related to pip and a missing `fastapi` module, indicating a package installation issue.  The file explorer shows a project directory structure.*image1919×1016 117 KB
this problem occuring sir since two days

    ---

    ### 💬 Post 601 by @Kabir1203  
    **Posted on:** 2025-02-16 17:02 UTC  

    How long does it take to make a docker image, I’ve been doing it for the past 25 minutes and it’s still not completed.

    ---

    ### 💬 Post 602 by @lakshaygarg654  
    **Posted on:** 2025-02-16 17:09 UTC  

    Your LLM app should be designed like it can give desire result based on task desc at run endpoint, and that result should be accessible at read endpoint.


Evaluation file just for reference to check how things works and it works for phase A tasks only. Also ensure datagen.py file and evaluation.py file are latest. There is one issue in evaluation.py file for task A1,  link of datagen.py file not correct, rectify that link. Even it corrected in GitHub repo file but when I download that raw file in local system it takes back previous link.

    ---

    ### 💬 Post 603 by @23f1002382  
    **Posted on:** 2025-02-16 17:18 UTC  

    I WONDER HOW MANY API REQUESTS THE SERVER IS PROCESSING . It’s too slow

    ---

    ### 💬 Post 604 by @23ds1000005  
    **Posted on:** 2025-02-16 17:43 UTC  

    too much in the last few hours it feel

    ---

    ### 💬 Post 605 by @22f1000120  
    **Posted on:** 2025-02-16 18:31 UTC  

    I guess what is done is done. I should have maintained my version history properly. I am getting 4 correct but with minor formatting issues so only 1 correct I guess.

    ---

    ### 💬 Post 606 by @22f1000120  
    **Posted on:** 2025-02-16 18:35 UTC  

    It was tough… I will probably not score much but I enjoyed it a lot. Thank you for pushing us so hard. At least I am not scared of docker now and function calling feels easier than before.

    ---

    ### 💬 Post 607 by @s.anand  
    **Posted on:** 2025-02-16 18:42 UTC  

    Well done, everyone! This is not an easy project. This is the kind of work our clients are asking us for.
I will keep you posted on the evaluation on this thread, it progresses.

2025-02-16T18:31:00Z Google Form closed
2025-02-16T18:35:00Z Validating submissions. Will post results shortly

    ---

    ### 💬 Post 608 by @22f1000150  
    **Posted on:** 2025-02-16 18:45 UTC  

    Sir i have missed the submission deadline  by 5  minutes, can you give permission for the google form to accept the response for half an hour more.

    ---

    ### 💬 Post 609 by @TheVishal  
    **Posted on:** 2025-02-16 18:46 UTC  

    Sir, due to time panic, I mistakenly named the Docker image incorrectly.

    ---

    ### 💬 Post 610 by @22f1000150  
    **Posted on:** 2025-02-16 18:47 UTC  

    Sir can you please allow submission for 5 more minutes?

    ---

    ### 💬 Post 611 by @Jivraj  
    **Posted on:** 2025-02-19 11:00 UTC  

    A post was merged into an existing topic: Project 1 - Casual banter

    ---

    ### 💬 Post 612 by @Rrishit  
    **Posted on:** 2025-02-16 18:51 UTC  

    @s.anand @carlton
Dear Sir,
I am writing to you in a state of distress and humility. An unfortunate mistake on my part has led to the upload of an incorrect Docker image link. When I checked the authenticity of the link, it showed an error, even though the GitHub repository link is functioning perfectly.
I have poured my heart and soul into this project, dedicating countless hours and sleepless nights to ensure its success. The project has successfully passed both Test A and Test B, and I was thrilled to see my hard work paying off. However, this single error has left me devastated.
I am pleading with you, with all my heart, to allow me to correct this mistake by updating the Docker image link. Alternatively, I humbly request that my application be reviewed directly through GitHub. Please consider this an exception, as I have worked tirelessly over the past two weeks to create an application that is 890 lines long.
I beg for your understanding and leniency in this matter. This project means the world to me, and I am genuinely sobbing over this setback.
Thank you for considering my heartfelt request.
Sincerely,
Rishit Jain
(24F2004595)

    ---

    ### 💬 Post 613 by @psisaddicted  
    **Posted on:** 2025-02-16 18:55 UTC  

    Although couldn’t complete handling every task, but really enjoyed working on this project and learned a lot throughout the process. I appreciate the opportunity to work on such an engaging project. For Project 2, I’ll make sure to allocate sufficient time and approach it with even greater commitment.

    ---

    ### 💬 Post 614 by @TheVishal  
    **Posted on:** 2025-02-16 18:57 UTC  

    Sorry @s.anand @carlton @Jivraj
Sir, due to time panic, I mistakenly named the Docker image incorrectly.

    ---

    ### 💬 Post 615 by @22f1000120  
    **Posted on:** 2025-02-16 19:15 UTC  

    Just push the latest image to docker asap. Hopefully the team considers it.

    ---

    ### 💬 Post 616 by @22f1000120  
    **Posted on:** 2025-02-16 19:16 UTC  

    True. Same here. Just giving 2 days for this project was definitely a big mistake on my part… but I couldn’t really give more time due to work commitments.

    ---

    ### 💬 Post 617 by @TheVishal  
    **Posted on:** 2025-02-16 19:28 UTC  

    @s.anand @carlton @Jivraj
Sir, due to time panic, I mistakenly named the Docker image incorrectly.
I am not 100% sure but i guess i used “ii” instead of “i” in “thevixhal/tdsvishal”… is there any way to check this ?

    ---

    ### 💬 Post 618 by @Sagan  
    **Posted on:** 2025-02-16 19:34 UTC  

    Can the submissions open just for some time? In minutes?
Many students did silly mistakes due toh nervousness, we can just correct it.

    ---

    ### 💬 Post 619 by @GIRISH_VISHVESHVAR_B  
    **Posted on:** 2025-02-17 02:56 UTC  

    I don’t think the project is too difficult to implement—it’s essentially a simple HTTP API for an AI agent that reads a task, converts it into parameters, and passes those parameters to specific functions to complete the task. However, the instructions in the project question aren’t very clear. Before the session, I am unable to fully understand the question. It took me almost an entire day just to understand what we need to do.
Sir Could you provide test cases or a sample answer for Phase B?

    ---

    ### 💬 Post 620 by @lakshaygarg654  
    **Posted on:** 2025-02-17 04:47 UTC  

    @s.anand
@carlton sorry to disturb you, project1 deadline is over.
I made a mistake in my project. In my call llm function i set some payload instead of default for open ai api call like max token, temp. , n, stop etc.
Due to this, some tasks may fail especially credit card image task will fail 100%, if possible can i just remove that payload from git hub repository . or you can check this call llm function present in my task_handler.py file of my repository.
I found this issue after deadline. If possible consider this request. I never engaged in a project or course like for this one. I love this project genuinely.
my github repo : GitHub - 21f3001076/TDS_Project_1: This is IITM Data Science TDS Course Project 1 Repository
Thankyou
Lakshay
student id: 21f3001076@ds.study.iitm.ac.in

    ---

    ### 💬 Post 621 by @23f1001611  
    **Posted on:** 2025-02-17 05:41 UTC  

    Dear @s.anand @carlton @Jivraj ,
Thank you so much for this wonderful project! We have learned so many things from this experience, especially the power of prompts. The team has put in tremendous effort, extending a few sessions and patiently clearing all our doubts. We truly appreciate the dedication and support
Regards,
Arjun

    ---

    ### 💬 Post 622 by @swatikap  
    **Posted on:** 2025-02-17 05:48 UTC  

    I would like to sincerely thank the course faculty @carlton @Jivraj @Saransh_Saini for their support on the project throughout the week. They were so patient in listening to our issues and helping us resolve them, even if the issues were repeated.
I was not able to complete some or maybe many of the tasks but overall, it was a very good learning for me, and I thoroughly enjoyed it.
Thanks very much again for your guidance and support.
Regards,
Swati

    ---

    ### 💬 Post 623 by @Saransh_Saini  
    **Posted on:** 2025-02-17 09:28 UTC  

    Thanks for your compliments Swati. It’s always nice to know our efforts paid off.
Happy Learning *🖼️ Image description: That's a cartoon image of a yellow hand giving a thumbs-up gesture.*

    ---

    ### 💬 Post 624 by @Udipth  
    **Posted on:** 2025-02-17 10:07 UTC  

    I have received a mail that my project has ""No “MIT” in LICENSE;No Dockerfile " which I saw today. My project has MIT licence and Dockerfile was also there… but to reconfirm I pulled my dockerfile from dockerhub to github only . NOw am not sure will that be considered now in my project submission or not. Requesting to kindly consider current state of my project in submission for my project.

    ---

    ### 💬 Post 625 by @23f1002382  
    **Posted on:** 2025-02-17 11:09 UTC  

    WOMP WOMP should i call a wambulance?

    ---

    ### 💬 Post 626 by @23f1002382  
    **Posted on:** 2025-02-17 11:10 UTC  

    (post deleted by author)

    ---

    ### 💬 Post 627 by @23f1002382  
    **Posted on:** 2025-02-17 11:12 UTC  

    @all those who didn’t submit, its ok EVEN I did NOT submit. Even though i get zero, i am happy with the learning i did. Once again thank you sir @carlton @s.anand . This a been awesome experience , i haven’t been this alive in forever. Cheers.

    