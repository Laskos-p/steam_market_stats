import { useParams } from "react-router-dom";
import Loader from "../components/Loader";
import useItem from "../lib/utils/useItem";
import ItemCard from "../components/Item";

export default function Item() {
  const { id } = useParams<{ id: string }>();

  const { item, error, isLoading } = useItem(id!);

  if (!item || error || isLoading)
    return (
      <div className="grid place-items-center">
        {error ? <p className="text-red-500">{error.message}</p> : <Loader />}
      </div>
    );

  return <ItemCard {...item} />;
}
