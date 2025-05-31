import json
import os

CONFIG_FILENAME = "platform_config.json"

def init_platform_config():
    if os.path.exists(CONFIG_FILENAME):
        print(f"[!] {CONFIG_FILENAME} already exists.")
        return

    config_data = {
        "zhihu": {
            "cookies": ""
        },
        "xiaohongshu": {
            "cookies": ""
        }
    }

    with open(CONFIG_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(config_data, f, indent=4, ensure_ascii=False)

    print(f"[*] Created {CONFIG_FILENAME}. Please fill in your cookies.")