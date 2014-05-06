from paygoal import app

@app.route('/')
def index():
    return "Welcome to Paygoal"

