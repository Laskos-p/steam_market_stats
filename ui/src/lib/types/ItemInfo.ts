export default interface ItemInfo {
  id: number;
  full_name: string;
  name?: string;
  weapon?: string;
  stattrak?: boolean;
  quality?: string;
  sell_listings: number;
  sell_price: number;
  icon_url: string;
  appid?: number;
}
