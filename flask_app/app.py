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
    mptcp = False

    conn = list(filter(None, check_output(["ss", "-Mt", "-n"]).decode("ascii").split('\n')))
    for c in conn:
        args = list(filter(None, c.split(' ')))
        if (args[-1] == f"{addr}:{port}" and args[0] == "mptcp"):
            mptcp = True
            break

    if mptcp:
        state_message = 'Established'
        state_class = 'success'
    else:
        state_message = 'Not Established'
        state_class = 'error'

    # print()
    return render_template('index.html', state_message=state_message, state_class=state_class)

@app.route('/stream_audio')
def stream_audio():
    def generate_audio():
        # Your audio streaming logic goes here
        # You can read audio data from a file or generate it dynamically
        # Example: Streaming a static audio file
        with open('sounds/joyful-whistle-186300.mp3', 'rb') as f:
            while True:
                audio_chunk = f.read(1024)
                if not audio_chunk:
                    break
                yield audio_chunk

    return Response(generate_audio(), mimetype='audio/mpeg')
