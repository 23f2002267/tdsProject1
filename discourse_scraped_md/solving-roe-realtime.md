# Thread Markdown: 168943

---

        ### 💬 Post 1 by @23f1002382  
        **Posted on:** 2025-03-02 07:30 UTC  

        I’ll try to post whatever i solve lol XD

        ---

        ### 💬 Post 2 by @23f1002382  
        **Posted on:** 2025-03-02 08:04 UTC  

        Q 7 LLM Embeddings (1 mark)
SecurePay, a leading fintech startup, has implemented an innovative feature to detect and prevent fraudulent activities in real time. As part of its security suite, the system analyzes personalized transaction messages by converting them into embeddings. These embeddings are compared against known patterns of legitimate and fraudulent messages to flag unusual activity.
Imagine you are working on the SecurePay team as a junior developer tasked with integrating the text embeddings feature into the fraud detection module. When a user initiates a transaction, the system sends a personalized v…
ANSWER:
{
“model”: “text-embedding-3-small”,
“input”: [
“Dear user, please verify your transaction code 33692 sent to roe-23f1002382@ds.study.iitm.ac.in”,
“Dear user, please verify your transaction code 66801 sent to roe-23f1002382@ds.study.iitm.ac.in”
]
}

        ---

        ### 💬 Post 3 by @23f1002382  
        **Posted on:** 2025-03-02 08:05 UTC  

        Q^: 6 Move and rename files (1 mark)
Download q-move-rename-files.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt.
ANSWER:
unzip /workspaces/TDS/q-move-rename-files.zip -d extracted_folder123123
    5  mkdir empty_folder 
    6  find extracted_folder -type f -exec mv {} empty_folder/ \; 
    7  ls
    8  find extracted_folder123123 -type f -exec mv {} empty_folder/ \; 
    9  cd empty_folder  
   10  for file in *; do       new_name=$(echo "$file" | tr '0123456789' '1234567890')  ;     mv "$file" "$new_name"  ; done  
   11  grep . * | LC_ALL=C sort | sha256sum

        ---

        ### 💬 Post 4 by @23f1002382  
        **Posted on:** 2025-03-02 08:13 UTC  

        Sydney,Brisbane,Perth,Jakarta,Singapore,Dubai,Doha
flights

        ---

        ### 💬 Post 5 by @23f1002382  
        **Posted on:** 2025-03-02 08:14 UTC  

        150,171,174
for studebts

        