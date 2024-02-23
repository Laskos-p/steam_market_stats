import { useEffect, useState } from "react";
import React from "react";

export default function Items() {
  const [data, setData] = useState<Array<unknown>>([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8080/items", { method: "GET" })
      .then(
        (response) => {
          if (response.ok) {
            return response.json();
          }
          throw response;
        },
        (error) => {
          console.log(error);
        },
      )
      .then((data) => {
        setData(data);
      });
  }, []);
  return (
    <>
      <h1>Items</h1>
      <ul className="items">
        {data &&
          data.map((item: unknown) => (
            <li key={crypto.randomUUID()}>
              <img
                src={
                  "https://community.akamai.steamstatic.com/economy/image/" +
                  (item as { icon_url: string }).icon_url
                }
                alt="logo"
              />
              <div className="item-info">
                <div className="item-name">
                  {(item as { full_name: string }).full_name}
                </div>
                <div className="item-price-info">
                  <span className="item-price-label">Price</span>
                  <span className="item-price">
                    {"$" +
                      (item as { sell_price: number }).sell_price / 100 +
                      " USD"}
                  </span>
                </div>
                <div className="item-quantity-info">
                  <span className="item-quality-label">Quantity</span>
                  <span className="item-quantity">
                    {(item as { sell_listings: number }).sell_listings}
                  </span>
                </div>
                <div className="link-to-steam">
                  <a
                    href={
                      "https://steamcommunity.com/market/listings/730/" +
                      (item as { full_name: string }).full_name
                    }
                  >
                    Link to item on steam
                  </a>
                </div>
              </div>
            </li>
          ))}
      </ul>
    </>
  );
}
