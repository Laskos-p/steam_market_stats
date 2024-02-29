export interface ItemInfo {
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

export default function Item({ ...item }: ItemInfo) {
  return (
    <div className="m-5 flex h-[200px] rounded-[10px] bg-[#1f232e] p-6">
      <img
        src={
          "https://community.akamai.steamstatic.com/economy/image/" +
          item.icon_url
        }
        alt="logo"
        className="h-full border-2 border-black bg-[#395865] bg-gradient-radial from-[#395865] via-[#294048] to-[#191919]"
      />
      <div className="ml-4 grid w-full grid-cols-2 grid-rows-[25%_50%_25%] text-[white]">
        <div className="col-span-2 text-left text-2xl font-bold">
          {item.full_name}
        </div>
        <div className="flex flex-col items-center justify-between">
          <span>Price</span>
          <span>{"$" + item.sell_price / 100 + " USD"}</span>
        </div>
        <div className="flex flex-col items-center justify-between">
          <span>Quantity</span>
          <span>{item.sell_listings}</span>
        </div>
        <div className="col-span-2 flex content-center justify-end">
          <a
            href={
              "https://steamcommunity.com/market/listings/730/" + item.full_name
            }
            className="text-[#4b8cf5] hover:underline"
          >
            Link to item on steam
          </a>
        </div>
      </div>
    </div>
  );
}
