import { queryOptions } from "@tanstack/react-query";
import { fetchItems } from "./items";

export const itemsQueryOptions = queryOptions({
  queryKey: ["items"],
  queryFn: () => fetchItems(),
});
