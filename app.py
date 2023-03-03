from flask import Flask, render_template, request, redirect, url_for
import openai
import os
import random
import json
import webbrowser

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = "YOUR KEY HERE"

# Define function to generate a new sentence
def generate_sentence(prompt):
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Define function to generate a weird sentence
def generate_weird_sentence(prompt):
    response = openai.Completion.create(
        engine="text-ada-001",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
	#temperature=2,
	#frequency_penalty=2.0
    )
    return response.choices[0].text.strip()

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generate_story():
    button = request.form.get('button')
    #print(button);
    story_so_far = request.form['story']
    if button == 'normal':
	    new_sentence = generate_sentence(story_so_far)
	    print('normal')
    elif button == 'weird':
            new_sentence = generate_weird_sentence(story_so_far)
            print('weird')
    story_so_far += " " + new_sentence
    return render_template('index.html', story=story_so_far, new_sentence=new_sentence)

@app.route('/review')
def review():
    return render_template('review.html')


if __name__ == '__main__':
    webbrowser.open_new('http://localhost:5000')
    app.run(debug=True,use_reloader=False) # use_reloader=False prevents web page opening twice per https://stackoverflow.com/questions/63958054/webbrowser-open-open-two-tabs

