from flask import Flask, render_template, redirect
import subprocess, time
app = Flask(__name__) 

@app.route('/', methods=['GET'])
def index():
    return render_template('pc_options.html')

@app.route('/pc/options/<option>', methods=['POST'])
def pcsleep(option):
    if option == 'sleep':
        return subprocess.run('rundll32.exe powrprof.dll,SetSuspendState 0,1,0', shell=True)
    elif option == 'shutdown':
        return  subprocess.run('Shutdown.exe -s -t 00', shell=True)
    else:
        return redirect('http://localhost:5000/', code=302)