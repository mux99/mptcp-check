from flask import Flask, request, render_template, Response
from subprocess import check_output

app = Flask(__name__)

@app.route("/")
def mptcp_status_page():
    """
    Flask route to display MPTCP connection status.

    Retrieves the visitor's IP and port, checks for MPTCP data in the connections dictionary,
    and renders the webpage with the connection status.

    Returns:
    Rendered webpage with connection status and MPTCP version if established.
    """

    addr = request.remote_addr
    port = request.environ.get('REMOTE_PORT')

    try:
        conn = check_output(f"ss -MnH dest {addr} dport {port}").decode()
        if conn.startswith("ESTAB"):
            state_message = 'Established'
            state_class = 'success'
        else:
            state_message = 'Not Established'
            state_class = 'fail'
    except Exception as e:
        state_message = '[error: ' + str(e) + ']'
        state_class = 'error'

    return render_template('index.html', state_message=state_message, state_class=state_class)

@app.route('/stream_audio')
def stream_audio():
    def generate_audio():
        with open('sounds/joyful-whistle-186300.mp3', 'rb') as f:
            while True:
                audio_chunk = f.read(1024)
                if not audio_chunk:
                    break
                yield audio_chunk

    return Response(generate_audio(), mimetype='audio/mpeg')

