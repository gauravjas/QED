from flask import Flask, request, send_from_directory, redirect, render_template, flash, url_for, jsonify, \
    make_response, abort

from predict import WordGloveChatBot



app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

word_glove_chat_bot = WordGloveChatBot()


word_glove_chat_bot_conversations = []



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return 'About Us'


@app.route('/word_glove_reply', methods=['POST', 'GET'])
def word_glove_reply():
    if request.method == 'POST':
        if 'sentence' not in request.form:
            flash('No sentence post')
            redirect(request.url)
        elif request.form['sentence'] == '':
            flash('No sentence')
            redirect(request.url)
        else:
            sent = request.form['sentence']
            word_glove_chat_bot_conversations.append('YOU: ' + sent)
            reply = word_glove_chat_bot.reply(sent)
            word_glove_chat_bot_conversations.append('MR. DROGO: ' + reply)
    return render_template('word_glove_reply.html', conversations=word_glove_chat_bot_conversations)



    target_text = sentence
    if level == 'word-glove' and dialogs == 'Anoop':
        target_text = word_glove_chat_bot.reply(sentence)
    
    return jsonify({
        'sentence': sentence,
        'reply': target_text,
        'dialogs': dialogs,
        'level': level
    })


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
   
    word_glove_chat_bot.test_run()
   
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    main()
