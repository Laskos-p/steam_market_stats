import { StoryObj, Meta, composeStories } from "@storybook/react";
import * as stories from "./Item.stories";

const { DefaultItem } = composeStories(stories);

export default {
  title: "ItemList",
  tags: ["autodocs"],
} satisfies Meta;

type Story = StoryObj;

export const Default: Story = {
  render: () => (
    <ul className="space-y-4">
      {Array.from({ length: 4 }).map(() => (
        <li key={crypto.randomUUID()}>
          <DefaultItem />
        </li>
      ))}
    </ul>
  ),
};
