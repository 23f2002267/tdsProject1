#script for uv



#import desired libraries
import requests
import json
from datetime import datetime, timezone
import time
import os
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, GoogleAPIError

#initialize variables
flag = True
check = 0
page = 1
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 4, 14)
filtered_topics = []


#set request to desired url
headers = {
    "User-Agent": "Mozilla/5.0",  # Trick to act like a browser
    "Cookie": "_fbp=fb.2.1718951579112.28665138622696015; _ga_QHXRKWW9HH=GS1.3.1719729972.1.1.1719730294.0.0.0; _ga=GA1.1.29277095.1718951579; _ga_YRLBGM14X9=GS1.1.1725418822.1.0.1725418824.58.0.0; _gcl_au=1.1.2073226685.1742536470; _ga_5HTJMW67XK=GS2.1.s1750168191$o105$g1$t1750168263$j60$l0$h0; _ga_08NPRH5L4M=GS2.1.s1750168156$o445$g1$t1750169893$j33$l0$h0; _t=TkavLwh3nA2GOq9omDDK5TCFN38oYT%2B1Oz%2BocPWcVdfUvdfVHg5uObPG2IOk%2F4NDAeyj7T3NvD0%2Bj6brv210stiAIem9bH%2BoyplYUSvB8n4psxRYJvhxE8OWZmAbrOMogAVKNTEOWdOOKTbMqnmAkMYW8eatrVxTgQ6W0qhLk%2Bsb1jHrW00p6zh3s64A5trSLc73FO6ivJsmZfag3pkblH3n3X02C4O3Wk75GV4vKAQxduVc42I2Eq0%2B4CwumSTUVA95%2BceghGa%2Bsd8i9JqMSkzotoz5QbWyKr0wNOJHTqRbmGat96z77qNnIwhgDCse--IjXjI9wtJERQCNgD--G8HGtKI1vc8aDePOL22%2BpA%3D%3D;_forum_session=pSWmw4akuKRcP9s4k3I3TPg0r%2B237qjL9lBYPbMfduIu3yLH9Vp9T8m8U%2F6eg%2FBpMb%2BAWPvOwYX97fi8C%2BzM%2B4gjYbDlKcCzQfKmXkfWhvxQa8K%2FROX73LYQZc849uwNytIpgQamcUGjdJMbxPLn4eiyCudyylsWB5qVjRmKHtbdVOZtUsmKAIryK5Ss0c5%2B28Ll2Q6YuEPa81k3DVCflJJfB%2BXn268LlPUxpBkdNmtkk5DLaYLkijHDmjd0Qa0Db8AjH1VgpgiBwSrb%2Ba3KwAumwbAtFw%3D%3D--RUVEodq4S1FdsmMv--4ISbkmJR8Z%2Fjjd0Gz60hog%3D%3D"
}

while check < 5:
    try:
        url = f"https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34/l/latest.json"
        params = {
            "filter": "latest",
            "page": page
        }
        res = requests.get(url, params=params, headers=headers)
        data = res.json()
        topics = data['topic_list']['topics']
        if check == 5:
            print("No more topics. Scraping complete.")
            break

        for topic in topics:
            created_at = datetime.fromisoformat(topic["created_at"].replace("Z", "+00:00"))
            created_at = created_at.replace(tzinfo=None)
            if start_date <= created_at <= end_date:
                flag = False
                filtered_topics.append((topic["id"], topic["slug"]))
            else:
                continue

        if flag == False:
            flag = True
        else:
            check += 1

        page += 1
        print(check)
        time.sleep(0.5)  # Sleep to respect the server

    except Exception as e:
        print(f"An error occurred: {e}")
        break


#loop the request to get the data until the end of the date
for topic_id, topic_slug in filtered_topics:
    url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}.json"
    res1 = requests.get(url, headers=headers)
    data1 = res1.json()
    post_ids = data1['post_stream']['stream']    
    output_file = f"{topic_slug}.md"
    #if output file already exists, skip to avoid overwriting
    if os.path.exists(output_file):
        print(f"File {output_file} already exists. Skipping...")
        continue
    else:
        chunk_size = 20
        sleep_sec = 0.5
        max_retries = 10

        # ---- CREATE / CLEAN FILE ----
        Path(output_file).write_text(f"# Thread Markdown: {topic_id}\n\n", encoding="utf-8")

        # ---- DUMMY IMAGE DESCRIBER ----
        def describe_image_via_llm(image_url: str) -> str:

            genai.configure(api_key="API_KEY_HERE")  # Replace with your actual API key

            try:
                # Download image
                response = requests.get(image_url)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
            except Exception as e:
                return f"Failed to load image: {e}"

            model = genai.GenerativeModel("gemini-1.5-flash")

            retries = 0
            wait = 1  # initial wait time in seconds

            while retries < max_retries:
                try:
                    result = model.generate_content([
                        "Describe this image briefly. Ignore emojis.",
                        image
                    ])
                    return result.text.strip()

                except ResourceExhausted as e:
                    print(f"[Retry {retries+1}] Quota exhausted: {e}. Retrying in {wait}s...")
                except GoogleAPIError as e:
                    if e.code == 429:
                        print(f"[Retry {retries+1}] Rate limit hit: {e}. Retrying in {wait}s...")
                    else:
                        raise
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    break

                time.sleep(wait)
                retries += 1
                wait *= 2  # exponential backoff

            return "Unable to describe image due to rate limits or quota exhaustion."
        # ---- HTML → Markdown with Image Descriptions ----
        def convert_html_to_markdown_with_image_descriptions(html):
            soup = BeautifulSoup(html, "html.parser")

            for img in soup.find_all("img"):
                src = img.get("src", "")
                img_url = f"https://discourse.onlinedegree.iitm.ac.in{src}" if src.startswith("/") else src
                description = describe_image_via_llm(img_url)
                desc_tag = soup.new_tag("p")
                desc_tag.string = f"*🖼️ Image description: {description}*"
                img.replace_with(desc_tag)

            return soup.get_text().strip()

        # ---- CHUNK HANDLER ----
        def chunker(lst, size):
            for i in range(0, len(lst), size):
                yield lst[i:i + size]

        # ---- FETCH POSTS ----
        def fetch_posts(post_chunk):
            url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}/posts.json"
            params = [("post_ids[]", pid) for pid in post_chunk]
            params.append(("include_suggested", "false"))
            res = requests.get(url, headers=headers, params=params)
            return res.json().get("post_stream", {}).get("posts", [])

        # ---- MARKDOWN BUILDER ----
        def to_markdown(post):
            created = datetime.fromisoformat(post["created_at"].replace("Z", "+00:00"))
            author = post.get("username", "unknown")
            raw_html = post.get("cooked", "").strip()
            markdown_body = convert_html_to_markdown_with_image_descriptions(raw_html)

            return f"""---

        ### 💬 Post {post['post_number']} by @{author}  
        **Posted on:** {created.strftime('%Y-%m-%d %H:%M')} UTC  

        {markdown_body}

        """

        # ---- MAIN LOOP ----
        for chunk in chunker(post_ids, chunk_size):
            posts = fetch_posts(chunk)
            markdown_blocks = [to_markdown(p) for p in posts]

            with open(output_file, "a", encoding="utf-8") as f:
                f.writelines(markdown_blocks)

            print(f"✅ Appended {len(posts)} posts.")
            time.sleep(sleep_sec)

        print(f"\n🎉 Done. Markdown saved to: {output_file}")