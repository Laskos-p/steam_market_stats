import ItemInfo from "../lib/types/ItemInfo";

export default function Item({ ...item }: ItemInfo) {
  return (
    <div className="mx-auto flex max-w-screen-sm flex-col bg-primary p-4 md:rounded-sm lg:max-w-screen-lg lg:flex-row">
      <img
        loading="lazy"
        src={
          "https://community.cloudflare.steamstatic.com/economy/image/" +
          item.icon_url
        }
        alt="item icon"
        className="aspect-video object-scale-down lg:w-1/3"
      />
      <div className="grid grow gap-4 md:justify-items-center lg:grid-cols-2 lg:gap-0">
        <div className="lg:col-span-2">
          <h3>{item.full_name}</h3>
        </div>
        <div className="grid grid-cols-2 gap-4 lg:grid-cols-1">
          <span>Price</span>
          <span>{"$" + item.sell_price / 100 + " USD"}</span>
        </div>
        <div className="grid grid-cols-2 gap-4 lg:grid-cols-1">
          <span>Quantity</span>
          <span>{item.sell_listings}</span>
        </div>
        <div className="lg:col-start-2 lg:place-self-end ">
          <a
            href={
              "https://steamcommunity.com/market/listings/730/" + item.full_name
            }
            className="text-blue-500 hover:underline"
          >
            Link to item on steam
          </a>
        </div>
      </div>
    </div>
  );
}
