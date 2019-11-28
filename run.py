#for info on how to host with py anywhere.com
#https://www.youtube.com/watch?v=M-QRwEEZ9-8&t=492s
from flask_issue_tracker import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)