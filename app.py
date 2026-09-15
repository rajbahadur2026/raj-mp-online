
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Raj MP Online Centre</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #222;
        }

        header {
            background: linear-gradient(135deg, #0d6efd, #084298);
            color: white;
            padding: 18px 7%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }

        .logo {
            font-size: 26px;
            font-weight: bold;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 22px;
            font-size: 15px;
        }

        .hero {
            background: linear-gradient(135deg, #0d6efd, #084298);
            color: white;
            text-align: center;
            padding: 75px 20px;
        }

        .hero h1 {
            font-size: 45px;
            margin-bottom: 15px;
        }

        .hero p {
            font-size: 19px;
            margin-bottom: 28px;
        }

        .btn {
            display: inline-block;
            background: white;
            color: #0d6efd;
            padding: 13px 25px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
        }

        .section {
            max-width: 1100px;
            margin: auto;
            padding: 55px 20px;
        }

        .section-title {
            text-align: center;
            margin-bottom: 35px;
        }

        .section-title h2 {
            font-size: 32px;
            color: #084298;
            margin-bottom: 8px;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 22px;
        }

        .card {
            background: white;
            padding: 30px 22px;
            text-align: center;
            border-radius: 15px;
            box-shadow: 0 5px 18px rgba(0,0,0,0.08);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .icon {
            font-size: 42px;
            margin-bottom: 15px;
        }

        .card h3 {
            color: #0d6efd;
            margin-bottom: 10px;
        }

        .card p {
            color: #666;
            line-height: 1.5;
        }

        .about {
            background: white;
            text-align: center;
        }

        .about p {
            max-width: 800px;
            margin: auto;
            line-height: 1.8;
            color: #555;
        }

        .contact {
            text-align: center;
        }

        .whatsapp {
            display: inline-block;
            background: #25D366;
            color: white;
            padding: 14px 28px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            margin-top: 20px;
        }

        footer {
            background: #111827;
            color: white;
            text-align: center;
            padding: 25px 15px;
        }

        footer p {
            margin: 5px;
        }

        @media (max-width: 700px) {
            header {
                text-align: center;
                justify-content: center;
                gap: 15px;
            }

            nav a {
                margin: 0 8px;
            }

            .hero h1 {
                font-size: 34px;
            }

            .hero p {
                font-size: 16px;
            }
        }
    </style>
</head>

<body>

<header>
    <div class="logo">Raj MP Online Centre</div>

    <nav>
        <a href="#home">Home</a>
        <a href="#services">Services</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<section class="hero" id="home">
    <h1>Raj MP Online Centre</h1>

    <p>आपकी Online Services का भरोसेमंद Digital Centre</p>

    <a href="#services" class="btn">हमारी Services देखें</a>
</section>

<section class="section" id="services">

    <div class="section-title">
        <h2>हमारी Services</h2>
        <p>आपके लिए उपलब्ध प्रमुख Online Services</p>
    </div>

    <div class="services">

        <div class="card">
            <div class="icon">📄</div>
            <h3>Online Forms</h3>
            <p>सरकारी एवं अन्य Online Forms भरने की सुविधा।</p>
        </div>

        <div class="card">
            <div class="icon">📋</div>
            <h3>Resume / CV</h3>
            <p>Professional Resume और CV बनाने की सुविधा।</p>
        </div>

        <div class="card">
            <div class="icon">📑</div>
            <h3>PDF Services</h3>
            <p>PDF बनाने, बदलने और Document से जुड़ी सेवाएं।</p>
        </div>

        <div class="card">
            <div class="icon">📸</div>
            <h3>Photo Services</h3>
            <p>Passport Size Photo और Photo Editing Services।</p>
        </div>

        <div class="card">
            <div class="icon">💼</div>
            <h3>Job Services</h3>
            <p>Job Forms और रोजगार से जुड़ी Online Services।</p>
        </div>

        <div class="card">
            <div class="icon">🖨️</div>
            <h3>Print & Document</h3>
            <p>Document तैयार करने और Digital काम की सुविधा।</p>
        </div>

    </div>
</section>

<section class="section about" id="about">

    <div class="section-title">
        <h2>About Raj MP Online</h2>
    </div>

    <p>
        Raj MP Online Centre एक Digital Service Centre है,
        जहां आपको Online Forms, Resume/CV, PDF, Photo Editing,
        Job Services और विभिन्न Online कार्यों में सहायता प्रदान की जाती है।
    </p>

</section>

<section class="section contact" id="contact">

    <div class="section-title">
        <h2>Contact Us</h2>
        <p>Online Service के लिए हमसे संपर्क करें</p>
    </div>

    <a class="whatsapp" href="https://wa.me/918827579512" target="_blank">
        💬 WhatsApp पर संपर्क करें
    </a>

</section>

<footer>
    <p>© 2026 Raj MP Online Centre</p>
    <p>All Rights Reserved</p>
</footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)