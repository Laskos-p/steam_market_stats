import { Suspense, lazy } from "react";
import Loader from "../components/Loader";
import useItems from "../lib/utils/useItems";

const ItemList = lazy(() => import("../components/ItemList"));

export default function Items() {
  const { items, error, isLoading } = useItems();

  if (error || isLoading)
    return (
      <div className="grid place-items-center">
        {error ? <p className="text-red-500">{error.message}</p> : <Loader />}
      </div>
    );
  return (
    <Suspense fallback={<Loader />}>
      <ItemList data={items ?? []} />
    </Suspense>
  );
}
