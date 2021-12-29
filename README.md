# rythem-App-Python
This is app is used to extract Arabic words by their endings. this was built mainly to help me write poems. 


## this is app takes tons of arabic poems in `poetry.txt` then formats the file as words seperated with new lines. 

This function return the list of words that match the endstring argument.
also the mode argument specifys if the search should be `reduced` or `nreduced` which means wether we want the endig exactly match the `تشكيل` or not. 
```python
findWords(words, endString="ل", mode="reduced")
``` 
