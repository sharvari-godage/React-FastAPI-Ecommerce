import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/products")
      .then((res) => {
        setProducts(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.log(err);
        setError("Failed to load products");
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <h2 className="loading">Loading Products...</h2>;
  }

  if (error) {
    return <h2 className="loading">{error}</h2>;
  }

  return (
    <div>
      {/* Navbar */}
      <nav className="navbar">
        <h2>🛒 ShopEase</h2>

        <ul>
          <li>Home</li>
          <li>Products</li>
          <li>Categories</li>
          <li>Contact</li>
        </ul>
      </nav>

      {/* Hero Section */}
      <div className="hero">
        <h1>Discover Amazing Products</h1>
        <p>Best Quality • Best Prices • Fast Delivery</p>
      </div>

      {/* Heading */}
      <h2 className="section-title">Our Products</h2>

      {/* Product Grid */}
      <div className="product-grid">
        {products.map((product) => (
          <div className="card" key={product.id}>
            <img
              src={product.image}
              alt={product.name}
              className="product-image"
            />

            <span className="category">
              {product.category}
            </span>

            <h3>{product.name}</h3>

            <p className="price">
              ₹{product.price}
            </p>

            <p className="description">
              {product.description}
            </p>

            <p className="stock">
              Stock Available: {product.stock}
            </p>

            <button>Add To Cart</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;