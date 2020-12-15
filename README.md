# kindle-highlights

A python script that organises your kindle's "My Clippings.txt" file, by removing duplicates and separating highlights into their respective books. Organised highlights are made readable due to a simple user interface.

### To use

It is important to run the following bash command prior to executing the script to ensure the clippings file is of correct format.

```
awk '{ gsub(/\xef\xbb\xbf/,""); print }' My\ Clippings.txt > clippings
python3 highlights.py
```

