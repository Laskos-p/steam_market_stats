import { createFileRoute } from "@tanstack/react-router";
import { itemsQueryOptions } from "../../lib/utils/itemsQueryOptions";

export const Route = createFileRoute("/items/")({
  loader: ({ context: { queryClient } }) =>
    queryClient.ensureQueryData(itemsQueryOptions),
});
