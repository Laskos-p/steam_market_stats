import ItemList from "../components/ItemList";
import Loader from "../components/Loader";
import useItems from "../lib/utils/useItems";

export default function Items() {
  const { items, error, isLoading } = useItems();

  if (error || isLoading)
    return (
      <div className="grid place-items-center">
        {error ? <p className="text-red-500">{error.message}</p> : <Loader />}
      </div>
    );
  return <ItemList data={items ?? []} />;
}
