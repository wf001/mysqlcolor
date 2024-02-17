import sys
import re
import json
from termcolor import colored

# JSON ファイルから置換対象と色付け対象を読み込む
with open('query_keywords_replace.json') as replace_file:
    QUERY_KEYWORDS_REPLACE = json.load(replace_file)

with open('query_keywords_color.json') as color_file:
    QUERY_KEYWORDS_COLOR = json.load(color_file)

def colorize_mysql_log():
    try:
        # パイプから入力を受け取る
        for line in sys.stdin:
            # 行を整形
            formatted_line = re.sub(r'\s+', ' ', line.strip())
            formatted_line = re.sub(r'\s*Execute\s*', ' Execute', formatted_line)
            formatted_line = formatted_line.replace('Execute', colored('Execute', 'red'))
            
            # クエリのキーワードごとに置換を行う
            for keyword, replace_str in QUERY_KEYWORDS_REPLACE.items():
                formatted_line = re.sub(r'\s*' + re.escape(keyword), replace_str, formatted_line)

            # クエリのキーワードごとに色付けを行う
            for keyword, color in QUERY_KEYWORDS_COLOR.items():
                formatted_line = formatted_line.replace(keyword, colored(keyword, color))

            if 'Prepare' in formatted_line:
                continue

            print(colored("===========================================", 'blue'))
            print(formatted_line, "\n")
    except KeyboardInterrupt:
        # Ctrl+Cが押されたときに終了する
        sys.exit(0)

if __name__ == "__main__":
    colorize_mysql_log()

