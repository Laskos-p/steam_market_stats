import { createFileRoute } from "@tanstack/react-router";
import { itemQueryOptions } from "../../lib/utils/itemQueryOptions";

export const Route = createFileRoute("/items/$itemId")({
  loader: ({ context: { queryClient }, params: { itemId } }) =>
    queryClient.ensureQueryData(itemQueryOptions(itemId)),
});
