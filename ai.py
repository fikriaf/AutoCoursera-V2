import requests, time, sys, string, random, re
import json


hashnya = "czva0ffte"
url = "https://qwen-qwen3-demo.hf.space/gradio_api/queue/join?__theme=light"
url_res = (
    "https://qwen-qwen3-demo.hf.space/gradio_api/queue/data?session_hash=" + hashnya
)
headers = {
    "Host": "qwen-qwen3-demo.hf.space",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
    "Origin": "https://qwen-qwen3-demo.hf.space",
    "Referer": "https://qwen-qwen3-demo.hf.space/?__theme=light",
}

hist = []
n=1
def getanswer(soal):
    teks = soal
    
    print("AI : ")
    # Data JSON yang dikirim
    data = {
        "data": [
                    teks,
                    {
                        "model": "qwen3-235b-a22b",
                        "sys_prompt": "You are a helpful assistant.",
                        "thinking_budget": 38
                    },
                    [],
                    []
                 ],
        "event_data": "null",
        "fn_index": 13,
        "trigger_id": 31,
        "session_hash": hashnya,
    }
    
    requests.post(url, json=data, headers=headers)

    start_time = time.time()
    berhenti = False
    respon = ""
    found_end = False
    try:
        with requests.get(url_res, stream=True) as get_res1:
            for chunk in get_res1.iter_content(chunk_size=1280000000000):
                # print(chunk)
                if chunk:
                    data_string = chunk.decode("utf-8")
                    messages = data_string.split("\n\ndata: ")
                    
                    if "process_completed" in data_string:
                        sys.exit()

                    for message in messages:
                        if "process_generating" in message:
                            try:
                                message_clean = re.sub(r"^data: ", "", message)
                                data_json = json.loads(message_clean)

                                if "output" in data_json and "data" in data_json["output"]:
                                    data_section = data_json["output"]["data"]
                                    
                                    if len(data_section) > 5:
                                        for item in data_section[5]:
                                            if isinstance(item, list) and len(item) > 2:
                                                text_value = item[2]
                                                if item[0] == "replace" and isinstance(item[2], str):
                                                    if "End of Thought" in item[2]:
                                                        found_end = True
                                                elif (
                                                    item[0] == "add"
                                                    and found_end
                                                    and isinstance(item[2], dict)
                                                    and item[2].get("type") == "text"
                                                ):
                                                    print(item[2]["content"], end="", flush=True)
                                                elif isinstance(text_value, str) and text_value not in hist and found_end:
                                                    print(text_value, end="", flush=True)
                                                    respon += text_value
                                                    hist.append(text_value)
                            except Exception as e:
                                pass
    except:
        print("\n")
    hist.append([teks, respon])
    end_time = time.time()
    print(f"Waktu respons: {end_time - start_time:.3f} detik\n")
    return respon
    