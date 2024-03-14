import {
  ErrorComponent,
  ErrorComponentProps,
  createLazyFileRoute,
} from "@tanstack/react-router";
import Item from "../../components/Item";

export const Route = createLazyFileRoute("/items/$itemId")({
  notFoundComponent,
  errorComponent,
  component,
});
function errorComponent({ error }: ErrorComponentProps) {
  return <ErrorComponent error={error} />;
}

function notFoundComponent() {
  const { itemId } = Route.useParams();
  return <p>Item with id {itemId} not found</p>;
}

function component() {
  const item = Route.useLoaderData();

  return <Item {...item} />;
}
