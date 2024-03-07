import ItemInfo from "../lib/types/ItemInfo";
import Item from "./Item";

export default function ItemList({ data }: { data: ItemInfo[] }) {
  return (
    <>
      <ul role="list" className="space-y-4">
        {data.map((item: ItemInfo) => (
          <li key={item.id} role="listitem">
            <Item {...item} />
          </li>
        ))}
      </ul>
    </>
  );
}
