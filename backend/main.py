from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "category": "Electronics",
        "description": "High performance laptop",
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500",
        "stock": 10
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 20000,
        "category": "Electronics",
        "description": "Latest smartphone",
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500",
        "stock": 15
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 3000,
        "category": "Accessories",
        "description": "Wireless headphones",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500",
        "stock": 20
    },
    {
        "id": 4,
        "name": "Keyboard",
        "price": 1500,
        "category": "Accessories",
        "description": "Mechanical keyboard",
        "image": "https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=500",
        "stock": 30
    },
    {
        "id": 5,
        "name": "Mouse",
        "price": 800,
        "category": "Accessories",
        "description": "Gaming mouse",
        "image": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500",
        "stock": 25
    },
    {
        "id": 6,
        "name": "Monitor",
        "price": 12000,
        "category": "Electronics",
        "description": "24-inch monitor",
        "image": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500",
        "stock": 8
    },
    {
        "id": 7,
        "name": "Speaker",
        "price": 2500,
        "category": "Audio",
        "description": "Bluetooth speaker",
        "image": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500",
        "stock": 18
    },
    {
        "id": 8,
        "name": "Smart Watch",
        "price": 5000,
        "category": "Wearables",
        "description": "Fitness tracking watch",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
        "stock": 12
    },
    {
        "id": 9,
        "name": "Power Bank",
        "price": 1200,
        "category": "Accessories",
        "description": "10000mAh power bank",
        "image": "https://images.unsplash.com/photo-1609592806596-b43bada2f2f5?w=500",
        "stock": 20
    },
    {
        "id": 10,
        "name": "Printer",
        "price": 7000,
        "category": "Office",
        "description": "Color printer",
        "image": "https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?w=500",
        "stock": 5
    }
]

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

@app.get("/products")
def get_products():
    return products