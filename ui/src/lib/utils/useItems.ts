import useSWR from "swr";
import ItemInfo from "../types/ItemInfo";

export default function useItems() {
  const { data, error, isLoading } = useSWR<ItemInfo[], Error>(
    "http://127.0.0.1:8080/items",
    async (url: string) => {
      const response = await fetch(url);
      if (!response.ok)
        throw new Error(
          `Failed to fetch items from ${url}: ${response.status} ${response.statusText}`,
        );
      return response.json();
    },
  );

  return { items: data, error, isLoading };
}
