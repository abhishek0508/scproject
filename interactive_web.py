#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""
Talk with a model using a web UI.

## Examples

```shell
parlai interactive_web --model-file "zoo:tutorial_transformer_generator/model"
```
"""


from http.server import BaseHTTPRequestHandler, HTTPServer
from parlai.scripts.interactive import setup_args
from parlai.core.agents import create_agent
from parlai.core.worlds import create_task
from typing import Dict, Any
from parlai.core.script import ParlaiScript, register_script
import parlai.utils.logging as logging
from gtts import gTTS
import os
from  playsound import playsound

import speech_recognition as sr


# playsound("out.mp3", True)
# import pyttsx3
# engine = pyttsx3.init()
# engine.setProperty('rate',125)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

import json
import time

HOST_NAME = 'localhost'
PORT = 8080

SHARED: Dict[Any, Any] = {}
STYLE_SHEET = "https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.3.1/js/all.js"
WEB_HTML = """
<html>
    <link rel="stylesheet" href={} />
    <script defer src={}></script>
    <head><title> Interactive Run </title></head>
    <body>
        <div class="columns" style="height: 100%">
            <div class="column is-three-fifths is-offset-one-fifth">
              <section class="hero is-info is-large has-background-light has-text-grey-dark" style="height: 100%">
                <div id="parent" class="hero-body" style="overflow: auto; height: calc(100% - 76px); padding-top: 1em; padding-bottom: 0;">
                    <article class="media">
                      <div class="media-content">
                        <div class="content">
                          <p>
                            <strong>Instructions</strong>
                            <br>
                            Taiga, the chatbot that loves talking to you :)
                          </p>
                        </div>
                      </div>
                    </article>
                </div>
                <div class="hero-foot column is-three-fifths is-offset-one-fifth" style="height: 76px">
                  <form id = "interact">
                      <div class="field is-grouped">
                        <p class="control is-expanded">
                          <input class="input" type="text" id="userIn" placeholder="Type in a message">
                        </p>
                        <p class="control">
                          <button id="respond" type="submit" class="button has-text-white-ter has-background-grey-dark">
                            Submit
                          </button>
                        </p>
                        <p class="control">
                          <button id="restart" type="reset" class="button has-text-white-ter has-background-grey-dark">
                            Restart Conversation
                          </button>
                        </p>
                      </div>
                  </form>
                </div>
              </section>
            </div>
        </div>

        <script>
            function createChatRow(agent, text) {{
                var article = document.createElement("article");
                article.className = "media"

                var figure = document.createElement("figure");
                figure.className = "media-left";

                var span = document.createElement("span");
                span.className = "icon is-large";

                var icon = document.createElement("i");
                icon.className = "fas fas fa-2x" + (agent === "You" ? " fa-user " : agent === "Taiga" ? " fa-robot" : "");

                var media = document.createElement("div");
                media.className = "media-content";

                var content = document.createElement("div");
                content.className = "content";

                var para = document.createElement("p");
                var paraText = document.createTextNode(text);

                var strong = document.createElement("strong");
                strong.innerHTML = agent;
                var br = document.createElement("br");

                para.appendChild(strong);
                para.appendChild(br);
                para.appendChild(paraText);
                content.appendChild(para);
                media.appendChild(content);

                span.appendChild(icon);
                figure.appendChild(span);

                if (agent !== "Instructions") {{
                    article.appendChild(figure);
                }};

                article.appendChild(media);

                return article;
            }}
            document.getElementById("interact").addEventListener("submit", function(event){{
                event.preventDefault()
                var text = document.getElementById("userIn").value;
                document.getElementById('userIn').value = "";

                fetch('/interact', {{
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    method: 'POST',
                    body: text
                }}).then(response=>response.json()).then(data=>{{
                    var parDiv = document.getElementById("parent");

                    parDiv.append(createChatRow("You", text));

                    // Change info for Model response
                    parDiv.append(createChatRow("Taiga", data.text));
                    parDiv.scrollTo(0, parDiv.scrollHeight);
                }})
            }});
            document.getElementById("interact").addEventListener("reset", function(event){{
                event.preventDefault()
                var text = document.getElementById("userIn").value;
                document.getElementById('userIn').value = "";

                fetch('/reset', {{
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    method: 'POST',
                }}).then(response=>response.json()).then(data=>{{
                    var parDiv = document.getElementById("parent");

                    parDiv.innerHTML = '';
                    parDiv.append(createChatRow("Instructions", "Enter a message, and the model will respond interactively."));
                    parDiv.scrollTo(0, parDiv.scrollHeight);
                }})
            }});
        </script>

    </body>
</html>
"""  # noqa: E501


class MyHandler(BaseHTTPRequestHandler):
    """
    Handle HTTP requests.
    """

    def _interactive_running(self, opt, reply_text):
        reply = {'episode_done': False, 'text': reply_text}
        print(reply_text)
        SHARED['agent'].observe(reply)
        model_res = SHARED['agent'].act()
        # print(model_res['text'])
        if "my name is" in model_res['text']: 
             model_res.force_set('text','My name is Taiga, the friend who loves talking to you.') 
        return model_res

    def do_HEAD(self):
        """
        Handle HEAD requests.
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        """
        Handle POST request, especially replying to a chat message.
        """
        print("Chatbot listening")
        if self.path == '/interact':
            r = sr.Recognizer()
            text = ""

            with sr.Microphone() as source:
                print("Adjusting noise ")
                r.adjust_for_ambient_noise(source, duration=1)
                print("Recording for 4 seconds")
                recorded_audio = r.listen(source, timeout=8)
                print("Done recording")

            ''' Recognizing the Audio '''
            try:
                print("Recognizing the text")
                text = r.recognize_google(
                        recorded_audio, 
                        language="en-US"
                    )
                print("Decoded Text : {}".format(text))

            except Exception as ex:
                print(ex)
                
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            body = text
            # model_response = self._interactive_running(
            #     SHARED.get('opt'), body.decode('utf-8')
            # )
            model_response = self._interactive_running(
                SHARED.get('opt'), body
            )
            # print(model_response)
            print(model_response['text'])
            # engine.say(model_response['text'])
            # engine.runAndWait()
            assistant = gTTS(text=model_response['text'], lang='en', slow=False)
            assistant.save("out.mp3")
            # os.system("vlc out.mp3")
            playsound('out.mp3',True)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            json_str = json.dumps(model_response)
            # print(json_str)
            self.wfile.write(bytes(json_str, 'utf-8'))
        elif self.path == '/reset':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            SHARED['agent'].reset()
            self.wfile.write(bytes("{}", 'utf-8'))
        else:
            return self._respond({'status': 500})

    def do_GET(self):
        """
        Respond to GET request, especially the initial load.
        """
        paths = {
            '/': {'status': 200},
            '/favicon.ico': {'status': 202},  # Need for chrome
        }
        if self.path in paths:
            self._respond(paths[self.path])
        else:
            self._respond({'status': 500})

    def _handle_http(self, status_code, path, text=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content = WEB_HTML.format(STYLE_SHEET, FONT_AWESOME)
        return bytes(content, 'UTF-8')

    def _respond(self, opts):
        response = self._handle_http(opts['status'], self.path)
        # print(response)
        self.wfile.write(response)


def setup_interweb_args(shared):
    """
    Build and parse CLI opts.
    """
    parser = setup_args()
    parser.description = 'Interactive chat with a model in a web browser'
    parser.add_argument('--port', type=int, default=PORT, help='Port to listen on.')
    parser.add_argument(
        '--host',
        default=HOST_NAME,
        type=str,
        help='Host from which allow requests, use 0.0.0.0 to allow all IPs',
    )
    return parser


def shutdown():
    global SHARED
    if 'server' in SHARED:
        SHARED['server'].shutdown()
    SHARED.clear()


def wait():
    global SHARED
    while not SHARED.get('ready'):
        time.sleep(0.01)


def interactive_web(opt):
    global SHARED

    opt['task'] = 'parlai.agents.local_human.local_human:LocalHumanAgent'

    # Create model and assign it to the specified task
    agent = create_agent(opt, requireModelExists=True)
    agent.opt.log()
    SHARED['opt'] = agent.opt
    SHARED['agent'] = agent
    SHARED['world'] = create_task(SHARED.get('opt'), SHARED['agent'])

    MyHandler.protocol_version = 'HTTP/1.0'
    httpd = HTTPServer((opt['host'], opt['port']), MyHandler)
    SHARED['server'] = httpd
    logging.info('http://{}:{}/'.format(opt['host'], opt['port']))

    try:
        SHARED['ready'] = True
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


@register_script('interactive_web', aliases=['iweb'], hidden=True)
class InteractiveWeb(ParlaiScript):
    @classmethod
    def setup_args(cls):
        return setup_interweb_args(SHARED)

    def run(self):
        return interactive_web(self.opt)


if __name__ == '__main__':
    InteractiveWeb.main()