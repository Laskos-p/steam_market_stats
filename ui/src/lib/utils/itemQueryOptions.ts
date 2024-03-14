import { queryOptions } from "@tanstack/react-query";
import { fetchItem } from "./items";

export const itemQueryOptions = (itemId: string) =>
  queryOptions({
    queryKey: ["items", { itemId }],
    queryFn: () => fetchItem(itemId),
  });
