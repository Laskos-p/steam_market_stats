import { StoryObj, Meta, composeStories } from "@storybook/react";
import * as stories from "./Item.stories";
import ItemList from "../ItemList";
import { ItemInfo } from "../../lib/types/ItemInfo";

const { Default: DefaultItem } = composeStories(stories);

export default {
  title: "ItemList",
  component: ItemList,
  tags: ["autodocs"],
  args: {
    data: Array.from({ length: 5 }, (_, i) => ({
      id: i,
      ...(DefaultItem.args as Omit<ItemInfo, "id">),
    })),
  },
} satisfies Meta<typeof ItemList>;

type Story = StoryObj<typeof ItemList>;

export const Default: Story = {};
