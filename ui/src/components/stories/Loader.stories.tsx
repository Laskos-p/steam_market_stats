import Loader from "../Loader";
import { StoryObj, Meta } from "@storybook/react";

export default {
  component: Loader,
  title: "Loader",
  tags: ["autodocs"],
  parameters: {
    layout: "centered",
  },
} satisfies Meta<typeof Loader>;

type Story = StoryObj<typeof Loader>;

export const DefaultLoader: Story = {};
