import ItemList from "../../components/ItemList";
import { useSuspenseQuery } from "@tanstack/react-query";
import { createLazyFileRoute } from "@tanstack/react-router";
import { itemsQueryOptions } from "../../lib/utils/itemsQueryOptions";

export const Route = createLazyFileRoute("/items/")({
  component,
});

function component() {
  const itemsQuery = useSuspenseQuery(itemsQueryOptions);
  const items = itemsQuery.data;

  return <ItemList data={items} />;
}
