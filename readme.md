# getch
getch impl im python
## usage
```python
import getch


# return a char
ch = getch.getch() 

 # return a char without clearing message
ch = getch.getch(message='enter a key')

# return a char and clear message
ch = getch.getch(message='enter a key', clear_line_after_getch=True)

# pause and wait for enter a key [pass -> return_key=True for return pressed key]
getch.pause()

# get password and replace them with '*' you can custom it by replace_with param
# return a list of user inputs
passwd = getch.password('password: ') 

```
# Clone
`git clone https://github.com/omidekz/getch.git`
### and use it like above code 

# Note
it worked with terminals like cmd and bash etc. not working in pycharm console or ...
