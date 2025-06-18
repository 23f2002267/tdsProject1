# Thread Markdown: 161120

---

        ### 💬 Post 1 by @s.anand  
        **Posted on:** 2025-01-03 07:12 UTC  

        Please post any questions related to Graded Assignment 2 - Deployment Tools.

Important Instruction
Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. Visit this link for more details: Extended Syntax | Markdown Guide.
A friendly suggestion: kindly go through Discourse Docs! *🖼️ Image description: That's a simple yellow smiley face emoticon.  It has two small black dots for eyes and a small, slightly curved line for a mouth.*

Deadline: Sunday, February 2, 2025 6:29 PM
@carlton @Jivraj

        ---

        ### 💬 Post 2 by @carlton  
        **Posted on:** 2025-01-08 03:10 UTC  

        

        ---

        ### 💬 Post 4 by @22f3001315  
        **Posted on:** 2025-01-12 17:08 UTC  

        *🖼️ Image description: The image shows a code snippet asking for a GitHub Pages URL, followed by an error message and some HTML code.  The error indicates a specific URL is not found in the response. The HTML includes metadata and basic styling for a webpage.*Screenshot 2025-01-12 2236301727×195 27.1 KB
i have included the email address still its giving error

        ---

        ### 💬 Post 5 by @22f3001315  
        **Posted on:** 2025-01-12 17:12 UTC  

        *🖼️ Image description: The image shows a code snippet asking for a Vercel URL, showing an example, and then a user-entered URL.  Below that, a "TypeError: Failed to fetch" error message is displayed.*Screenshot 2025-01-12 2239561674×158 12.8 KB
that website is working fine . just  write the parameters after /api

        ---

        ### 💬 Post 6 by @Jivraj  
        **Posted on:** 2025-01-12 21:38 UTC  

        Hi Guddu,
Can you share your GitHub repo. For GitHub pages question.

        ---

        ### 💬 Post 7 by @Jivraj  
        **Posted on:** 2025-01-12 21:39 UTC  

        Check your browser console most probably CORS is causing problem.
Try adding CORS to your code it might work.
Kind regards
Jivraj

        ---

        ### 💬 Post 8 by @22f3001315  
        **Posted on:** 2025-01-13 04:10 UTC  

        github.com



*🖼️ Image description: The image shows a GitHub repository page for `gkfrombs/dolfacts`.  The repository has one contributor, zero issues, zero stars, and zero forks.  A simple graphic is displayed next to the repository name.*
GitHub - gkmfrombs/dolfacts
Contribute to gkmfrombs/dolfacts development by creating an account on GitHub.






I have added email in body two times in different ways.

        ---

        ### 💬 Post 9 by @23F300327  
        **Posted on:** 2025-01-13 20:23 UTC  

        *🖼️ Image description: A screenshot shows a macOS terminal window running a Python FastAPI application using Uvicorn.  The code defines an API endpoint to retrieve student data from a CSV file, optionally filtered by class.  The terminal also displays Uvicorn's startup messages and API request logs.  A web browser window shows a simple UI for interacting with the API.*Screenshot 2025-01-14 at 1.39.39 AM1440×900 154 KB
@carlton can you please tell me what is wrong in this because I am getting “Error: Response undefined does not match expected” to my answer

        ---

        ### 💬 Post 10 by @22f2001640  
        **Posted on:** 2025-01-14 08:16 UTC  

        Facing Issue in GA 2 Question 10 LLM ngrok
*🖼️ Image description: An ngrok error message (ERR_NGROK_8012) indicates that while traffic successfully reached the ngrok agent, a connection to the upstream web service at `http://localhost:8080` failed due to a connection refusal.  Instructions are provided for developers (check the local web service) and visitors (wait and refresh).*image1920×886 45.7 KB
I tired multiple times but issue is still there.
@carlton @Jivraj @s.anand Kindly help me out.

        ---

        ### 💬 Post 11 by @carlton  
        **Posted on:** 2025-01-14 08:51 UTC  

        Hi Mishkat,
Please use  triple backticks to encapsulate code, so that we can debug your code more easily.
eg
if __name__ == "__main__":
   print ("Hello")

Please use this discourse etiquette to share code.
Thanks and kind regards

        ---

        ### 💬 Post 12 by @22f3001315  
        **Posted on:** 2025-01-14 09:20 UTC  

        sir did you check yet what is the problem in this one?

        ---

        ### 💬 Post 13 by @23F300327  
        **Posted on:** 2025-01-14 10:12 UTC  

        from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load student data from the specified CSV file
students = []
with open('/Users/mish/Downloads/q-fastapi.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
async def get_students(class_: Optional[List[str]] = Query(None)):
    print(f"Requested classes: {class_}")  # Debugging line
    if class_:
        filtered_students = [student for student in students if student["class"] in class_]
        print(f"Filtered students: {filtered_students}")  # Debugging line
        return {"students": filtered_students}
    return {"students": students}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

        ---

        ### 💬 Post 14 by @Jivraj  
        **Posted on:** 2025-01-14 10:30 UTC  

        Hi Mishkat,
This error is because you are filtering on class_ instead of class
So if you send a request on http://127.0.0.1/api?class_=1S you will see response for that 1S class only.
kind regards

        ---

        ### 💬 Post 15 by @23F300327  
        **Posted on:** 2025-01-14 10:38 UTC  

        thank you so much after modifying the code it got accepted

        ---

        ### 💬 Post 16 by @Jivraj  
        **Posted on:** 2025-01-14 11:17 UTC  

        Hi Guddu,
Inside index.html file of your repo, don’t put html code just put your email in the file nothing else.
This issue is because when you deploy on github pages it encrypts any email that’s on page.
kind regards.

        ---

        ### 💬 Post 17 by @Nelson  
        **Posted on:** 2025-01-14 11:23 UTC  

        I am facing an issue with Docker Desktop.
*🖼️ Image description: A Docker Desktop error message indicates an unexpected WSL error.  It suggests shutting down WSL using the command `wsl --shutdown`, rebooting, or reinstalling WSL and/or Docker Desktop.  The detailed error shows WSL2 is not supported with the current configuration.  Options to gather diagnostics and quit are provided.*Docker Desktop Error558×377 27 KB
I have uninstalled and installed Docker (run as administrator).
wsl --version
WSL version: 2.3.26.0
Kernel version: 5.15.167.4-1
WSLg version: 1.0.65
MSRDC version: 1.2.5620
Direct3D version: 1.611.1-81528511
DXCore version: 10.0.26100.1-240331-1435.ge-release
Windows version: 10.0.19045.5011

Tried many solutions after googling for the issue.
So far no solution. Anyone else faced this issue and found a solution?

        ---

        ### 💬 Post 18 by @Jivraj  
        **Posted on:** 2025-01-14 11:26 UTC  

        Hi Telvin,
Try opening localhost:8080 in browser if that works, if it opens in browser then issue might be with some network configurations.
I solved this question in github codespace, which didn’t require me to make any changes in network.
kind regards
kind regards

        ---

        ### 💬 Post 19 by @s.anand  
        **Posted on:** 2025-01-14 11:43 UTC  

        @Nelson I would recommend Podman or Docker CE rather than Docker Desktop.
Docker Desktop is not free for organizations over 250 people and many organizations have therefore moved away from it.

        ---

        ### 💬 Post 20 by @22f2001640  
        **Posted on:** 2025-01-14 12:26 UTC  

        @s.anand @carlton @Jivraj I tired , in browser localhost:8080 is working fine but ngrok is not working. Is there any other tools for tunneling that can be used.

        ---

        ### 💬 Post 21 by @s.anand  
        **Posted on:** 2025-01-14 12:52 UTC  

        @22f2001640 in that case

a firewall or local security settings might block access to port 8080, or
a network restriction is blocking access to port 8080

Please try one of these:

Try the same on a personal laptop on a public / home network
GitHub codespaces, as @Jivraj suggested

You could try an ngrok alternative like localtunnel but I don’t think that’ll work.

        