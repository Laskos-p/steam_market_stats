import Item, { ItemInfo } from "./Item";
import useSWR from "swr";

export default function ItemList() {
  const { data, error } = useSWR<ItemInfo[], Error>(
    "http://127.0.0.1:8080/items",
    (url: string) => fetch(url).then((res) => res.json()),
  );
  return (
    <>
      {error ? (
        <span>{error.message}</span>
      ) : (
        <ul role="list" className="space-y-4">
          {data &&
            data.map((item: ItemInfo) => (
              <li key={item.id} role="listitem">
                <Item {...item} />
              </li>
            ))}
        </ul>
      )}
    </>
  );
}
