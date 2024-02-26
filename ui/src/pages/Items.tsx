import { useEffect, useState } from "react";

interface Item {
  id: number;
  full_name: string;
  name: string;
  weapon: string;
  stattrak: boolean;
  quality: string;
  sell_listings: number;
  sell_price: number;
  icon_url: string;
  appid: number;
}

export default function Items() {
  const [data, setData] = useState<Item[]>([]);
  const [error, setError] = useState<string | null>(null);

  async function fetchItems() {
    const response = await fetch("http://127.0.0.1:8080/items");
    return (await response.json()) as Item[];
  }

  useEffect(() => {
    fetchItems()
      .then((data) => setData(data))
      .catch((error: Error) => {
        setError(error.message);
      });
  }, []);

  return (
    <>
      <h1>Items</h1>
      {error || (
        <ul className="items">
          {data &&
            data.map((item: Item) => (
              <li key={crypto.randomUUID()}>
                <img
                  src={
                    "https://community.akamai.steamstatic.com/economy/image/" +
                    item.icon_url
                  }
                  alt="logo"
                />
                <div className="item-info">
                  <div className="item-name">{item.full_name}</div>
                  <div className="item-price-info">
                    <span className="item-price-label">Price</span>
                    <span className="item-price">
                      {"$" + item.sell_price / 100 + " USD"}
                    </span>
                  </div>
                  <div className="item-quantity-info">
                    <span className="item-quality-label">Quantity</span>
                    <span className="item-quantity">{item.sell_listings}</span>
                  </div>
                  <div className="link-to-steam">
                    <a
                      href={
                        "https://steamcommunity.com/market/listings/730/" +
                        item.full_name
                      }
                    >
                      Link to item on steam
                    </a>
                  </div>
                </div>
              </li>
            ))}
        </ul>
      )}
    </>
  );
}
