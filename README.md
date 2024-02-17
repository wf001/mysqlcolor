# mysqlcolor
mysqlcolor is a simple Python script that enhances the readability of log files by adding indentation and colorizing SQL queries. It is particularly useful for developers and system administrators who frequently inspect log files containing SQL queries.

## Features
- **Indentation**: Automatically adds indentation to SQL queries and other key log entries, making it easier to identify query blocks.
- **Colorization**: Highlights SQL keywords and query components with different colors, improving visibility and comprehension.
- **Customization**: Easily customize the color scheme and indentation preferences to suit your preferences or project requirements.
- **Real-time Processing**: Supports real-time processing of log files, allowing users to monitor logs as they are updated.

| before                                                                                   | after                                                                                    |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| ![](https://github.com/wf001/wf001/assets/36895006/795db3e0-cb8f-47fb-ae85-67c79c50c8c4) | ![](https://github.com/wf001/wf001/assets/36895006/3b630671-8d84-492c-88de-3fc6bde55bab) |

## Installation
``` bash
git clone https://github.com/wf001/mysqlcolor
```
``` bash
cd mysqlcolor
```
``` bash
pip instatll termcolor
```
Any addtional installation required. Simply download the log_colorizer.py script and run it with Python.


## Usage
Simply pipe the log file content to the script to apply indentation and colorization. For example:

``` bash
tail -f your_log_file.log | python main.py
```

## Requirements
- Python 3.x
- termcolor library (install via pip install termcolor)

## License
- This project is licensed under the MIT License - see the LICENSE file for details.
