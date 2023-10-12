import {useEffect, useState} from "react";

export default function Items() {
    const [data, setData] = useState(null);
    useEffect(() => {
        fetch("http://127.0.0.1:8000/items", {method: "GET"})
            .then(
                response => {
                    if (response.ok) {
                        return response.json()
                    }
                    throw response;
                }, error => {
                    console.log(error);
                }
            )
            .then(
                data => {
                    setData(data);
                }
            )
    }, []);
    return (
        <>
            <h1>Items</h1>
            <ul className="items">
                {data && data.map(item => (
                    <li key={crypto.randomUUID()}>
                        <img
                            src={"https://community.akamai.steamstatic.com/economy/image/" + item.icon_url}
                            alt="logo"
                        />
                        <div className="item-info">
                            <div className="item-name">
                                {item.full_name}
                            </div>
                            <div className="item-price-info">
                                <span className="item-price-label">Price</span>
                                <span className="item-price">
                                    {"$" + item.sell_price/100 +" USD"}
                                </span>
                            </div>
                            <div className="item-quantity-info">
                                <span className="item-quality-label">Quantity</span>
                                <span className="item-quantity">
                                    {item.sell_listings}
                                </span>
                            </div>
                            <div className="link-to-steam">
                                <a href={"https://steamcommunity.com/market/listings/730/" +
                                    (item.stattrak ? "StatTrak™ " : "") +
                                    item.weapon +
                                    " | " + item.name +
                                    " (" + item.quality+")"}>Link to item on steam</a>
                            </div>
                        </div>
                    </li>
                ))}
            </ul>
        </>
    )
}