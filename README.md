# kindle-highlights

A python script that organises your kindle's "My Clippings.txt" file, by removing duplicates and separating highlights into their respective books. Organised highlights are made readable due to a simple user interface.

### To use

Run "highlights.sh" which executes the following (Ensure that "My Clippings.txt" is in current directory):

```
awk '{ gsub(/\xef\xbb\xbf/,""); print }' My\ Clippings.txt > clippings
python3 highlights.py
```

