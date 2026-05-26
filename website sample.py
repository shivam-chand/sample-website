from flask import Flask, render_template_string, request, redirect
import sqlite3

app = Flask(__name__)

HTML = """

<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Modern Shop</title>

<link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css"/>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial;
}

body{
    background:#0f172a;
    color:white;
}

.light{
    background:white;
    color:black;
}

header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:20px 50px;
    background:rgba(0,0,0,0.3);
    position:sticky;
    top:0;
    backdrop-filter:blur(10px);
    z-index:100;
}

.logo{
    font-size:30px;
    font-weight:bold;
    color:#38bdf8;
}

nav a{
    color:white;
    text-decoration:none;
    margin-left:20px;
}

.hero{
    height:90vh;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    background:
    linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
    url('https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=1600&auto=format&fit=crop');

    background-size:cover;
    background-position:center;
}

.hero-content h1{
    font-size:60px;
}

.hero-content p{
    margin:20px 0;
    font-size:22px;
}

.hero-content button{
    padding:15px 30px;
    border:none;
    border-radius:10px;
    background:#38bdf8;
    color:white;
    cursor:pointer;
}

.products,
.reviews,
.contact,
.chatbot,
.map-section{
    padding:80px 50px;
    text-align:center;
}

.products h2,
.reviews h2,
.contact h2,
.chatbot h2{
    margin-bottom:40px;
    font-size:40px;
}

.product-grid,
.review-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit, minmax(250px,1fr));
    gap:30px;
}

.card,
.review-card{
    background:#1e293b;
    border-radius:20px;
    overflow:hidden;
    transition:0.3s;
    padding-bottom:20px;
}

.card:hover{
    transform:translateY(-10px);
}

.card img{
    width:100%;
    height:250px;
    object-fit:cover;
}

.card h3{
    margin-top:20px;
}

.card p{
    margin:15px 0;
    color:#38bdf8;
}

.card button{
    padding:12px 20px;
    border:none;
    border-radius:10px;
    background:#38bdf8;
    color:white;
    cursor:pointer;
}

.review-card{
    padding:30px;
}

input,
textarea{
    width:100%;
    max-width:500px;
    padding:15px;
    margin:10px 0;
    border:none;
    border-radius:10px;
}

.contact button,
.chatbot button{
    padding:15px 30px;
    border:none;
    border-radius:10px;
    background:#38bdf8;
    color:white;
    cursor:pointer;
}

.whatsapp{
    position:fixed;
    bottom:20px;
    right:20px;
    width:60px;
    height:60px;
    background:#25d366;
    border-radius:50%;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:30px;
    text-decoration:none;
    color:white;
}

#theme{
    position:fixed;
    top:20px;
    right:20px;
    padding:10px;
    border:none;
    border-radius:10px;
    cursor:pointer;
}

footer{
    background:black;
    padding:20px;
    text-align:center;
}

@media(max-width:768px){

    header{
        flex-direction:column;
    }

    .hero-content h1{
        font-size:40px;
    }

}

</style>

</head>
<body>

<header>

<div class="logo">SHOPIFY MART</div>

<nav>
<a href="#home">Home</a>
<a href="#products">Products</a>
<a href="#reviews">Reviews</a>
<a href="#contact">Contact</a>
</nav>

</header>

<button id="theme">🌙</button>

<section class="hero" id="home">

<div class="hero-content">

<h1>Grow Your Shop Online 🚀</h1>

<p>Premium websites for local businesses</p>

<button>Get Started</button>

</div>

</section>

<section class="products" id="products">

<h2>Our Products</h2>

<div class="product-grid">

{% for product in products %}

<div class="card" data-aos="zoom-in">

<img src="{{ product[3] }}">

<h3>{{ product[1] }}</h3>

<p>{{ product[2] }}</p>

<form action="/order" method="POST">

<input type="hidden" name="name" value="Customer">

<button type="submit">Order Now</button>

</form>

</div>

{% endfor %}

</div>

</section>

<section class="reviews" id="reviews">

<h2>Customer Reviews</h2>

<div class="review-grid">

<div class="review-card">
<h3>Rahul Kumar</h3>
<p>Amazing products and fast delivery.</p>
</div>

<div class="review-card">
<h3>Priya Sharma</h3>
<p>Very premium looking website.</p>
</div>

</div>

</section>

<section class="chatbot">

<h2>AI Chatbot</h2>

<input type="text" placeholder="Ask something...">

<br>

<button>Send</button>

</section>

<section class="map-section">

<h2>Our Location</h2>

<iframe
src="https://www.google.com/maps/embed?pb=!1m18"
width="100%"
height="400"
style="border:0;"
allowfullscreen=""
loading="lazy">
</iframe>

</section>

<section class="contact" id="contact">

<h2>Contact Us</h2>

<form>

<input type="text" placeholder="Your Name">

<input type="email" placeholder="Your Email">

<textarea placeholder="Your Message"></textarea>

<br>

<button type="submit">Send Message</button>

</form>

</section>

<a href="https://wa.me/919999999999" class="whatsapp">
💬
</a>

<footer>

<p>© 2026 Modern Shop Website</p>

</footer>

<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>

<script>

AOS.init();

const theme = document.getElementById("theme");

theme.onclick = () => {
    document.body.classList.toggle("light");
}

</script>

</body>
</html>

"""

def get_products():

    conn = sqlite3.connect("shop.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price TEXT,
        image TEXT
    )
    """)

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    if len(products) == 0:

        sample = [

            (
                "Smart Watch",
                "₹1999",
                "https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=1200&auto=format&fit=crop"
            ),

            (
                "Running Shoes",
                "₹2999",
                "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=1200&auto=format&fit=crop"
            ),

            (
                "Smart Phone",
                "₹14999",
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=1200&auto=format&fit=crop"
            )

        ]

        cursor.executemany(
            "INSERT INTO products(name, price, image) VALUES(?,?,?)",
            sample
        )

        conn.commit()

        cursor.execute("SELECT * FROM products")

        products = cursor.fetchall()

    conn.close()

    return products

@app.route('/')
def home():

    products = get_products()

    return render_template_string(HTML, products=products)

@app.route('/order', methods=['POST'])
def order():

    customer = request.form['name']

    return f"""
    <h1>
    Order placed successfully by {customer}
    </h1>
    """

if __name__ == '__main__':
    app.run(debug=True)