import random
import json

def get_random_list_value(target_list:list) -> str:
    return target_list[random.randint(0, len(target_list)-1)]

def check_word_exists(word:str, text:str) -> bool:
    if f" {word}" in text or f"{word} " in text or f"{word}" == text:
        return True
    return False

if __name__ == "__main__":
    print(get_random_list_value(["oi", "tudo", "bem"]))