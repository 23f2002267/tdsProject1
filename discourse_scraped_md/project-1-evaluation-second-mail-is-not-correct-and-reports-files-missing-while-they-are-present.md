# Thread Markdown: 171477

---

    ### 💬 Post 1 by @22f3001832  
    **Posted on:** 2025-04-01 03:38 UTC  

    Mail I received Yesterday:
*🖼️ Image description: This is an email informing a learner that their Project 1 submission failed prerequisite checks.  The checks involved verifying the existence and accessibility of a GitHub repository, a valid Dockerfile, and an MIT license, all of which failed.  Only the Docker image's presence in Dockerhub passed.  The email details the requirements and provides the evaluation results.*Screenshot from 2025-04-01 09-01-071174×451 54.2 KB
Previous Correct Evaluation Mail:
*🖼️ Image description: This is an email evaluating a Project 1 Docker image submission.  The email lists several log files and scripts related to the evaluation, noting that missing files will result in a score of 0.  The evaluation environment is described, and the scores are stated as preliminary, with a deadline for reporting issues.  A final marking schema will be determined based on feedback and the highest scores, including a sample script.*Screenshot from 2025-04-01 09-02-351687×650 144 KB
Good Morning Sir,
This is my github repo: GitHub - kohliaryan/TDS_Project_1 ()You can verify that it is public, MIT License is present and Dockerfile is also present.)
I also got a mail 2 days ago in which everything is mentioned correctly but the mail I got yesterday worry me.  Sir, I have worked really hard for project 1. Please look into this matter.
@carlton

    ---

    ### 💬 Post 2 by @22f3001832  
    **Posted on:** 2025-04-03 12:03 UTC  

    @Jivraj Sir, Please look into in this matter, no reply from your side till now and 2 days have been passed.

    ---

    ### 💬 Post 3 by @carlton  
    **Posted on:** 2025-04-04 06:10 UTC  

    Apologies for that,
The second email was an automated script that used a stricter criteria. You have passed evaluation and also have a score. So dont worry. We will push scores over this weekend. We are currently doing normalisation.
Kind regards

    ---

    ### 💬 Post 4 by @23f2000345  
    **Posted on:** 2025-04-04 14:22 UTC  

    Hi @carlton,
I’m experiencing the same issue mentioned in this thread regarding Project 1 evaluation emails:

The first email I received confirmed all requirements were met (public repo, MIT License, Dockerfile, etc.)
The second email incorrectly flagged missing files despite their presence in my repository

Here are screenshots of both emails showing the discrepancy:
*🖼️ Image description: This is an email containing the results of a project evaluation.  The sender assessed a Docker image submission, noting missing files resulting in a score of 0.  The email provides links to various log files and scripts related to the evaluation, conducted on a Google Cloud compute unit.  The score is preliminary, with a deadline for reporting issues before the final score is determined.*First Evaluation Email1511×724 76.2 KB
*🖼️ Image description: This is an email containing the results of a Project 1 evaluation.  The project required several prerequisites including a public GitHub repository with a Dockerfile and MIT license, and a publicly accessible Docker image matching the repository's Dockerfile. The evaluation shows the Docker image passed but the other checks failed, resulting in a score of 0.*Second Evaluation Email1247×681 37.5 KB
My GitHub repo remains publicly accessible with all required components:
GitHub repo
Could you please confirm this was an automated error and that my submission will be evaluated based on the actual repository contents? Your clarification would be greatly appreciated.
Thank you for your time and assistance!

    ---

    ### 💬 Post 5 by @carlton  
    **Posted on:** 2025-04-04 16:03 UTC  

    Hi,
Prerequisite checks have passed. But your docker image was missing a dependency that you forgot to copy into the image. so it failed to evaluate because it failed to run.

    ---

    ### 💬 Post 6 by @22f3001832  
    **Posted on:** 2025-04-04 17:00 UTC  

    You talking about me or @23f2000345 ?

    ---

    ### 💬 Post 8 by @Sudhishnarayan  
    **Posted on:** 2025-04-12 05:11 UTC  

    Good Morning Sir, Actually even I got the mail regarding Project-1 Evaluation, where I got the message like the prerequisites were not met. But, sir actually I have uploaded my MIT License file, requirements.txt file, my Project.py file and the Dockerfile. Sir, and when I sent a request to my API from my device, it worked sir. I have got 0 in my project 1 sir, but I have met the pre-requisites Can you please check this once sir?
My GitHub repository for Project-1: GitHub - sudhishssn134/project_1_tds
Thanking You
Just attaching the mail I recieved.
*🖼️ Image description: This is an email containing the results of a project evaluation.  The evaluation involved a Docker image submission.  The email states that some files were missing, resulting in a score of 0.  It provides links to various log files and attachments detailing the evaluation's technical aspects and performance.  The email also notes that the evaluation environment was high-performance, and offers to address any concerns about the scoring.*Screenshot 2025-04-12 1042111429×750 71 KB

    ---

    ### 💬 Post 9 by @carlton  
    **Posted on:** 2025-04-12 05:19 UTC  

    Your Dockerfile was misconfigured. When we try to build the docker image from your github repo, we get this error:
tried copying parent folder(COPY failed: forbidden path outside the build context: .. ())
You have to replicate the test environment. If it works when you follow this test setup then you should get in touch with us.


*🖼️ Image description: That's a headshot of a man with short dark hair and glasses. He's wearing a purple collared shirt and has a slight smile.  The background is a plain, light yellow or beige.*
Tds-official-Project1-discrepencies Tools in Data Science


    To replicate the test environment: 
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv. 
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.…

    ---

    ### 💬 Post 10 by @Sudhishnarayan  
    **Posted on:** 2025-04-12 05:22 UTC  

    Oh OK Sir. I will try it out. Thank You so much sir

    ---

    ### 💬 Post 11 by @Sudhishnarayan  
    **Posted on:** 2025-04-12 06:28 UTC  

    Sir, I have extracted the files from the GitHub Repository, built my DockerFile withe the DockerImage I have posted. The build is successful and the dockerimage is also running sir. I have attached the screen shot below
*🖼️ Image description: The image shows a terminal window displaying the output of a Docker build process.  The output includes numerous SHA256 checksums, file sizes, and build steps with their execution times. The process concludes with a message indicating that a Uvicorn server is running on a specified port.  A command line is visible at the bottom, showing the docker run command used.*Screenshot 2025-04-12 1153421466×702 50.4 KB
Sir, But I couldn’t run the last command you gave,
uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000

As I dont have evaluate.py
But, the DockerImage is built and is running without error sir.
Please guide me after this sir
Thank You So much sir

    ---

    ### 💬 Post 12 by @Sudhishnarayan  
    **Posted on:** 2025-04-29 14:34 UTC  

    Sir, I have extracted the files from the GitHub Repository, built my DockerFile withe the DockerImage I have posted. The build is successful and the dockerimage is also running sir. I have attached the screen shot below
*🖼️ Image description: The image shows a terminal window displaying the output of a Docker build process.  The build stages, including extracting layers, exporting manifests, and pushing to a docker registry, are shown with timestamps.  The final lines indicate a successful build and startup of a Uvicorn web server.*Screenshot 2025-04-12 1153421466×702 50.4 KB
Sir, But I couldn’t run the last command you gave,
uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000

As I dont have evaluate.py
But, the DockerImage is built and is running without error sir.
Please guide me after this sir
Thank You So much sir

    ---

    ### 💬 Post 13 by @Jivraj  
    **Posted on:** 2025-04-29 15:19 UTC  

    *🖼️ Image description: Failed to load image: 451 Client Error:  for url: https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png*
URGENT ATTN REQ: technical discrepancy and inconsistency in the evaluation scripts of graded assignment and project 2 Tools in Data Science


    Project 1 : You tried to copy parent folder(Ref:line number 8 in your Dockerfile) but there is no parent folder with respect to github repo’s root folder, so it fails evaluation. 
Project 2 : Response we received through google form was http://127.0.0.1:8000/api which is local host url not a vercel endpoint.

    