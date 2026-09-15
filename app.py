
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Raj MP Online</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f7fb;
            }

            header {
                background: #0d6efd;
                color: white;
                padding: 25px;
                text-align: center;
            }

            header h1 {
                margin: 0;
                font-size: 35px;
            }

            header p {
                margin: 8px 0 0;
                font-size: 17px;
            }

            .container {
                max-width: 1000px;
                margin: 30px auto;
                padding: 20px;
            }

            .services {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
            }

            .card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 4px 15px rgba(0,0,0,0.10);
            }

            .card h2 {
                color: #0d6efd;
            }

            .card p {
                color: #555;
            }

            .btn {
                display: inline-block;
                background: #0d6efd;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                text-decoration: none;
            }

            footer {
                margin-top: 40px;
                background: #222;
                color: white;
                text-align: center;
                padding: 20px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>Raj MP Online</h1>
            <p>Online Services & Digital Solutions</p>
        </header>

        <div class="container">

            <h2 style="text-align:center;">हमारी Services</h2>

            <div class="services">

                <div class="card">
                    <h2>📄 Online Forms</h2>
                    <p>Online form filling और application services.</p>
                    <a class="btn" href="#">View Service</a>
                </div>

                <div class="card">
                    <h2>📋 Resume / CV</h2>
                    <p>Professional Resume और CV बनाने की सुविधा.</p>
                    <a class="btn" href="#">Create CV</a>
                </div>

                <div class="card">
                    <h2>📑 PDF Tools</h2>
                    <p>PDF और document related services.</p>
                    <a class="btn" href="#">Open Tools</a>
                </div>

                <div class="card">
                    <h2>📸 Photo Tools</h2>
                    <p>Passport photo और image editing services.</p>
                    <a class="btn" href="#">Open Tools</a>
                </div>

                <div class="card">
                    <h2>💼 Jobs</h2>
                    <p>Job information और local opportunities.</p>
                    <a class="btn" href="#">View Jobs</a>
                </div>

                <div class="card">
                    <h2>📞 Contact</h2>
                    <p>हमसे online contact करें.</p>
                    <a class="btn" href="#">Contact Us</a>
                </div>

            </div>
        </div>

        <footer>
            © 2026 Raj MP Online | All Rights Reserved
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)