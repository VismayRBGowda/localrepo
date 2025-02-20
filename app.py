from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    try:
        top_output = subprocess.check_output("top -b -n 1", shell=True).decode("utf-8")
        return "<pre>" + top_output + "</pre>" 
    except Exception as e:
        return str(e)

@app.route('/htop')
def htop():
    name = "Vismay R B Gowda"  
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <h2>Top Output:</h2>
    {get_top_output()}
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug = False)
