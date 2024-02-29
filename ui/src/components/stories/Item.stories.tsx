import type { StoryObj, Meta } from "@storybook/react";
import Item from "../Item";

export default {
  title: "Item",
  component: Item,
  tags: ["autodocs"],
  args: {
    full_name: "StatTrak™ USP-S | Cortex (Field-Tested)",
    sell_listings: 98,
    sell_price: 640,
    icon_url:
      "-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpoo6m1FBRp3_bGcjhQ09-jq5WYh8j3Jq_um25V4dB8xLrCo9Tw3VGx80RvYTqmdYHDeg9saVmGq1m4xry7gJK56M_BwXA26Ck8pSGKD6d5YK8",
  },
  argTypes: {
    id: { table: { disable: true } },
    name: { table: { disable: true } },
    weapon: { table: { disable: true } },
    stattrak: { table: { disable: true } },
    quality: { table: { disable: true } },
    icon_url: { table: { disable: true } },
    appid: { table: { disable: true } },
  },
} satisfies Meta<typeof Item>;

type Story = StoryObj<typeof Item>;

export const DefaultItem: Story = {};
