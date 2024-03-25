import React, { useState } from "react";

function MustangCard({ mustang }) {
    const [isInStock, setIsInStock] = useState(true);

    const toggleStockStatus = () => {
        setIsInStock(!isInStock);
    };

    return (
        <li className="card" data-testid="mustang-item">
            <img src={mustang.image} alt={mustang.year} />
            <h4>{mustang.year}, {mustang.color}</h4>
            <p>Price: ${mustang.price}</p>
            {isInStock ? (
                <button className="primary" onClick={toggleStockStatus}>In Stock</button>
            ) : (
                <button onClick={toggleStockStatus}>Out of Stock</button>
            )}
        </li>
    );
}

export default MustangCard;