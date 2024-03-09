import useSWR from "swr";
import { ItemInfo, ItemInfoSchema } from "../types/ItemInfo";

export default function useItem(id: string) {
  const { data, error, isLoading } = useSWR<ItemInfo, Error>(
    `http://127.0.0.1:8080/items/${id}`,
    async (url: string) => {
      const response = await fetch(url);
      if (!response.ok)
        throw new Error(
          `Failed to fetch item from ${url} - ${response.status} ${response.statusText}`,
        );
      return ItemInfoSchema.parse(await response.json());
    },
  );
  return { item: data, error, isLoading };
}
