# Print the zen of Python
info = '''The Zen of Python is a collection of 19 "guiding principles" for writing computer programs that influence the design of the Python programming language.\n'''
print(info, '\n')

print('Call it simply by using "import this".\n')
import this

enc = f'There is an encrpyted message accessible with this.s\n\n{this.s}:\n'
print(enc)

print(f'''
Decode it by accessing the decypher keys stored in this.d: 
\n{this.d}\n
Which translates to:\n
'''
)
print(''.join([this.d.get(c, c) for c in this.s]))
# help(this)