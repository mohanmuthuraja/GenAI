from flask import Flask

#app = Flask(__name__) # __name__ is a special variable in Python that represents the name of the current module. 
# When you run a Python script, __name__ is set to "__main__". When you import a module, __name__ is set to the name of the module. 
# In this case, it allows Flask to know where to look for resources and templates.


#print(__name__) # Output: __main__

# what does this __main__ do in flask?
# In Flask, when you run a script directly, __name__ is set to "__main__". 
# This allows Flask to know that the script is being run directly and not imported as a module.

app = Flask(__name__)  # This line creates an instance of the Flask class, which is the main application object.

@app.route('/') # This is a decorator that tells Flask to execute the following function when the root URL ("/") is accessed.
def hello_world():
    return 'Hello, World!' # This function returns the string "Hello, World!" when the root URL is accessed.

if __name__ == '__main__': # This checks if the script is being run directly (as the main program) and not imported as a module.
    app.run(debug=True) # If the script is run directly, this line starts the Flask development server with debug mode enabled.
