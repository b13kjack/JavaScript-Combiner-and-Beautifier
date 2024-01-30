# About [JavaScript Combiner and Beautifier](https://github.com/b13kjack/JavaScript-Combiner-and-Beautifier)

Simple python script that combines and beautifies js chunks (from compiled react web apps etc.) or multiple scripts into one file.
In the future I plan to add deobfuscate feature as well


# Install

Script runs fine on python 3.9+

To install JSCB and it's requirements:
```
git clone https://github.com/b13kjack/JavaScript-Combiner-and-Beautifier

cd JavaScript-Combiner-and-Beautifier

pip install -r requirements.txt
```

# Usage

Simply run:
```
python jscb.py <directory>

For example:

python jscb.py C:\js_chunks
```

You can also hardcode the directory in the script itself. Just change the value of the variable "js_directory" to your desired directory.
