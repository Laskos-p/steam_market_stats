import ItemInfo, { ItemInfoSchema } from "../types/ItemInfo";
import axios, { AxiosError, isAxiosError } from "axios";
import { notFound } from "@tanstack/react-router";

export const fetchItem = async (itemId: string) => {
  const item = await axios
    .get<ItemInfo>(`http://127.0.0.1:8080/items/${itemId}`)
    .then((response) => ItemInfoSchema.parse(response.data))
    .catch((error: AxiosError) => {
      if (!isAxiosError(error)) {
        throw new Error(`Failed to fetch item with id "${itemId}"`);
      }
      if (
        error.response &&
        typeof error.response.data === "object" &&
        error.response.data !== null &&
        "detail" in error.response.data &&
        typeof error.response.data.detail === "string" &&
        error.response.data.detail === "Item doesnt exist"
      )
        throw notFound();
      throw error;
    });

  return item;
};

export const fetchItems = async () => {
  const items = await axios
    .get<ItemInfo[]>("http://127.0.0.1:8080/items")
    .then((response) => ItemInfoSchema.array().nonempty().parse(response.data));

  return items;
};
