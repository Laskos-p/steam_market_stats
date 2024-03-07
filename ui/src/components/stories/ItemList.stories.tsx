import { StoryObj, Meta, composeStories } from "@storybook/react";
import * as stories from "./Item.stories";
import ItemList from "../ItemList";
import ItemInfo from "../../lib/types/ItemInfo";

const { DefaultItem } = composeStories(stories);

export default {
  title: "ItemList",
  component: ItemList,
  tags: ["autodocs"],
  args: {
    data: Array.from({ length: 5 }, (_, i) => ({
      ...(DefaultItem.args as ItemInfo),
      id: i,
    })),
  },
} satisfies Meta<typeof ItemList>;

type Story = StoryObj<typeof ItemList>;

export const Default: Story = {};
