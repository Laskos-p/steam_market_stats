import { z } from "zod";

export const ItemInfoSchema = z
  .object({
    id: z.number().safe().nonnegative(),
    full_name: z.string(),
    name: z.string(),
    weapon: z.string(),
    stattrak: z.boolean(),
    quality: z.string(),
    sell_listings: z.number().safe().nonnegative(),
    sell_price: z.number().safe().nonnegative(),
    icon_url: z.string(),
    appid: z.number().safe().nonnegative(),
  })
  .partial({
    name: true,
    weapon: true,
    stattrak: true,
    quality: true,
    appid: true,
  })
  .strict();

export type ItemInfo = z.infer<typeof ItemInfoSchema>;
export default ItemInfo;
